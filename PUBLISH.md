# Publishing to GitHub

## Repository Status

The repository has been initialized and committed locally. To publish to GitHub:

### Option 1: Create Repository via GitHub Web Interface

1. Go to https://github.com/new
2. Repository name: `spring-2026`
3. Owner: `sweeden-ttu`
4. Description: "Spring 2026 coursework materials and Jekyll site"
5. Choose: **Public** or **Private**
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

### Option 2: Create Repository via GitHub CLI

```bash
gh repo create sweeden-ttu/spring-2026 --public --source=. --remote=origin --push
```

### Option 3: Manual Push (after creating repository)

```bash
cd /home/sdw/Source/coursework/Spring2026
git remote add origin https://github.com/sweeden-ttu/spring-2026.git
git branch -M main
git push -u origin main
```

## Current Status

- ✅ Git repository initialized
- ✅ All files committed locally
- ✅ Remote configured
- ⏳ Waiting for GitHub repository creation

## After Publishing

Once published, you can:

1. **Enable GitHub Pages** (if desired):
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main` / `/ (root)`
   - Save

2. **View the site**:
   - Local: `bundle exec jekyll serve` (http://localhost:4000)
   - GitHub Pages: `https://sweeden-ttu.github.io/spring-2026/`

## Repository Contents

- Course materials for CS-5374 and CS-6343
- Jekyll site configuration
- YAML data files (course info, lectures)
- Agent instructions
- Faculty profiles
- Download scripts for Canvas LMS integration
