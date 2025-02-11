declare module 'markdownlint' {
    interface LintError {
        lineNumber: string | number;
        ruleDescription?: string;
        errorDetail?: string;
        errorContext?: string;
        errorRange?: number[];
        fixInfo?: {
            lineNumber: number;
            editColumn: number;
            deleteCount: number;
            insertText: string;
        };
    }

    interface LintResults {
        [key: string]: LintError[];
    }

    interface Options {
        config?: {
            default?: boolean;
            [key: string]: any;
        };
        customRules?: any[];
        files?: string[];
        strings?: { [key: string]: string };
        frontMatter?: RegExp;
        handleRuleFailures?: boolean;
        noInlineConfig?: boolean;
        resultVersion?: number;
    }

    function sync(options: Options): LintResults;
    
    export = {
        sync
    };
}
