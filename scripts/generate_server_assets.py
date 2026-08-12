import os
import json
import base64
from PIL import Image

BASE_DIR = r'e:\Mei\下载\cs\demon-slayer-counter'
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
SERVER_DIR = os.path.join(BASE_DIR, 'server')
API_DIR = os.path.join(SERVER_DIR, 'api')

os.makedirs(API_DIR, exist_ok=True)

THEMES = ['demon-slayer']

def generate_base64_dict():
    theme_assets = {}
    
    for theme in THEMES:
        theme_dir = os.path.join(ASSETS_DIR, theme)
        theme_assets[theme] = {}
        
        for i in range(10):
            png_path = os.path.join(theme_dir, f'{i}.png')
            if not os.path.exists(png_path):
                continue
                
            img = Image.open(png_path)
            aspect = img.width / img.height
            target_h = 240
            target_w = int(target_h * aspect)
            
            resampled = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
            
            import io
            buf = io.BytesIO()
            resampled.save(buf, format='WEBP', quality=85)
            buf.seek(0)
            
            b64_str = base64.b64encode(buf.read()).decode('utf-8')
            theme_assets[theme][str(i)] = {
                'width': target_w,
                'height': target_h,
                'data': f'data:image/webp;base64,{b64_str}'
            }
            print(f'Encoded {theme} [{i}]: {target_w}x{target_h}, b64 len: {len(b64_str)}')
            
    return theme_assets

def build_vercel_serverless(theme_assets):
    assets_json_str = json.dumps(theme_assets, ensure_ascii=False)
    
    code = f'''// Vercel Serverless Function for GitHub Profile Dynamic Counter
// Theme: Demon Slayer (鬼灭之刃全明星 0~9)
// Supports Vercel KV / Upstash Redis for 100% permanent persistence

const ASSETS = {assets_json_str};
const memoryStore = new Map();

export default async function handler(req, res) {{
  const {{ name = 'visitor', theme = 'demon-slayer', length = '7' }} = req.query;

  const currentTheme = 'demon-slayer';
  const digitsAssets = ASSETS[currentTheme];
  const key = `${{currentTheme}}:${{name}}`;

  let count = 1;
  let hasPersistentStore = false;
  let kvErrorMsg = '';

  // 1. Try Vercel KV / Upstash Redis REST API (100% Permanent Storage)
  const kvUrl = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
  const kvToken = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;

  if (kvUrl && kvToken) {{
    try {{
      const kvRes = await fetch(`${{kvUrl}}/incr/${{encodeURIComponent(key)}}`, {{
        headers: {{ Authorization: `Bearer ${{kvToken}}` }}
      }});
      if (kvRes.ok) {{
        const kvData = await kvRes.json();
        if (typeof kvData.result === 'number') {{
          count = kvData.result;
          hasPersistentStore = true;
        }} else {{
          kvErrorMsg = `Invalid result format: ${{JSON.stringify(kvData)}}`;
        }}
      }} else {{
        const errText = await kvRes.text();
        kvErrorMsg = `HTTP ${{kvRes.status}}: ${{errText}}`;
      }}
    }} catch (err) {{
      kvErrorMsg = `Fetch exception: ${{err.message}}`;
    }}
  }} else {{
    kvErrorMsg = `Missing Env: kvUrl=${{Boolean(kvUrl)}}, kvToken=${{Boolean(kvToken)}}`;
  }}

  // 2. Fallback to Memory Store if KV not connected
  if (!hasPersistentStore) {{
    count = (memoryStore.get(key) || 0) + 1;
    memoryStore.set(key, count);
  }}

  const minLen = parseInt(length, 10) || 7;
  const countStr = count.toString().padStart(minLen, '0');

  const digits = countStr.split('');
  let totalWidth = 0;
  const height = 240;

  const imagesSvg = digits.map(d => {{
    const asset = digitsAssets[d] || digitsAssets['0'];
    const x = totalWidth;
    totalWidth += asset.width;
    return `<image x="${{x}}" y="0" width="${{asset.width}}" height="${{asset.height}}" href="${{asset.data}}" />`;
  }}).join('\\n  ');

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${{totalWidth}}" height="${{height}}" viewBox="0 0 ${{totalWidth}} ${{height}}">
  <style>
    svg {{ background: transparent; }}
  </style>
  ${{imagesSvg}}
</svg>`;

  res.setHeader('Content-Type', 'image/svg+xml');
  res.setHeader('Cache-Control', 'max-age=0, no-cache, no-store, must-revalidate, proxy-revalidate');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('Expires', '0');
  res.setHeader('X-Storage-Type', hasPersistentStore ? 'Vercel-KV' : 'Memory-Fallback');
  res.setHeader('X-KV-Debug', kvErrorMsg.replace(/[^a-zA-Z0-9 =:_.-]/g, ''));
  res.status(200).send(svg);
}}
'''
    with open(os.path.join(API_DIR, 'counter.js'), 'w', encoding='utf-8') as f:
        f.write(code)
    print("Generated Persistent Vercel Function with Diagnostics")

def main():
    theme_assets = generate_base64_dict()
    build_vercel_serverless(theme_assets)

if __name__ == '__main__':
    main()
