#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const readline = require('readline');
const { execSync } = require('child_process');

// Create readline interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Helper function to prompt for input
function askQuestion(question) {
  return new Promise((resolve) => {
    rl.question(question, (answer) => {
      resolve(answer.trim());
    });
  });
}

// Validation functions
function validateTitle(title) {
  if (title.length > 60) {
    return `❌ Title is ${title.length} characters (max 60). Please shorten it.`;
  }
  return `✅ Title is ${title.length} characters (within 60 limit)`;
}

function validateMetaDesc(metaDesc) {
  if (metaDesc.length > 160) {
    return `❌ Meta description is ${metaDesc.length} characters (max 160). Please shorten it.`;
  }
  return `✅ Meta description is ${metaDesc.length} characters (within 160 limit)`;
}

// Helper function to create slug from title
function createSlug(title) {
  return title
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .trim('-');
}

// Helper function to format date for sortable_date
function formatSortableDate(dateStr, timeStr, timezone) {
  const date = new Date(`${dateStr}T${timeStr}`);
  const offset = timezone === 'EDT' ? '-04:00' : 
                 timezone === 'EST' ? '-05:00' :
                 timezone === 'PDT' ? '-07:00' :
                 timezone === 'PST' ? '-08:00' : '-00:00';
  return date.toISOString().replace('Z', offset);
}

// Git functions
function runGitCommand(command, options = {}) {
  try {
    return execSync(command, { 
      encoding: 'utf8', 
      stdio: options.silent ? 'pipe' : 'inherit',
      ...options 
    });
  } catch (error) {
    if (!options.silent) {
      console.error(`❌ Git command failed: ${command}`);
      console.error(error.message);
    }
    throw error;
  }
}

function checkGitStatus() {
  try {
    const status = runGitCommand('git status --porcelain', { silent: true });
    return status.trim();
  } catch (error) {
    return null;
  }
}

function createBranchAndCommit(filePath, title, fileType) {
  const branchName = `add-${fileType}-${createSlug(title).replace(/-/g, '-')}`;
  const commitMessage = `Add ${fileType}: ${title}`;
  
  console.log('\n🔄 Setting up Git...');
  
  try {
    // Check if we're in a git repository
    runGitCommand('git rev-parse --git-dir', { silent: true });
    
    // Create and checkout new branch
    console.log(`📝 Creating branch: ${branchName}`);
    runGitCommand(`git checkout -b ${branchName}`);
    
    // Add the new file
    console.log(`📁 Adding file: ${filePath}`);
    runGitCommand(`git add ${filePath}`);
    
    // Commit the changes
    console.log(`💾 Committing changes...`);
    runGitCommand(`git commit -m "${commitMessage}"`);
    
    // Push the branch
    console.log(`🚀 Pushing branch to remote...`);
    runGitCommand(`git push -u origin ${branchName}`);
    
    console.log(`\n✅ Git operations completed successfully!`);
    console.log(`🌿 Branch: ${branchName}`);
    console.log(`📝 Commit: ${commitMessage}`);
    
    return branchName;
  } catch (error) {
    console.log(`\n⚠️  Git operations failed. You can manually commit later:`);
    console.log(`   git add ${filePath}`);
    console.log(`   git commit -m "${commitMessage}"`);
    return null;
  }
}

function createPullRequest(branchName, title, fileType) {
  console.log('\n🔗 Creating Pull Request...');
  
  try {
    // Try to get the repository info
    const remoteUrl = runGitCommand('git config --get remote.origin.url', { silent: true }).trim();
    
    if (remoteUrl.includes('github.com')) {
      const repoMatch = remoteUrl.match(/github\.com[:/]([^/]+)\/([^/]+?)(?:\.git)?$/);
      if (repoMatch) {
        const [, owner, repo] = repoMatch;
        const prUrl = `https://github.com/${owner}/${repo}/compare/${branchName}?expand=1`;
        
        console.log(`\n🎉 Pull Request ready to create!`);
        console.log(`🔗 Click here to create the PR: ${prUrl}`);
        console.log(`\n📋 Suggested PR details:`);
        console.log(`   Title: Add ${fileType}: ${title}`);
        console.log(`   Description: Created new ${fileType} file with proper YAML frontmatter and linting compliance.`);
        
        return prUrl;
      }
    }
    
    console.log(`\n📝 To create a Pull Request:`);
    console.log(`   1. Go to your repository on GitHub`);
    console.log(`   2. You should see a banner to create a PR for branch: ${branchName}`);
    console.log(`   3. Use title: "Add ${fileType}: ${title}"`);
    
  } catch (error) {
    console.log(`\n⚠️  Could not generate PR link automatically.`);
    console.log(`   Please create a PR manually for branch: ${branchName}`);
  }
}

// Main function to create workshop file
async function createWorkshopFile() {
  console.log('\n🎯 Creating a Workshop File\n');
  console.log('📋 Linting Requirements:');
  console.log('   • Title must be ≤ 60 characters');
  console.log('   • Meta description must be ≤ 160 characters\n');

  // Get basic info
  let title = await askQuestion('📝 Workshop Title: ');
  while (title.length > 60) {
    console.log(validateTitle(title));
    title = await askQuestion('📝 Workshop Title (shortened): ');
  }
  console.log(validateTitle(title));

  let metaDesc = await askQuestion('📄 Meta Description: ');
  while (metaDesc.length > 160) {
    console.log(validateMetaDesc(metaDesc));
    metaDesc = await askQuestion('📄 Meta Description (shortened): ');
  }
  console.log(validateMetaDesc(metaDesc));

  const description = await askQuestion('📖 Full Description: ');
  
  // Get learning objectives
  console.log('\n🎓 Learning Objectives (enter one per line, empty line to finish):');
  const learn = [];
  while (true) {
    const objective = await askQuestion('   • ');
    if (!objective) break;
    learn.push(objective);
  }

  // Get presenter info
  const presenterName = await askQuestion('👤 Presenter Name: ');
  const presenterRole = await askQuestion('💼 Presenter Role: ');

  // Get event details
  const date = await askQuestion('📅 Date (YYYY-MM-DD): ');
  const time = await askQuestion('⏰ Time (HH:MM): ');
  const timezone = await askQuestion('🌍 Timezone (EDT/EST/PDT/PST): ');
  const duration = await askQuestion('⏱️  Duration (e.g., "60 minutes"): ');

  // Get tags
  const level = await askQuestion('📊 Level (Beginner/Intermediate/Advanced): ');
  const topics = await askQuestion('🏷️  Topics (comma-separated): ').split(',').map(t => t.trim()).filter(t => t);
  const languages = await askQuestion('💻 Languages (comma-separated): ').split(',').map(t => t.trim()).filter(t => t);
  const clouds = await askQuestion('☁️  Clouds (comma-separated): ').split(',').map(t => t.trim()).filter(t => t);

  // Get form IDs
  const hubspotFormId = await askQuestion('📋 HubSpot Form ID: ');
  const salesforceCampaignId = await askQuestion('📊 Salesforce Campaign ID: ');

  // Create folder and file
  const slug = createSlug(title);
  const folderPath = path.join('content', 'events', slug);
  const filePath = path.join(folderPath, 'index.md');

  // Create directory if it doesn't exist
  if (!fs.existsSync(folderPath)) {
    fs.mkdirSync(folderPath, { recursive: true });
  }

  // Generate content
  const sortableDate = formatSortableDate(date, time, timezone);
  const endTime = new Date(new Date(`${date}T${time}`).getTime() + (parseInt(duration) * 60000));
  const endDate = endTime.toISOString().replace('Z', timezone === 'EDT' ? '-04:00' : 
                                                      timezone === 'EST' ? '-05:00' :
                                                      timezone === 'PDT' ? '-07:00' :
                                                      timezone === 'PST' ? '-08:00' : '-00:00');

  const content = `---
# Name of the event, <= 60 characters
title: "${title}"
meta_desc: ${metaDesc}
meta_image:

# A featured webinar will display first in the list.
featured: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: ${slug}

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "${title}"
    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: 

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: ${sortableDate}

    # Duration of the webinar.
    duration: ${duration}

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        ${description}
    learn:
${learn.map(item => `        - ${item}`).join('\n')}

    # The webinar presenters
    presenters:
        - name: ${presenterName}
          role: ${presenterRole}
          photo: /images/team/${presenterName.toLowerCase().replace(/\s+/g, '-')}.jpg

    # case-sensitive
    tags:
        level: ${level} # Beginner, Intermediate, Advanced
        topics:  [${topics.map(t => `"${t}"`).join(', ')}]
        languages: [${languages.map(l => `"${l}"`).join(', ')}]
        clouds: [${clouds.map(c => `"${c}"`).join(', ')}]

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id: ${hubspotFormId}
    salesforce_campaign_id: ${salesforceCampaignId}

event_data:
  name: "${title}"
  start_date: ${sortableDate}
  end_date: ${endDate}
  url: "https://www.pulumi.com/resources/${slug}/"
  description: |
    ${description}
---`;

  // Write file
  fs.writeFileSync(filePath, content);

  console.log(`\n✅ Workshop file created successfully!`);
  console.log(`📁 Location: ${filePath}`);
  console.log(`🔗 URL slug: ${slug}`);

  // Ask about Git operations
  const useGit = await askQuestion('\n🔄 Would you like to commit this to Git and create a PR? (y/n): ');
  
  if (useGit.toLowerCase() === 'y' || useGit.toLowerCase() === 'yes') {
    const branchName = createBranchAndCommit(filePath, title, 'workshop');
    if (branchName) {
      createPullRequest(branchName, title, 'workshop');
    }
  } else {
    console.log('\n📝 To commit manually later:');
    console.log(`   git add ${filePath}`);
    console.log(`   git commit -m "Add workshop: ${title}"`);
  }
}

// Main function to create event file
async function createEventFile() {
  console.log('\n🎯 Creating an Event File\n');
  console.log('📋 Linting Requirements:');
  console.log('   • Title must be ≤ 60 characters');
  console.log('   • Meta description must be ≤ 160 characters\n');

  // Get basic info
  let title = await askQuestion('📝 Event Title: ');
  while (title.length > 60) {
    console.log(validateTitle(title));
    title = await askQuestion('📝 Event Title (shortened): ');
  }
  console.log(validateTitle(title));

  let metaDesc = await askQuestion('📄 Meta Description: ');
  while (metaDesc.length > 160) {
    console.log(validateMetaDesc(metaDesc));
    metaDesc = await askQuestion('📄 Meta Description (shortened): ');
  }
  console.log(validateMetaDesc(metaDesc));

  const description = await askQuestion('📖 Full Description: ');

  // Get event details
  const date = await askQuestion('📅 Date (YYYY-MM-DD): ');
  const time = await askQuestion('⏰ Time (HH:MM): ');
  const timezone = await askQuestion('🌍 Timezone (EDT/EST/PDT/PST): ');
  const duration = await askQuestion('⏱️  Duration (e.g., "2 hours"): ');
  const location = await askQuestion('📍 Location (e.g., "Atlanta, GA"): ');

  // Get external URL
  const externalUrl = await askQuestion('🔗 External Registration URL: ');

  // Create folder and file
  const slug = createSlug(title);
  const folderPath = path.join('content', 'events', slug);
  const filePath = path.join(folderPath, 'index.md');

  // Create directory if it doesn't exist
  if (!fs.existsSync(folderPath)) {
    fs.mkdirSync(folderPath, { recursive: true });
  }

  // Generate content
  const sortableDate = formatSortableDate(date, time, timezone);

  const content = `---
# Name of the event, <= 60 characters
title: ${title}
meta_desc: ${metaDesc}
meta_image: 

# A featured webinar will display first in the list.
featured: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: true
block_external_search_index: true

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: ${externalUrl}

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: ${title}

    event_type: event # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: ${sortableDate}

    # Duration of the webinar.
    duration: ${duration}

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: ${location}

    # Description of the webinar.
    description: ${description}

    # The webinar presenters
    presenters:

    # case-sensitive
    tags:
        level: # Beginner, Intermediate, Advanced
        topics: []
        languages: []
        clouds: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---`;

  // Write file
  fs.writeFileSync(filePath, content);

  console.log(`\n✅ Event file created successfully!`);
  console.log(`📁 Location: ${filePath}`);
  console.log(`🔗 External URL: ${externalUrl}`);

  // Ask about Git operations
  const useGit = await askQuestion('\n🔄 Would you like to commit this to Git and create a PR? (y/n): ');
  
  if (useGit.toLowerCase() === 'y' || useGit.toLowerCase() === 'yes') {
    const branchName = createBranchAndCommit(filePath, title, 'event');
    if (branchName) {
      createPullRequest(branchName, title, 'event');
    }
  } else {
    console.log('\n📝 To commit manually later:');
    console.log(`   git add ${filePath}`);
    console.log(`   git commit -m "Add event: ${title}"`);
  }
}

// Main function
async function main() {
  console.log('🚀 Pulumi Event/Workshop File Creator\n');
  
  const fileType = await askQuestion('What would you like to create? (workshop/event): ');
  
  if (fileType.toLowerCase() === 'workshop') {
    await createWorkshopFile();
  } else if (fileType.toLowerCase() === 'event') {
    await createEventFile();
  } else {
    console.log('❌ Invalid option. Please choose "workshop" or "event".');
  }
  
  rl.close();
}

// Handle Ctrl+C gracefully
process.on('SIGINT', () => {
  console.log('\n👋 Goodbye!');
  rl.close();
  process.exit(0);
});

// Run the script
main().catch(console.error);
