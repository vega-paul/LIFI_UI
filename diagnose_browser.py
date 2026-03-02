#!/usr/bin/env python3
"""
Browser Diagnostic Script for Playwright
This script helps diagnose browser launch issues on macOS
"""

import sys
import subprocess
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a command and return the result"""
    print(f"\n🔍 {description}")
    print(f"Command: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("✅ Success")
            if result.stdout.strip():
                print(f"Output: {result.stdout.strip()}")
        else:
            print("❌ Failed")
            if result.stderr.strip():
                print(f"Error: {result.stderr.strip()}")
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print("⏰ Timeout")
        return False
    except Exception as e:
        print(f"💥 Exception: {e}")
        return False

def check_system():
    """Check system requirements"""
    print("=== System Diagnostic ===")

    # Check Python version
    print(f"Python version: {sys.version}")

    # Check if we're in virtual environment
    in_venv = sys.prefix != sys.base_prefix
    print(f"Virtual environment: {'Yes' if in_venv else 'No'}")
    if in_venv:
        print(f"Virtual env path: {sys.prefix}")

    # Check macOS version
    run_command(["sw_vers"], "Check macOS version")

    # Check available browsers
    browsers = [
        "/Applications/Google Chrome.app",
        "/Applications/Microsoft Edge.app",
        "/Applications/Firefox.app",
        "/Applications/Safari.app"
    ]

    print("\n📱 Installed Browsers:")
    for browser in browsers:
        exists = Path(browser).exists()
        print(f"{'✅' if exists else '❌'} {Path(browser).name}: {'Found' if exists else 'Not found'}")

def check_playwright():
    """Check Playwright installation and browsers"""
    print("\n=== Playwright Diagnostic ===")

    # Check if playwright is installed
    try:
        import playwright
        try:
            version = playwright.__version__
            print(f"✅ Playwright installed: {version}")
        except AttributeError:
            print("✅ Playwright installed (version unknown)")
    except ImportError:
        print("❌ Playwright not
    if playwright_path.exists():
        print(f"✅ Playwright cache exists: {playwright_path}")
        browsers = list(playwright_path.glob("*-*"))
        for browser in browsers:
            print(f"  - {browser.name}")
    else:
        print("❌ Playwright cache not found")

    # Try to install browsers
    run_command([sys.executable, "-m", "playwright", "install", "--dry-run"], "Check browser installation")

    return True

def test_browser_launch():
    """Test basic browser launch"""
    print("\n=== Browser Launch Test ===")

    # Test with playwright-python directly
    test_script = '''
from playwright.sync_api import sync_playwright

def test_launch():
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False, args=["--no-sandbox", "--disable-dev-shm-usage"])
            page = browser.new_page()
            page.goto("https://example.com")
            title = page.title()
            print(f"Page title: {title}")
            browser.close()
            return True
        except Exception as e:
            print(f"Launch failed: {e}")
            return False

if __name__ == "__main__":
    success = test_launch()
    print(f"Test result: {'PASS' if success else 'FAIL'}")
'''

    with open('temp_test.py', 'w') as f:
        f.write(test_script)

    try:
        run_command([sys.executable, 'temp_test.py'], "Test browser launch with Playwright")
    finally:
        Path('temp_test.py').unlink(missing_ok=True)

def main():
    """Main diagnostic function"""
    print("🚀 Playwright Browser Diagnostic Tool")
    print("=" * 50)

    check_system()
    check_playwright()
    test_browser_launch()

    print("\n" + "=" * 50)
    print("📋 Troubleshooting Tips:")
    print("1. Reinstall Playwright browsers: playwright install --force")
    print("2. Try with different browser: pytest --browser firefox")
    print("3. Run in headless mode: pytest --headed=false")
    print("4. Check system resources and permissions")
    print("5. Update macOS and Xcode command line tools")
    print("6. Try running without virtual environment")

if __name__ == "__main__":
    main()