import * as fs from 'fs';
import * as path from 'path';
import { execSync } from 'child_process';
import { z } from 'zod';
import { parse as parseMatter } from 'zod-matter';

const frontMatterSchema = z.object({}).catchall(z.any());

type FrontMatter = z.infer<typeof frontMatterSchema>;

export interface MarkdownFile {
    path: string;
    isNew: boolean;
    content: string;
    // frontMatter can be anything that we parse out
    frontMatter?: FrontMatter;
  }

/**
 * Different modes for finding markdown files and determining if they're new
 */
export type FinderMode = 'git' | 'gha';

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
 * Get list of files that are newly added in the current branch compared to base branch,
 * including staged and unstaged changes. Handles both local git and GitHub Actions environments.
 */
function getGitModifiedFiles(baseBranch?: string): Set<string> {
    try {
        debug('Getting git modified files...');
        const newFiles = new Set<string>();

        // In GitHub Actions, use FETCH_HEAD since we just fetched the base branch
        const isGHA = process.env.GITHUB_ACTIONS === 'true';
        const baseRef = isGHA ? 'FETCH_HEAD' : (baseBranch || process.env.BASE_BRANCH || 'master');
        debug('Using base ref:', baseRef);

        try {
            // In GHA, we've just fetched the base branch to FETCH_HEAD, so this is safe
            const diffOutput = execSync(`git diff --name-status ${baseRef} HEAD`, { encoding: 'utf8' });
            debug('Got diff output');
            diffOutput.split('\n')
                .filter(line => line.startsWith('A\t'))
                .map(line => line.split('\t')[1])
                .forEach(file => newFiles.add(file));
        } catch (error) {
            debug('Diff failed:', error);
            if (isGHA) {
                // In GHA, if diff fails, something is wrong with our setup
                throw error;
            }
            // In local dev, try to get staged/untracked files
            debug('Falling back to staged/untracked files only');
        }

        // In local dev, also look for staged and untracked files
        if (!isGHA) {
            try {
                // Get new files from staged changes
                const stagedFiles = execSync('git diff --name-status --cached', { encoding: 'utf8' });
                stagedFiles.split('\n')
                    .filter(line => line.startsWith('A\t'))
                    .map(line => line.split('\t')[1])
                    .forEach(file => newFiles.add(file));

                // Get untracked files
                debug('Getting untracked files...');
                const untrackedFiles = execSync('git ls-files --others --exclude-standard --full-name', { encoding: 'utf8' });
                debug('Raw untracked files output:', untrackedFiles);
                untrackedFiles.split('\n').filter(Boolean).forEach(file => newFiles.add(file));

                // Also get untracked markdown files specifically
                const untrackedMarkdown = execSync('git ls-files --others --exclude-standard --full-name "*.md"', { encoding: 'utf8' });
                debug('Raw untracked markdown files:', untrackedMarkdown);
                untrackedMarkdown.split('\n').filter(Boolean).forEach(file => newFiles.add(file));
            } catch (error) {
                debug('Failed to get staged/untracked files:', error);
            }
        }

        debug('Found new files:', newFiles);
        return newFiles;
    } catch (error) {
        console.warn('Failed to get git modified files:', error);
        if (process.env.GITHUB_ACTIONS === 'true') {
            console.warn('Running in GitHub Actions - treating all files as existing');
        } else {
            console.warn('Running locally - treating all files as existing');
        }
        return new Set<string>();
    }
}



/**
 * Find all markdown files in the given directory and its subdirectoriesA
 * Optionally marks files as new based on git/GHA context.
 */
export function findMarkdownFiles(
    rootDir: string,
    mode: FinderMode = 'git',
    excludePaths: string[] = ['/content/docs/reference/pkg', '/content/registry', '/node_modules']
): MarkdownFile[] {
    const files: MarkdownFile[] = [];
    
    // Determine which files are considered new based on mode
    let modifiedFiles = new Set<string>();
    if (mode === 'git') {
        modifiedFiles = getGitModifiedFiles();
    } else if (mode === 'gha') {
        const baseBranch = process.env.BASE_BRANCH;
        debug('GHA mode using base branch:', baseBranch);
        modifiedFiles = getGitModifiedFiles(baseBranch);
    }

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
                    // Convert absolute path to relative for comparing with git modified files
                    const relPath = path.relative(process.cwd(), fullPath);
                    files.push({
                        path: fullPath,
                        isNew: modifiedFiles.has(relPath),
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
    const mode = (process.argv[2] as FinderMode) || 'gha';
    const showAll = process.argv.includes('--show-all');
    debug('Running in mode:', mode, 'show all:', showAll);
    
    // Find all markdown files
    const files = findMarkdownFiles('.', mode);
    
    if (showAll) {
        console.log('All markdown files (new files marked with *):')
        console.log(JSON.stringify(files.map(f => `${f.isNew ? '*' : ' '} ${f.path}`), null, 2));
    } else {
        const newFiles = files.filter(f => f.isNew).map(f => f.path);
        console.log('New markdown files detected:');
        console.log(JSON.stringify(newFiles, null, 2));
    }
}
