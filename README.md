Första raden i Reamde



# ✅ Daily Git Checklist

## 📥 Start of Day
1. Navigate to your project folder:
   ```bash
   cd ~/path/to/project
   ```
2. Pull latest changes to stay in sync:
   ```bash
   git pull
   ```

## 🛠️ During Work
3. Make code changes
4. Check status:
   ```bash
   git status
   ```
5. Stage changes:
   ```bash
   git add <filename>
   # or
   git add .
   ```
6. Commit changes:
   ```bash
   git commit -m "feat: your message"
   ```
7. Use diff tools:
   ```bash
   git diff              # unstaged
   git diff --cached     # staged
   git diff origin/main  # local vs GitHub
   ```

## ☁️ End of Day
8. Push changes to GitHub:
   ```bash
   git push
   ```

## 🧠 Bonus: Undo & Rollback
- Unstage a file:
  ```bash
  git restore --staged <file>
  ```
- Restore file to last commit:
  ```bash
  git restore <file>
  ```
- Undo last commit, keep changes:
  ```bash
  git reset --soft HEAD~1
  git reset --mixed HEAD~1
  ```
- Panic reset everything:
  ```bash
  git reset --hard HEAD
  ```
