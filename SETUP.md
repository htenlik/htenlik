# Setup

GitHub profile README repositories must have exactly the same name as the GitHub username.

For this profile:

1. Create a public repository named `htenlik`.
2. Do not add a README while creating it.
3. Copy this package's contents into the repository root.
4. Commit and push.

Commands:

```bash
cd ~/Desktop
mkdir htenlik
cd htenlik
git init
git branch -M main

# Copy README.md and assets/ from this package into this folder.

git add README.md assets
git commit -m "feat: launch Windows XP themed GitHub profile"
git remote add origin https://github.com/htenlik/htenlik.git
git push -u origin main
```
