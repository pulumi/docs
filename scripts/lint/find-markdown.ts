import * as fs from 'fs';
import * as path from 'path';
import { execSync } from 'child_process';
import { z } from 'zod';
import { parse as parseMatter } from 'zod-matter';

// Define the front matter schema
const frontMatterSchema = z.object({
    // Optional fields that affect file filtering
    no_edit_this_page: z.boolean().optional(),
    redirect_to: z.string().optional(),
    block_external_search_index: z.boolean().optional(),
    allow_long_title: z.boolean().optional(),
    // Other common fields
    title: z.string().optional(),
    meta_desc: z.string().optional(),
    meta_image: z.string().optional(),
});

type FrontMatter = z.infer<typeof frontMatterSchema>;

export interface MarkdownFile {
    path: string;
    isNew: boolean;
    content: string;
    frontMatter?: FrontMatter;
}

/**
 * Different modes for finding markdown files and determining if they're new
 */
type FinderMode = 'git' | 'gha' | 'standard';

const AUTO_GENERATED_HEADING_REGEX = /^> This page was automatically generated\./m;

/**
 * Parse front matter from a markdown file
 */
function parseFrontMatter(filePath: string): FrontMatter | undefined {
    try {
        const content = fs.readFileSync(filePath, 'utf8');
        
        // Check for auto-generated heading in content
        if (content.match(AUTO_GENERATED_HEADING_REGEX)) {
            return { no_edit_this_page: true };
        }

        // Parse front matter with zod-matter
        const { data } = parseMatter(content, frontMatterSchema);
        return data;
    } catch (e) {
        // If there's no front matter or it's invalid, return null
        return undefined;
    }
}

/**
 * Check if a file should be excluded based on its front matter
 */
function shouldExcludeByFrontMatter(frontMatter: FrontMatter | undefined): boolean {
    if (!frontMatter) return false;

    return frontMatter.no_edit_this_page === true ||
           typeof frontMatter.redirect_to === 'string' ||
           frontMatter.block_external_search_index === true ||
           !!frontMatter.allow_long_title;
}

import { debug } from './utils';

/**
 * Get list of files modified in the latest git commit
 */
function getGitModifiedFiles(): Set<string> {
    try {
        debug('Getting git modified files...');
        const output = execSync('git diff-tree --no-commit-id --name-only -r HEAD', { encoding: 'utf8' });
        const set = new Set(output.split('\n').filter(Boolean));
        debug('Modified files:', set);
        return set;
    } catch (error) {
        console.warn('Failed to get git modified files, treating all files as existing');
        return new Set<string>();
    }
}

/**
 * Get list of files modified in the current PR (GitHub Actions)
 */
function getGHAModifiedFiles(): Set<string> {
    const eventPath = process.env.GITHUB_EVENT_PATH;
    if (!eventPath) {
        console.warn('No GITHUB_EVENT_PATH found, treating all files as existing');
        return new Set<string>();
    }

    try {
        const event = JSON.parse(fs.readFileSync(eventPath, 'utf8'));
        const files = event.pull_request?.changed_files || [];
        return new Set(files);
    } catch (error) {
        console.warn('Failed to get PR modified files, treating all files as existing');
        return new Set<string>();
    }
}

/**
 * Find all markdown files in the given directory and its subdirectories.
 * Optionally marks files as new based on git/GHA context.
 */
export function findMarkdownFiles(
    rootDir: string,
    mode: FinderMode = 'standard',
    excludePaths: string[] = ['/content/docs/reference/pkg', '/content/registry']
): MarkdownFile[] {
    const files: MarkdownFile[] = [];
    const modifiedFiles = mode === 'git' ? getGitModifiedFiles() 
                       : mode === 'gha' ? getGHAModifiedFiles()
                       : new Set<string>();

    function isExcluded(filePath: string): boolean {
        return excludePaths.some(excludePath => filePath.includes(excludePath));
    }

    function searchDirectory(dir: string) {
        const entries = fs.readdirSync(dir);
        
        for (const entry of entries) {
            const fullPath = path.join(dir, entry);
            const stat = fs.statSync(fullPath);

            if (isExcluded(fullPath)) {
                continue;
            }

            if (stat.isDirectory()) {
                searchDirectory(fullPath);
                continue;
            }

            if (path.extname(fullPath) === '.md') {
                const content = fs.readFileSync(fullPath, 'utf8');
                const frontMatter = parseFrontMatter(fullPath);
                if (!shouldExcludeByFrontMatter(frontMatter)) {
                    files.push({
                        path: fullPath,
                        isNew: modifiedFiles.has(fullPath),
                        content,
                        frontMatter
                    });
                }
            }
        }
    }

    searchDirectory(path.resolve(rootDir));
    return files;
}

// If run directly, output found files
if (require.main === module) {
    const mode = (process.argv[2] as FinderMode) || 'standard';
    const rootDir = process.argv[3] || '../../content';
    const files = findMarkdownFiles(rootDir, mode);
    console.log(JSON.stringify(files, null, 2));
}
