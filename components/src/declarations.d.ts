import CodeMirror from "codemirror";
import JSZip from "jszip";
import FileSaver from "file-saver";

declare global {
    const CodeMirror: typeof CodeMirror;
    const JSZip: JSZip;
    const clipboard: Clipboard;
}
