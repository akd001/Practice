#!/bin/bash

# macOS Development Environment Setup Script
# This script configures a clean macOS installation for development

echo "Starting macOS development environment setup..."

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "Error: This script is intended for macOS only"
    exit 1
fi

# Install Xcode Command Line Tools (required for git, gcc, etc.)
echo "Installing Xcode Command Line Tools..."
xcode-select --install

# Check if Homebrew is installed, install if not
if ! command -v brew &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    # Add Homebrew to PATH
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

# Update Homebrew
echo "Updating Homebrew..."
brew update

# Install common development tools
echo "Installing development tools..."
brew install git
brew install python
brew install node
brew install docker
brew install wget
brew install curl
brew install tree
brew install vim
brew install tmux

# Install additional useful tools
echo "Installing additional tools..."
brew install htop
brew install fzf
brew install ripgrep
brew install bat
brew install jq

# Install development environments
echo "Installing programming language environments..."
brew install pyenv
brew install nodenv

# Install common editors and IDEs (if not already installed)
echo "Installing code editors..."
brew install --cask visual-studio-code
brew install --cask sublime-text

# Create development directory structure
echo "Creating development directories..."
mkdir -p ~/Development/{projects,tools,notes}

# Configure Git
echo "Configuring Git..."
git config --global user.name "Developer"
git config --global user.email "developer@example.com"
git config --global core.editor "vim"

# Set up shell configuration
echo "Setting up shell configuration..."

# Create .zshrc if it doesn't exist
if [ ! -f ~/.zshrc ]; then
    cat > ~/.zshrc << 'EOF'
# ZSH Configuration for Development

# Enable auto-suggestions and syntax highlighting
source /opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh 2>/dev/null || true
source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null || true

# Aliases for common commands
alias ll='ls -la'
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias grep='grep --color=auto'

# Python environment
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Node.js environment
export NODENV_ROOT="$HOME/.nodenv"
export PATH="$NODENV_ROOT/bin:$PATH"
eval "$(nodenv init -)"

# Set default editor
export EDITOR=vim

# Add custom path for development tools
export PATH="$HOME/Development/tools:$PATH"

# Prompt customization
export PS1="%n@%m:%~$ "

EOF
fi

# Install zsh plugins if not present
echo "Installing zsh plugins..."
brew install zsh-autosuggestions
brew install zsh-syntax-highlighting

# Create a simple README for the setup
cat > ~/Development/README.md << 'EOF'
# Development Environment Setup

This directory contains development tools and projects.

## Tools Installed
- Git
- Python
- Node.js
- Docker
- Various command-line utilities

## Directories
- projects: Source code projects
- tools: Development tools and scripts
- notes: Personal development notes

## Configuration
The setup script configures:
- Git with default settings
- Python environment via pyenv
- Node.js environment via nodenv
- ZSH shell with autosuggestions and syntax highlighting
EOF

echo "Setup complete!"
echo "Please restart your terminal or run 'source ~/.zshrc' to apply changes."
echo "You may also want to install additional tools specific to your development needs."