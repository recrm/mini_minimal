---
title: About This Project
template: base.jinja
content: this is a test
---
This is a minimal computing tool designed to generate websites from markdown files and templates.

[← Back to home](index.html)

## Philosophy

{{ content }}

The template is right below this.

{{ template }}

The template is right above this.

The goal is to keep things simple:
- Minimal dependencies
- Easy to understand
- Easy to customize
- No unnecessary complexity

## Technology

- Python for the generator script
- Markdown for content
- HTML/CSS for templates
- Static output for easy deployment

![This is an image](static/img/DSC06223.jpeg)

{% for p in site %}

{{ p.title }} {{ p.output_url }}

{% endfor %}

