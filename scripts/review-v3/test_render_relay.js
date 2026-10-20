// The board's comment relay, exercised in jsdom against a fake
// `claude.use("comments")`: what the page sends on each button, and what it
// does when there is no capability, no session, or a refused send.
//
// Run by test_render.py (`test_the_relay_sends_only_what_the_board_composed`);
// runnable by hand too:
//
//   node scripts/review-v3/test_render_relay.js BOARD.html '{"digest":"…","thread":"t1","stamp":"11"}'
"use strict";
const fs = require("fs");
const path = require("path");
const { JSDOM } = require(path.join(process.cwd(), "node_modules", "jsdom"));

const html = fs.readFileSync(process.argv[2], "utf8");
const want = JSON.parse(process.argv[3]);
const tick = () => new Promise((r) => setTimeout(r, 30));

let failures = 0;
function expect(name, got, exp) {
  if (JSON.stringify(got) === JSON.stringify(exp)) { console.log(`  ok: ${name}`); return; }
  failures++;
  console.error(`  FAIL: ${name}\n    got:  ${JSON.stringify(got)}\n    want: ${JSON.stringify(exp)}`);
}

function board({ claude, avail = "available", reject = null } = {}) {
  const sent = [];
  const comments = {
    canSendToClaude: () => Promise.resolve(avail),
    anchorFor: () => Promise.resolve({ path: "body", x: 1, y: 1 }),
    sendToClaude: (t) => { sent.push(t); return reject ? Promise.reject({ code: reject, message: reject }) : Promise.resolve({ threadId: "new", commentId: "c" }); },
  };
  const dom = new JSDOM(html, {
    runScripts: "dangerously",
    beforeParse(w) { if (claude !== false) w.claude = { use: (n) => Promise.resolve(n === "comments" ? comments : null) }; },
  });
  const d = dom.window.document;
  const click = (el) => el.dispatchEvent(new dom.window.MouseEvent("click", { bubbles: true }));
  return { d, sent, click, $: (id) => d.getElementById(id) };
}

(async () => {
  // 1. Served without the capability (or a saved copy): the worksheet it always was.
  {
    const b = board({ claude: false });
    await tick();
    expect("no capability: send hidden", b.$("relayrun").hidden, true);
    expect("no capability: refresh hidden", b.$("relayrefresh").hidden, true);
    expect("no capability: confirm stays disabled", b.d.querySelector('[data-relay="confirm"]').disabled, true);
  }

  // 2. A watching session: the composed command goes out verbatim, behind the header.
  {
    const b = board();
    await tick();
    expect("available: send shown", b.$("relayrun").hidden, false);
    expect("available: send enabled", b.$("relayrun").disabled, false);
    b.click(b.$("relayrun"));
    await tick();
    expect("send carries the composed command", b.sent.map((t) => t.text), [`pr-review relay: plan\n/pr-review --act --stamp ${want.stamp}`]);
    expect("a new thread, anchored on the page", !!b.sent[0].anchor, true);
    expect("buttons stay disabled while the session works", b.$("relayrun").disabled, true);
  }

  // 3. Confirm replies into the plan's thread with the digest the server rendered -- nothing else.
  {
    const b = board();
    await tick();
    b.click(b.d.querySelector('[data-relay="confirm"]'));
    await tick();
    expect("confirm sends the digest into the plan's thread", b.sent, [{ threadId: want.thread, text: `pr-review relay: confirm ${want.digest}` }]);
  }

  // 4. Discard and refresh.
  {
    const b = board();
    await tick();
    b.click(b.d.querySelector('[data-relay="cancel"]'));
    await tick();
    expect("discard names the digest", b.sent.map((t) => t.text), [`pr-review relay: cancel ${want.digest}`]);
    const r = board();
    await tick();
    r.click(r.$("relayrefresh"));
    await tick();
    expect("refresh sends refresh", r.sent.map((t) => t.text), ["pr-review relay: refresh"]);
  }

  // 5. Nothing lit: refused on the page, nothing sent.
  {
    const b = board();
    await tick();
    b.click(b.$("clear"));
    b.click(b.$("relayrun"));
    await tick();
    expect("nothing lit: nothing sent", b.sent.length, 0);
    expect("nothing lit: says so", /Nothing is lit/.test(b.$("relaystate").textContent), true);
  }

  // 6. No session watching: shown, disabled, with the reason.
  {
    const b = board({ avail: "no_session" });
    await tick();
    expect("no session: send disabled", b.$("relayrun").disabled, true);
    expect("no session: confirm disabled", b.d.querySelector('[data-relay="confirm"]').disabled, true);
    expect("no session: reason shown", /No Claude session/.test(b.$("relaystate").textContent), true);
  }

  // 7. A refused send says why and gives the buttons back.
  {
    const b = board({ reject: "claude_unavailable" });
    await tick();
    b.click(b.$("relayrun"));
    await tick();
    expect("refused: error shown", b.$("relaystate").classList.contains("err"), true);
    expect("refused: send usable again", b.$("relayrun").disabled, false);
  }

  if (failures) { console.error(`${failures} relay check(s) failed`); process.exit(1); }
  console.log("all relay checks passed");
})();
