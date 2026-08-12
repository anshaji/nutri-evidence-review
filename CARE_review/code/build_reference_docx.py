"""Build a styled pandoc reference.docx for the CARE deep-dive report.

Pandoc's default reference doc is functional but plain. This regenerates it and
patches word/styles.xml so the rendered report reads as a finished document:
serif body text, coloured sans headings, shaded verdict boxes (markdown
blockquotes), and ruled tables with a shaded header row.

Fonts are restricted to Cambria and Calibri, both of which ship with Microsoft
Office on macOS and Windows, so the file renders identically for CARE partners
without embedding anything.

Run:  python3 CARE_review/code/build_reference_docx.py
Out:  CARE_review/code/assets/reference.docx
"""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

ASSETS = Path(__file__).resolve().parent / "assets"
REFERENCE = ASSETS / "reference.docx"

BODY_FONT = "Cambria"
HEAD_FONT = "Calibri"

INK = "1A1A1A"        # body text
DEEP = "12495B"       # H1 / title — deep teal
MID = "1F6B7B"        # H2
SLATE = "3D4A52"      # H3/H4
RULE = "C9D6DB"       # table + box borders
BOX_FILL = "F2F7F9"   # verdict-box background
HEAD_FILL = "E4EDF1"  # table header row


def fonts(name: str) -> str:
    return (f'<w:rFonts w:ascii="{name}" w:hAnsi="{name}" '
            f'w:eastAsia="{name}" w:cs="{name}"/>')


def replace_style(xml: str, style_id: str, *, ppr: str = "", rpr: str = "") -> str:
    """Replace the <w:pPr>/<w:rPr> payload of one style, preserving the rest."""
    pattern = re.compile(
        r'(<w:style [^>]*w:styleId="' + re.escape(style_id) + r'".*?</w:style>)',
        re.S)
    match = pattern.search(xml)
    if not match:
        return xml
    block = match.group(1)

    def swap(blk: str, tag: str, payload: str) -> str:
        if not payload:
            return blk
        existing = re.search(rf'<w:{tag}>.*?</w:{tag}>', blk, re.S)
        new = f'<w:{tag}>{payload}</w:{tag}>'
        if existing:
            return blk.replace(existing.group(0), new)
        return blk.replace('</w:style>', new + '</w:style>')

    block = swap(block, 'pPr', ppr)
    block = swap(block, 'rPr', rpr)
    return xml.replace(match.group(1), block)


def patch_styles(xml: str) -> str:
    # ---- body -------------------------------------------------------------
    xml = replace_style(
        xml, "Normal",
        ppr='<w:spacing w:before="0" w:after="140" w:line="276" w:lineRule="auto"/>',
        rpr=f'{fonts(BODY_FONT)}<w:color w:val="{INK}"/><w:sz w:val="21"/>'
            f'<w:szCs w:val="21"/>')
    xml = replace_style(
        xml, "BodyText",
        ppr='<w:spacing w:before="0" w:after="140" w:line="276" w:lineRule="auto"/>')

    # ---- title block ------------------------------------------------------
    xml = replace_style(
        xml, "Title",
        ppr='<w:spacing w:before="0" w:after="120"/>'
            '<w:pBdr><w:bottom w:val="single" w:sz="12" w:space="6" '
            f'w:color="{DEEP}"/></w:pBdr>',
        rpr=f'{fonts(HEAD_FONT)}<w:b/><w:color w:val="{DEEP}"/>'
            f'<w:sz w:val="52"/><w:szCs w:val="52"/>')
    xml = replace_style(
        xml, "Subtitle",
        ppr='<w:spacing w:before="0" w:after="240"/>',
        rpr=f'{fonts(HEAD_FONT)}<w:color w:val="{MID}"/><w:sz w:val="26"/>'
            f'<w:szCs w:val="26"/>')

    # ---- headings ---------------------------------------------------------
    heads = [
        ("Heading1", DEEP, 34, True, 420, 160),
        ("Heading2", MID, 27, True, 320, 120),
        ("Heading3", SLATE, 23, True, 260, 100),
        ("Heading4", SLATE, 21, True, 220, 90),
    ]
    for sid, colour, size, bold, before, after in heads:
        xml = replace_style(
            xml, sid,
            ppr=f'<w:keepNext/><w:keepLines/>'
                f'<w:spacing w:before="{before}" w:after="{after}"/>'
                f'<w:outlineLvl w:val="{int(sid[-1]) - 1}"/>',
            rpr=f'{fonts(HEAD_FONT)}{"<w:b/>" if bold else ""}'
                f'<w:color w:val="{colour}"/><w:sz w:val="{size}"/>'
                f'<w:szCs w:val="{size}"/>')

    # ---- verdict boxes (markdown blockquotes) -----------------------------
    xml = replace_style(
        xml, "BlockText",
        ppr=f'<w:pBdr>'
            f'<w:top w:val="single" w:sz="4" w:space="8" w:color="{RULE}"/>'
            f'<w:left w:val="single" w:sz="18" w:space="10" w:color="{MID}"/>'
            f'<w:bottom w:val="single" w:sz="4" w:space="8" w:color="{RULE}"/>'
            f'<w:right w:val="single" w:sz="4" w:space="8" w:color="{RULE}"/>'
            f'</w:pBdr>'
            f'<w:shd w:val="clear" w:color="auto" w:fill="{BOX_FILL}"/>'
            f'<w:spacing w:before="160" w:after="160" w:line="264" '
            f'w:lineRule="auto"/><w:ind w:left="0" w:right="0"/>',
        rpr=f'{fonts(BODY_FONT)}<w:color w:val="{INK}"/><w:sz w:val="20"/>'
            f'<w:szCs w:val="20"/>')

    # ---- tables -----------------------------------------------------------
    border = (lambda side: f'<w:{side} w:val="single" w:sz="4" w:space="0" '
                           f'w:color="{RULE}"/>')
    table_style = (
        f'<w:style w:type="table" w:styleId="Table">'
        f'<w:name w:val="Table"/><w:uiPriority w:val="99"/>'
        f'<w:pPr><w:spacing w:before="40" w:after="40" w:line="240" '
        f'w:lineRule="auto"/></w:pPr>'
        f'<w:rPr>{fonts(BODY_FONT)}<w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr>'
        f'<w:tblPr><w:tblBorders>'
        f'{border("top")}{border("left")}{border("bottom")}{border("right")}'
        f'{border("insideH")}{border("insideV")}'
        f'</w:tblBorders>'
        f'<w:tblCellMar>'
        f'<w:top w:w="60" w:type="dxa"/><w:left w:w="100" w:type="dxa"/>'
        f'<w:bottom w:w="60" w:type="dxa"/><w:right w:w="100" w:type="dxa"/>'
        f'</w:tblCellMar></w:tblPr>'
        # header row: shaded and bold
        f'<w:tblStylePr w:type="firstRow"><w:rPr><w:b/>'
        f'<w:color w:val="{DEEP}"/></w:rPr>'
        f'<w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="{HEAD_FILL}"/>'
        f'</w:tcPr></w:tblStylePr>'
        f'</w:style>'
    )
    existing = re.search(r'<w:style w:type="table" w:styleId="Table".*?</w:style>',
                         xml, re.S)
    if existing:
        xml = xml.replace(existing.group(0), table_style)
    else:
        xml = xml.replace('</w:styles>', table_style + '</w:styles>')

    return xml


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        base = tmp / "base.docx"
        subprocess.run(
            ["pandoc", "-o", str(base), "--print-default-data-file",
             "reference.docx"],
            check=True)

        work = tmp / "unpacked"
        with zipfile.ZipFile(base) as zf:
            zf.extractall(work)

        styles = work / "word" / "styles.xml"
        styles.write_text(patch_styles(styles.read_text()))

        out = tmp / "reference.docx"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            for path in sorted(work.rglob("*")):
                if path.is_file():
                    zf.write(path, path.relative_to(work).as_posix())

        shutil.move(str(out), REFERENCE)

    print(f"wrote {REFERENCE}")


if __name__ == "__main__":
    main()
