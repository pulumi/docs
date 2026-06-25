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
    // client-side filter over it, and re-create the live site's "Copy Page" markdown menu.
    // Both are independent of the manifest and injected by the loader (not baked into the
    // snapshot) so they work on already-published archives and stay controllable from the
    // main repo.
    onReady(function () {
      wireCliNavFilter();
      wireCliCopyMenu(cfg);
    });

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

  // Re-create the live site's "Copy Page" menu on CLI archive pages. That menu is the
  // pulumi-llm-menu web component (theme/stencil/src/components/llm-menu), compiled into the
  // site JS bundle — which snapshots strip, so the bare element never upgrades. But every
  // archived page publishes its markdown sibling (index.md) next to index.html, so the menu's
  // actions still work against the snapshot's own files. We rebuild the component's exact DOM
  // and classes here, so the shared archive theme bundle (/css/versioned-docs-archive.css,
  // which carries the .llm-menu-* styles) renders it identically. Only on archive pages that
  // have the CLI right-rail; idempotent.
  function wireCliCopyMenu(cfg) {
    if (cfg.mode !== "archive") return;
    var rail = document.querySelector(".docs-table-of-contents.docs-toc-desktop");
    if (!rail || document.querySelector(".vdocs-copy-menu")) return;
    ensureCss();
    // The page's own markdown lives at <dir>/index.md, same origin as the archive.
    var md = location.origin + location.pathname.replace(/\/?$/, "/") + "index.md";
    var prompt = "Read from " + md + " so I can ask questions about it.";

    var container = el("div", "llm-menu-container");
    var trigger = el("button", "llm-menu-trigger text-gray-600 hover:text-gray-700 text-xs");
    trigger.type = "button";
    trigger.innerHTML = ICON.copy("ph-icon ph-icon--regular mr-2") + "Copy Page" +
      ICON.chevron("ph-icon ph-icon--bold vdocs-copy-chevron");

    var dropdown = el("div", "llm-menu-dropdown");
    dropdown.style.display = "none";
    dropdown.appendChild(menuItem(ICON.link(), "Copy URL", "Copy page link to share", "", function (t) {
      copyText(location.href, t, "Copy URL");
    }));
    dropdown.appendChild(menuItem(ICON.copy("llm-menu-icon"), "Copy as Markdown", "Copy page for LLMs", "", function (t) {
      fetch(md, { credentials: "omit" })
        .then(function (r) { if (!r.ok) throw new Error(); return r.text(); })
        .then(function (text) { return navigator.clipboard.writeText(text); })
        .then(function () { flash(t, "Copy as Markdown"); })
        .catch(function () {});
    }));
    dropdown.appendChild(menuItem(ICON.markdown(), "View as Markdown", "Open Markdown in new tab", ICON.external(), function () {
      window.open(md, "_blank");
    }));
    dropdown.appendChild(document.createElement("hr"));
    dropdown.appendChild(menuItem(ICON.chatgpt(), "Open in ChatGPT", "Ask ChatGPT about this page", ICON.external(), function () {
      window.open("https://chat.openai.com/?q=" + encodeURIComponent(prompt), "_blank");
    }));
    dropdown.appendChild(menuItem(ICON.claude(), "Open in Claude", "Ask Claude about this page", ICON.external(), function () {
      window.open("https://claude.ai/new?q=" + encodeURIComponent(prompt), "_blank");
    }));

    var open = false;
    function setOpen(v) {
      open = v;
      dropdown.style.display = open ? "" : "none";
      trigger.classList.toggle("vdocs-copy-open", open);
    }
    trigger.addEventListener("click", function (e) { e.stopPropagation(); setOpen(!open); });
    document.addEventListener("click", function (e) { if (open && !container.contains(e.target)) setOpen(false); });

    container.appendChild(trigger);
    container.appendChild(dropdown);
    // Match the live placement: a feedback-style list directly below the ToC. Insert it INSIDE
    // the sticky desktop rail, right after the ToC accordion, so it tracks the ToC instead of
    // being pushed down by the rail's 90vh height (which happens if it's a trailing sibling).
    var wrap = el("ul", "p-0 list-none table-of-contents-feedback vdocs-copy-menu");
    var liEl = document.createElement("li");
    liEl.appendChild(container);
    wrap.appendChild(liEl);
    var toc = rail.querySelector(".table-of-contents");
    if (toc) toc.parentNode.insertBefore(wrap, toc.nextSibling);
    else rail.appendChild(wrap);
  }

  function el(tag, cls) { var e = document.createElement(tag); if (cls) e.className = cls; return e; }

  function menuItem(iconHtml, title, subtitle, externalHtml, onClick) {
    var b = el("button", "llm-menu-item");
    b.type = "button";
    b.innerHTML = iconHtml + '<div class="llm-menu-text"><div class="llm-menu-title"></div>' +
      '<div class="llm-menu-subtitle"></div></div>' + (externalHtml || "");
    b.querySelector(".llm-menu-title").textContent = title;     // textContent: never inject raw strings
    b.querySelector(".llm-menu-subtitle").textContent = subtitle;
    var titleEl = b.querySelector(".llm-menu-title");
    b.addEventListener("click", function (e) { e.stopPropagation(); onClick(titleEl); });
    return b;
  }

  function copyText(text, titleEl, label) {
    if (!navigator.clipboard) return;
    navigator.clipboard.writeText(text).then(function () { flash(titleEl, label); }).catch(function () {});
  }
  function flash(titleEl, label) {
    titleEl.textContent = "Copied!";
    setTimeout(function () { titleEl.textContent = label; }, 2000);
  }

  // SVG icons lifted verbatim from the pulumi-llm-menu component so the menu reads identically.
  function svg(cls, vb, inner, fill) {
    return '<svg class="' + cls + '" viewBox="' + vb + '" fill="' + (fill || "currentColor") +
      '" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">' + inner + '</svg>';
  }
  var ICON = {
    copy: function (cls) { return svg(cls || "llm-menu-icon", "0 0 256 256", '<path d="M216,32H88a8,8,0,0,0-8,8V80H40a8,8,0,0,0-8,8V216a8,8,0,0,0,8,8H168a8,8,0,0,0,8-8V176h40a8,8,0,0,0,8-8V40A8,8,0,0,0,216,32ZM160,208H48V96H160Zm48-48H176V88a8,8,0,0,0-8-8H96V48H208Z"/>'); },
    chevron: function (cls) { return svg(cls, "0 0 256 256", '<path d="M216.49,104.49l-80,80a12,12,0,0,1-17,0l-80-80a12,12,0,0,1,17-17L128,159l71.51-71.52a12,12,0,0,1,17,17Z"/>'); },
    external: function () { return svg("ph-icon ph-icon--regular llm-menu-external", "0 0 256 256", '<path d="M224,104a8,8,0,0,1-16,0V59.32l-66.33,66.34a8,8,0,0,1-11.32-11.32L196.68,48H152a8,8,0,0,1,0-16h64a8,8,0,0,1,8,8Zm-40,24a8,8,0,0,0-8,8v72H48V80h72a8,8,0,0,0,0-16H48A16,16,0,0,0,32,80V208a16,16,0,0,0,16,16H176a16,16,0,0,0,16-16V136A8,8,0,0,0,184,128Z"/>'); },
    link: function () { return svg("llm-menu-icon", "0 0 24 24", '<path d="M9.172 14.828L14.828 9.172M7.05 11.293L4.222 14.121C2.562 15.781 2.562 18.439 4.222 20.099C5.882 21.759 8.54 21.759 10.2 20.099L13.029 17.271M10.971 6.729L13.8 3.901C15.46 2.241 18.118 2.241 19.778 3.901C21.438 5.561 21.438 8.219 19.778 9.879L16.95 12.707" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>', "none"); },
    markdown: function () { return svg("llm-menu-icon", "0 0 16 16", '<path d="M14 3a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h12zM2 2a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H2z"/><path d="M9.146 8.146a.5.5 0 0 1 .708 0L11.5 9.793l1.646-1.647a.5.5 0 0 1 .708.708l-2 2a.5.5 0 0 1-.708 0l-2-2a.5.5 0 0 1 0-.708zM11.5 5a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-1 0v-4a.5.5 0 0 1 .5-.5zM3.56 11V5.01h1.44L6.5 7.98 8 5.01h1.44V11H8.2V6.57L6.5 9.56l-1.7-2.99V11H3.56z"/>'); },
    chatgpt: function () { return svg("llm-menu-icon", "0 0 320 320", '<path d="m297.06 130.97c7.26-21.79 4.76-45.66-6.85-65.48-17.46-30.4-52.56-46.04-86.84-38.68-15.25-17.18-37.16-26.95-60.13-26.81-35.04-.08-66.13 22.48-76.91 55.82-22.51 4.61-41.94 18.7-53.31 38.67-17.59 30.32-13.58 68.54 9.92 94.54-7.26 21.79-4.76 45.66 6.85 65.48 17.46 30.4 52.56 46.04 86.84 38.68 15.24 17.18 37.16 26.95 60.13 26.8 35.06.09 66.16-22.49 76.94-55.86 22.51-4.61 41.94-18.7 53.31-38.67 17.57-30.32 13.55-68.51-9.94-94.51zm-120.28 168.11c-14.03.02-27.62-4.89-38.39-13.88.49-.26 1.34-.73 1.89-1.07l63.72-36.8c3.26-1.85 5.26-5.32 5.24-9.07v-89.83l26.93 15.55c.29.14.48.42.52.74v74.39c-.04 33.08-26.83 59.9-59.91 59.97zm-128.84-55.03c-7.03-12.14-9.56-26.37-7.15-40.18.47.28 1.3.79 1.89 1.13l63.72 36.8c3.23 1.89 7.23 1.89 10.47 0l77.79-44.92v31.1c.02.32-.13.63-.38.83l-64.41 37.19c-28.69 16.52-65.33 6.7-81.92-21.95zm-16.77-139.09c7-12.16 18.05-21.46 31.21-26.29 0 .55-.03 1.52-.03 2.2v73.61c-.02 3.74 1.98 7.21 5.23 9.06l77.79 44.91-26.93 15.55c-.27.18-.61.21-.91.08l-64.42-37.22c-28.63-16.58-38.45-53.21-21.95-81.89zm221.26 51.49-77.79-44.92 26.93-15.54c.27-.18.61-.21.91-.08l64.42 37.19c28.68 16.57 38.51 53.26 21.94 81.94-7.01 12.14-18.05 21.44-31.2 26.28v-75.81c.03-3.74-1.96-7.2-5.2-9.06zm26.8-40.34c-.47-.29-1.3-.79-1.89-1.13l-63.72-36.8c-3.23-1.89-7.23-1.89-10.47 0l-77.79 44.92v-31.1c-.02-.32.13-.63.38-.83l64.41-37.16c28.69-16.55 65.37-6.7 81.91 22 6.99 12.12 9.52 26.31 7.15 40.1zm-168.51 55.43-26.94-15.55c-.29-.14-.48-.42-.52-.74v-74.39c.02-33.12 26.89-59.96 60.01-59.94 14.01 0 27.57 4.92 38.34 13.88-.49.26-1.33.73-1.89 1.07l-63.72 36.8c-3.26 1.85-5.26 5.31-5.24 9.06l-.04 89.79zm14.63-31.54 34.65-20.01 34.65 20v40.01l-34.65 20-34.65-20z"/>'); },
    claude: function () { return svg("llm-menu-icon", "0 0 1200 1200", '<path d="M 233.959793 800.214905 L 468.644287 668.536987 L 472.590637 657.100647 L 468.644287 650.738403 L 457.208069 650.738403 L 417.986633 648.322144 L 283.892639 644.69812 L 167.597321 639.865845 L 54.926208 633.825623 L 26.577238 627.785339 L 3.3e-05 592.751709 L 2.73832 575.27533 L 26.577238 559.248352 L 60.724873 562.228149 L 136.187973 567.382629 L 249.422867 575.194763 L 331.570496 580.026978 L 453.261841 592.671082 L 472.590637 592.671082 L 475.328857 584.859009 L 468.724915 580.026978 L 463.570557 575.194763 L 346.389313 495.785217 L 219.543671 411.865906 L 153.100723 363.543762 L 117.181267 339.060425 L 99.060455 316.107361 L 91.248367 266.01355 L 123.865784 230.093994 L 167.677887 233.073853 L 178.872513 236.053772 L 223.248367 270.201477 L 318.040283 343.570496 L 441.825592 434.738342 L 459.946411 449.798706 L 467.194672 444.64447 L 468.080597 441.020203 L 459.946411 427.409485 L 392.617493 305.718323 L 320.778564 181.932983 L 288.80542 130.630859 L 280.348999 99.865845 C 277.369171 87.221436 275.194641 76.590698 275.194641 63.624268 L 312.322174 13.20813 L 332.8591 6.604126 L 382.389313 13.20813 L 403.248352 31.328979 L 434.013519 101.71814 L 483.865753 212.537048 L 561.181274 363.221497 L 583.812134 407.919434 L 595.892639 449.315491 L 600.40271 461.959839 L 608.214783 461.959839 L 608.214783 454.711609 L 614.577271 369.825623 L 626.335632 265.61084 L 637.771851 131.516846 L 641.718201 93.745117 L 660.402832 48.483276 L 697.530334 24.000122 L 726.52356 37.852417 L 750.362549 72 L 747.060486 94.067139 L 732.886047 186.201416 L 705.100708 330.52356 L 686.979919 427.167847 L 697.530334 427.167847 L 709.61084 415.087341 L 758.496704 350.174561 L 840.644348 247.490051 L 876.885925 206.738342 L 919.167847 161.71814 L 946.308838 140.29541 L 997.61084 140.29541 L 1035.38269 196.429626 L 1018.469849 254.416199 L 965.637634 321.422852 L 921.825562 378.201538 L 859.006714 462.765259 L 819.785278 530.41626 L 823.409424 535.812073 L 832.75177 534.92627 L 974.657776 504.724915 L 1051.328979 490.872559 L 1142.818848 475.167786 L 1184.214844 494.496582 L 1188.724854 514.147644 L 1172.456421 554.335693 L 1074.604126 578.496765 L 959.838989 601.449829 L 788.939636 641.879272 L 786.845764 643.409485 L 789.261841 646.389343 L 866.255127 653.637634 L 899.194702 655.409424 L 979.812134 655.409424 L 1129.932861 666.604187 L 1169.154419 692.537109 L 1192.671265 724.268677 L 1188.724854 748.429688 L 1128.322144 779.194641 L 1046.818848 759.865845 L 856.590759 714.604126 L 791.355774 698.335754 L 782.335693 698.335754 L 782.335693 703.731567 L 836.69812 756.885986 L 936.322205 846.845581 L 1061.073975 962.81897 L 1067.436279 991.490112 L 1051.409424 1014.120911 L 1034.496704 1011.704712 L 924.885986 929.234924 L 882.604126 892.107544 L 786.845764 811.48999 L 780.483276 811.48999 L 780.483276 819.946289 L 802.550415 852.241699 L 919.087341 1027.409424 L 925.127625 1081.127686 L 916.671204 1098.604126 L 886.469849 1109.154419 L 853.288696 1103.114136 L 785.073914 1007.355835 L 714.684631 899.516785 L 657.906067 802.872498 L 650.979858 806.81897 L 617.476624 1167.704834 L 601.771851 1186.147705 L 565.530212 1200 L 535.328857 1177.046997 L 519.302124 1139.919556 L 535.328857 1066.550537 L 554.657776 970.792053 L 570.362488 894.68457 L 584.536926 800.134277 L 592.993347 768.724976 L 592.429626 766.630859 L 585.503479 767.516968 L 514.22821 865.369263 L 405.825531 1011.865906 L 320.053711 1103.677979 L 299.516815 1111.812256 L 263.919525 1093.369263 L 267.221497 1060.429688 L 287.114136 1031.114136 L 405.825531 880.107361 L 477.422913 786.52356 L 523.651062 732.483276 L 523.328918 724.671265 L 520.590698 724.671265 L 205.288605 929.395935 L 149.154434 936.644409 L 124.993355 914.01355 L 127.973183 876.885986 L 139.409409 864.80542 L 234.201385 799.570435 L 233.879227 799.8927 Z"/>'); }
  };

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
