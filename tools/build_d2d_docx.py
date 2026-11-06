import os
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

ms_path = r"C:\Users\ketro\Downloads\Publication_Packages\the_dead_and_the_siege\manuscript.md"
out_docx = r"C:\Users\ketro\Downloads\Publication_Packages\the_dead_and_the_siege\The_Dead_and_the_Siege.docx"

with open(ms_path, "r", encoding="utf-8") as f:
    text = f.read()

doc = Document()

# Set standard 1-inch margins
sections = doc.sections
for s in sections:
    s.top_margin = Inches(1)
    s.bottom_margin = Inches(1)
    s.left_margin = Inches(1)
    s.right_margin = Inches(1)

# Normal style font
style = doc.styles['Normal']
font = style.font
font.name = 'Georgia'
font.size = Pt(11)
font.color.rgb = RGBColor(0x1a, 0x1a, 0x1a)

# --- 1. TITLE PAGE ---
for _ in range(3):
    doc.add_paragraph()

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_title = p_title.add_run("THE DEAD AND THE SIEGE")
run_title.font.name = 'Georgia'
run_title.font.size = Pt(28)
run_title.bold = True

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_sub = p_sub.add_run("Behind the Redoubt")
run_sub.font.name = 'Georgia'
run_sub.font.size = Pt(16)
run_sub.italic = True

for _ in range(4):
    doc.add_paragraph()

p_auth = doc.add_paragraph()
p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_auth = p_auth.add_run("Gabriel Simon")
run_auth.font.name = 'Georgia'
run_auth.font.size = Pt(16)
run_auth.bold = True

doc.add_page_break()

# --- 2. COPYRIGHT PAGE ---
p_cr = doc.add_paragraph()
p_cr.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_cr.add_run("The Dead and the Siege: Behind the Redoubt\n").bold = True
p_cr.add_run("Copyright © 2026 Gabriel Simon\n")
p_cr.add_run("All rights reserved.\n\n")
p_cr.add_run("This is a work of fiction. Names, characters, businesses, places, events, and incidents are either the products of the author’s imagination or used in a fictitious manner. Any resemblance to actual persons, living or dead, or actual events is purely coincidental.\n\n")
p_cr.add_run("Cover design and interior formatting by Gabriel Simon.\n")
p_cr.add_run("First Edition: November 2026\n")

doc.add_page_break()

# --- 3. BODY CHAPTERS ---
lines = text.splitlines()
in_chapter = False
current_part = None

for line in lines:
    l = line.strip()
    if not l:
        continue
    if l.startswith("# The Dead and the Siege") or l.startswith("## Behind the Redoubt") or l.startswith("### By Gabriel Simon") or l == "---":
        continue
    
    if l.startswith("PART "):
        current_part = l
        p_part = doc.add_paragraph()
        p_part.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_part.paragraph_format.space_before = Pt(36)
        p_part.paragraph_format.space_after = Pt(18)
        run_part = p_part.add_run(l)
        run_part.font.name = 'Georgia'
        run_part.font.size = Pt(14)
        run_part.bold = True
        run_part.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
        continue

    if l.startswith("CHAPTER "):
        if in_chapter:
            doc.add_page_break()
        in_chapter = True
        
        # Heading 1 for D2D automatic Table of Contents & Paperback headers
        h1 = doc.add_heading(level=1)
        h1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        h1.paragraph_format.space_before = Pt(24)
        h1.paragraph_format.space_after = Pt(18)
        run_h1 = h1.add_run(l)
        run_h1.font.name = 'Georgia'
        run_h1.font.size = Pt(18)
        run_h1.bold = True
        run_h1.font.color.rgb = RGBColor(0x11, 0x11, 0x11)
        continue

    # Body Paragraph
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.first_line_indent = Inches(0.25)
    
    run = p.add_run(l)
    run.font.name = 'Georgia'
    run.font.size = Pt(11)

doc.save(out_docx)
sz_mb = os.path.getsize(out_docx) / (1024 * 1024)
print(f"Successfully generated D2D Master DOCX: {out_docx} ({sz_mb:.2f} MB)")
