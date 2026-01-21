"""
Script to push latest changes (including cat picture) to GitHub
This will trigger automatic deployment on Render
"""

import subprocess
import sys
import os

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return False
    except FileNotFoundError:
        print(f"Command not found. Make sure Git is installed and in your PATH.")
        return False

def main():
    print("=" * 50)
    print("Pushing changes to GitHub for Render deployment")
    print("=" * 50)
    
    # Check if we're in a git repository
    try:
        result = subprocess.run('git rev-parse --git-dir', shell=True, 
                              capture_output=True, text=True, timeout=5)
        if result.returncode != 0:
            print("\n[!] Error: This directory is not a Git repository.")
            print("Please make sure you've initialized Git and connected to GitHub.")
            return
    except Exception as e:
        print(f"\n[!] Could not check Git status: {e}")
        print("Make sure Git is installed and accessible.")
        return
    
    # Step 1: Check status
    print("\n📋 Checking git status...")
    result = subprocess.run('git status', shell=True, capture_output=True, text=True)
    print(result.stdout)
    
    # Ask for confirmation
    response = input("\n❓ Do you want to commit and push these changes? (yes/no): ").strip().lower()
    if response not in ['yes', 'y']:
        print("Cancelled.")
        return
    
    # Step 2: Add all changes
    if not run_command('git add templates/index.html static/style.css', 
                      "📦 Adding changed files"):
        return
    
    # Step 3: Commit
    commit_message = input("\n💬 Enter commit message (or press Enter for default): ").strip()
    if not commit_message:
        commit_message = "Added cat picture to homepage"
    
    if not run_command(f'git commit -m "{commit_message}"', 
                      f"💾 Committing changes with message: {commit_message}"):
        return
    
    # Step 4: Push to GitHub
    if not run_command('git push origin main', 
                      "🚀 Pushing to GitHub"):
        # Try 'master' branch if 'main' fails
        print("\nTrying 'master' branch instead...")
        if not run_command('git push origin master', 
                          "🚀 Pushing to GitHub (master branch)"):
            return
    
    print("\n" + "=" * 50)
    print("✅ Successfully pushed to GitHub!")
    print("=" * 50)
    print("\n📡 Render will automatically deploy your changes in 2-3 minutes.")
    print("🌐 Check your site at: https://alarics-website.onrender.com/")
    print("\nYou can check deployment status at: https://dashboard.render.com")

if __name__ == "__main__":
    main()

