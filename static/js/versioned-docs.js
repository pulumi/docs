// Versioned SDK & CLI docs — version-selector loader.
//
// PERMANENT CONTRACT URL: every archived doc page references this file by the exact
// path /js/versioned-docs.js. Rewrite this file freely, but NEVER move or rename it —
// archived snapshots are immutable and will request this URL forever. All selector and
// banner styling lives in the sibling /js/versioned-docs.css, so the chrome can be
// restyled at any time without republishing a single archive.
//
// The script tag (injected by scripts/versioned-docs/inject-version-switcher.sh, or
// emitted by layouts/partials/docs/cli-command-banner.html on live pages) carries:
//   data-vdocs-tool       tool id, e.g. "pulumi-cli" or "python"
//   data-vdocs-mode       "archive" (a frozen snapshot) | "latest" (the live page)
//   data-vdocs-version    this page's version (archive mode)
//   data-vdocs-live-root  canonical live root, e.g. "/docs/iac/cli/commands/"
//   data-vdocs-rel        this page's path within its version root, e.g. "up/"
//
// Hard rule: fail SILENT. PR previews and any environment without published archives
// have no versions.json; on any error we render nothing and the page is unaffected.
(function () {
  "use strict";
  try {
    var script = document.querySelector("script[data-vdocs-tool]");
    if (!script) return;
    var cfg = {
      tool: script.getAttribute("data-vdocs-tool"),
      mode: script.getAttribute("data-vdocs-mode") || "latest",
      version: script.getAttribute("data-vdocs-version") || "",
      liveRoot: script.getAttribute("data-vdocs-live-root") || "/",
      rel: script.getAttribute("data-vdocs-rel") || "",
    };
    if (!cfg.tool) return;

    fetch("/docs/versioned/" + cfg.tool + "/versions.json", { credentials: "omit" })
      .then(function (r) {
        if (!r.ok) throw new Error("manifest " + r.status);
        return r.json();
      })
      .then(function (manifest) {
        if (!manifest || !Array.isArray(manifest.versions) || manifest.versions.length === 0) return;
        render(cfg, manifest);
      })
      .catch(function () {
        /* fail silent — no versioned content here */
      });
  } catch (e) {
    /* fail silent */
  }

  function ensureCss() {
    if (document.querySelector("link[data-vdocs-css]")) return;
    var l = document.createElement("link");
    l.rel = "stylesheet";
    l.href = "/js/versioned-docs.css";
    l.setAttribute("data-vdocs-css", "");
    document.head.appendChild(l);
  }

  // The latest entry links to the canonical live root, not its archived copy.
  function baseFor(entry, cfg) {
    return entry.latest ? cfg.liveRoot : entry.path;
  }

  function buildSelect(cfg, manifest, label) {
    var select = document.createElement("select");
    select.className = "vdocs-select";
    select.setAttribute("aria-label", label + " version");
    manifest.versions.forEach(function (entry) {
      var opt = document.createElement("option");
      opt.value = entry.version;
      opt.textContent = entry.version + (entry.latest ? " (latest)" : "");
      select.appendChild(opt);
    });
    var latest = manifest.versions.find(function (e) { return e.latest; }) || manifest.versions[0];
    select.value = cfg.mode === "archive" ? cfg.version : latest.version;
    select.addEventListener("change", function () {
      var entry = manifest.versions.find(function (e) { return e.version === select.value; });
      if (entry) navigate(baseFor(entry, cfg), cfg.rel);
    });
    return select;
  }

  function labelEl() {
    var lab = document.createElement("span");
    lab.className = "vdocs-inline-label";
    lab.textContent = "Version";
    return lab;
  }

  function render(cfg, manifest) {
    ensureCss();
    var label = manifest.label || cfg.tool;
    var select = buildSelect(cfg, manifest, label);
    var mount = document.querySelector("[data-vdocs-mount]");

    if (cfg.mode === "archive") {
      var bar = document.createElement("div");
      bar.className = "vdocs-banner";

      var msg = document.createElement("span");
      msg.className = "vdocs-banner-text";
      msg.textContent = "You are viewing docs for " + label + " " + cfg.version + ".";
      bar.appendChild(msg);

      var latest = manifest.versions.find(function (e) { return e.latest; });
      if (latest) {
        var a = document.createElement("a");
        a.className = "vdocs-banner-link";
        a.href = cfg.liveRoot + cfg.rel;
        a.textContent = "View latest";
        a.addEventListener("click", function (ev) {
          ev.preventDefault();
          navigate(cfg.liveRoot, cfg.rel);
        });
        bar.appendChild(a);
      }

      var ctrl = document.createElement("span");
      ctrl.className = "vdocs-banner-control";
      ctrl.appendChild(labelEl());
      ctrl.appendChild(select);
      bar.appendChild(ctrl);

      if (mount) {
        mount.appendChild(bar);
      } else {
        document.body.insertBefore(bar, document.body.firstChild);
        document.body.classList.add("vdocs-has-banner");
      }
    } else {
      // Latest page: dropdown only.
      var wrap = document.createElement("span");
      wrap.className = "vdocs-inline";
      wrap.appendChild(labelEl());
      wrap.appendChild(select);
      (mount || floatingMount()).appendChild(wrap);
    }
  }

  function floatingMount() {
    var m = document.createElement("div");
    m.className = "vdocs-floating";
    document.body.appendChild(m);
    return m;
  }

  // target = base + rel. Pages don't always exist across versions, so HEAD-probe and
  // fall back to the version/live root on a non-200 — bounds page-path drift.
  function navigate(base, rel) {
    var target = base + (rel || "");
    fetch(target, { method: "HEAD", credentials: "omit" })
      .then(function (r) { window.location.href = r.ok ? target : base; })
      .catch(function () { window.location.href = base; });
  }
})();
