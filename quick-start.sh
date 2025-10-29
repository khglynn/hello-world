#!/bin/bash

# n8n Quick Start Script
# Run this after installing Docker Desktop

set -e

echo "🚀 n8n Quick Start Script"
echo "========================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed!"
    echo ""
    echo "Please install Docker Desktop first:"
    echo "  https://www.docker.com/products/docker-desktop/"
    echo ""
    echo "Or install via Homebrew:"
    echo "  brew install --cask docker"
    exit 1
fi

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo "❌ Docker is not running!"
    echo ""
    echo "Please start Docker Desktop (look for whale icon in menu bar)"
    exit 1
fi

echo "✅ Docker is installed and running"
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  No .env file found, copying from .env.example..."
    cp .env.example .env
    echo "✅ Created .env file"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and change the default password!"
    echo ""
fi

# Create directories if they don't exist
mkdir -p notes processed backups
echo "✅ Created directories: notes/, processed/, backups/"
echo ""

# Start n8n
echo "🐳 Starting n8n..."
echo ""
docker compose up -d

echo ""
echo "⏳ Waiting for n8n to start (this may take 30 seconds)..."
sleep 5

# Wait for health check
attempt=0
max_attempts=12
until docker compose ps | grep -q "healthy" || [ $attempt -eq $max_attempts ]; do
    echo "   Still starting... ($((attempt+1))/$max_attempts)"
    sleep 5
    ((attempt++))
done

echo ""
if [ $attempt -eq $max_attempts ]; then
    echo "⚠️  n8n took longer than expected to start"
    echo "   Check status with: docker compose ps"
    echo "   View logs with: docker compose logs"
else
    echo "✅ n8n is running!"
fi

echo ""
echo "================================================"
echo "🎉 n8n is ready!"
echo "================================================"
echo ""
echo "Access n8n at: http://localhost:5678"
echo ""
echo "Login credentials (from .env file):"
echo "  Username: admin"
echo "  Password: (check your .env file)"
echo ""
echo "Useful commands:"
echo "  docker compose ps       - Check status"
echo "  docker compose logs -f  - View logs"
echo "  docker compose down     - Stop n8n"
echo "  docker compose restart  - Restart n8n"
echo ""
echo "📚 Next steps:"
echo "  1. Open http://localhost:5678 in your browser"
echo "  2. Log in with your credentials"
echo "  3. Add notes to the 'notes/' folder"
echo "  4. Create your first workflow!"
echo ""
echo "Happy automating! 🎉"

