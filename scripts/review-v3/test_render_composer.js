// The board's command composer, exercised in jsdom: click the buttons a
// person would and check the command bar after every click.
//
// Run by test_render.py (`test_the_composer_reads_the_lit_buttons`) against a
// board it renders from a fixture queue; runnable by hand too:
//
//   node scripts/review-v3/test_render_composer.js BOARD.html '{"stamp":[11,12],...}'
//
// Needs jsdom, which is already a devDependency of the repo (`make ensure`).
// The scenarios are the ones an audit reproduced as defects: a Do-next card
// doubling every fragment, the bar running a click behind the cards, several
// --stamp flags where act.py expects one, and refresh / re-run not counting
// as decisions. Each is a full click sequence, not a unit of the script.
"use strict";
const fs = require("fs");
const path = require("path");
const { JSDOM } = require(path.join(process.cwd(), "node_modules", "jsdom"));

const html = fs.readFileSync(process.argv[2], "utf8");
const prs = JSON.parse(process.argv[3]);   // {stamp:[bot, human], judge, route:[a,b], refresh, rerun, team}
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
const card = (kind) => [...d.querySelectorAll("button.btn[data-targets]")].find((b) => b.dataset.cmd.startsWith(kind));

let failures = 0;
function expect(name, got, want) {
  if (got === want) { console.log(`  ok: ${name}`); return; }
  failures++;
  console.error(`  FAIL: ${name}\n    got:  ${JSON.stringify(got)}\n    want: ${JSON.stringify(want)}`);
}

const [bot, human] = prs.stamp;
const [r1, r2] = prs.route;
const route = (n) => `--route ${n}:${prs.team}`;
const routeCard = card("--route");

// The defaults: every stamp row starts selected, folded into one --stamp.
expect("default command folds the stamp rows", cmd(), `$ /pr-review --act --stamp ${bot},${human}`);
expect("stamp card lights from its rows", routeCard !== card("--stamp") && card("--stamp").classList.contains("sel"), true);
// 7 rows carry a decision button; the two stamp rows arrive decided.
expect("progress counts every row with a decision to make", progress(), "2 of 7 decisions made");

// 1. A card presses its rows and adds nothing of its own.
click(routeCard);
expect("route card: each fragment once", cmd(), `$ /pr-review --act --stamp ${bot},${human} ${route(r1)} ${route(r2)}`);
expect("route card lit", routeCard.classList.contains("sel"), true);
expect("route rows count as decided", progress(), "4 of 7 decisions made");

// 2. The bar tracks the card state on the same click.
click(btn(r1, route(r1)));
expect("un-pressing a row drops only that fragment", cmd(), `$ /pr-review --act --stamp ${bot},${human} ${route(r2)}`);
expect("and the card goes out", routeCard.classList.contains("sel"), false);
click(routeCard);
click(btn(r2, `--stamp ${r2} --force`));   // approve anyway on a routed row: a contrary decision
expect("a contrary row decision replaces the card's fragment for that row", cmd(),
  `$ /pr-review --act --stamp ${bot},${human},${r2} --force ${route(r1)}`);
expect("card is out after the contrary decision", routeCard.classList.contains("sel"), false);

// Pressing every row of a card by hand lights the card without doubling.
clear();
expect("clear empties the command", cmd(), "$ /pr-review --act");
expect("clear resets progress", progress(), "0 of 7 decisions made");
click(btn(r1, route(r1))); click(btn(r2, route(r2)));
expect("rows pressed by hand light the card", routeCard.classList.contains("sel"), true);
expect("and the command still says each once", cmd(), `$ /pr-review --act ${route(r1)} ${route(r2)}`);
click(btn(prs.judge, "--rerun " + prs.judge));   // an unrelated click must not re-add anything
expect("an unrelated click does not double lit fragments", cmd(), `$ /pr-review --act --rerun ${prs.judge} ${route(r1)} ${route(r2)}`);

// 3. Every --stamp N[:mode][ --force] folds into one list, --force once.
clear();
click(btn(bot, `--stamp ${bot}`)); click(btn(human, `--stamp ${human}:merge`));
click(btn(prs.judge, `--stamp ${prs.judge}:no-merge --force`)); click(btn(r1, `--stamp ${r1} --force`));
expect("modes and --force fold into one --stamp", cmd(), `$ /pr-review --act --stamp ${bot},${human}:merge,${prs.judge}:no-merge,${r1} --force`);
click(btn(human, `--stamp ${human}`));
expect("switching a row's mode replaces it in the list", cmd(), `$ /pr-review --act --stamp ${bot},${human},${prs.judge}:no-merge,${r1} --force`);

// 6. refresh and re-run are decisions, on blocked rows too.
clear();
click(btn(prs.refresh, `--refresh ${prs.refresh}`)); click(btn(prs.rerun, `--rerun ${prs.rerun}`));
expect("refresh and re-run compose", cmd(), `$ /pr-review --act --refresh ${prs.refresh} --rerun ${prs.rerun}`);
expect("refresh and re-run count as decisions", progress(), "2 of 7 decisions made");
expect("their cards light", card("--refresh").classList.contains("sel") && card("--rerun").classList.contains("sel"), true);

// The page keeps exactly one runnable script whatever the queue held.
expect("one script element runs", [...d.querySelectorAll("script")].filter((s) => !s.type).length, 1);

if (failures) { console.error(`${failures} composer check(s) failed`); process.exit(1); }
console.log("composer checks passed");
