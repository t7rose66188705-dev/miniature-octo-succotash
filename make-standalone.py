"""Wrap garden.html (written for the Claude artifact viewer, which adds its own
<head>) into index.html, a standalone page that opens in any browser."""
from pathlib import Path

src = Path(__file__).with_name('garden.html').read_text(encoding='utf-8')
cut = src.index('</style>') + len('</style>')
head, body = src[:cut], src[cut:]
page = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>body{{margin:0}}[hidden]{{display:none!important}}:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}</style>
{head}
</head>
<body>{body}
</body>
</html>
"""
Path(__file__).with_name('index.html').write_text(page, encoding='utf-8')
print('wrote index.html')
