import CodeMirror from "codemirror";
import JSZip from "jszip";
import FileSaver from "file-saver";
import Prism from "prismjs";

declare global {
    const CodeMirror: typeof CodeMirror;
    const JSZip: JSZip;
    const Prism: typeof Prism;
}
