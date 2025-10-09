#!/bin/bash

# Heroku Deployment Helper Script
# This script helps you deploy your Django app to Heroku quickly

set -e  # Exit on error

echo "╔════════════════════════════════════════════════╗"
echo "║     Django Project - Heroku Deployment        ║"
echo "╚════════════════════════════════════════════════╝"
echo ""

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI not found!"
    echo ""
    echo "Please install it first:"
    echo "  macOS:  brew tap heroku/brew && brew install heroku"
    echo "  Linux:  curl https://cli-assets.heroku.com/install.sh | sh"
    echo ""
    exit 1
fi

echo "✅ Heroku CLI found"
echo ""

# Check if logged in
if ! heroku auth:whoami &> /dev/null; then
    echo "🔐 Please login to Heroku..."
    heroku login
fi

echo "✅ Logged in to Heroku"
echo ""

# Check if git repo
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not a git repository!"
    echo "Please run: git init && git add . && git commit -m 'Initial commit'"
    exit 1
fi

echo "✅ Git repository detected"
echo ""

# Check for uncommitted changes
if [[ -n $(git status -s) ]]; then
    echo "⚠️  You have uncommitted changes."
    read -p "Commit them now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git add .
        read -p "Enter commit message: " commit_msg
        git commit -m "$commit_msg"
        echo "✅ Changes committed"
    fi
fi

echo ""

# Check if Heroku remote exists
if git remote | grep -q heroku; then
    echo "✅ Heroku remote found"
    HEROKU_APP=$(heroku apps:info -r heroku --json | python3 -c "import sys, json; print(json.load(sys.stdin)['app']['name'])")
    echo "   App name: $HEROKU_APP"
    echo ""
else
    echo "🆕 No Heroku app connected to this repository"
    echo ""
    read -p "Create a new Heroku app? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "Enter app name (or press Enter for auto-generated): " app_name
        if [ -z "$app_name" ]; then
            heroku create
        else
            heroku create "$app_name"
        fi
        HEROKU_APP=$(heroku apps:info -r heroku --json | python3 -c "import sys, json; print(json.load(sys.stdin)['app']['name'])")
        echo "✅ Created Heroku app: $HEROKU_APP"
        echo ""
    else
        echo "Deployment cancelled."
        exit 0
    fi
fi

# Check for PostgreSQL addon
echo "🔍 Checking for PostgreSQL addon..."
if heroku addons -r heroku | grep -q postgres; then
    echo "✅ PostgreSQL addon found"
else
    echo "⚠️  No PostgreSQL addon found"
    read -p "Add PostgreSQL addon? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        heroku addons:create heroku-postgresql:essential-0
        echo "✅ PostgreSQL addon added"
    fi
fi

echo ""

# Check environment variables
echo "🔍 Checking environment variables..."

if heroku config:get SECRET_KEY -r heroku > /dev/null 2>&1; then
    echo "✅ SECRET_KEY is set"
else
    echo "⚠️  SECRET_KEY not set"
    echo "Generating SECRET_KEY..."
    SECRET_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
    heroku config:set SECRET_KEY="$SECRET_KEY"
    echo "✅ SECRET_KEY set"
fi

if heroku config:get DEBUG -r heroku > /dev/null 2>&1; then
    echo "✅ DEBUG is set"
else
    heroku config:set DEBUG="False"
    echo "✅ DEBUG set to False"
fi

if heroku config:get ALLOWED_HOSTS -r heroku > /dev/null 2>&1; then
    echo "✅ ALLOWED_HOSTS is set"
else
    heroku config:set ALLOWED_HOSTS="$HEROKU_APP.herokuapp.com"
    echo "✅ ALLOWED_HOSTS set"
fi

echo ""
echo "════════════════════════════════════════════════"
echo "📋 Configuration Summary"
echo "════════════════════════════════════════════════"
heroku config -r heroku
echo "════════════════════════════════════════════════"
echo ""

# Deploy
read -p "🚀 Ready to deploy to Heroku? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "🚀 Deploying to Heroku..."
    echo ""
    
    git push heroku main || git push heroku master
    
    echo ""
    echo "✅ Deployment complete!"
    echo ""
    
    # Ask if user wants to create superuser
    read -p "Create Django superuser? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        heroku run python manage.py createsuperuser
    fi
    
    echo ""
    echo "╔════════════════════════════════════════════════╗"
    echo "║            Deployment Successful! 🎉           ║"
    echo "╚════════════════════════════════════════════════╝"
    echo ""
    echo "Your app is live at: https://$HEROKU_APP.herokuapp.com"
    echo ""
    echo "Useful commands:"
    echo "  View logs:        heroku logs --tail"
    echo "  Open app:         heroku open"
    echo "  Open admin:       heroku open /admin"
    echo "  Run migrations:   heroku run python manage.py migrate"
    echo ""
    echo "For more information, see docs/heroku-deployment.md"
    echo ""
    
    read -p "Open app in browser? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        heroku open
    fi
else
    echo "Deployment cancelled."
fi
