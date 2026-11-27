#!/bin/bash
# 🦅 GHOSTHAWK v2.0 - Linux Optimized Security Scanner
# Shell Script for Direct Execution on Linux

set -e

SCRIPT_NAME="cetj_security_scan_v2_linux.py"

# Function to show help
show_help() {
    echo "======================================================================="
    echo "🦅 GHOSTHAWK v2.0 - Linux Optimized Security Scanner"
    echo "======================================================================="
    echo ""
    echo "📋 Usage:"
    echo "   $0 [OPTIONS]"
    echo ""
    echo "🎯 Options:"
    echo "   --target, -t     Target URL (default: https://cetj.edu.ly)"
    echo "   --proxy, -p      Proxy type: tor/ssh/http/https (default: none)"
    echo "   --timeout, -T    Request timeout in seconds (default: 10)"
    echo "   --output, -o     Output file for report (default: full_security_report.json)"
    echo "   --quiet, -q      Quiet mode - only show critical results"
    echo "   --help, -h       Show this help message"
    echo ""
    echo "📝 Examples:"
    echo "   $0 --target https://example.com"
    echo "   $0 -t https://example.com -p tor -T 15 -o report.json"
    echo "   $0 --target https://example.com --quiet"
    echo ""
    echo "======================================================================="
}

# Function to check dependencies
check_dependencies() {
    if ! command -v python3 &> /dev/null; then
        echo "❌ Error: Python3 is not installed!"
        echo "📦 Install it with: sudo apt install python3 python3-pip"
        exit 1
    fi

    if ! pip3 show requests &> /dev/null; then
        echo "⚠️ Warning: 'requests' module not found!"
        echo "📦 Installing dependencies..."
        pip3 install -r requirements.txt
    fi

    if ! pip3 show beautifulsoup4 &> /dev/null; then
        echo "⚠️ Warning: 'beautifulsoup4' module not found!"
        echo "📦 Installing dependencies..."
        pip3 install -r requirements.txt
    fi
}

# Parse arguments
TARGET_URL="https://cetj.edu.ly"
USE_PROXY="false"
PROXY_TYPE=""
TIMEOUT=10
OUTPUT_FILE="full_security_report.json"
QUIET_MODE="false"

while [[ $# -gt 0 ]]; do
    case $1 in
        --target|-t)
            TARGET_URL="$2"
            shift 2
            ;;
        --proxy|-p)
            USE_PROXY="true"
            PROXY_TYPE="$2"
            shift 2
            ;;
        --timeout|-T)
            TIMEOUT="$2"
            shift 2
            ;;
        --output|-o)
            OUTPUT_FILE="$2"
            shift 2
            ;;
        --quiet|-q)
            QUIET_MODE="true"
            shift
            ;;
        --help|-h)
            show_help
            exit 0
            ;;
        *)
            echo "❌ Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

# Show header (unless quiet mode)
if [[ "$QUIET_MODE" != "true" ]]; then
    echo ""
    echo "======================================================================="
    echo "🦅 GHOSTHAWK v2.0 - Linux Optimized Security Scanner"
    echo "======================================================================="
    echo ""
fi

# Check dependencies
check_dependencies

# Run the Python script
echo "🚀 Starting comprehensive security scan: $TARGET_URL"
python3 "$SCRIPT_NAME" \
    --target "$TARGET_URL" \
    --proxy "$USE_PROXY" \
    --timeout "$TIMEOUT" \
    --output "$OUTPUT_FILE" \
    --quiet "$QUIET_MODE"

echo ""
echo "======================================================================="
echo "✅ Scan completed successfully!"
echo "======================================================================="