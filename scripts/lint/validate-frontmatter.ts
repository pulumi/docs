import * as path from 'path';
import { MarkdownFile, findMarkdownFiles, FinderMode } from './find-markdown';
import { debug, validatePublishDate, validatePublishDateInPST } from './utils';

export interface ValidationConfig {
  checkNewFileDates: boolean;
  allowedPublishDays: ('Tuesday' | 'Wednesday' | 'Thursday')[];
  formatters: {
    error: (msg: string, file: string) => string;
    warning: (msg: string, file: string) => string;
  };
}

// Environment-specific formatters
export const formatters = {
  github: {
    error: (msg: string, file: string) => `::error file=${file},title=${msg}::${msg} (${file})`,
    warning: (msg: string, file: string) => `::warning file=${file},title=${msg}::${msg} (${file})`
  },
  console: {
    error: (msg: string, file: string) => `${file}:\n\t${msg}`,
    warning: (msg: string, file: string) => `${file}:\n\t${msg}`
  }
};

// A single validation “issue” (whether error or warning)
interface ValidationIssue {
  type: string;            // e.g. "title", "meta_desc", or "general"
  message: string;         // e.g. "Title is required"
  level: 'error' | 'warn'; // "error" or "warn"
  file: string;            // path to the file
}



// Imperative checks for each rule:

export function validateFrontMatter(files: MarkdownFile[]): ValidationIssue[] {
  if (!files || files.length === 0) {
    return [];
  }
  const issues: ValidationIssue[] = [];

  for (const file of files) {
    const fm = file.frontMatter || {};

    // --- TITLE RULES ---
    const title = typeof fm.title === 'string' ? fm.title.trim() : '';
    const allowLong = !!fm.allow_long_title;

    if (!title) {
      issues.push({
        type: 'title',
        message: 'A non-empty title is required',
        level: 'error',
        file: file.path
      });
    } else if (!allowLong && title.length > 60) {
      issues.push({
        type: 'title',
        message: 'Title must be 60 characters or fewer',
        level: 'error',
        file: file.path
      });
    }

    // --- META DESCRIPTION RULES ---
    // Must be between 50 and 160 chars if present
    if (typeof fm.meta_desc === 'string') {
      const metaDesc = fm.meta_desc.trim();
      if (metaDesc.length < 50) {
        issues.push({
          type: 'meta_desc',
          message: 'Meta description must be at least 50 characters',
          level: 'error',
          file: file.path
        });
      } else if (metaDesc.length > 160) {
        issues.push({
          type: 'meta_desc',
          message: 'Meta description must be less than 160 characters',
          level: 'error',
          file: file.path
        });
      }
    }

    // --- META IMAGE RULES ---
    // Must end with .png (case-insensitive) if present
    if (typeof fm.meta_image === 'string') {
      if (!/\.png$/i.test(fm.meta_image)) {
        issues.push({
          type: 'meta_image',
          message: 'Meta image must be a PNG file',
          level: 'error',
          file: file.path
        });
      }
    }

    // --- REDIRECT URL RULES ---
    // If present, must be valid URL
    if (typeof fm.redirect_to === 'string' && fm.redirect_to.trim()) {
      try {
        new URL(fm.redirect_to);
      } catch {
        issues.push({
          type: 'redirect_to',
          message: 'Redirect URL must be a valid URL',
          level: 'error',
          file: file.path
        });
      }
    }

    // --- CONTROL FLAGS ---
    // If these fields exist, they should be boolean
    const booleanFields = ['no_edit_this_page', 'block_external_search_index'];
    for (const bf of booleanFields) {
      if (bf in fm && typeof fm[bf] !== 'boolean') {
        issues.push({
          type: bf,
          message: `'${bf}' field must be a boolean`,
          level: 'error',
          file: file.path
        });
      }
    }

    // --- DATE RULES FOR NEW FILES ---
    if (file.isNew) {
      // Check for twitter field
      if (!fm.twitter) {
        issues.push({
          type: 'social',
          message: 'New posts should include a `twitter` field for social sharing.',
          level: 'warn',
          file: file.path,
        });
      }

      // Check for linkedin field
      if (!fm.linkedin) {
        issues.push({
          type: 'social',
          message: 'New posts should include a `linkedin` field for social sharing.',
          level: 'warn',
          file: file.path,
        });
      }
      if (!fm.date) {
        issues.push({
          type: 'date',
          message: 'New files must have a date field',
          level: 'error',
          file: file.path
        });
      } else {
        // Enforce normal date validation (e.g. must not be today)
        const dateError = validatePublishDate(fm.date);
        if (dateError) {
          issues.push({
            type: "date",
            message: dateError,
            level: "error",
            file: file.path,
          });
        }

        // Warn if post is scheduled for a non-optimal day
        const dateValidation = validatePublishDateInPST(fm.date);

        // Check for non-optimal publish days (Tue-Thu are optimal)
        if (dateValidation.dayOfWeek < 2 || dateValidation.dayOfWeek > 4) {
          issues.push({
            type: "date",
            message: `Post is scheduled for ${dateValidation.dayName}. Posts scheduled for Tuesday, Wednesday, or Thursday tend to get better response.`,
            level: "warn",
            file: file.path,
          });
        }

        // Warn if date has a time portion
        if (dateValidation.hasTimeComponent) {
          issues.push({
            type: "date",
            message: "Time portion found in `date`; this may confuse Hugo publishing. Use only YYYY-MM-DD.",
            level: "warn",
            file: file.path,
          });
        }
      }
    }
  }

  return issues;
}


/**
 * Format a validation report from the list of issues.
 */
export function formatValidationReport(
  issues: ValidationIssue[],
  config: ValidationConfig
): { report: string; errorCount: number; warningCount: number } {
  let errorCount = 0;
  let warningCount = 0;
  const errors: string[] = [];
  const warnings: string[] = [];

  // Sort issues into errors and warnings
  for (const issue of issues) {
    const message = `${issue.type}: ${issue.message}`;
    if (issue.level === 'error') {
      errorCount++;
      errors.push(config.formatters.error(message, issue.file));
    } else {
      warningCount++;
      warnings.push(config.formatters.warning(message, issue.file));
    }
  }

  // Build report sections
  const sections: string[] = ['Front Matter Validation Results:'];

  // Add error section if there are errors
  if (errors.length > 0) {
    sections.push(`\nErrors (${errorCount}):`, ...errors);
  }

  // Add warning section if there are warnings
  if (warnings.length > 0) {
    sections.push(`\nWarnings (${warningCount}):`, ...warnings);
  }

  // If no issues, show success message
  if (errors.length === 0 && warnings.length === 0) {
    sections.push('No front matter validation issues found.');
  }

  return {
    report: sections.join('\n'),
    errorCount,
    warningCount
  };
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
  const mode = (process.argv[2] as FinderMode) || 'git';
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
    formatters: process.env.GITHUB_ACTIONS ? formatters.github : formatters.console
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
