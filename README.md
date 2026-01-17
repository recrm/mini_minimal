# Mini-Minimal Computing Website Generator

A simple tool to generate static websites from markdown files and HTML templates.

## Installation

1. Install Python 3.6 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your markdown files in the `content/` directory
2. Customize the template in `templates/base.jinja`
3. Run the generator:
   ```bash
   python build.py
   ```
4. Find your generated HTML files in the `output/` directory

## Custom Directories

You can specify custom directories by modifying values in config.py.

## Markdown Files

Create `.md` files in the `content/` directory. You can add frontmatter at the top:

```markdown
---
title: My Page Title
template: base.html
footer: Custom footer text
---


# Content goes here
```


## Templates

To assign a page to a template, please set the "template" attribute to the pages frontmatter.

To use a different template, specify it in the frontmatter:
```markdown
---
title: My Gallery Page
template: gallery.html
---
```

## Project Structure

```
.
├── build.py          # Main generator script
├── config.py         # Configuration variables for build.py
├── requirements.txt  # Python dependencies
├── templates/        # HTML templates
│   ├── base.html     # Default template
│   └── gallery.html  # Gallery template for images
├── content/          # Markdown source files
│   ├── index.md
│   ├── about.md
│   ├── pictures.md
│   └── pictures/     # Image files for gallery
│       └── *.jpg, *.png, etc.
└── output/           # Generated HTML files
    └── pictures/     # Copied image files
```
