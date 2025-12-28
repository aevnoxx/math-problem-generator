# Setup Guide

## Initial Repository Setup

### 1. Create GitHub Repository

1. Go to GitHub and create a new repository
2. Name it: `math-problem-generator`
3. Initialize with README: **No** (we already have one)
4. Add .gitignore: **No** (we already have one)

### 2. Upload Project Files

#### Option A: Using Git (Recommended)

```bash
# Navigate to project directory
cd math-problem-generator

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Math Problem Generator with CI/CD"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/math-problem-generator.git

# Push to GitHub
git push -u origin main
```

#### Option B: Using GitHub Web Interface

1. Go to your repository on GitHub
2. Click "uploading an existing file"
3. Drag and drop all project files
4. Commit changes

### 3. Enable GitHub Actions

GitHub Actions should be enabled by default. Verify:
1. Go to repository → **Actions** tab
2. You should see the workflow "Tests and Weekly Problem Generation"
3. If not enabled, click "Enable Actions"

### 4. Update README Badges

In `README.md`, replace `YOUR_USERNAME` with your actual GitHub username:

```markdown
![Tests](https://img.shields.io/github/actions/workflow/status/YOUR_USERNAME/math-problem-generator/ci-cd.yml?branch=main&label=tests)
```

### 5. First Test Run

After pushing, the GitHub Actions workflow will run automatically:
1. Go to **Actions** tab
2. Watch the workflow execute
3. Ensure all tests pass ✅

## Troubleshooting

### Tests Failing

If tests fail on first run:
1. Check the Actions log for error messages
2. Common issues:
   - Missing dependencies → Add to `requirements.txt`
   - Python version mismatch → Update workflow Python version
   - Import errors → Check file paths

### Workflow Not Running

If the workflow doesn't trigger:
1. Check `.github/workflows/` directory exists
2. Verify `ci-cd.yml` is correctly formatted (YAML syntax)
3. Check repository settings → Actions → Allow workflows

### Manual Workflow Trigger

To manually trigger problem generation:
1. Go to **Actions** tab
2. Select "Tests and Weekly Problem Generation"
3. Click **Run workflow**
4. Choose branch and set parameters
5. Click **Run workflow** button

## Configuration Options

### Customize Weekly Schedule

Edit `.github/workflows/ci-cd.yml`:

```yaml
schedule:
  # Change cron expression
  # Format: minute hour day-of-month month day-of-week
  - cron: '0 9 * * 1'  # Monday at 9:00 AM UTC
```

Examples:
- `'0 0 * * 0'` - Sunday at midnight
- `'0 12 * * 1-5'` - Weekdays at noon
- `'0 9 1 * *'` - First day of month at 9 AM

### Change Python Versions

In the workflow file, modify:

```yaml
strategy:
  matrix:
    python-version: ['3.9', '3.10', '3.11']  # Add or remove versions
```

### Adjust Problem Generation Defaults

In the workflow, change:

```yaml
PROBLEM_COUNT="10"   # Number of problems
DIFFICULTY="medium"  # Difficulty level
```

## Verification Checklist

After setup, verify:

- [ ] All files are in the repository
- [ ] GitHub Actions workflow runs successfully
- [ ] Tests pass (35/35)
- [ ] Coverage report shows ~95%
- [ ] Badge in README shows "passing"
- [ ] Weekly schedule is configured
- [ ] Manual workflow dispatch works
- [ ] Generated files appear in `examples/` directory

## Next Steps

1. **Customize**: Modify problem generation logic in `src/generator.py`
2. **Extend**: Add new problem types or difficulty levels
3. **Share**: Share your repository with students or colleagues
4. **Monitor**: Check weekly generated problems in `examples/`

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/actions)
- [SymPy Documentation](https://docs.sympy.org/)
- [pytest Documentation](https://docs.pytest.org/)
