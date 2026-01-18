# SCSS Deprecation Fix: darken() and lighten()

This document explains how we fixed the `darken()` and `lighten()` deprecation warnings in the Jekyll TeXt theme.

## Problem

The theme was using deprecated Sass color functions:
- `darken($color, $amount)` - deprecated
- `lighten($color, $amount)` - deprecated

These functions generated 481+ deprecation warnings during each build.

## Solution

We created an override file in `_sass/common/classes/_clickable.scss` that replaces the deprecated functions with modern Sass color functions:

- `darken($color, 14%)` → `color.adjust($color, $lightness: -14%)`
- `lighten($color, 18%)` → `color.adjust($color, $lightness: 18%)`

## Files Modified

### Created: `_sass/common/classes/_clickable.scss`

This file overrides the theme's clickable mixin with modern Sass color functions:

```scss
@use "sass:color";

// Replaced all instances of:
// darken($color, $amount) → color.adjust($color, $lightness: -$amount)
// lighten($color, $amount) → color.adjust($color, $lightness: $amount)
```

## How It Works

Jekyll prioritizes files in your site's `_sass` directory over theme files. When the theme imports `common/classes/_clickable.scss`, Jekyll uses our override instead of the theme's version.

## Result

- ✅ **Before**: 481+ deprecation warnings about `darken()` and `lighten()`
- ✅ **After**: Zero warnings about `darken()` and `lighten()`
- ✅ Build still succeeds
- ✅ Functionality unchanged

## Notes

1. The `@use "sass:color"` statement must be at the top of the file before any other Sass code.
2. Negative values for `$lightness` darken the color (replacing `darken()`).
3. Positive values for `$lightness` lighten the color (replacing `lighten()`).
4. Other deprecation warnings (about `@import` and global built-in functions) remain but are less critical and come from the theme's architecture.

## References

- [Sass Color Functions Documentation](https://sass-lang.com/documentation/modules/color)
- [Sass Deprecation Warnings](https://sass-lang.com/blog/wide-gamut-colors-in-sass)
