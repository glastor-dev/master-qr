# Git Commit Message Convention

**Write clear, semantic commit messages that help humans and tools understand your changes.**

This project follows [Conventional Commits](https://www.conventionalcommits.org/) specification, based on [Angular's commit convention](https://github.com/conventional-changelog/conventional-changelog).

---

## 📚 Table of Contents

- [Git Commit Message Convention](#git-commit-message-convention)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Why Use This Convention?](#-why-use-this-convention)
  - [⚡ Quick Reference](#-quick-reference)
    - [Format](#format)

---

## 🎯 Why Use This Convention?

**Benefits:**

- **🤖 Automated changelogs**: Tools can generate CHANGELOG.md automatically
- **📦 Semantic versioning**: Determine version bumps (major/minor/patch) from commits
- **🔍 Better navigation**: Quickly find features, fixes, or breaking changes in history
- **📊 Clear communication**: Team members instantly understand what changed
- **🚀 Release automation**: CI/CD can trigger releases based on commit types

**In practice:**
- `feat:` → Minor version bump (1.0.0 → 1.1.0)
- `fix:` → Patch version bump (1.0.0 → 1.0.1)
- `BREAKING CHANGE:` → Major version bump (1.0.0 → 2.0.0)

---

## ⚡ Quick Reference

### Format

():

```
Rules
✅ Header (required): type(scope): subject
✅ Type (required): See Commit Types
⚠️ Scope (optional): Component/module affected
✅ Subject (required): Short description (50 chars max)
⚠️ Body (optional): Detailed explanation
⚠️ Footer (optional): Breaking changes, issue references
Regex
/^(revert: )?(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\(.+\))?: .{1,50}/
📐 Format Structure
Header (Required)
type(scope): subject
Components:

Type (required): What kind of change
Scope (optional): What part of the codebase
Subject (required): Brief description
Example:

feat(auth): add OAuth2 login support
Body (Optional)
Use when you need to explain:

Why the change was necessary
What problem it solves
How it differs from previous behavior
Format:

Blank line after header
Use imperative mood: "add" not "added"
Wrap at 72 characters
Example:

feat(auth): add OAuth2 login support

Users can now authenticate using Google and GitHub OAuth2 providers.
This replaces the basic username/password auth to improve security
and provide social login options.
Footer (Optional)
Use for:

Breaking changes: Start with BREAKING CHANGE:
Issue references: Closes #123, Fixes #456
Co-authors: Co-authored-by: Name <email>
Example:

feat(api)!: remove deprecated /v1 endpoints

BREAKING CHANGE: The /v1/users endpoint has been removed.
Use /v2/users instead.

Closes #789
🏷️ Commit Types
Primary Types (Appear in CHANGELOG)
Type	When to Use	Version Bump	Changelog Section
feat	New feature for users	Minor (1.X.0)	Features
fix	Bug fix for users	Patch (1.0.X)	Bug Fixes
perf	Performance improvement	Patch (1.0.X)	Performance
Secondary Types (Internal changes)
Type	When to Use	Changelog
docs	Documentation only	No
style	Formatting (no logic change)	No
refactor	Code restructure (no behavior change)	No
test	Adding or updating tests	No
build	Build system or dependencies	No
ci	CI/CD configuration	No
chore	Maintenance tasks	No
revert	Reverting previous commit	Yes (Reverts)
Decision Tree
📝 Is it user-facing?
  ├─ Yes → New functionality?
  │   ├─ Yes → feat
  │   └─ No → Fixes a bug?
  │       ├─ Yes → fix
  │       └─ No → Makes it faster?
  │           ├─ Yes → perf
  │           └─ No → refactor
  └─ No → Internal change?
      ├─ Documentation → docs
      ├─ Tests → test
      ├─ CI/CD → ci
      ├─ Dependencies → build
      └─ Other → chore
📝 Examples
✅ Good Commits
Feature
feat(readme): add multi-language template support

Users can now generate READMEs in English, Spanish, and French.
Templates are stored in templates/lang/ directory.

Closes #42
Bug Fix
fix(generator): handle missing config values gracefully

Previously crashed with KeyError when optional config fields were
missing. Now uses sensible defaults.

Fixes #156
Performance
perf(parser): optimize template rendering by 40%

Switched from regex to compiled patterns. Benchmarks show
40% reduction in rendering time for large templates.
Breaking Change
feat(api)!: redesign configuration schema

BREAKING CHANGE: Config format has changed from JSON to YAML.
Migration guide: docs/migration-v2.md

Old format:
{
  "project": "name"
}

New format:
project:
  name: "name"

Closes #200
Refactoring
refactor(utils): extract validation into separate module

No behavior change. Improves code organization and testability.
Validation logic now in src/validators.py
Documentation
docs: update installation instructions for Windows

Added troubleshooting section for common Windows setup issues.
Includes PowerShell-specific commands.
Tests
test(generator): add coverage for edge cases

Adds tests for:
- Empty config files
- Missing template directories
- Invalid variable names

Coverage increased from 78% to 92%.
Chore
chore(deps): update dependencies to latest versions

- Jinja2: 3.0.0 → 3.1.2
- Click: 8.0.0 → 8.1.0
- Pytest: 7.0.0 → 7.4.0

All tests passing.
Revert
revert: feat(compiler): add comments option

This reverts commit 667ecc1654a317a13331b17617d973392f415f02.

Reason: Caused performance regression in production.
Will be re-implemented with caching in future PR.
❌ Bad Commits (Anti-Examples)
❌ update stuff
Problem: No type, vague subject

❌ Fixed bug
Problem: No type, past tense, not descriptive

❌ feat: Added new feature for users that allows them to...
Problem: Past tense, subject too long (>50 chars)

❌ WIP
Problem: Not descriptive, should use draft PR instead

❌ fix: fix
Problem: Subject doesn't explain what was fixed

❌ feat(everything): complete rewrite
Problem: Scope too broad, commit probably too large

✅ Better alternatives:

feat(auth): add OAuth2 login support
fix(parser): prevent crash on empty input files
refactor: extract validation logic into validators module
✍️ Writing Guidelines
Subject Line Rules
Use imperative mood

✅ "add feature"
❌ "added feature"
❌ "adds feature"
Keep it short

✅ Maximum 50 characters
✅ Ideally under 40 characters
Don't capitalize first letter

✅ "add OAuth login"
❌ "Add OAuth login"
No period at the end

✅ "fix validation bug"
❌ "fix validation bug."
Be specific

✅ "fix memory leak in template parser"
❌ "fix bug"
Body Guidelines
Wrap at 72 characters for readability
Explain WHY, not HOW (code shows how)
Use bullet points for multiple changes
Reference issues when relevant
Scope Guidelines
Good scopes:

Component names: auth, api, cli
Module names: parser, generator, validator
File/folder names: readme, config, templates
Avoid:

all (too broad)
misc (be specific)
Multiple scopes in one: auth,api (split into separate commits)
💥 Breaking Changes
Indicating Breaking Changes
Method 1: ! in header

feat(api)!: remove deprecated endpoints
Method 2: Footer with BREAKING CHANGE:

feat(api): update response format

BREAKING CHANGE: API responses now include metadata object.
When to Use
Breaking changes are changes that require users to modify their code:

Removing features
Changing API signatures
Altering default behavior
Removing or renaming configuration options
What to Include
What changed: Describe the breaking change clearly
Why it changed: Explain the motivation
Migration path: How to update existing code
Before/After examples: Show old and new way
Example:

feat(config)!: change configuration format from JSON to YAML

BREAKING CHANGE: Configuration files must now use YAML format.

Migration:
1. Rename config.json to config.yaml
2. Convert JSON syntax to YAML
3. Update import statements

Before:
{
  "project": {
    "name": "My Project"
  }
}

After:
project:
  name: My Project

See docs/migration-v2.md for detailed guide.

Closes #300
🔗 Issue References
Closing Keywords
Use these to automatically close issues when PR merges:

Closes #123 - Closes a single issue
Fixes #123 - Fixes a bug (same as Closes)
Resolves #123 - Resolves an issue (same as Closes)
Multiple issues:

fix(auth): prevent token expiration race condition

Fixes #123, #456, #789
Reference-Only
Use Refs to reference without closing:

docs: update API documentation

Refs #123 (work in progress)
PR Numbers
When commit is from a merged PR, optionally include PR number:

fix(api): handle timeout errors (#234)
🤝 Co-Authors
For pair programming or collaborative commits:

feat(parser): implement new template engine

Co-authored-by: Jane Doe <jane@example.com>
Co-authored-by: John Smith <john@example.com>
🔧 Tools & Automation
Commitizen
Interactive CLI for writing commits:

npm install -g commitizen
git cz  # Instead of git commit
Commitlint
Validate commit messages in CI:

npm install --save-dev @commitlint/cli @commitlint/config-conventional
echo "module.exports = {extends: ['@commitlint/config-conventional']}" > commitlint.config.js
Husky + Commitlint
Validate locally before push:

npm install --save-dev husky
npx husky install
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"'
Standard Version
Automated versioning and CHANGELOG generation:

npm install --save-dev standard-version
npm run release  # Bumps version, generates CHANGELOG, creates git tag
📋 Quick Checklist
Before committing, ask yourself:

 Does the commit have a type?
 Is the subject under 50 characters?
 Is the subject in imperative mood?
 Does the subject clearly describe the change?
 If breaking change, is it marked with ! or BREAKING CHANGE:?
 Are issue references in the footer?
 Is the commit focused on ONE logical change?
🎓 Common Questions
Should I use feat or fix for small improvements?
Use fix if it corrects incorrect behavior. Use feat if it adds new functionality, even if small.

What if my change affects multiple areas?
Consider splitting into multiple commits. If that's not practical, choose the most significant area as the scope.

Can I have multiple types in one commit?
No. One commit = one type. If you have both a feature and a fix, make two commits.

Do I need a scope for every commit?
No, scope is optional. Use it when it adds clarity, skip it for project-wide changes.

What about merge commits?
Merge commits from PRs don't need to follow this format, but PR titles should.

📚 Additional Resources
Conventional Commits: https://www.conventionalcommits.org/
Angular Convention: https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit
Semantic Versioning: https://semver.org/
Commitlint: https://commitlint.js.org/
Commitizen: https://github.com/commitizen/cz-cli
📜 Examples from This Project
Browse our commit history for real-world examples:

git log --oneline --all --graph
Filter by type:

git log --oneline --grep="^feat"
git log --oneline --grep="^fix"
Questions about commit messages?

Open an issue or check CONTRIBUTING.md

Following these conventions helps maintain a clean, navigable history 📖

Last updated: 2025-12-28