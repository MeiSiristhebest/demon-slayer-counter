// Cloudflare Workers - Dynamic SVG Counter for GitHub Profile
// Supports 'demon-slayer' and 'misaka-network' themes

import ASSETS from './assets.json';

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const params = url.searchParams;
    const name = params.get('name') || 'visitor';
    const theme = params.get('theme') || 'demon-slayer';
    const length = parseInt(params.get('length') || '6', 10);

    const currentTheme = ASSETS[theme] ? theme : 'demon-slayer';
    const digitsAssets = ASSETS[currentTheme];

    // KV / Memory count lookup
    let count = 1000;
    if (env && env.COUNTER_KV) {
      const stored = await env.COUNTER_KV.get(`${currentTheme}:${name}`);
      count = stored ? parseInt(stored, 10) + 1 : 1000;
      await env.COUNTER_KV.put(`${currentTheme}:${name}`, count.toString());
    } else {
      count = Math.floor(Math.random() * 900000) + 100000;
    }

    const countStr = count.toString().padStart(length, '0');
    const digits = countStr.split('');

    let totalWidth = 0;
    const height = 240;

    const imagesSvg = digits.map(d => {
      const asset = digitsAssets[d] || digitsAssets['0'];
      const x = totalWidth;
      totalWidth += asset.width;
      return `<image x="${x}" y="0" width="${asset.width}" height="${asset.height}" href="${asset.data}" />`;
    }).join('\n  ');

    const svg = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${totalWidth}" height="${height}" viewBox="0 0 ${totalWidth} ${height}">
  <style>
    svg { background: transparent; }
  </style>
  ${imagesSvg}
</svg>`;

    return new Response(svg, {
      headers: {
        'Content-Type': 'image/svg+xml',
        'Cache-Control': 'max-age=0, no-cache, no-store, must-revalidate, proxy-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0',
        'Access-Control-Allow-Origin': '*'
      }
    });
  }
};
