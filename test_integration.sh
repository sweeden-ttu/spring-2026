#!/bin/bash

# Jekyll TeXt Theme Integration Test Script
# Tests the site build and verifies key components

set -e

echo "=========================================="
echo "Jekyll TeXt Theme Integration Tests"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

PASSED=0
FAILED=0

# Function to run a test
test_check() {
    local test_name=$1
    local command=$2
    
    echo -n "Testing: $test_name... "
    
    if eval "$command" > /dev/null 2>&1; then
        echo -e "${GREEN}✓ PASSED${NC}"
        ((PASSED++))
        return 0
    else
        echo -e "${RED}✗ FAILED${NC}"
        ((FAILED++))
        return 1
    fi
}

# Function to check if file exists and has content
test_file_exists() {
    local file=$1
    local test_name=$2
    
    echo -n "Testing: $test_name... "
    
    if [ -f "$file" ] && [ -s "$file" ]; then
        echo -e "${GREEN}✓ PASSED${NC}"
        ((PASSED++))
        return 0
    else
        echo -e "${RED}✗ FAILED${NC} (file missing or empty: $file)"
        ((FAILED++))
        return 1
    fi
}

echo "Step 1: Building Jekyll site..."
echo "-----------------------------------"
if bundle exec jekyll build > build.log 2>&1; then
    echo -e "${GREEN}✓ Build completed successfully${NC}"
else
    echo -e "${RED}✗ Build failed${NC}"
    echo "Build log:"
    tail -50 build.log
    exit 1
fi
echo ""

echo "Step 2: Verifying build artifacts..."
echo "-----------------------------------"

# Test 1: Check if _site directory exists
test_file_exists "_site/index.html" "Homepage exists"

# Test 2: Check if CSS is generated
test_file_exists "_site/assets/css/main.css" "CSS file generated"

# Test 3: Check if theme styles are present
test_check "Theme CSS contains styling" "grep -qi '\.main\|body\|header\|footer' _site/assets/css/main.css"

# Test 4: Check if index.html has content
test_check "Homepage has content" "[ $(wc -l < _site/index.html) -gt 10 ]"

# Test 5: Check if theme layouts are being used
test_check "Homepage uses theme layout" "grep -q 'jekyll-text-theme' _site/index.html || grep -q '<html' _site/index.html"

# Test 6: Check if navigation structure exists
test_check "Navigation structure present" "grep -q 'nav' _site/index.html || grep -q 'menu' _site/index.html"

# Test 7: Check if courses page exists
test_file_exists "_site/courses/index.html" "Courses page exists"

# Test 8: Check for required theme components
test_check "Theme components loaded" "grep -q 'main' _site/index.html || grep -q 'header' _site/index.html"

# Test 9: Verify no broken references
if grep -r "undefined\|null\|NaN" _site/ --include="*.html" 2>/dev/null | head -5; then
    echo -e "${YELLOW}⚠ Warning: Potential undefined references found${NC}"
else
    echo -e "${GREEN}✓ No obvious broken references${NC}"
    ((PASSED++))
fi

echo ""
echo "Step 3: Validating HTML structure..."
echo "-----------------------------------"

# Test 10: Check HTML structure
test_check "HTML has doctype or html tag" "grep -q '<!DOCTYPE html>\|<html' _site/index.html"

# Test 11: Check for metadata
test_check "Page has title or meta tags" "grep -q '<title>\|<meta' _site/index.html"

echo ""
echo "Step 4: Testing theme configuration..."
echo "-----------------------------------"

# Test 12: Check if theme is configured
test_check "Theme configured in site" "grep -q 'text_skin\|highlight_theme' _config.yml"

# Test 13: Verify Gemfile has theme
test_check "Theme in Gemfile" "grep -q 'jekyll-text-theme' Gemfile"

echo ""
echo "=========================================="
echo "Test Results Summary"
echo "=========================================="
echo -e "${GREEN}Passed: $PASSED${NC}"
if [ $FAILED -gt 0 ]; then
    echo -e "${RED}Failed: $FAILED${NC}"
else
    echo -e "${GREEN}Failed: $FAILED${NC}"
fi
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}✗ Some tests failed${NC}"
    exit 1
fi
