#!/usr/bin/env node
/**
 * Decap CMS local backend proxy (replaces `npx decap-server`).
 *
 * Identical behaviour to decap-server's local_fs mode, with one fix:
 * `getEntry` falls back to `{slug}/index.md` when the flat `{slug}.md`
 * path doesn't exist.  This is needed because Decap CMS doesn't apply
 * the `path: "{{slug}}/index"` collection template when constructing
 * getEntry requests.
 */

"use strict";

const http = require("http");
const fs = require("fs");
const fsp = fs.promises;
const path = require("path");
const crypto = require("crypto");

const PORT = Number(process.env.PORT) || 8081;
const REPO = path.resolve(process.env.GIT_REPO_DIRECTORY || process.cwd());

// ── helpers ──────────────────────────────────────────────────────────────────

function sha256(buf) {
  return crypto.createHash("sha256").update(buf).digest("hex");
}

function posix(p) {
  return p.replace(/\\/g, "/");
}

async function readEntry(filePath) {
  const full = path.join(REPO, filePath);
  try {
    const buf = await fsp.readFile(full);
    return { data: buf.toString(), file: { path: posix(filePath), id: sha256(buf) } };
  } catch {
    return { data: null, file: { path: posix(filePath), id: null } };
  }
}

/**
 * If `filePath` doesn't exist, try substituting the extension with
 * `/index.<ext>` (e.g. `content/blog/my-post.md` → `content/blog/my-post/index.md`).
 */
async function resolveEntryPath(filePath) {
  const full = path.join(REPO, filePath);
  try {
    await fsp.access(full);
    return filePath; // exists as-is
  } catch {
    const withoutExt = filePath.replace(/\.[^./]+$/, "");
    const ext = path.extname(filePath);
    const indexPath = `${withoutExt}/index${ext}`;
    try {
      await fsp.access(path.join(REPO, indexPath));
      return indexPath;
    } catch {
      return filePath; // neither exists; return original so caller can handle
    }
  }
}

async function listFiles(dir, ext, depth) {
  if (depth <= 0) return [];
  const full = path.join(REPO, dir);
  let entries;
  try {
    entries = await fsp.readdir(full, { withFileTypes: true });
  } catch {
    return [];
  }
  const results = await Promise.all(
    entries.map(async (e) => {
      const rel = path.join(dir, e.name);
      if (e.isDirectory()) return listFiles(rel, ext, depth - 1);
      if (!ext || e.name.endsWith(`.${ext}`)) return [posix(rel)];
      return [];
    }),
  );
  return results.flat();
}

async function writeFileDeep(filePath, data) {
  const full = path.join(REPO, filePath);
  await fsp.mkdir(path.dirname(full), { recursive: true });
  await fsp.writeFile(full, data);
}

async function readMediaFile(filePath) {
  const full = path.join(REPO, filePath);
  const buf = await fsp.readFile(full);
  return {
    id: sha256(buf),
    content: buf.toString("base64"),
    encoding: "base64",
    path: posix(filePath),
    name: path.basename(filePath),
  };
}

// ── request handler ───────────────────────────────────────────────────────────

async function handle(body) {
  const { action, params = {} } = body;

  switch (action) {
    case "info":
      return { repo: path.basename(REPO), publish_modes: ["simple"], type: "local_fs" };

    case "entriesByFolder": {
      const files = await listFiles(params.folder, params.extension, params.depth);
      return Promise.all(files.map((f) => readEntry(f)));
    }

    case "entriesByFiles":
      return Promise.all(params.files.map((f) => readEntry(f.path)));

    case "getEntry": {
      const resolved = await resolveEntryPath(params.path);
      return readEntry(resolved);
    }

    case "persistEntry": {
      const dataFiles = params.dataFiles ?? (params.entry ? [params.entry] : []);
      const assets = params.assets ?? [];
      await Promise.all(dataFiles.map((f) => writeFileDeep(f.path, f.raw)));
      await Promise.all(
        assets.map((a) => writeFileDeep(a.path, Buffer.from(a.content, a.encoding))),
      );
      if (dataFiles.every((f) => f.newPath)) {
        await Promise.all(
          dataFiles.map(async (f) => {
            await fsp.rename(path.join(REPO, f.path), path.join(REPO, f.newPath));
          }),
        );
      }
      return { message: "entry persisted" };
    }

    case "getMedia": {
      const files = await listFiles(params.mediaFolder, "", 1);
      return Promise.all(
        files.filter((f) => !f.endsWith("/")).map((f) => readMediaFile(f)),
      );
    }

    case "getMediaFile":
      return readMediaFile(params.path);

    case "persistMedia": {
      const { asset } = params;
      await writeFileDeep(asset.path, Buffer.from(asset.content, asset.encoding));
      return readMediaFile(asset.path);
    }

    case "deleteFile":
      await fsp.unlink(path.join(REPO, params.path)).catch(() => {});
      return { message: `deleted file ${params.path}` };

    case "deleteFiles":
      await Promise.all(params.paths.map((p) => fsp.unlink(path.join(REPO, p)).catch(() => {})));
      return { message: `deleted files ${params.paths.join(", ")}` };

    case "getDeployPreview":
      return null;

    default:
      throw Object.assign(new Error(`Unknown action ${action}`), { status: 422 });
  }
}

// ── HTTP server ───────────────────────────────────────────────────────────────

const server = http.createServer(async (req, res) => {
  // CORS
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    res.writeHead(204);
    return res.end();
  }

  if (req.method !== "POST" || req.url !== "/api/v1") {
    res.writeHead(404, { "Content-Type": "application/json" });
    return res.end(JSON.stringify({ error: "Not found" }));
  }

  // Parse body
  let body;
  try {
    const raw = await new Promise((resolve, reject) => {
      const chunks = [];
      req.on("data", (c) => chunks.push(c));
      req.on("end", () => resolve(Buffer.concat(chunks).toString()));
      req.on("error", reject);
    });
    body = JSON.parse(raw);
  } catch {
    res.writeHead(400, { "Content-Type": "application/json" });
    return res.end(JSON.stringify({ error: "Invalid JSON" }));
  }

  try {
    const result = await handle(body);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(result));
  } catch (err) {
    const status = err.status ?? 500;
    res.writeHead(status, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ error: err.message ?? "Internal server error" }));
  }
});

server.listen(PORT, () => {
  console.info(`Decap CMS File System Proxy Server configured with ${REPO}`);
  console.info(`Decap CMS Proxy Server listening on port ${PORT}`);
});
