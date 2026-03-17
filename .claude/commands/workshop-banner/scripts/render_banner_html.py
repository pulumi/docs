#!/usr/bin/env python3
"""
Render workshop banners using HTML/CSS + Playwright screenshot.
Produces two PNGs per run:
  - <output>          — landscape 1200x628
  - <stem>-square.png — square    628x628

Usage:
    python3 render_banner_html.py --config config.json --output banner.png
"""

import argparse
import base64
import html
import json
import re
from pathlib import Path

HTML_TEMPLATE = """<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    width: 1200px;
    height: 628px;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
    background: #F9F9F9;
    position: relative;
  }}

  /* Right dark panel */
  .right-panel {{
    position: absolute;
    left: 786px; top: 0;
    width: 414px; height: 628px;
    background: #20054E;
    overflow: hidden;
  }}

  /* Decorative concentric rings — centered on speaker photo */
  .ring {{
    position: absolute;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.20);
    left: 207px;
    top: 252px;
    transform: translate(-50%, -50%);
    pointer-events: none;
  }}
  .ring-1 {{ width: 258px; height: 258px; }}
  .ring-2 {{ width: 311px; height: 311px; }}

  /* Company logo — top-center of right panel */
  .company-logo {{
    position: absolute;
    top: 33px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
  }}
  .company-logo img {{
    max-height: 44px;
    max-width: 175px;
    object-fit: contain;
  }}

  /* Speaker photo */
  .speaker-photo-wrapper {{
    position: absolute;
    width: 206px; height: 206px;
    left: 104px; top: 149px;
    border-radius: 50%;
    overflow: hidden;
    z-index: 1;
  }}
  .speaker-photo {{
    width: 100%; height: 100%;
    object-fit: cover;
    border-radius: 50%;
  }}
  .speaker-photo-placeholder {{
    width: 100%; height: 100%;
    background: rgba(255,255,255,0.10);
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .speaker-photo-placeholder svg {{
    width: 60px; height: 60px;
    opacity: 0.40;
  }}

  /* Speaker info */
  .speaker-name {{
    position: absolute;
    top: 441px; left: 0; right: 0;
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -1.2px;
    line-height: 1.1;
  }}
  .speaker-role {{
    position: absolute;
    top: 500px; left: 0; right: 0;
    text-align: center;
    font-size: 24px;
    font-weight: 400;
    color: #ffffff;
    letter-spacing: -0.72px;
  }}
  .speaker-company-text {{
    position: absolute;
    top: 536px; left: 0; right: 0;
    text-align: center;
    font-size: 24px;
    font-weight: 400;
    color: #ffffff;
    letter-spacing: -0.72px;
  }}

  /* Decorative background curves — full left panel */
  .bg-curves {{
    position: absolute;
    left: 0; top: 0;
    width: 786px; height: 628px;
    pointer-events: none;
  }}

  /* Left panel — flex column */
  .left-panel {{
    position: absolute;
    left: 0; top: 0;
    width: 786px; height: 628px;
    display: flex;
    flex-direction: column;
    padding: 33px 44px 45px 44px;
  }}

  /* Event type label */
  .event-type {{
    font-size: 36px;
    font-weight: 700;
    color: #673EAC;
    letter-spacing: -1.08px;
    line-height: 1.1;
    flex-shrink: 0;
  }}

  /* Title — grows to fill remaining space, text vertically centered */
  .title-area {{
    flex: 1;
    display: flex;
    align-items: center;
  }}
  .title-area h1 {{
    font-size: {title_size}px;
    font-weight: 700;
    line-height: 1.1;
    color: #2b2b2c;
    letter-spacing: -0.03em;
    max-width: 692px;
  }}

  /* Partner section */
  .partner-section {{
    flex-shrink: 0;
    margin-bottom: 28px;
  }}
  .partner-label-row {{
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 24px;
  }}
  .partner-label {{
    font-size: 20px;
    font-weight: 400;
    color: #757576;
    letter-spacing: -0.72px;
    white-space: nowrap;
    flex-shrink: 0;
  }}
  .partner-line {{
    flex: 1;
    height: 1px;
    background: rgba(0,0,0,0.15);
  }}
  .partner-logos-row {{
    display: flex;
    align-items: center;
    gap: 20px;
  }}
  .partner-logos-row img {{
    max-height: 40px;
    max-width: 100px;
    object-fit: contain;
  }}

  /* CTA button */
  .cta {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 82px;
    padding: 0 36px;
    background: #673EAC;
    color: #ffffff;
    font-size: 32px;
    font-weight: 400;
    border-radius: 10px;
    width: fit-content;
    flex-shrink: 0;
  }}
</style>
</head>
<body>
  <div class="bg-curves">
    <svg width="786" height="628" viewBox="0 0 786 628" fill="none" xmlns="http://www.w3.org/2000/svg">
      <g clip-path="url(#clip0_50_1454)">
        <path d="M301 -464L301 68.7283C301 86.2937 315.224 100.536 332.768 100.536L805.331 100.536" stroke="#DFDFDF" stroke-miterlimit="10"/>
        <path d="M326.943 -464L326.943 51.129C326.943 64.6931 337.95 75.7139 351.497 75.7139L802.996 75.7139" stroke="#DFDFDF" stroke-miterlimit="10"/>
        <path d="M352.852 -464L352.852 33.4958C352.852 43.0923 360.607 50.8577 370.192 50.8577L802.995 50.8578" stroke="#DFDFDF" stroke-miterlimit="10"/>
        <path d="M378.794 -464L378.794 15.8963C378.794 21.4915 383.333 26.0354 388.921 26.0354L810 26.0354" stroke="#DFDFDF" stroke-miterlimit="10"/>
      </g>
      <g clip-path="url(#clip1_50_1454)">
        <path d="M459 1066L459 533.272C459 515.706 473.224 501.464 490.768 501.464L963.331 501.464" stroke="#DFDFDF" stroke-miterlimit="10"/>
        <path d="M484.943 1066L484.943 550.871C484.943 537.307 495.95 526.286 509.497 526.286L960.996 526.286" stroke="#DFDFDF" stroke-miterlimit="10"/>
        <path d="M510.852 1066L510.852 568.504C510.852 558.908 518.607 551.142 528.192 551.142L960.995 551.142" stroke="#DFDFDF" stroke-miterlimit="10"/>
        <path d="M536.794 1066L536.794 586.104C536.794 580.509 541.333 575.965 546.921 575.965L968 575.965" stroke="#DFDFDF" stroke-miterlimit="10"/>
      </g>
      <defs>
        <clipPath id="clip0_50_1454">
          <rect width="485" height="127" fill="white" transform="translate(301 -26)"/>
        </clipPath>
        <clipPath id="clip1_50_1454">
          <rect width="327" height="127" fill="white" transform="matrix(1 0 0 -1 459 628)"/>
        </clipPath>
      </defs>
    </svg>
  </div>

  <div class="right-panel">
    <div class="ring ring-2"></div>
    <div class="ring ring-1"></div>
    <div class="company-logo">{company_logo_html}</div>
    <div class="speaker-photo-wrapper">{speaker_photo_html}</div>
    <div class="speaker-name">{speaker_name}</div>
    {speaker_role_html}
    {speaker_company_html}
  </div>

  <div class="left-panel">
    <div class="event-type">{badge_text}</div>
    <div class="title-area"><h1>{title}</h1></div>
    {partner_html}
    <div class="cta">{cta_text}</div>
  </div>
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
    badge_text = html.escape(config.get("event_type", "workshop").capitalize())
    title_len = len(config.get("title", ""))
    title = html.escape(config.get("title", ""))
    cta_text = html.escape(config.get("cta_text", "Register"))
    speaker_name = html.escape(config.get("speaker_name", ""))
    speaker_title = html.escape(config.get("speaker_title", ""))
    speaker_company = html.escape(config.get("speaker_company", ""))

    # Title size: scale down for longer titles (calibrated for 1200x628 at max-width 692px)
    if title_len <= 15:
        title_size = 80
    elif title_len <= 28:
        title_size = 72
    elif title_len <= 43:
        title_size = 64
    elif title_len <= 60:
        title_size = 52
    else:
        title_size = 42

    # Speaker role and company as separate right-panel elements
    speaker_role_html = (
        f'<div class="speaker-role">{speaker_title}</div>' if speaker_title else ""
    )
    speaker_company_html = (
        f'<div class="speaker-company-text">{speaker_company}</div>'
        if speaker_company
        else ""
    )

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

    # Company logo — img tag only (template wraps it in .company-logo)
    company_logo_path = config.get("company_logo", "")
    company_logo_html = ""
    if company_logo_path:
        uri = image_to_data_uri(company_logo_path)
        if uri:
            company_logo_html = f'<img src="{uri}" alt="Logo">'

    # Partner logos — combine both arrays for backward compatibility
    partner_logos = list(config.get("partner_logos", []))
    partner_logos += list(config.get("partner_logos_after_text", []))
    partner_text = config.get("partner_text", "")
    if partner_text:
        partner_text = html.escape(partner_text.strip())

    partner_html = ""
    if partner_logos or partner_text:
        label_html = (
            f'<span class="partner-label">{partner_text}</span>' if partner_text else ""
        )
        label_row = (
            f'<div class="partner-label-row">{label_html}'
            f'<div class="partner-line"></div></div>'
        )
        logo_imgs = []
        for lp in partner_logos:
            uri = image_to_data_uri(lp)
            if uri:
                logo_imgs.append(f'<img src="{uri}" alt="Partner">')
        logos_row = (
            f'<div class="partner-logos-row">{"".join(logo_imgs)}</div>'
            if logo_imgs
            else ""
        )
        partner_html = f'<div class="partner-section">{label_row}{logos_row}</div>'

    return HTML_TEMPLATE.format(
        title_size=title_size,
        badge_text=badge_text,
        title=title,
        cta_text=cta_text,
        speaker_name=speaker_name,
        speaker_role_html=speaker_role_html,
        speaker_company_html=speaker_company_html,
        speaker_photo_html=speaker_photo_html,
        company_logo_html=company_logo_html,
        partner_html=partner_html,
    )


HTML_TEMPLATE_SQUARE = """<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    width: 628px;
    height: 628px;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
    background: #F9F9F9;
    position: relative;
  }}

  /* Dark pill badge — top-right, company logo inside */
  .sq-logo-badge {{
    position: absolute;
    left: 397px; top: 0; right: 0;
    height: 107px;
    background: #20054E;
    border-bottom-left-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .sq-logo-badge img {{
    max-height: 44px;
    max-width: 175px;
    object-fit: contain;
  }}

  /* Decorative background curves — full square panel */
  .sq-bg-curves {{
    position: absolute;
    left: 0; top: 0;
    width: 628px; height: 628px;
    pointer-events: none;
  }}

  /* Full-width flex-column panel */
  .sq-panel {{
    position: absolute;
    left: 0; top: 0;
    width: 628px; height: 628px;
    display: flex;
    flex-direction: column;
    padding: 33px 44px 45px 44px;
  }}

  /* Event type label */
  .sq-event-type {{
    font-size: 36px;
    font-weight: 700;
    color: #673EAC;
    letter-spacing: -1.08px;
    line-height: 1.1;
    flex-shrink: 0;
  }}

  /* Title — grows to fill space, vertically centered */
  .sq-title-area {{
    flex: 1;
    display: flex;
    align-items: center;
  }}
  .sq-title-area h1 {{
    font-size: {title_size}px;
    font-weight: 700;
    line-height: 1.1;
    color: #2b2b2c;
    letter-spacing: -0.03em;
    max-width: 537px;
  }}

  /* Partner section */
  .sq-partner-section {{
    flex-shrink: 0;
    margin-bottom: 28px;
  }}
  .sq-partner-label-row {{
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 24px;
  }}
  .sq-partner-label {{
    font-size: 20px;
    font-weight: 400;
    color: #757576;
    letter-spacing: -0.72px;
    white-space: nowrap;
    flex-shrink: 0;
  }}
  .sq-partner-line {{
    flex: 1;
    height: 1px;
    background: rgba(0,0,0,0.15);
  }}
  .sq-partner-logos-row {{
    display: flex;
    align-items: center;
    gap: 20px;
  }}
  .sq-partner-logos-row img {{
    max-height: 40px;
    max-width: 100px;
    object-fit: contain;
  }}

  /* CTA button */
  .sq-cta {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 82px;
    padding: 0 36px;
    background: #673EAC;
    color: #ffffff;
    font-size: 32px;
    font-weight: 400;
    border-radius: 10px;
    width: fit-content;
    flex-shrink: 0;
  }}
</style>
</head>
<body>
  <div class="sq-bg-curves">
    <svg width="628" height="628" viewBox="0 0 628 628" fill="none" xmlns="http://www.w3.org/2000/svg">
      <g clip-path="url(#clip0_50_1463)">
        <path d="M272 -432.071L272 63.0088C272 79.3329 285.208 92.5686 301.499 92.5686L740.307 92.5687" stroke="#DFDFDF" stroke-miterlimit="10"/>
        <path d="M296.09 -432.071L296.09 46.6533C296.09 59.2588 306.311 69.5007 318.89 69.5007L738.139 69.5008" stroke="#DFDFDF" stroke-miterlimit="10"/>
        <path d="M320.148 -432.071L320.148 30.2662C320.148 39.1846 327.35 46.4012 336.25 46.4012L738.139 46.4012" stroke="#DFDFDF" stroke-miterlimit="10"/>
        <path d="M344.238 -432.071L344.238 13.9106C344.238 19.1104 348.452 23.3332 353.641 23.3332L744.643 23.3332" stroke="#DFDFDF" stroke-miterlimit="10"/>
      </g>
      <g clip-path="url(#clip1_50_1463)">
        <path d="M375 1066L375 533.272C375 515.706 389.224 501.464 406.768 501.464L879.331 501.464" stroke="#DFDFDF" stroke-miterlimit="10"/>
        <path d="M400.943 1066L400.943 550.871C400.943 537.307 411.95 526.286 425.497 526.286L876.996 526.286" stroke="#DFDFDF" stroke-miterlimit="10"/>
        <path d="M426.852 1066L426.852 568.504C426.852 558.908 434.607 551.142 444.192 551.142L876.995 551.142" stroke="#DFDFDF" stroke-miterlimit="10"/>
        <path d="M452.794 1066L452.794 586.104C452.794 580.509 457.333 575.965 462.921 575.965L884 575.965" stroke="#DFDFDF" stroke-miterlimit="10"/>
      </g>
      <defs>
        <clipPath id="clip0_50_1463">
          <rect width="353" height="93" fill="white" transform="translate(272)"/>
        </clipPath>
        <clipPath id="clip1_50_1463">
          <rect width="250" height="127" fill="white" transform="matrix(1 0 0 -1 375 628)"/>
        </clipPath>
      </defs>
    </svg>
  </div>
  {company_logo_html}
  <div class="sq-panel">
    <div class="sq-event-type">{badge_text}</div>
    <div class="sq-title-area"><h1>{title}</h1></div>
    {partner_html}
    <div class="sq-cta">{cta_text}</div>
  </div>
</body>
</html>"""


def build_html_square(config):
    """Build the HTML string for the 628x628 square variant."""
    badge_text = html.escape(config.get("event_type", "workshop").capitalize())
    title_len = len(config.get("title", ""))
    title = html.escape(config.get("title", ""))
    cta_text = html.escape(config.get("cta_text", "Register"))

    # Title size calibrated for 628x628, max-width 537px
    title_len = len(title)
    if title_len <= 15:
        title_size = 68
    elif title_len <= 28:
        title_size = 60
    elif title_len <= 43:
        title_size = 52
    elif title_len <= 65:
        title_size = 42
    else:
        title_size = 34

    # Company logo badge (absolute top-right block)
    company_logo_path = config.get("company_logo", "")
    company_logo_html = ""
    if company_logo_path:
        uri = image_to_data_uri(company_logo_path)
        if uri:
            company_logo_html = (
                f'<div class="sq-logo-badge"><img src="{uri}" alt="Logo"></div>'
            )

    # Partner section
    partner_logos = list(config.get("partner_logos", []))
    partner_logos += list(config.get("partner_logos_after_text", []))
    partner_text = config.get("partner_text", "")
    if partner_text:
        partner_text = html.escape(partner_text.strip())

    partner_html = ""
    if partner_logos or partner_text:
        label_html = (
            f'<span class="sq-partner-label">{partner_text}</span>'
            if partner_text
            else ""
        )
        label_row = (
            f'<div class="sq-partner-label-row">{label_html}'
            f'<div class="sq-partner-line"></div></div>'
        )
        logo_imgs = []
        for lp in partner_logos:
            uri = image_to_data_uri(lp)
            if uri:
                logo_imgs.append(f'<img src="{uri}" alt="Partner">')
        logos_row = (
            f'<div class="sq-partner-logos-row">{"" .join(logo_imgs)}</div>'
            if logo_imgs
            else ""
        )
        partner_html = (
            f'<div class="sq-partner-section">{label_row}{logos_row}</div>'
        )

    return HTML_TEMPLATE_SQUARE.format(
        title_size=title_size,
        badge_text=badge_text,
        title=title,
        cta_text=cta_text,
        company_logo_html=company_logo_html,
        partner_html=partner_html,
    )


def _placeholder_svg():
    return """<div class="speaker-photo-placeholder">
      <svg viewBox="0 0 24 24" fill="white"><path d="M12 12c2.7 0 4.8-2.1 4.8-4.8S14.7 2.4 12 2.4 7.2 4.5 7.2 7.2 9.3 12 12 12zm0 2.4c-3.2 0-9.6 1.6-9.6 4.8v2.4h19.2v-2.4c0-3.2-6.4-4.8-9.6-4.8z"/></svg>
    </div>"""


def render(config, output_path):
    """Render landscape and square banners to PNG using Playwright."""
    html_landscape = build_html(config)
    html_square = build_html_square(config)

    square_path = str(
        Path(output_path).with_name(
            Path(output_path).stem + "-square" + Path(output_path).suffix
        )
    )

    tmp_landscape = Path("/tmp/banner_render.html")
    tmp_square = Path("/tmp/banner_render_square.html")
    tmp_landscape.write_text(html_landscape)
    tmp_square.write_text(html_square)

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()

        page = browser.new_page(viewport={"width": 1200, "height": 628})
        page.goto(f"file://{tmp_landscape}")
        page.wait_for_load_state("networkidle")
        page.screenshot(path=output_path, type="png")

        page = browser.new_page(viewport={"width": 628, "height": 628})
        page.goto(f"file://{tmp_square}")
        page.wait_for_load_state("networkidle")
        page.screenshot(path=square_path, type="png")

        browser.close()

    print(f"Banner saved to: {output_path}")
    print(f"Square banner saved to: {square_path}")


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
    parser = argparse.ArgumentParser(
        description="Render workshop banner (HTML)")
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
        output_path = str(Path("/tmp") / auto_filename(config))

    render(config, output_path)


if __name__ == "__main__":
    main()
