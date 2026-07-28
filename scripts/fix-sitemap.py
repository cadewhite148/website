#!/usr/bin/env python3
"""Post-render fixups for _site/sitemap.xml.

Quarto lists the homepage as /index.html, but every internal link (and the
canonical tag in index.qmd) points at the bare root. Search Console flags the
two as duplicates, so rewrite the sitemap to agree with the canonical.

Also lists the linked PDFs, which Quarto treats as opaque resources and leaves
out of the sitemap entirely.
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

SITE_URL = "https://cadewhite.co"
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
SITEMAP = os.path.join("_site", "sitemap.xml")
EXTRA_ASSETS = ["papers/cv.pdf", "papers/jmp.pdf"]

ET.register_namespace("", NS)
tree = ET.parse(SITEMAP)
root = tree.getroot()


def loc_text(url):
    return url.find(f"{{{NS}}}loc").text


for url in root.findall(f"{{{NS}}}url"):
    loc = url.find(f"{{{NS}}}loc")
    if loc.text == f"{SITE_URL}/index.html":
        loc.text = f"{SITE_URL}/"

known = {loc_text(u) for u in root.findall(f"{{{NS}}}url")}

for asset in EXTRA_ASSETS:
    path = os.path.join("_site", asset)
    url = f"{SITE_URL}/{asset}"
    if url in known or not os.path.exists(path):
        continue
    entry = ET.SubElement(root, f"{{{NS}}}url")
    ET.SubElement(entry, f"{{{NS}}}loc").text = url
    mtime = datetime.fromtimestamp(os.path.getmtime(path), timezone.utc)
    ET.SubElement(entry, f"{{{NS}}}lastmod").text = mtime.isoformat(
        timespec="milliseconds"
    ).replace("+00:00", "Z")

ET.indent(tree, space="  ")
tree.write(SITEMAP, encoding="UTF-8", xml_declaration=True)
print(f"fix-sitemap: {len(root.findall(f'{{{NS}}}url'))} URLs in {SITEMAP}")
