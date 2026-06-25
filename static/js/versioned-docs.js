// Versioned SDK & CLI docs — version-selector loader.
//
// PERMANENT CONTRACT URL: every archived doc page references this file by the exact
// path /js/versioned-docs.js. Rewrite this file freely, but NEVER move or rename it —
// archived snapshots are immutable and will request this URL forever. All selector and
// banner styling lives in the sibling /js/versioned-docs.css, so the chrome can be
// restyled at any time without republishing a single archive.
//
// The script tag (injected by scripts/versioned-docs/inject-version-switcher.sh, emitted
// by layouts/partials/docs/cli-command-banner.html on live CLI pages, or added to live SDK
// pages at build time by scripts/versioned-docs/inject-live-sdk-selectors.sh) carries:
//   data-vdocs-tool       tool id, e.g. "pulumi-cli" or "python"
//   data-vdocs-mode       "archive" (a frozen snapshot) | "latest" (the live page)
//   data-vdocs-version    this page's version (archive mode)
//   data-vdocs-live-root  canonical live root, e.g. "/docs/iac/cli/commands/"
//   data-vdocs-rel        this page's path within its version root, e.g. "up/"
//
// Presentation (one control, context-appropriate framing):
//   * A page with an explicit [data-vdocs-mount] (live CLI command pages) gets a quiet
//     INLINE dropdown at the mount, sitting inside the site chrome.
//   * Any other page (archives + live SDK pages in their own generator themes) gets a
//     robust fixed TOP BAR — archive framing adds the "viewing old docs / view latest"
//     notice; latest framing is just the quiet dropdown. The bar measures its own height
//     and offsets known theme fixed-elements (Sphinx RTD sidebar, DocFX navbar, TypeDoc
//     toolbar) so it never clips them.
//
// Hard rule: fail SILENT. PR previews and any environment without published archives have
// no versions.json; on any error we render nothing and the page is unaffected.
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

    // On CLI archive pages the left nav is trimmed to a static command list; add a quiet
    // client-side filter over it. Independent of the manifest, and injected by the loader
    // (not baked into the snapshot) so it works on already-published archives and stays
    // controllable from the main repo.
    onReady(wireCliNavFilter);

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

  function onReady(fn) {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", fn);
    else fn();
  }

  // Inject a substring filter above the trimmed CLI-archive command list. No-op anywhere the
  // list isn't present (so it's safe to call unconditionally), and idempotent.
  function wireCliNavFilter() {
    var ul = document.querySelector("ul.vdocs-cli-nav");
    if (!ul || ul.parentNode.querySelector(".vdocs-cli-filter")) return;
    ensureCss();
    var input = document.createElement("input");
    input.type = "search";
    input.className = "vdocs-cli-filter";
    input.placeholder = "Filter commands…";
    input.setAttribute("aria-label", "Filter commands");
    ul.parentNode.insertBefore(input, ul);
    var items = [].slice.call(ul.getElementsByTagName("li"));
    input.addEventListener("input", function () {
      var q = input.value.trim().toLowerCase();
      for (var i = 0; i < items.length; i++) {
        var t = (items[i].textContent || "").toLowerCase();
        items[i].style.display = !q || t.indexOf(q) !== -1 ? "" : "none";
      }
    });
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

  function controlEl(cfg, manifest, label) {
    var ctrl = document.createElement("span");
    ctrl.className = "vdocs-control";
    ctrl.appendChild(labelEl());
    ctrl.appendChild(buildSelect(cfg, manifest, label));
    return ctrl;
  }

  function render(cfg, manifest) {
    ensureCss();
    var label = manifest.label || cfg.tool;
    var mount = document.querySelector("[data-vdocs-mount]");

    if (mount) {
      // Live page with an explicit mount (CLI command pages): quiet inline control.
      var wrap = document.createElement("span");
      wrap.className = "vdocs-inline";
      wrap.appendChild(controlEl(cfg, manifest, label));
      mount.appendChild(wrap);
      return;
    }
    // No mount — archives and live SDK pages in their own generator themes: top bar.
    renderTopBar(cfg, manifest, label);
  }

  function renderTopBar(cfg, manifest, label) {
    var bar = document.createElement("div");
    bar.className = "vdocs-bar vdocs-bar--" + (cfg.mode === "archive" ? "archive" : "latest");

    var msg = document.createElement("span");
    msg.className = "vdocs-bar-text";
    if (cfg.mode === "archive") {
      msg.textContent = "You are viewing docs for " + label + " " + cfg.version + ".";
      bar.appendChild(msg);
      var latest = manifest.versions.find(function (e) { return e.latest; });
      if (latest) {
        var a = document.createElement("a");
        a.className = "vdocs-bar-link";
        a.href = cfg.liveRoot + cfg.rel;
        a.textContent = "View latest";
        a.addEventListener("click", function (ev) {
          ev.preventDefault();
          navigate(cfg.liveRoot, cfg.rel);
        });
        bar.appendChild(a);
      }
    } else {
      msg.textContent = label + " — latest version";
      bar.appendChild(msg);
    }

    bar.appendChild(controlEl(cfg, manifest, label));
    document.body.insertBefore(bar, document.body.firstChild);

    // Reserve space so the fixed bar never overlaps content or a theme's fixed chrome.
    // Measured (not hard-coded) so a wrapped two-line bar on narrow viewports still fits.
    var root = document.documentElement;
    root.classList.add("vdocs-has-bar");
    var applyHeight = function () {
      root.style.setProperty("--vdocs-bar-h", bar.offsetHeight + "px");
    };
    applyHeight();
    // The stylesheet that gives the bar its real height (/js/versioned-docs.css) is
    // injected asynchronously, so the first measurement runs against an unstyled bar and
    // reserves too little space. Re-measure whenever the bar's box actually changes — when
    // the CSS applies, web fonts load, the bar wraps, or the viewport resizes — so the gap
    // always matches what's painted. ResizeObserver fires on the initial observe too.
    if (window.ResizeObserver) {
      new ResizeObserver(applyHeight).observe(bar);
    } else {
      if (window.addEventListener) {
        window.addEventListener("load", applyHeight);
        var css = document.querySelector("link[data-vdocs-css]");
        if (css) css.addEventListener("load", applyHeight);
      }
      if (window.requestAnimationFrame) window.requestAnimationFrame(applyHeight);
    }
    if (window.addEventListener) window.addEventListener("resize", applyHeight);
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
