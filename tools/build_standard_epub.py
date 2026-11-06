import os
import re
from ebooklib import epub

ms_path = r"C:\Users\ketro\Downloads\Publication_Packages\the_dead_and_the_siege\manuscript.md"
cover_path = r"C:\Users\ketro\Downloads\Publication_Packages\the_dead_and_the_siege\The_Dead_and_the_Siege_Cover.jpg"
out_epub = r"C:\Users\ketro\Downloads\Publication_Packages\the_dead_and_the_siege\The_Dead_and_the_Siege.epub"

with open(ms_path, "r", encoding="utf-8") as f:
    text = f.read()

book = epub.EpubBook()
book.set_identifier("the_dead_and_the_siege_2026")
book.set_title("The Dead and the Siege: Behind the Redoubt")
book.set_language("en")
book.add_author("Gabriel Simon")

# Set Cover if exists
if os.path.exists(cover_path):
    with open(cover_path, "rb") as cf:
        book.set_cover("cover.jpg", cf.read())

# CSS Style
style = '''
@namespace epub "http://www.idpf.org/2007/ops";
body {
    font-family: "Georgia", "Times New Roman", serif;
    margin: 5%;
    line-height: 1.4;
}
h1 {
    text-align: center;
    font-size: 1.5em;
    margin-top: 2em;
    margin-bottom: 1em;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
h2 {
    text-align: center;
    font-size: 1.2em;
    color: #555;
    margin-bottom: 2em;
}
p {
    text-indent: 1.5em;
    margin: 0;
    padding: 0;
    text-align: justify;
}
p.noindent {
    text-indent: 0;
}
'''
default_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
book.add_item(default_css)

# Parse chapters
lines = text.splitlines()
chapters = []
current_ch_title = None
current_ch_paras = []
ch_num = 1

for line in lines:
    l = line.strip()
    if not l:
        continue
    if l.startswith("# ") or l.startswith("## ") or l.startswith("### ") or l == "---":
        continue
    if l.startswith("PART "):
        continue
    if l.startswith("CHAPTER "):
        if current_ch_title and current_ch_paras:
            # create chapter
            c = epub.EpubHtml(title=current_ch_title, file_name=f'chap_{ch_num:02d}.xhtml', lang='en')
            body_html = f"<h1>{current_ch_title}</h1>\n"
            for p in current_ch_paras:
                body_html += f"<p>{p}</p>\n"
            c.content = body_html
            c.add_item(default_css)
            book.add_item(c)
            chapters.append(c)
            ch_num += 1
            current_ch_paras = []
        current_ch_title = l
        continue
    current_ch_paras.append(l)

# Last chapter
if current_ch_title and current_ch_paras:
    c = epub.EpubHtml(title=current_ch_title, file_name=f'chap_{ch_num:02d}.xhtml', lang='en')
    body_html = f"<h1>{current_ch_title}</h1>\n"
    for p in current_ch_paras:
        body_html += f"<p>{p}</p>\n"
    c.content = body_html
    c.add_item(default_css)
    book.add_item(c)
    chapters.append(c)

# Table of Contents & Spine
book.toc = tuple(chapters)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
book.spine = ['nav'] + chapters

epub.write_epub(out_epub, book)
sz_mb = os.path.getsize(out_epub) / (1024 * 1024)
print(f"Successfully generated standalone EPUB: {out_epub} ({sz_mb:.2f} MB)")
