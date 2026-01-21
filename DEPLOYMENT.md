# How to Deploy Your Website

Your Flask website is now ready to deploy! Here are the easiest options:

## Option 1: Render.com (Recommended - Easiest & Free)

### Steps:
1. **Create a Render account**: Go to https://render.com and sign up (free)

2. **Create a New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub account (you'll need to push your code to GitHub first)
   - Or use "Deploy without Git" and upload your files

3. **Configure**:
   - **Build Command**: Leave empty or use `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Python 3

4. **Deploy**: Click "Create Web Service"
   - Your site will be live at: `https://your-site-name.onrender.com`

## Option 2: Fly.io (Free with Credit Card)

### Steps:
1. **Install Fly CLI**: 
   ```powershell
   powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
   ```

2. **Login**:
   ```bash
   fly auth login
   ```

3. **Create app**:
   ```bash
   fly launch
   ```

4. **Deploy**:
   ```bash
   fly deploy
   ```

## Option 3: Railway.app (Easy & Free Trial)

### Steps:
1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect Flask and deploy

## Option 4: PythonAnywhere (Free for Python)

### Steps:
1. Sign up at https://www.pythonanywhere.com
2. Upload your files via Files tab
3. Go to Web tab and create a new Flask app
4. Configure the path to `app.py`
5. Reload and your site is live!

## First: Push to GitHub (Recommended)

Before deploying, you should push your code to GitHub:

```bash
# In the website directory
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

Then you can connect Render/Railway to your GitHub repo for automatic deployments!

---

**Recommendation**: Start with **Render.com** - it's the easiest and has a good free tier!


