# Deploy to Render - Step by Step

## Step 1: Push Latest Changes to GitHub

Since you already used GitHub, make sure all your latest changes (including the cat picture) are pushed:

**If using GitHub Desktop:**
1. Open GitHub Desktop
2. Open your repository (alarics-website or similar)
3. You should see the modified files: `templates/index.html` and `static/style.css`
4. Write a commit message (e.g., "Added cat picture to homepage")
5. Click "Commit to main"
6. Click "Push origin" to upload to GitHub

**If using Git in a different terminal:**
```bash
cd C:\Users\alari\website
git add .
git commit -m "Added cat picture to homepage"
git push origin main
```

## Step 2: Deploy to Render.com

1. Go to https://dashboard.render.com
2. Log in to your account
3. Click "New +" → "Web Service"
4. Connect your GitHub account (if not already connected)
5. Select your repository (alarics-website or whatever it's named)
6. Configure the service:
   - **Name**: `alarics-website` (or match your existing service name)
   - **Region**: Choose closest to you
   - **Branch**: `main` (or `master`)
   - **Root Directory**: Leave empty (or `./` if required)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
7. Click "Create Web Service"
8. Wait 2-3 minutes for deployment
9. Your site will be live at: https://alarics-website.onrender.com/

## Step 3: Verify Deployment

Once deployed, visit:
- https://alarics-website.onrender.com/
- Check that the cat picture appears on the homepage!

## Auto-Deploy

Render automatically deploys whenever you push to GitHub, so future updates will deploy automatically after you push changes!

