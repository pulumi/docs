#!/usr/bin/env python3
"""
Render a workshop banner using HTML/CSS + Playwright screenshot.
Produces a polished, design-quality 1368x768 PNG.

Usage:
    python3 render_banner_html.py --config config.json --output banner.png
"""

import argparse
import base64
import json
import re
from pathlib import Path

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&family=DM+Sans:wght@400;500;700&family=Outfit:wght@400;500;600;700;800&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    width: 1368px;
    height: 768px;
    overflow: hidden;
    font-family: 'Outfit', sans-serif;
    background: linear-gradient(135deg, #7c5cbf 0%, #9068d0 40%, #6b4fa8 100%);
    position: relative;
  }}

  /* Accent shapes */
  .accent-top {{
    position: absolute;
    top: 0; left: 0;
    width: 320px; height: 55px;
    background: linear-gradient(135deg, #e86b7a, #f07585);
    clip-path: polygon(0 0, 100% 0, 85% 100%, 0 100%);
    z-index: 2;
  }}

  .accent-bottom-left {{
    position: absolute;
    bottom: 0; left: 0;
    width: 380px; height: 50px;
    background: linear-gradient(135deg, #f07585, #e86b7a);
    clip-path: polygon(0 0, 90% 0, 100% 100%, 0 100%);
    z-index: 2;
  }}

  .accent-bottom-right {{
    position: absolute;
    bottom: 0; right: 0;
    width: 300px; height: 45px;
    background: linear-gradient(135deg, #e86b7a, #f07585);
    clip-path: polygon(15% 0, 100% 0, 100% 100%, 0 100%);
    z-index: 2;
  }}

  /* White card */
  .card {{
    position: absolute;
    top: 40px; left: 20px;
    width: 940px;
    height: 688px;
    background: #ffffff;
    border-radius: 22px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.15), 0 4px 16px rgba(0,0,0,0.08);
    z-index: 1;
    display: flex;
    flex-direction: column;
    padding: 48px 50px;
    overflow: hidden;
  }}

  /* Subtle card texture */
  .card::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 80% 20%, rgba(124,92,191,0.03) 0%, transparent 60%);
    border-radius: 22px;
    pointer-events: none;
  }}

  /* Badge */
  .badge {{
    display: inline-flex;
    align-items: center;
    padding: 18px 40px;
    background: linear-gradient(135deg, #8b7aed 0%, #7065e4 100%);
    color: #fff;
    font-size: 21px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    border-radius: 12px;
    width: fit-content;
    box-shadow: 0 4px 14px rgba(112,101,228,0.35);
  }}

  /* Title */
  .title {{
    flex: 1;
    display: flex;
    align-items: center;
    margin: 0;
    padding: 20px 0;
  }}

  .title h1 {{
    font-family: 'Outfit', sans-serif;
    font-size: {title_size}px;
    font-weight: 400;
    line-height: 1.15;
    color: #1a1a2e;
    letter-spacing: -0.5px;
    max-width: 800px;
  }}

  /* CTA */
  .cta {{
    display: inline-flex;
    align-items: center;
    padding: 24px 60px;
    background: linear-gradient(135deg, #7c5cbf 0%, #6b4fa8 100%);
    color: #fff;
    font-size: 26px;
    font-weight: 700;
    border-radius: 14px;
    width: fit-content;
    letter-spacing: 0.3px;
    box-shadow: 0 6px 20px rgba(107,79,168,0.4);
    transition: transform 0.2s;
  }}

  /* Right panel content */
  .right-panel {{
    position: absolute;
    top: 0; right: -80px;
    width: 600px;
    height: 768px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 1;
    padding-top: 20px;
  }}

  /* Company logo area */
  .company-logo {{
    margin-bottom: 32px;
    z-index: 3;
  }}

  .company-logo img {{
    max-height: 50px;
    max-width: 180px;
    object-fit: contain;
  }}

  /* Speaker photo */
  .speaker-photo-wrapper {{
    position: relative;
    width: 260px;
    height: 260px;
    margin-bottom: 28px;
  }}

  /* Outer glow ring — thick semi-transparent purple band like reference */
  .speaker-photo-wrapper::before {{
    content: '';
    position: absolute;
    inset: -18px;
    border-radius: 50%;
    border: 14px solid rgba(255,255,255,0.18);
    box-shadow: 0 0 50px rgba(255,255,255,0.12);
  }}

  /* White ring — crisp inner border */
  .speaker-photo-wrapper::after {{
    content: '';
    position: absolute;
    inset: -6px;
    border-radius: 50%;
    border: 3px solid rgba(255,255,255,0.85);
    box-shadow: 0 0 20px rgba(255,255,255,0.1);
  }}

  .speaker-photo {{
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    position: relative;
    z-index: 1;
  }}

  /* Placeholder when no photo */
  .speaker-photo-placeholder {{
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(255,255,255,0.12), rgba(255,255,255,0.04));
    backdrop-filter: blur(10px);
    position: relative;
    z-index: 1;
    display: flex;
    align-items: center;
    justify-content: center;
  }}

  .speaker-photo-placeholder svg {{
    width: 80px;
    height: 80px;
    opacity: 0.25;
  }}

  /* Speaker info */
  .speaker-name {{
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: #fff;
    text-align: center;
    margin-bottom: 6px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.15);
  }}

  .speaker-title {{
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    font-weight: 400;
    color: rgba(255,255,255,0.8);
    text-align: center;
    line-height: 1.5;
  }}

  /* Partner area */
  .partner-area {{
    position: absolute;
    bottom: 55px;
    right: 50px;
    display: flex;
    align-items: center;
    gap: 12px;
    z-index: 3;
  }}

  .partner-area img {{
    max-height: 36px;
    max-width: 70px;
    object-fit: contain;
  }}

  .partner-text {{
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: rgba(255,255,255,0.7);
    font-weight: 400;
  }}

  /* Decorative bg elements */
  .bg-orb {{
    position: absolute;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255,255,255,0.06), transparent 70%);
    pointer-events: none;
  }}

  .bg-orb-1 {{
    width: 500px; height: 500px;
    top: -100px; right: -80px;
  }}

  .bg-orb-2 {{
    width: 300px; height: 300px;
    bottom: -50px; right: 200px;
  }}

  .bg-grid {{
    position: absolute;
    inset: 0;
    background-image:
      radial-gradient(rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 32px 32px;
    pointer-events: none;
  }}
</style>
</head>
<body>
  <div class="bg-grid"></div>
  <div class="bg-orb bg-orb-1"></div>
  <div class="bg-orb bg-orb-2"></div>

  <div class="accent-top"></div>
  <div class="accent-bottom-left"></div>
  <div class="accent-bottom-right"></div>

  <div class="card">
    <div class="badge">{badge_text}</div>
    <div class="title">
      <h1>{title}</h1>
    </div>
    <div class="cta">{cta_text}</div>
  </div>

  <div class="right-panel">
    {company_logo_html}
    <div class="speaker-photo-wrapper">
      {speaker_photo_html}
    </div>
    <div class="speaker-name">{speaker_name}</div>
    <div class="speaker-title">{speaker_title_line}</div>
  </div>

  {partner_html}
</body>
</html>"""


def image_to_data_uri(path):
    """Convert an image file to a base64 data URI."""
    p = Path(path)
    if not p.exists():
        return None
    suffix = p.suffix.lower()
    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".svg": "image/svg+xml",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }.get(suffix, "image/png")
    data = base64.b64encode(p.read_bytes()).decode()
    return f"data:{mime};base64,{data}"


def build_html(config):
    """Build the HTML string from config."""
    badge_text = config.get("event_type", "WORKSHOP").upper()
    title = config.get("title", "")
    cta_text = config.get("cta_text", "Register")
    speaker_name = config.get("speaker_name", "")
    speaker_title = config.get("speaker_title", "")
    speaker_company = config.get("speaker_company", "")

    # Title size: scale down for longer titles (light weight needs larger sizes)
    title_len = len(title)
    if title_len <= 25:
        title_size = 96
    elif title_len <= 40:
        title_size = 86
    elif title_len <= 60:
        title_size = 76
    else:
        title_size = 62

    # Speaker title line
    parts = [p for p in [speaker_title, speaker_company] if p]
    speaker_title_line = "<br>".join(parts) if parts else ""

    # Speaker photo
    speaker_photo_path = config.get("speaker_photo", "")
    if speaker_photo_path:
        uri = image_to_data_uri(speaker_photo_path)
        if uri:
            speaker_photo_html = (
                f'<img class="speaker-photo" src="{uri}" alt="Speaker">'
            )
        else:
            speaker_photo_html = _placeholder_svg()
    else:
        speaker_photo_html = _placeholder_svg()

    # Company logo
    company_logo_path = config.get("company_logo", "")
    if company_logo_path:
        uri = image_to_data_uri(company_logo_path)
        if uri:
            company_logo_html = (
                f'<div class="company-logo"><img src="{uri}" alt="Logo"></div>'
            )
        else:
            company_logo_html = ""
    else:
        company_logo_html = ""

    # Partner area
    partner_logos = config.get("partner_logos", [])
    partner_text = config.get("partner_text", "")
    partner_logos_after = config.get("partner_logos_after_text", [])

    partner_parts = []
    for lp in partner_logos:
        uri = image_to_data_uri(lp)
        if uri:
            partner_parts.append(f'<img src="{uri}" alt="Partner">')
    if partner_text:
        partner_parts.append(f'<span class="partner-text">{partner_text}</span>')
    for lp in partner_logos_after:
        uri = image_to_data_uri(lp)
        if uri:
            partner_parts.append(f'<img src="{uri}" alt="Partner">')

    if partner_parts:
        partner_html = '<div class="partner-area">' + "".join(partner_parts) + "</div>"
    else:
        partner_html = ""

    return HTML_TEMPLATE.format(
        title_size=title_size,
        badge_text=badge_text,
        title=title,
        cta_text=cta_text,
        speaker_name=speaker_name,
        speaker_title_line=speaker_title_line,
        speaker_photo_html=speaker_photo_html,
        company_logo_html=company_logo_html,
        partner_html=partner_html,
    )


def _placeholder_svg():
    return """<div class="speaker-photo-placeholder">
      <svg viewBox="0 0 24 24" fill="white"><path d="M12 12c2.7 0 4.8-2.1 4.8-4.8S14.7 2.4 12 2.4 7.2 4.5 7.2 7.2 9.3 12 12 12zm0 2.4c-3.2 0-9.6 1.6-9.6 4.8v2.4h19.2v-2.4c0-3.2-6.4-4.8-9.6-4.8z"/></svg>
    </div>"""


def render(config, output_path):
    """Render banner to PNG using Playwright."""
    html = build_html(config)

    # Write temp HTML
    tmp_html = Path("/tmp/banner_render.html")
    tmp_html.write_text(html)

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1368, "height": 768})
        page.goto(f"file://{tmp_html}")
        page.wait_for_timeout(800)  # let fonts load
        page.screenshot(path=output_path, type="png")
        browser.close()

    print(f"Banner saved to: {output_path}")


def to_kebab(text):
    """Convert text to kebab-case."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def auto_filename(config):
    """Generate kebab-case filename: <title>-<speaker-name>.png"""
    title = config.get("title", "banner")
    speaker_name = config.get("speaker_name", "")
    parts = [to_kebab(title)]
    if speaker_name:
        parts.append(to_kebab(speaker_name))
    return "-".join(parts) + ".png"


def main():
    parser = argparse.ArgumentParser(description="Render workshop banner (HTML)")
    parser.add_argument("--config", required=True, help="JSON config path")
    parser.add_argument(
        "--output", default=None, help="Output PNG path (auto-generated if omitted)"
    )
    args = parser.parse_args()

    with open(args.config) as f:
        config = json.load(f)

    if args.output:
        output_path = args.output
    else:
        output_path = str(Path.home() / "Desktop" / auto_filename(config))

    render(config, output_path)


if __name__ == "__main__":
    main()
