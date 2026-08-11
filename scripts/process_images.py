import os
import shutil
import numpy as np
from PIL import Image, ImageDraw

BRAIN_DIR = r'C:\Users\Mei\.gemini\antigravity\brain\532adfa7-583e-4ea4-8ab7-b466db7f88a7'
BASE_DIR = r'e:\Mei\下载\cs\demon-slayer-counter'
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
WEB_ASSETS_DIR = os.path.join(BASE_DIR, 'web', 'assets')

THEMES = {
    'demon-slayer': {
        '0': 'tanjiro_0_1786441919559.jpg',
        '1': 'nezuko_1_1786442055146.jpg',
        '2': 'zenitsu_2_1786443829320.jpg',
        '3': 'inosuke_3_aligned_1786460641637.jpg',
        '4': 'kanao_4_1786460744274.jpg',
        '5': 'giyu_5_1786460818787.jpg',
        '6': 'shinobu_6_1786460903089.jpg',
        '7': 'rengoku_7_1786461387481.jpg',
        '8': 'mitsuri_8_1786461497618.jpg',
        '9': 'muichiro_9_1786461624298.jpg'
    }
}

def remove_background_and_crop(img_path, target_height=480):
    img = Image.open(img_path).convert('RGB')
    w, h = img.size
    arr = np.array(img, dtype=np.float32)
    
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    diff = np.sqrt((255.0 - r)**2 + (255.0 - g)**2 + (255.0 - b)**2)
    
    binary_bg = Image.fromarray(np.uint8((diff < 45) * 255), mode='L')
    draw = ImageDraw.Draw(binary_bg)
    
    seeds = []
    for x in range(0, w, 5):
        seeds.append((x, 0))
        seeds.append((x, h - 1))
    for y in range(0, h, 5):
        seeds.append((0, y))
        seeds.append((w - 1, y))
        
    for seed in seeds:
        if binary_bg.getpixel(seed) == 255:
            ImageDraw.floodfill(binary_bg, seed, 128, thresh=0)
            
    bg_mask = (np.array(binary_bg) == 128)
    
    alpha = np.ones((h, w), dtype=np.float32) * 255.0
    outer_diff = diff[bg_mask]
    alpha_norm = np.clip((outer_diff - 12.0) / 33.0, 0.0, 1.0)
    alpha[bg_mask] = alpha_norm * 255.0
    
    rgba_arr = np.zeros((h, w, 4), dtype=np.float32)
    rgba_arr[:, :, :3] = arr
    
    for c in range(3):
        channel = arr[:, :, c]
        unmix = (channel - (1.0 - alpha / 255.0) * 255.0) / np.maximum(alpha / 255.0, 1e-4)
        rgba_arr[:, :, c] = np.where(bg_mask & (alpha > 0), np.clip(unmix, 0, 255), channel)
        
    rgba_arr[:, :, 3] = alpha
    rgba_img = Image.fromarray(rgba_arr.astype(np.uint8), mode='RGBA')
    
    bbox = rgba_img.getbbox()
    if bbox:
        left = max(0, bbox[0] - 10)
        upper = max(0, bbox[1] - 10)
        right = min(rgba_img.width, bbox[2] + 10)
        lower = min(rgba_img.height, bbox[3] + 10)
        rgba_img = rgba_img.crop((left, upper, right, lower))
        
    aspect = rgba_img.width / rgba_img.height
    target_width = int(target_height * aspect)
    resampled = rgba_img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    return resampled

def create_preview_grid(images, theme_name, target_height=480):
    padding = 20
    bg_color = (15, 23, 42, 255)
    
    total_width = sum(img.width for img in images) + padding * (len(images) + 1)
    grid_height = target_height + padding * 2
    
    grid = Image.new('RGBA', (total_width, grid_height), bg_color)
    x_offset = padding
    
    for i, img in enumerate(images):
        grid.paste(img, (x_offset, padding), img)
        x_offset += img.width + padding
        
    return grid

def main():
    print("Starting image processing pipeline (Demon Slayer only)...")
    
    for theme_name, mapping in THEMES.items():
        out_dir = os.path.join(ASSETS_DIR, theme_name)
        web_out_dir = os.path.join(WEB_ASSETS_DIR, theme_name)
        
        os.makedirs(out_dir, exist_ok=True)
        os.makedirs(web_out_dir, exist_ok=True)
        
        processed_imgs = []
        
        for num, fname in mapping.items():
            src_file = os.path.join(BRAIN_DIR, fname)
            if not os.path.exists(src_file):
                print(f"ERROR: Missing source file {fname}")
                continue
                
            proc_img = remove_background_and_crop(src_file, target_height=480)
            processed_imgs.append(proc_img)
            
            png_path = os.path.join(out_dir, f"{num}.png")
            webp_path = os.path.join(out_dir, f"{num}.webp")
            
            proc_img.save(png_path, "PNG")
            proc_img.save(webp_path, "WEBP", quality=95)
            
            shutil.copy(png_path, os.path.join(web_out_dir, f"{num}.png"))
            shutil.copy(webp_path, os.path.join(web_out_dir, f"{num}.webp"))
            
        if len(processed_imgs) == 10:
            preview_grid = create_preview_grid(processed_imgs, theme_name, target_height=480)
            preview_png_path = os.path.join(out_dir, "preview.png")
            web_preview_png_path = os.path.join(WEB_ASSETS_DIR, theme_name, "preview.png")
            
            preview_grid.save(preview_png_path, "PNG")
            shutil.copy(preview_png_path, web_preview_png_path)
            
            brain_artifact_preview = os.path.join(r'C:\Users\Mei\.gemini\antigravity\brain\145a8ecc-ec47-443e-b5c6-77ac23b6420e', f'{theme_name}_preview.png')
            preview_grid.save(brain_artifact_preview, "PNG")
            print(f"Generated preview grid: {preview_png_path}")

    print("Demon Slayer processing finished successfully!")

if __name__ == '__main__':
    main()
