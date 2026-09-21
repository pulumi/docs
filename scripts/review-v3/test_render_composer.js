// The board's command composer, exercised in jsdom: click the buttons a
// person would and check the command bar after every click.
//
// Run by test_render.py (`test_the_composer_reads_the_lit_buttons`) against a
// board it renders from a fixture queue; runnable by hand too:
//
//   node scripts/review-v3/test_render_composer.js BOARD.html '{"stamp":[11,12],...}'
//
// Needs jsdom, which is already a devDependency of the repo (`make ensure`).
// The scenarios are the ones an audit reproduced as defects: the bar running
// a click behind, several --stamp flags where act.py expects one, refresh /
// re-run not counting as decisions, the interactive handoff leaking into the
// --act command -- and the chain, the one decision that acts on two rows,
// which has to keep the row it covers and the lead's button in agreement.
// Each is a full click sequence, not a unit of the script.
"use strict";
const fs = require("fs");
const path = require("path");
const { JSDOM } = require(path.join(process.cwd(), "node_modules", "jsdom"));

const html = fs.readFileSync(process.argv[2], "utf8");
const prs = JSON.parse(process.argv[3]);   // {stamp:[bot, human], judge, route:[a,b], refresh, rerun, handfix, chain:[lead, next], team}
const dom = new JSDOM(html, { runScripts: "dangerously" });
const d = dom.window.document;

const cmd = () => d.getElementById("cmd").textContent;
const progress = () => d.getElementById("progress").textContent;
const btn = (pr, c) => {
  const b = [...d.querySelectorAll("button.btn[data-cmd]")].find((x) => x.dataset.pr == pr && x.dataset.cmd == c);
  if (!b) throw new Error(`no button ${pr} ${c}`);
  return b;
};
const click = (b) => b.dispatchEvent(new dom.window.MouseEvent("click", { bubbles: true }));
const clear = () => click(d.getElementById("clear"));
const rowOf = (pr) => d.querySelector(`.mrow[data-pr="${pr}"]`);
const covered = (pr) => !!rowOf(pr).querySelector(".claimnote");

let failures = 0;
function expect(name, got, want) {
  if (got === want) { console.log(`  ok: ${name}`); return; }
  failures++;
  console.error(`  FAIL: ${name}\n    got:  ${JSON.stringify(got)}\n    want: ${JSON.stringify(want)}`);
}

const [bot, human] = prs.stamp;
const [r1, r2] = prs.route;
const [lead, next] = prs.chain;
const route = (n) => `--route ${n}:${prs.team}`;
const TOTAL = 10;   // rows carrying a decision button

// Nothing on the page but rows: no batch strip, no card, no button whose
// fragment a row does not carry.
expect("no Do-next strip", d.querySelector(".donext"), null);
expect("no batch buttons", d.querySelectorAll("button[data-targets], button[data-claims]").length, 0);

// The defaults: every stamp row starts selected, folded into one --stamp.
expect("default command folds the stamp rows", cmd(), `$ /pr-review --act --stamp ${bot},${human}`);
expect("progress counts every row with a decision to make", progress(), `2 of ${TOTAL} decisions made`);

// 1. Routing two rows by hand says each fragment once, in PR order.
click(btn(r2, route(r2))); click(btn(r1, route(r1)));
expect("route rows compose in PR order", cmd(), `$ /pr-review --act --stamp ${bot},${human} ${route(r1)} ${route(r2)}`);
expect("route rows count as decided", progress(), `4 of ${TOTAL} decisions made`);
click(btn(r1, route(r1)));
expect("un-pressing a row drops only that fragment", cmd(), `$ /pr-review --act --stamp ${bot},${human} ${route(r2)}`);
click(btn(r2, `--stamp ${r2} --force`));   // approve anyway on a routed row: a contrary decision
expect("one decision per row: the contrary decision replaces the route", cmd(),
  `$ /pr-review --act --stamp ${bot},${human},${r2} --force`);

// 2. Clear empties everything.
clear();
expect("clear empties the command", cmd(), "$ /pr-review --act");
expect("clear resets progress", progress(), `0 of ${TOTAL} decisions made`);
click(btn(r1, route(r1))); click(btn(r2, route(r2)));
click(btn(prs.judge, "--rerun " + prs.judge));   // an unrelated click must not re-add anything
expect("an unrelated click does not double lit fragments", cmd(), `$ /pr-review --act --rerun ${prs.judge} ${route(r1)} ${route(r2)}`);

// 3. Every --stamp N[:mode][ --force] folds into one list, --force once.
clear();
click(btn(bot, `--stamp ${bot}`)); click(btn(human, `--stamp ${human}:merge`));
click(btn(prs.judge, `--stamp ${prs.judge}:no-merge --force`)); click(btn(r1, `--stamp ${r1} --force`));
expect("modes and --force fold into one --stamp", cmd(), `$ /pr-review --act --stamp ${bot},${human}:merge,${prs.judge}:no-merge,${r1} --force`);
click(btn(human, `--stamp ${human}`));
expect("switching a row's mode replaces it in the list", cmd(), `$ /pr-review --act --stamp ${bot},${human},${prs.judge}:no-merge,${r1} --force`);

// 4. refresh and re-run are decisions, on blocked rows too.
clear();
click(btn(prs.refresh, `--refresh ${prs.refresh}`)); click(btn(prs.rerun, `--rerun ${prs.rerun}`));
expect("refresh and re-run compose", cmd(), `$ /pr-review --act --refresh ${prs.refresh} --rerun ${prs.rerun}`);
expect("refresh and re-run count as decisions", progress(), `2 of ${TOTAL} decisions made`);

// 5. The chain: one button on the lead, covering the next link.
clear();
const chain = btn(lead, "--chain C1");
expect("the chain is the lead row's coloured button", chain.classList.contains("p"), true);
expect("and says which row it covers", chain.dataset.covers, String(next));
expect("the next link is not covered until the chain is lit", covered(next), false);
click(chain);
expect("the chain composes as its own fragment", cmd(), "$ /pr-review --act --chain C1");
expect("the next link is marked covered", covered(next), true);
expect("both links count as decided", progress(), `2 of ${TOTAL} decisions made`);
click(btn(next, `--stamp ${next} --force`));   // a decision on the covered row contradicts the chain
expect("a decision on the covered row puts the chain out", chain.classList.contains("sel"), false);
expect("and the cover mark goes with it", covered(next), false);
expect("the covered row's own choice is what composes", cmd(), `$ /pr-review --act --stamp ${next} --force`);
click(chain);
expect("re-lighting the chain clears the covered row's decision", btn(next, `--stamp ${next} --force`).classList.contains("sel"), false);
expect("and composes the chain alone", cmd(), "$ /pr-review --act --chain C1");
expect("covered again", covered(next), true);
click(btn(lead, `--stamp ${lead} --force`));   // approve-as-is on the lead is the other decision on that row
expect("another decision on the lead puts the chain out", chain.classList.contains("sel"), false);
expect("which uncovers the next link", covered(next), false);
expect("and composes the plain approval", cmd(), `$ /pr-review --act --stamp ${lead} --force`);
click(chain);
clear();
expect("clear takes the chain and its cover with it", `${chain.classList.contains("sel")}|${covered(next)}`, "false|false");

// 6. "fix it yourself" is a run, not a write: its own line, never --act.
clear();
const handWrap = d.getElementById("handwrap"), handCmd = d.getElementById("handcmd");
const hand = d.querySelector(`button.btn.hand[data-run="/address-review ${prs.handfix}"]`);
if (!hand) throw new Error("no handoff button for " + prs.handfix);
expect("the interactive line is hidden until one is lit", handWrap.hidden, true);
click(hand);
expect("the handoff composes on its own line", handCmd.textContent, `$ /address-review ${prs.handfix}`);
expect("which is now shown", handWrap.hidden, false);
expect("and --act is untouched by it", cmd(), "$ /pr-review --act");
expect("a handoff is not a decision", progress(), `0 of ${TOTAL} decisions made`);
click(btn(prs.handfix, `--close ${prs.handfix}`));
expect("the row's own decision still composes into --act", cmd(), `$ /pr-review --act --close ${prs.handfix}`);
expect("without disturbing the interactive line", handCmd.textContent, `$ /address-review ${prs.handfix}`);
clear();
expect("clear empties both lines", `${handCmd.textContent}|${cmd()}`, "|$ /pr-review --act");
expect("and hides the interactive one again", handWrap.hidden, true);

// 7. The two ways to fix a stuck row are alternatives, so they put each
// other out -- across the handoff/fragment boundary, which `clearRow` cannot
// cross because a handoff is deliberately not a decision.
clear();
const askFix = btn(prs.handfix, `--ask-fix ${prs.handfix}`);
click(hand);
click(askFix);
expect("asking @claude composes into --act", cmd(), `$ /pr-review --act --ask-fix ${prs.handfix}`);
expect("and puts the interactive handoff out", handCmd.textContent, "");
expect("so its line hides again", handWrap.hidden, true);
expect("the ask is a decision, the handoff was not", progress(), `1 of ${TOTAL} decisions made`);
click(hand);
expect("lighting the handoff back puts the ask out", cmd(), "$ /pr-review --act");
expect("and composes the run again", handCmd.textContent, `$ /address-review ${prs.handfix}`);
expect("leaving no decision on the row", progress(), `0 of ${TOTAL} decisions made`);
// A different decision on the same row is not in that group: it displaces
// the ask by the one-decision rule, but leaves the handoff riding along.
click(askFix);
click(btn(prs.handfix, `--close ${prs.handfix}`));
expect("close displaces the ask", cmd(), `$ /pr-review --act --close ${prs.handfix}`);
clear();

// The page keeps exactly one runnable script whatever the queue held.
expect("one script element runs", [...d.querySelectorAll("script")].filter((s) => !s.type).length, 1);

if (failures) { console.error(`${failures} composer check(s) failed`); process.exit(1); }
console.log("composer checks passed");
