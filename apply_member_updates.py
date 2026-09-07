import os
import re

SCOPE_PATH = r"c:\Users\ABHIJIT\Downloads\ccic web\templates\scope_members.html"
MAGIC_PATH = r"c:\Users\ABHIJIT\Downloads\ccic web\templates\magic_members.html"

# --- 1. Update scope_members.html ---
with open(SCOPE_PATH, "r", encoding="utf-8") as f:
    scope_content = f.read()

# Mathupriya: replace placeholder account_circle with real image
scope_content = re.sub(
    r'<div class="w-20 h-20 rounded-xl overflow-hidden shrink-0 bg-surface-container-high relative flex items-center justify-center">\s*<span class="material-symbols-outlined text-outline text-5xl">account_circle</span>\s*</div>',
    '<div class="w-20 h-20 rounded-xl overflow-hidden shrink-0 bg-surface-container-high relative shadow-sm"><img class="w-full h-full object-cover" alt="Ms. Mathupriya" src="/static/images/mathupriya.jpg"></div>',
    scope_content
)

# Ebenezer Roselin: replace image src
scope_content = re.sub(
    r'<img class="w-full h-full object-cover"[^>]*data-alt="Academic portrait of Mrs\. S\. Ebenezer Roselin[^>]*>',
    '<img class="w-full h-full object-cover" alt="Mrs. S. Ebenezer Roselin" src="/static/images/ebenezer.jpg">',
    scope_content
)

# Anitha: replace image src
scope_content = re.sub(
    r'<img class="w-full h-full object-cover"[^>]*data-alt="Portrait photograph of Ms\. M\. Anitha[^>]*>',
    '<img class="w-full h-full object-cover" alt="Ms. M. Anitha" src="/static/images/anitha.jpg">',
    scope_content
)

# Hari Priyan: replace image src
scope_content = re.sub(
    r'<img class="w-full h-full object-cover"[^>]*data-alt="Portrait of S L Hari Priyan[^>]*>',
    '<img class="w-full h-full object-cover" alt="S L HARI PRIYAN" src="/static/images/haripriyan.jpg">',
    scope_content
)

# Add Guru Prakash card next to Hari Priyan
guru_card = """
<!-- Co-ordinator 2: K Guru Prakash -->
<div class="bg-surface-container-lowest p-space-lg rounded-xl shadow-md flex items-center gap-space-md">
<div class="w-16 h-16 rounded-xl overflow-hidden bg-surface-container-high shrink-0">
<img class="w-full h-full object-cover" alt="K GURU PRAKASH" src="/static/images/guru.jpg">
</div>
<div class="flex flex-col">
<div class="flex items-center gap-space-xs">
<span class="font-label-sm text-label-sm text-secondary font-bold uppercase">Student Co-ordinator</span>
<span class="text-on-surface-variant text-label-sm font-label-sm">• SEC CSE (AIML)</span>
</div>
<h3 class="font-title-md text-title-md text-on-surface font-bold">K GURU PRAKASH</h3>
<p class="font-body-md text-body-md text-on-surface-variant">Robotics, Vision Systems &amp; Hardware Technical Acceleration</p>
</div>
</div>
"""

# Replace the comment or add below Hari Priyan
if "<!-- Co-ordinator 2: K Guru Prakash -->" in scope_content:
    scope_content = scope_content.replace("<!-- Co-ordinator 2: K Guru Prakash -->", guru_card)

# Change the grid from max-w-3xl single column to 2-column or grid-cols-1 md:grid-cols-2
scope_content = scope_content.replace(
    '<div class="grid grid-cols-1 gap-space-lg max-w-3xl">\n<!-- Co-ordinator 1: S L Hari Priyan -->',
    '<div class="grid grid-cols-1 md:grid-cols-2 gap-space-lg max-w-5xl">\n<!-- Co-ordinator 1: S L Hari Priyan -->'
)

with open(SCOPE_PATH, "w", encoding="utf-8") as f:
    f.write(scope_content)
print("Updated scope_members.html")

# --- 2. Update magic_members.html ---
with open(MAGIC_PATH, "r", encoding="utf-8") as f:
    magic_content = f.read()

# Update Hari Priyan in magic_members.html
magic_content = re.sub(
    r'<img class="w-full h-full object-cover rounded-lg"[^>]*data-alt="Editorial portrait of an articulate Indian male engineering student leader in a navy formal blazer[^>]*>',
    '<img class="w-full h-full object-cover rounded-lg" alt="S L HARI PRIYAN" src="/static/images/haripriyan.jpg">',
    magic_content
)

# Update Guru in magic_members.html
magic_content = re.sub(
    r'<img class="w-full h-full object-cover rounded-lg"[^>]*data-alt="Professional studio portrait of an ambitious Indian male software engineer student wearing a modern charcoal formal shirt[^>]*>',
    '<img class="w-full h-full object-cover rounded-lg" alt="K GURU PRAKASH" src="/static/images/guru.jpg">',
    magic_content
)

with open(MAGIC_PATH, "w", encoding="utf-8") as f:
    f.write(magic_content)
print("Updated magic_members.html")
