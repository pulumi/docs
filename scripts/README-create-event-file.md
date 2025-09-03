# Event/Workshop File Creator

This script helps you create properly formatted workshop and event files for the Pulumi website with built-in linting validation.

## How to Run the Script

### Step 1: Open Terminal/Command Prompt
- **On Mac**: Press `Cmd + Space`, type "Terminal", and press Enter
- **On Windows**: Press `Windows + R`, type "cmd", and press Enter
- **On Linux**: Press `Ctrl + Alt + T`

### Step 2: Get the Docs Repository

#### If you already have the docs repo:
Navigate to the folder where your docs repo is:
```bash
cd /Users/pulumipus/docs
```
*(Replace `/Users/pulumipus/docs` with the actual path to your project folder)*

#### If you don't have the docs repo yet:
Clone the repository first:
```bash
git clone https://github.com/pulumi/docs.git
cd docs
```
*(This will download the entire docs repository to your computer)*

### Step 3: Run the Script
Type this command and press Enter:
```bash
node scripts/create-event-file.js
```

### What Happens Next
The script will start and ask you questions. Just type your answers and press Enter after each one. The script will guide you through everything!

## Features

### ✅ Built-in Linting Validation
- **Title Length**: Automatically validates that titles are ≤ 60 characters
- **Meta Description Length**: Automatically validates that meta descriptions are ≤ 160 characters
- **Real-time Feedback**: Shows character counts and validation status as you type

### 🎯 Two File Types

#### Workshop Files
- Interactive prompts for all required fields
- Learning objectives collection
- Presenter information
- Tags and categorization
- HubSpot/Salesforce form integration
- Automatic date/time formatting

#### Event Files
- External event support
- Location information
- Registration URL handling
- Simplified structure for external events

### 📋 What the Script Prompts For

**Common Fields:**
- Title (with length validation)
- Meta description (with length validation)
- Full description
- Date, time, timezone, duration
- Location (for events)

**Workshop-Specific:**
- Learning objectives (multiple)
- Presenter name and role
- Tags (level, topics, languages, clouds)
- HubSpot Form ID
- Salesforce Campaign ID

**Event-Specific:**
- External registration URL

### 🎨 Automatic Features

- **Slug Generation**: Creates URL-friendly slugs from titles
- **Date Formatting**: Converts dates to proper ISO format with timezone
- **File Structure**: Creates proper folder structure and file naming
- **YAML Formatting**: Generates properly formatted YAML frontmatter

### 📁 Output

The script creates:
- A new folder in `content/events/[slug]/`
- An `index.md` file with all the proper YAML frontmatter
- Proper file structure matching existing patterns

### 🔄 Git Integration (Optional)

After creating the file, the script can automatically:
- Create a new Git branch with a descriptive name
- Commit the new file with a proper commit message
- Push the branch to the remote repository
- Generate a link to create a Pull Request on GitHub

**Example Git workflow:**
```
🔄 Would you like to commit this to Git and create a PR? (y/n): y

🔄 Setting up Git...
📝 Creating branch: add-workshop-my-amazing-workshop
📁 Adding file: content/events/my-amazing-workshop/index.md
💾 Committing changes...
🚀 Pushing branch to remote...

✅ Git operations completed successfully!
🌿 Branch: add-workshop-my-amazing-workshop
📝 Commit: Add workshop: My Amazing Workshop

🔗 Creating Pull Request...

🎉 Pull Request ready to create!
🔗 Click here to create the PR: https://github.com/owner/repo/compare/add-workshop-my-amazing-workshop?expand=1
```

### 🔧 Example Usage

Here's what you'll see when you run the script:

```
$ node scripts/create-event-file.js

🚀 Pulumi Event/Workshop File Creator

What would you like to create? (workshop/event): workshop

🎯 Creating a Workshop File

📋 Linting Requirements:
   • Title must be ≤ 60 characters
   • Meta description must be ≤ 160 characters

📝 Workshop Title: My Amazing Workshop
✅ Title is 20 characters (within 60 limit)

📄 Meta Description: Learn amazing things in this workshop
✅ Meta description is 45 characters (within 160 limit)

📖 Full Description: This workshop will teach you...
...
```

**Just type your answers and press Enter!** The script will guide you through each step.

## Troubleshooting

### "node: command not found" Error
If you see this error, you need to install Node.js:
1. Go to https://nodejs.org/
2. Download and install the LTS version
3. Restart your terminal/command prompt
4. Try running the script again

### "No such file or directory" Error
Make sure you're in the right folder:
1. Check that you're in the project folder (the one containing the `scripts` folder)
2. You can type `ls` (Mac/Linux) or `dir` (Windows) to see what's in your current folder
3. You should see a `scripts` folder in the list

### Script Stops or Freezes
- Press `Ctrl + C` to stop the script
- Make sure you're answering each question and pressing Enter
- If you need to start over, just run the script again

### Git Issues

#### "Not a git repository" Error
If you see this error, you need to initialize Git or navigate to the right folder:
1. Make sure you're in the project folder (the one with `.git` folder)
2. If there's no `.git` folder, run: `git init`

#### "Authentication failed" Error
If Git push fails due to authentication:
1. Make sure you're logged into GitHub on your computer
2. You may need to set up a Personal Access Token
3. The script will show manual commit instructions if Git fails

#### "Branch already exists" Error
If the branch name already exists:
1. The script will show an error message
2. You can manually create a branch with a different name
3. Or delete the existing branch if it's not needed

### 🚨 Linting Prevention

The script actively prevents linting errors by:
- Validating title length in real-time
- Validating meta description length in real-time
- Providing character counts and feedback
- Requiring corrections before proceeding

This ensures your files will pass the linter on first creation!
