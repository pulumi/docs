import { z } from 'zod';
import { parse as parseMatter } from 'zod-matter';
import * as path from 'path';
import { MarkdownFile, findMarkdownFiles } from './find-markdown';
import { debug } from './utils';

// Schema for front matter validation
const frontMatterSchema = z.object({
  // Control fields
  allow_long_title: z.boolean().optional().default(false),
  
  // Required fields
  title: z.string(),
  
  // Optional fields with validation
  meta_desc: z.string()
    .transform(s => s.trim())
    .pipe(
      z.string()
        .min(50, "Meta description must be at least 50 characters")
        .max(160, "Meta description must be less than 160 characters")
    )
    .optional(),
  meta_image: z.union([
    z.string().regex(/\.png$/i, "Meta image must be a PNG file"),
    z.null(),
  ]).optional(),
  
  // Control fields
  no_edit_this_page: z.boolean().optional(),
  redirect_to: z.string().url("Redirect URL must be a valid URL").optional(),
  block_external_search_index: z.boolean().optional(),
  
  // Publication date (for new files)
  publish_date: z.coerce.date().optional(),
});



type FrontMatter = z.infer<typeof frontMatterSchema>;

// Custom validation function for title length
const validateTitle = (title: string, allowLongTitle: boolean): string | null => {
  const trimmedTitle = title.trim();
  if (trimmedTitle.length < 1) {
    return "Title is required";
  }
  if (!allowLongTitle && trimmedTitle.length > 60) {
    return "Title must be less than 60 characters";
  }
  return null;
};

export interface ValidationConfig {
  checkNewFileDates: boolean;
  allowedPublishDays: ('Tuesday' | 'Wednesday' | 'Thursday')[];
  warningFormatter: (msg: string, file: string) => string;
}

// Environment-specific warning formatters
export const warningFormatters = {
  github: (msg: string, file: string) => `::warning file=${file}::${msg}`,
  console: (msg: string, file: string) => `Warning: ${file}: ${msg}`,
};

// A single validation “issue” (whether error or warning)
interface ValidationIssue {
  type: string;            // e.g. "title", "meta_desc", or "general"
  message: string;         // e.g. "Title is required"
  level: 'error' | 'warn'; // "error" or "warn"
  file: string;            // path to the file
}

/**
 * Validate the front matter of each file and return an array of issues.
 */
function validateFrontMatter(
  files: MarkdownFile[]
): ValidationIssue[] {
  const issues: ValidationIssue[] = [];

  for (const file of files) {
    try {
      // Parse front matter with zod-matter
      const { data } = parseMatter(file.content, frontMatterSchema);
      const frontMatter: FrontMatter = data;

      // Validate parsed data with Zod
      // Pre-validate title before schema validation
      const titleError = validateTitle(frontMatter.title, !!frontMatter.allow_long_title);
      if (titleError) {
        issues.push({
          type: "title",
          message: titleError,
          level: "error",
          file: file.path,
        });
        continue;
      }

    const result = frontMatterSchema.safeParse(frontMatter);
      if (!result.success) {
        // Collect each Zod issue as an error
        for (const zodIssue of result.error.issues) {
          const path = zodIssue.path.length
            ? zodIssue.path.join('.')
            : 'general';

          issues.push({
            type: path,
            message: zodIssue.message,
            level: 'error',
            file: file.path,
          });
        }
      }

      // If you later reintroduce warnings (e.g. date checks),
      // you'd do something like:
      //
      // if (result.success) {
      //   const dateWarnings = checkSomething(result.data, file, config);
      //   for (const msg of dateWarnings) {
      //     issues.push({
      //       type: 'publish_date',
      //       message: msg,
      //       level: 'warn',
      //       file: file.path,
      //     });
      //   }
      // }

    } catch (err) {
      // Handle Zod validation errors consistently
      if (err instanceof z.ZodError) {
        for (const zodIssue of err.issues) {
          const path = zodIssue.path.length
            ? zodIssue.path.join('.')
            : 'general';

          issues.push({
            type: path,
            message: zodIssue.message,
            level: 'error',
            file: file.path,
          });
        }
      } else {
        // For non-Zod errors
        const message =
          err instanceof Error ? err.message : 'Failed to parse front matter';
        issues.push({
          type: 'frontmatter',
          message,
          level: 'error',
          file: file.path,
        });
      }
    }
  }

  return issues;
}

/**
 * Format a validation report from the list of issues.
 */
function formatValidationReport(
  issues: ValidationIssue[],
  config: ValidationConfig
): { report: string; errorCount: number; warningCount: number } {
  let errorCount = 0;
  let warningCount = 0;
  const lines: string[] = [];

  for (const issue of issues) {
    if (issue.level === 'error') {
      errorCount++;
      lines.push(config.warningFormatter(`${issue.type}: ${issue.message}`, issue.file));
    } else {
      // issue.level === 'warn'
      warningCount++;
      lines.push(config.warningFormatter(`${issue.type}: ${issue.message}`, issue.file));
    }
  }

  const report =
    lines.length === 0
      ? 'No front matter validation issues found.'
      : [
          'Front Matter Validation Results:',
          `Found ${errorCount} error${errorCount === 1 ? '' : 's'} and ${warningCount} warning${warningCount === 1 ? '' : 's'}:`,
          ...lines,
        ].join('\n');

  return { report, errorCount, warningCount };
}

/**
 * Main entry point to run the validation. 
 * Finds markdown files, runs validation, prints a report, and exits with nonzero code on errors.
 */
export function runValidation(
  baseDir: string = '../../content',
  excludePaths: string[] = []
): number {
  // Get mode from command line args, defaulting to 'standard'
  const mode = (process.argv[2] as 'git' | 'gha' | 'standard') || 'standard';
  debug('Starting frontmatter validation in mode:', mode);

  // Get markdown files to validate
  const markdownFiles = findMarkdownFiles(
    path.resolve(__dirname, baseDir),
    mode,
    excludePaths
  );
  debug(`Found ${markdownFiles.length} markdown files to validate`);

  // Configure validation
  const config: ValidationConfig = {
    checkNewFileDates: false, // turned off for now (or keep it on, no effect if we’re not checking)
    allowedPublishDays: ['Tuesday', 'Wednesday', 'Thursday'],
    warningFormatter: process.env.GITHUB_ACTIONS
      ? warningFormatters.github
      : warningFormatters.console,
  };

  // Run validation
  debug('Starting frontmatter validation...');
  const issues = validateFrontMatter(markdownFiles);
  debug('Completed frontmatter validation');

  // Generate a formatted report
  const { report, errorCount } = formatValidationReport(issues, config);
  debug(`Validation complete: ${errorCount} errors found`);

  // Output results
  console.log(`\n${report}\n`);

  // Return error count for exit code
  return errorCount;
}

// Run validation if this is the main module
if (require.main === module) {
  try {
    const errorCount = runValidation(
      '../../content',
      ['/content/docs/reference/pkg', '/content/registry']
    );
    const noError = process.argv.indexOf('--no-error') > -1;
    process.exit(noError || errorCount === 0 ? 0 : 1);
  } catch (error) {
    console.error('Front matter validation failed:', error);
    process.exit(1);
  }
}
