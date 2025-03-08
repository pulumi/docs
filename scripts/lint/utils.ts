/**
 * Debug logging helper
 */
export function debug(...args: any[]) {
    if (process.env.DEBUG === '1') {
        console.log('[DEBUG]', ...args);
    }
}


/**
 * Convert "now" (UTC) to local time in PST using toLocaleString with timeZone
 */
export function getNowInPST(): Date {
    const pstString = new Date().toLocaleString("en-US", {
      timeZone: "America/Los_Angeles",
    });
    return new Date(pstString);
  }
  
  /**
   * Zero out hours/min/seconds on a date so we compare only by day
   */
export function toDateOnly(d: Date): Date {
    return new Date(d.getFullYear(), d.getMonth(), d.getDate());
  }
  
  /**
   * Return the "earliest allowed publish date" in PST
   * given the current local PST time and the noon cutoff rule.
   */
export function getEarliestAllowedDate(): Date {
    const nowPST = getNowInPST();
    const hour = nowPST.getHours();
  
    // Convert "today" to a date with 0:00 hours
    const todayPST = toDateOnly(nowPST);
  
    if (hour < 12) {
      // Before noon PST => earliest is tomorrow
      // (today + 1 day)
      const tomorrow = new Date(todayPST);
      tomorrow.setDate(todayPST.getDate() + 1);
      return tomorrow;
    } else {
      // After noon PST => earliest is day after tomorrow
      const dayAfter = new Date(todayPST);
      dayAfter.setDate(todayPST.getDate() + 2);
      return dayAfter;
    }
  }

export interface DateValidationResult {
  dayOfWeek: number;
  dayName: string;
  hasTimeComponent: boolean;
}

export const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

/**
 * Parse a date value (string or Date) and validate it in PST timezone
 */
export function validatePublishDateInPST(dateValue: string | Date): DateValidationResult {
  // Convert to ISO string if needed
  const dateStr = typeof dateValue === 'string' ? dateValue : dateValue.toISOString();
  const hasTimeComponent = dateStr.includes('T') && !dateStr.endsWith('T00:00:00.000Z');

  // Get just the date part and parse components
  const [datePart] = dateStr.split('T');
  const [year, month, day] = datePart.split('-').map(Number);
  
  // Create date at noon PST to avoid timezone issues
  const pstDate = new Date(year, month - 1, day, 12).toLocaleString('en-US', { timeZone: 'America/Los_Angeles' });
  const publishDate = new Date(pstDate);
  
  const dayOfWeek = publishDate.getDay();
  return {
    dayOfWeek,
    dayName: dayNames[dayOfWeek],
    hasTimeComponent
  };
}

export function validatePublishDate(fmDateStr: string): string | null {
    // Attempt to parse front matter date
    // e.g. "2025-02-10"
    const fmDate = new Date(fmDateStr);
    if (isNaN(fmDate.getTime())) {
      return "Invalid date format in front matter";
    }
  
    // Convert the front matter date to a "date-only" object
    const fmDateOnly = toDateOnly(fmDate);
  
    // Get the earliest allowed date
    const earliest = getEarliestAllowedDate();
  
    if (fmDateOnly < earliest) {
      // It's too soon
      const earliestStr = earliest.toISOString().slice(0, 10); // e.g. "2025-02-11"
      return `Post date must be at least ${earliestStr} (based on noon PST cutoff)`;
    }
  
    return null; // no error
  }