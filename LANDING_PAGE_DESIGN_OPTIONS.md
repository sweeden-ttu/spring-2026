# Landing Page Design Options

This document outlines various landing page design options for the Spring 2026 coursework site, using jekyll-TeXt-theme's landing layout capabilities.

## Current Design: "Card-Based Course Hub"

**Features:**
- Full-height hero with dark theme
- Course cards with icons and images
- Recent updates section
- External resources links
- Tools and software section
- Quick navigation

**Colors:** Dark blues/teals (currently) - **Should be updated to TTU Scarlet/Black/White**

## Alternative Design Options

### Option 1: "Modern Research Hub" Theme

**Concept:** Clean, professional academic site with TTU branding

**Hero Section:**
- White/light background with subtle TTU Scarlet accents
- Double T logo watermark in background
- Large headline: "Computer Science at Texas Tech"
- Clean typography (Helvetica Neue style)
- 3 CTAs: View Courses, Browse Topics, Resources

**Sections:**
1. **Featured Courses** - 2 large cards side-by-side (CS-5374, CS-6343)
2. **Research & Labs** - Grid of 4 items (LangSmith, HPCC, Kaggle, Tools)
3. **Quick Links** - Horizontal button bar
4. **Updates** - Timeline-style announcements

**Color Palette:**
- Primary: TTU Scarlet (#E90802)
- Secondary: Black (#000000)
- Background: White (#FFFFFF)
- Accents: Grays (#333333, #666666)

**Pros:** Professional, clean, easy to navigate
**Cons:** Less visual interest than darker themes

---

### Option 2: "Dark Tech Hub" Theme

**Concept:** Modern, tech-forward design with dark backgrounds

**Hero Section:**
- Dark background (Black or very dark gray #1a1a1a)
- Scarlet accents for buttons and highlights
- Code-themed background pattern (circuit lines, brackets)
- Glowing Scarlet CTAs

**Sections:**
1. **Courses** - Cards with code/terminal aesthetic
2. **Tools** - Icon-based grid with hover effects
3. **Resources** - Tabbed interface
4. **Updates** - Card carousel

**Color Palette:**
- Primary: TTU Scarlet (#E90802)
- Background: Black (#000000) / Dark Gray (#1a1a1a)
- Text: White (#FFFFFF)
- Accents: Medium Gray (#666666)

**Pros:** Modern, tech-focused, visually striking
**Cons:** Can be harder to read, less traditional academic

---

### Option 3: "Minimalist Academic" Theme

**Concept:** Typography-focused, content-first design

**Hero Section:**
- White background
- Large serif/slab-serif heading (Neutraface Slab style)
- Minimal text: "Spring 2026 Coursework"
- Single prominent CTA
- Double T logo as subtle watermark

**Sections:**
1. **Courses** - Text-based list with icons
2. **Recent Updates** - Simple timeline
3. **Quick Links** - Vertical navigation sidebar
4. **Contact/Resources** - Simple link list

**Color Palette:**
- Primary: Black (#000000)
- Accent: TTU Scarlet (#E90802) for links/CTAs
- Background: White (#FFFFFF)
- Text: Dark Gray (#333333)

**Pros:** Clean, readable, professional, accessible
**Cons:** Less visually engaging

---

### Option 4: "One-Page Scroll" Theme

**Concept:** Single continuous page with smooth scrolling sections

**Structure:**
- Fixed navigation bar (becomes sticky on scroll)
- Hero (100vh)
- Courses (full-width cards)
- Updates (horizontal timeline)
- Resources (icon grid)
- Tools (feature grid)
- Footer (contact/links)

**Color Palette:**
- Alternating: White / Light Gray (#f5f5f5) sections
- Scarlet for CTAs and highlights
- Black for text

**Pros:** Modern, engaging, tells a story
**Cons:** Can be long, less traditional navigation

---

### Option 5: "Dashboard Style" Theme

**Concept:** Information-dense, widget-based layout

**Structure:**
- Hero banner (shorter, 50vh)
- Dashboard grid:
  - Course cards (top left)
  - Recent updates feed (top right)
  - Quick links widget (bottom left)
  - Calendar/events widget (bottom right)
- Stats/numbers panel

**Color Palette:**
- Light gray background (#f8f9fa)
- White cards with shadows
- Scarlet accents
- Black text

**Pros:** Information-rich, functional
**Cons:** Can feel busy, less elegant

---

## jekyll-TeXt-theme Landing Layout Features

The landing layout supports:

1. **Hero Header (`article_header`)**:
   - Full height (100vh) or custom height
   - Dark or light theme
   - Background color and/or image
   - Gradient overlays
   - Action buttons (CTAs)

2. **Sections (`data.sections`)**:
   - Multiple sections with different themes (light/dark)
   - Background colors per section
   - Images (full-width or inline)
   - Grid layouts (`children` arrays)
   - Action buttons per section/item

3. **Layout Patterns**:
   - Single column sections
   - Grid layouts (2, 3, 4 columns via `children`)
   - Image + text combinations
   - Card-based layouts

## Recommended: "Modern Research Hub" (Option 1)

**Recommended for:** Professional academic site that aligns with TTU branding

**Implementation:**
- Use white/light backgrounds
- TTU Scarlet for CTAs and accents
- Black for primary text
- Double T or code-themed SVG patterns
- Clean, readable typography

**Why:** 
- Matches TTU brand guidelines
- Professional and accessible
- Easy to maintain and update
- Works well for academic content

---

## Color Guidelines (Texas Tech Brand)

### Primary Colors:
- **TTU Scarlet**: `#E90802`
- **Black**: `#000000`
- **White**: `#FFFFFF`

### Grays (Accents):
- Dark Gray: `#333333`
- Medium Gray: `#666666`
- Light Gray: `#CCCCCC`
- Very Light Gray: `#F5F5F5`

### Usage:
- Use Scarlet sparingly (CTAs, highlights, accents)
- Use Black for primary text
- Use White/Light Gray for backgrounds
- Maintain good contrast for accessibility

---

## Icon and Image Themes for CS

### Computer Science Icons

**Code & Development:**
- Code brackets: `<>`, `{}`, `[]`
- Terminal/console (monospace styling)
- Function syntax: `function()`, `def`, `class`
- Code blocks with syntax highlighting
- Git branches and commits

**Hardware & Circuits:**
- Circuit boards with traces
- Logic gates (AND, OR, XOR)
- CPU/microprocessor icons
- Memory/data storage symbols
- Network nodes and connections

**Data & Algorithms:**
- Binary code (0101 patterns)
- Data structures (trees, graphs, arrays)
- Flowcharts and decision trees
- Database schemas
- Data flow arrows and pipelines

**Visual Patterns:**
- Matrix-style dots/grids
- Hexagonal patterns (hex grids)
- Parallel lines (data streams)
- Geometric fractals
- Minimalist circuit diagrams

### Academic Icons

**Education & Learning:**
- Graduation cap (master's/PhD)
- Books/documents with code overlay
- Calculator/math symbols (∑, ∫, ∀)
- Lab equipment (test tubes, beakers)
- Research symbols (microscopes, charts)

**Institutional:**
- Texas Tech Double T logo
- University seal elements
- Department badges
- Academic building silhouettes

### Theme-Specific Combinations

**Dark Tech Hub (Currently Applied):**
- Black backgrounds (#000000, #1a1a1a)
- TTU Scarlet (#E90802) for accents and highlights
- Code bracket patterns (`</>`) as background texture
- Circuit grid overlays in Scarlet
- Terminal/console aesthetic with monospace fonts
- Glowing effects on interactive elements

**Combination Guidelines:**
- Code + Academic = Modern CS education at Texas Tech
- Circuit patterns + TTU Scarlet = Strong brand identity
- Minimal geometric shapes + Dark theme = Professional tech hub
- Binary/code patterns + Scarlet accents = Distinctive CS branding

### SVG Image Guidelines

**Current Assets:**
- `logo.svg` - TTU Scarlet/Black gradient with Double T and code brackets
- `hero-background.svg` - Black gradient with code patterns and circuit lines
- `course-verification.svg` - Scarlet/Black gradient with checkmark and code accents
- `course-cryptography.svg` - Black/Scarlet gradient with lock icon and binary code

**Best Practices:**
- Always use TTU Scarlet (#E90802) for primary accents
- Use Black (#000000) for backgrounds in dark themes
- Maintain SVG scalability (vector graphics)
- Include opacity variations (0.1-0.3) for overlays
- Keep file sizes optimized (< 50KB per SVG)

---

## Implementation Notes

### Current Implementation: Dark Tech Hub Theme

The site currently uses the **Dark Tech Hub** theme as configured in `index.html`:

**Configuration:**
```yaml
# In index.html
article_header:
  theme: dark
  background_color: "#000000"
  background_image:
    gradient: "linear-gradient(rgba(233, 8, 2, 0.1), rgba(0, 0, 0, 0.9))"
    src: /assets/images/hero-background.svg

data:
  sections:
    - theme: dark
      background_color: "#1a1a1a"  # or "#000000"
```

**Global Theme:**
- `_config.yml`: `text_skin: dark` (site-wide dark theme)
- `highlight_theme: tomorrow-night` (dark code highlighting)

### To Implement a Different Design

1. **Update `index.html`** front matter:
   ```yaml
   # Change hero section
   article_header:
     theme: light        # or dark
     background_color: "#FFFFFF"  # Change for different theme
     background_image:
       gradient: "..."   # Adjust gradient overlay
   
   # Modify sections
   data:
     sections:
       - theme: light    # or dark
         background_color: "#F5F5F5"  # Adjust per section
   ```

2. **Update SVGs** in `assets/images/`:
   - Replace color gradients: Use TTU Scarlet (#E90802) for accents
   - Add TTU Double T: Include in logo and hero elements
   - Modify patterns: Adjust code brackets, circuit lines for different density
   - Test contrast: Ensure SVGs work on both light and dark backgrounds

3. **Update Global Theme** in `_config.yml`:
   ```yaml
   text_skin: dark       # Options: default, dark, forest, ocean, chocolate, orange
   highlight_theme: tomorrow-night  # Options: tomorrow, tomorrow-night, etc.
   ```

4. **Custom CSS** (if needed) in `assets/css/custom.scss`:
   ```scss
   // Override theme defaults
   .hero {
     background-color: #000000;
   }
   
   // Add TTU-branded components
   .button--ttu-scarlet {
     background-color: #E90802;
     color: #FFFFFF;
   }
   ```

5. **Test Responsiveness**:
   - Mobile layouts: Check `< 768px` breakpoints
   - Grid collapsing: Verify `children` arrays collapse to single column
   - Button sizes: Ensure CTAs are tappable (min 44px touch target)
   - Image scaling: Test SVG responsiveness on small screens
   - Dark mode: Verify text contrast ratios (WCAG AA: 4.5:1 for normal text)

### Switching Between Themes

**Quick Theme Switch:**

To change from Dark Tech Hub to another option:

1. **Modern Research Hub (Light)**:
   ```yaml
   # _config.yml
   text_skin: default
   
   # index.html - change all sections to:
   theme: light
   background_color: "#FFFFFF" or "#F5F5F5"
   ```

2. **Minimalist Academic (Light)**:
   ```yaml
   # _config.yml
   text_skin: default
   highlight_theme: tomorrow
   
   # index.html - use white backgrounds, minimal sections
   ```

3. **Keep Dark Tech Hub**:
   ```yaml
   # Already configured - no changes needed
   text_skin: dark
   highlight_theme: tomorrow-night
   ```
