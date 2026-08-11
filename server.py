import os
import json
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

BASE_DIR = r'e:\Mei\下载\cs\demon-slayer-counter'
WEB_DIR = os.path.join(BASE_DIR, 'web')
SERVER_DIR = os.path.join(BASE_DIR, 'server')

ASSETS_PATH = os.path.join(SERVER_DIR, 'assets.json')
with open(ASSETS_PATH, 'r', encoding='utf-8') as f:
    ASSETS = json.load(f)

COUNTER_STORE = {}

class CounterHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        
        if parsed.path.startswith('/api/counter'):
            query = urllib.parse.parse_qs(parsed.query)
            name = query.get('name', ['visitor'])[0]
            length = int(query.get('length', ['6'])[0])
            
            current_theme = 'demon-slayer'
            digits_assets = ASSETS[current_theme]
            
            key = f"{current_theme}:{name}"
            count = COUNTER_STORE.get(key, 12345) + 1
            COUNTER_STORE[key] = count
            
            count_str = str(count).zfill(length)
            digits = list(count_str)
            
            total_width = 0
            height = 240
            images_svg_list = []
            
            for d in digits:
                asset = digits_assets.get(d, digits_assets['0'])
                x = total_width
                total_width += asset['width']
                images_svg_list.append(
                    f'<image x="{x}" y="0" width="{asset["width"]}" height="{asset["height"]}" href="{asset["data"]}" />'
                )
                
            images_svg = '\n  '.join(images_svg_list)
            
            svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{total_width}" height="{height}" viewBox="0 0 {total_width} {height}">
  <style>
    svg {{ background: transparent; }}
  </style>
  {images_svg}
</svg>'''

            svg_bytes = svg.encode('utf-8')
            
            self.send_response(200)
            self.send_header('Content-Type', 'image/svg+xml')
            self.send_header('Cache-Control', 'max-age=0, no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Length', str(len(svg_bytes)))
            self.end_headers()
            self.wfile.write(svg_bytes)
            return

        return super().do_GET()

def main():
    port = 8080
    server_address = ('', port)
    httpd = HTTPServer(server_address, CounterHandler)
    print(f"Demon Slayer Counter Server running at http://localhost:{port}/")
    print(f"Dynamic SVG API: http://localhost:{port}/api/counter?name=Mei")
    httpd.serve_forever()

if __name__ == '__main__':
    main()
