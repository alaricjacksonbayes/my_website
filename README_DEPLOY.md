# Quick Deploy Guide

## Easiest Method: Render.com (5 minutes)

1. Go to: https://render.com
2. Sign up (free)
3. Click "New +" → "Web Service"
4. Choose one:
   - Option A: Connect GitHub (recommended)
     - Push code to GitHub first
     - Connect repo to Render
   - Option B: Deploy without Git
     - Upload ZIP of your website folder
5. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Click "Create Web Service"
7. Wait 2-3 minutes - your site is live!

Your website will be at: `https://your-app-name.onrender.com`

---

Need help? The full guide is in DEPLOYMENT.md


