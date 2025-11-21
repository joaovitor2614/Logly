#!/usr/bin/env bash
set -e  # Stop script on error

# Go to web folder
cd web

# Build the project
echo "Running npm build..."
npm run build


# Go back to root foder
cd ..

# Deploy to Vercel
echo "Deploying to Vercel..."
vercel deploy