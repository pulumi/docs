(function () {
    "use strict";

    var REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;

    var hero = document.getElementById("cjs26-hero");
    if (!hero) return;

    // Scroll parallax pushes layers down (positive Y) so the foreground's
    // bottom extends past the hero edge instead of retracting up and exposing
    // the background beneath it.
    var PARALLAX = {
        bg: { mouse: 2, scroll: 0.04 },
        fg: { mouse: 5, scroll: 0.09 },
    };

    var layers = [].slice.call(hero.querySelectorAll("[data-cjs26-parallax]")).map(function (el) {
        var p = PARALLAX[el.dataset.cjs26Parallax] || { mouse: 0, scroll: 0 };
        return { el: el, mouse: p.mouse, scroll: p.scroll };
    });

    var mx = 0, my = 0, sy = 0, raf = null;

    function applyParallax() {
        for (var i = 0; i < layers.length; i++) {
            var l = layers[i];
            var x = -mx * l.mouse;
            var y = -my * l.mouse + sy * l.scroll;
            l.el.style.transform = "translate3d(" + x.toFixed(2) + "px," + y.toFixed(2) + "px,0)";
        }
        raf = null;
    }
    function schedule() { if (!raf) raf = requestAnimationFrame(applyParallax); }

    if (!REDUCED) {
        hero.addEventListener("mousemove", function (e) {
            var r = hero.getBoundingClientRect();
            mx = (e.clientX - r.left - r.width / 2) / r.width;
            my = (e.clientY - r.top - r.height / 2) / r.height;
            schedule();
        }, { passive: true });
        hero.addEventListener("mouseleave", function () { mx = 0; my = 0; schedule(); });
        window.addEventListener("scroll", function () {
            sy = window.scrollY;
            schedule();
        }, { passive: true });
    }

    var ufo = document.getElementById("cjs26-ufo");
    var ufoBounds = document.getElementById("cjs26-ufo-bounds");

    // TODO: lengthen once approved — short cadence is for dev visibility.
    var UFO_INTERVAL = { min: 4000, max: 9000 };

    function rand(a, b) { return a + Math.random() * (b - a); }

    function scheduleUfo() {
        setTimeout(flyUfo, rand(UFO_INTERVAL.min, UFO_INTERVAL.max));
    }

    function flyUfo() {
        if (!ufo || !ufoBounds) return;
        var br = ufoBounds.getBoundingClientRect();
        var w = br.width, h = br.height;
        if (w <= 0 || h <= 0) { scheduleUfo(); return; }
        var ufoW = ufo.getBoundingClientRect().width || 60;

        var leftToRight = Math.random() < 0.5;
        var startX = leftToRight ? -ufoW : w;
        var endX   = leftToRight ?  w   : -ufoW;
        var startY = h * rand(0.15, 0.7);
        var endY   = h * rand(0.15, 0.7);
        var midX   = (startX + endX) / 2;
        var midY   = (startY + endY) / 2 - h * rand(0, 0.15);
        var peak   = rand(0.55, 1.1);
        var baseRot = (leftToRight ? 1 : -1) * rand(2, 6);
        var wobble  = rand(18, 28);

        function kf(x, y, scale, rot, blur, opacity, offset) {
            return {
                transform: "translate3d(" + x.toFixed(1) + "px," + y.toFixed(1) + "px,0) scale(" + scale.toFixed(3) + ") rotate(" + rot.toFixed(1) + "deg)",
                filter: "blur(" + blur.toFixed(2) + "px)",
                opacity: opacity,
                offset: offset,
            };
        }

        var dur = rand(5500, 8500);
        // fill:forwards keeps the final keyframe (scale 0, opacity 0) until
        // the next flight replaces it.
        ufo.animate([
            kf(startX,             startY,             0,           baseRot - wobble,       6, 0,   0),
            kf((startX + midX) / 2, (startY + midY) / 2, peak * 0.45, baseRot + wobble * 0.5, 4, 0.6, 0.25),
            kf(midX,               midY,               peak,        baseRot - wobble * 0.3, 1, 1,   0.5),
            kf((midX + endX) / 2,   (midY + endY) / 2,   peak * 0.45, baseRot + wobble * 0.3, 4, 0.5, 0.75),
            kf(endX,               endY,               0,           baseRot - wobble,       6, 0,   1),
        ], { duration: dur, easing: "ease-in-out", fill: "forwards" }).onfinish = scheduleUfo;

        // Once the user is logged in, every flyby pings the log at the peak.
        if (state === "app") {
            setTimeout(function () { pushLog(pickRandom(UFO_LOGS)); }, dur * 0.45);
        }
    }

    if (!REDUCED && ufo && ufoBounds) {
        scheduleUfo();
    }

    var termOut = document.getElementById("cjs26-terminal-out");
    var keysInput = document.getElementById("cjs26-keys");
    if (!termOut) return;

    // Measure the parent — termOut's getBoundingClientRect would return its
    // post-matrix3d size and the warp needs the unwarped width/height.
    var termContainer = document.getElementById("cjs26-terminal");
    function updateTerminalSize() {
        if (!termContainer) return;
        var w = termContainer.clientWidth;
        var h = termContainer.clientHeight;
        if (w <= 0 || h <= 0) return;
        termOut.style.setProperty("--cjs26-w", w);
        termOut.style.setProperty("--cjs26-h", h);
    }
    updateTerminalSize();
    if (typeof ResizeObserver !== "undefined" && termContainer) {
        new ResizeObserver(updateTerminalSize).observe(termContainer);
    } else {
        window.addEventListener("resize", updateTerminalSize);
    }

    var PASSWORD = "W4TCHTHECL0UDS";
    var FIELD_WIDTH = 36; // chars between "ENTER PASSCODE:  " and the trailing "  ║"

    var state = "booting"; // booting | ready | granted | denied
    var typed = "";

    var BOOT = [
        "",
        "> CLOUD-WATCHER V6.26 (BUILD 2026.03.CASCADIA)",
        "> RESOLVING PROVIDERS.............. OK",
        "> HYDRATING SKY STATE......... 1.4 MIB",
        "> CALIBRATING SENSOR ARRAY... 12 NODES",
        "> UPLINK CAS-SEA-1.............. 24 MS",
        "> [READY]",
        "",
    ];

    function sleep(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }

    // Pad/truncate msg to the 57-char inner box width and wrap with ║.
    function centerInField(msg) {
        var content = " " + msg + " ";
        if (content.length > 57) content = content.slice(0, 57);
        var pad = 57 - content.length;
        var left = Math.floor(pad / 2);
        var right = pad - left;
        return "║" + " ".repeat(left) + content + " ".repeat(right) + "║";
    }

    function escapeHTML(s) {
        return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }

    function passcodeLineHTML() {
        if (state === "granted") return escapeHTML(centerInField("✧ ACCESS GRANTED — WELCOME WATCHER ✧"));
        if (state === "denied")  return escapeHTML(centerInField("!! ACCESS DENIED !!"));
        var remaining = "▓".repeat(Math.max(0, FIELD_WIDTH - typed.length));
        return escapeHTML("║ ENTER PASSCODE:  " + typed) +
               '<span class="cjs26-caret">_</span>' +
               escapeHTML(remaining + "  ║");
    }

    function renderFrameHTML() {
        var lines = [
            "╔═════════════════════════════════════════════════════════╗",
            "║ CLOUD WATCHER 3000                                v6.26 ║",
            "║                                                         ║",
            "║ PULUMI CLOUD WATCHERS CLUB   *OFFICIAL MEMBER USE ONLY* ║",
            "╠═════════════════════════════════════════════════════════╣",
            "║                                                         ║",
            "║ [STATUS]  ◉ ONLINE   ◉ ENCRYPTED   ◌ STANDBY            ║",
            "║                                                         ║",
            "║                                                         ║",
            null, // passcode line — rendered via passcodeLineHTML below.
            "║                                                         ║",
            "╚═════════════════════════════════════════════════════════╝",
        ];
        var html = lines.map(function (l) {
            return l === null ? passcodeLineHTML() : escapeHTML(l);
        }).join("\n");
        termOut.innerHTML = html;
    }

    // ---- App (post-login) — radar sweep on the left, log feed on the right. ----
    var RADAR_W = 25, RADAR_H = 9, LOG_W = 29;
    // Fired when a UFO flies by — all should read as a sighting event.
    var UFO_LOGS = [
        "DRIFT DETECTED!",
        "ANOMALY DETECTED!",
        "UNKNOWN CRAFT!",
        "STELLAR DRIFT!",
        "WATCHER ALERT!",
        "INCURSION DETECTED!",
        "RADAR CONTACT!",
    ];
    // Fired on an idle cadence between sightings — ambient infra chatter.
    var AMBIENT_LOGS = [
        "STACK UPDATED",
        "STATE LOCKED",
        "PROVIDER PINGED",
        "HEARTBEAT OK",
        "POLICY MATCH",
        "ENCRYPTION OK",
        "TELEMETRY OK",
        "CONFIG SYNCED",
        "STATE STORE OK",
        "CHANNEL ENCRYPTED",
    ];
    var appLogs = [];
    var appInterval = null;
    var ambientTimer = null;
    var appStartTime = 0;

    function fmtTime(d) {
        var pad = function (n) { return String(n).padStart(2, "0"); };
        return pad(d.getHours()) + ":" + pad(d.getMinutes()) + ":" + pad(d.getSeconds());
    }
    function pushLog(msg) {
        var line = "[" + fmtTime(new Date()) + "] " + msg;
        appLogs.push(line.slice(0, LOG_W));
        if (appLogs.length > RADAR_H) appLogs.shift();
    }
    function pickRandom(pool) {
        return pool[Math.floor(Math.random() * pool.length)];
    }
    function scheduleAmbient() {
        clearTimeout(ambientTimer);
        ambientTimer = setTimeout(function () {
            if (state !== "app") return;
            pushLog(pickRandom(AMBIENT_LOGS));
            scheduleAmbient();
        }, rand(3000, 7000));
    }

    function renderRadar(angle) {
        var grid = [];
        for (var y = 0; y < RADAR_H; y++) {
            grid.push(Array(RADAR_W).fill(" "));
        }
        var cx = 12, cy = 4, rx = 11, ry = 4;
        // Outer ring.
        for (var t = 0; t < Math.PI * 2; t += 0.07) {
            var rx_x = Math.round(cx + rx * Math.cos(t));
            var ry_y = Math.round(cy + ry * Math.sin(t));
            if (rx_x >= 0 && rx_x < RADAR_W && ry_y >= 0 && ry_y < RADAR_H) {
                grid[ry_y][rx_x] = "·";
            }
        }
        // Sweep line — brighter toward the tip.
        for (var r = 1; r <= rx; r++) {
            var sx = Math.round(cx + r * Math.cos(angle));
            var sy = Math.round(cy + r * (ry / rx) * Math.sin(angle));
            if (sx >= 0 && sx < RADAR_W && sy >= 0 && sy < RADAR_H) {
                grid[sy][sx] = r >= rx - 1 ? "*" : ":";
            }
        }
        grid[cy][cx] = "+";
        return grid.map(function (row) { return row.join(""); });
    }

    function renderAppHTML() {
        var angle = (Date.now() - appStartTime) * 0.003;
        var radar = renderRadar(angle);
        var lines = [
            "╔═════════════════════════════════════════════════════════╗",
            "║ CLOUD WATCHER 3000                                v6.26 ║",
            "╠═════════════════════════════════════════════════════════╣",
        ];
        for (var i = 0; i < RADAR_H; i++) {
            var radarRow = radar[i] || " ".repeat(RADAR_W);
            var logRow = appLogs[i] || "";
            logRow = logRow + " ".repeat(Math.max(0, LOG_W - logRow.length));
            lines.push("║" + radarRow + " │ " + logRow + "║");
        }
        lines.push("╚═════════════════════════════════════════════════════════╝");
        termOut.textContent = lines.join("\n");
    }

    function startApp() {
        state = "app";
        appStartTime = Date.now();
        appLogs = [];
        pushLog("SYSTEM ONLINE");
        pushLog("SCAN INITIATED");
        renderAppHTML();
        if (appInterval) clearInterval(appInterval);
        appInterval = setInterval(renderAppHTML, 200);
        scheduleAmbient();
    }

    async function bootSequence() {
        var buf = [];
        for (var i = 0; i < BOOT.length; i++) {
            var line = BOOT[i];
            buf.push("");
            if (line === "") {
                termOut.textContent = buf.join("\n");
                await sleep(120);
                continue;
            }
            for (var j = 0; j <= line.length; j++) {
                buf[buf.length - 1] = line.slice(0, j);
                termOut.textContent = buf.join("\n");
                await sleep(22);
            }
            await sleep(line === "> [READY]" ? 600 : 220);
        }
        await sleep(500);
        state = "ready";
        renderFrameHTML();
    }

    function handleKey(e) {
        if (state !== "ready") return;
        var k = e.key;
        if (k === "Enter") {
            e.preventDefault();
            if (typed.toUpperCase() === PASSWORD) {
                state = "granted";
                renderFrameHTML();
                setTimeout(startApp, 2200);
            } else {
                state = "denied";
                renderFrameHTML();
                setTimeout(function () {
                    typed = "";
                    if (keysInput) keysInput.value = "";
                    state = "ready";
                    renderFrameHTML();
                }, 1600);
            }
            return;
        }
        // When the hidden input has focus, its "input" handler covers character
        // insertion and Backspace via value changes — skip them here to avoid
        // double-recording. Enter doesn't change the value, so it's handled above.
        if (e.target === keysInput) return;
        if (k === "Backspace") {
            e.preventDefault();
            if (typed.length > 0) {
                typed = typed.slice(0, -1);
                if (keysInput) keysInput.value = typed;
                renderFrameHTML();
            }
            return;
        }
        if (k && k.length === 1 && /[A-Za-z0-9!@#$%^&*\-_]/.test(k)) {
            if (typed.length < FIELD_WIDTH) {
                typed += k.toUpperCase();
                if (keysInput) keysInput.value = typed;
                renderFrameHTML();
            }
        }
    }

    document.addEventListener("keydown", handleKey);

    // Mobile soft-keyboard path: sync the hidden input back into our state.
    if (keysInput) {
        keysInput.addEventListener("input", function () {
            if (state !== "ready") return;
            typed = (keysInput.value || "").toUpperCase().slice(0, FIELD_WIDTH);
            renderFrameHTML();
        });

        // Any tap inside the hero focuses the hidden input so mobile soft
        // keyboards pop up. focus() must run inside the gesture handler.
        hero.addEventListener("click", function () {
            if (state === "ready") keysInput.focus();
        });
    }

    bootSequence();
})();
