#!/usr/bin/env bash
# Deep Research Skill Installer
# Usage: bash install.sh [target_dir]
#
# If target_dir is not specified, auto-detects:
#   - ~/.hermes/skills/  (Hermes)
#   - ~/.claude/skills/  (Claude Code)
#
# The skill will be installed to: <target_dir>/deep-research/

set -e

REPO_URL="https://github.com/kai0258/Kai.git"
SUBDIR="deep-research"
SKILL_NAME="deep-research"

# --- Colors ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

info()  { echo -e "${GREEN}[✓]${NC} $1"; }
warn()  { echo -e "${YELLOW}[!]${NC} $1"; }
error() { echo -e "${RED}[✗]${NC} $1"; }

# --- Determine target ---
if [ -n "$1" ]; then
    TARGETS=("$1")
else
    TARGETS=()
    [ -d "$HOME/.hermes/skills" ] && TARGETS+=("$HOME/.hermes/skills")
    [ -d "$HOME/.claude/skills" ] && TARGETS+=("$HOME/.claude/skills")
    if [ ${#TARGETS[@]} -eq 0 ]; then
        error "No skills directory found. Pass target as argument:"
        echo "  bash install.sh /path/to/your/skills/"
        exit 1
    fi
fi

# --- Clone to temp ---
TMPDIR=$(mktemp -d)
info "Downloading from $REPO_URL ..."
git clone --depth 1 "$REPO_URL" "$TMPDIR/repo" 2>/dev/null

if [ ! -d "$TMPDIR/repo/$SUBDIR" ]; then
    error "Subdirectory '$SUBDIR' not found in repo"
    rm -rf "$TMPDIR"
    exit 1
fi

# --- Install to each target ---
for TARGET in "${TARGETS[@]}"; do
    DEST="$TARGET/$SKILL_NAME"
    if [ -d "$DEST" ]; then
        warn "Existing installation found at $DEST"
        read -p "  Overwrite? [y/N] " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            info "Skipped $DEST"
            continue
        fi
        rm -rf "$DEST"
    fi
    mkdir -p "$DEST"
    cp -r "$TMPDIR/repo/$SUBDIR"/* "$DEST/"
    info "Installed to $DEST"
done

rm -rf "$TMPDIR"

# --- Remind about customization ---
echo ""
echo "============================================"
echo -e "${YELLOW}  ⚠️  SETUP REQUIRED BEFORE FIRST USE  ${NC}"
echo "============================================"
echo ""
echo "  You MUST customize these placeholder values:"
echo ""
echo "  1. Banned source list (3 files):"
echo "     - references/irsp.md           (line ~20: example list)"
echo "     - references/audit-checklist.md ([用户自定义的受控媒体名单])"
echo "     - references/source-audit-methodology.md (banned = [...])"
echo ""
echo "     → Add state-controlled media names relevant to YOUR research"
echo ""
echo "  2. Archive path:"
echo "     - SKILL.md  ([your-archive-directory])"
echo "     → Replace with your actual report save path"
echo ""
echo "  3. Tools:"
echo "     - firecrawl, exa, academic-research MCP (optional but recommended)"
echo ""
echo "  See README.md for full details."
echo "============================================"
