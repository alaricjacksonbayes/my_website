"""
Script to set up Git and push changes to GitHub for Render deployment
"""

import subprocess
import sys
import os
import json

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def run_command(command, description, check=True):
    """Run a shell command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True, timeout=30)
        if result.stdout:
            print(result.stdout)
        if result.stderr and check:
            print(result.stderr)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return False
    except FileNotFoundError:
        print(f"Command not found. Make sure Git is installed.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("=" * 60)
    print("Setting up Git and pushing to GitHub for Render deployment")
    print("=" * 60)
    
    # Check if Git is available
    git_check = subprocess.run('git --version', shell=True, capture_output=True, text=True)
    if git_check.returncode != 0:
        print("\n[!] Git is not installed or not in PATH.")
        print("Please install Git from https://git-scm.com/download/win")
        print("\nAlternatively, you can manually upload your files to GitHub through:")
        print("- GitHub Desktop (https://desktop.github.com/)")
        print("- GitHub web interface")
        return
    
    print(f"\nGit found: {git_check.stdout.strip()}")
    
    # Check if we're already in a git repo
    is_git_repo = run_command('git rev-parse --git-dir', "Checking if Git repository exists", check=False)
    
    if not is_git_repo:
        print("\nThis directory is not a Git repository.")
        print("\nYou have two options:")
        print("1. Initialize this directory as a new Git repo and connect to GitHub")
        print("2. Clone your existing GitHub repository")
        
        choice = input("\nEnter choice (1 or 2): ").strip()
        
        if choice == "1":
            # Initialize new repo
            print("\n--- Initializing new Git repository ---")
            
            # Get GitHub repo URL
            repo_url = input("\nEnter your GitHub repository URL (e.g., https://github.com/username/repo.git): ").strip()
            if not repo_url:
                print("[!] Repository URL is required.")
                return
            
            run_command('git init', "Initializing Git repository")
            run_command('git branch -M main', "Setting branch to main")
            run_command('git add .', "Adding all files")
            
            commit_msg = input("\nEnter commit message (or press Enter for default): ").strip()
            if not commit_msg:
                commit_msg = "Added cat picture to homepage"
            
            run_command(f'git commit -m "{commit_msg}"', f"Committing: {commit_msg}")
            run_command(f'git remote add origin {repo_url}', "Adding GitHub remote")
            run_command('git push -u origin main', "Pushing to GitHub")
            
        elif choice == "2":
            # Clone existing repo
            repo_url = input("\nEnter your GitHub repository URL to clone: ").strip()
            if not repo_url:
                print("[!] Repository URL is required.")
                return
            
            parent_dir = os.path.dirname(os.path.abspath('.'))
            print(f"\nRepository will be cloned to: {parent_dir}")
            
            if os.listdir('.'):
                print("\n[!] Warning: Current directory is not empty.")
                print("Please clone to a different location or move files manually.")
                return
            
            run_command(f'cd .. && git clone {repo_url}', "Cloning repository")
            print("\nAfter cloning, copy your files to the cloned directory and push changes.")
            return
        else:
            print("Invalid choice.")
            return
    else:
        # Already a git repo, just push changes
        print("\n--- Git repository found ---")
        
        # Check status
        run_command('git status', "Checking status")
        
        # Ask for confirmation
        response = input("\nDo you want to add, commit, and push changes? (yes/no): ").strip().lower()
        if response not in ['yes', 'y']:
            print("Cancelled.")
            return
        
        # Add changes
        run_command('git add templates/index.html static/style.css', "Adding changed files")
        
        # Commit
        commit_msg = input("\nEnter commit message (or press Enter for default): ").strip()
        if not commit_msg:
            commit_msg = "Added cat picture to homepage"
        
        run_command(f'git commit -m "{commit_msg}"', f"Committing: {commit_msg}")
        
        # Push
        run_command('git push origin main', "Pushing to GitHub")
    
    print("\n" + "=" * 60)
    print("SUCCESS!")
    print("=" * 60)
    print("\nYour changes have been pushed to GitHub.")
    print("Render will automatically deploy in 2-3 minutes.")
    print("\nCheck your site at: https://alarics-website.onrender.com/")
    print("Check deployment status at: https://dashboard.render.com")

if __name__ == "__main__":
    main()

