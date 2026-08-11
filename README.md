# 鬼灭全明星 & 御坂网络 Moe-Counter 动态计数器系统

本项目包含了**《鬼灭之刃全明星》**与**《御坂网络》**二次元 0~9 举牌卡牌数字动态计数器的全流程资产制作与交互展示测试系统。

---

## 🌟 核心特色

1. **二次元考据立绘资产**：
   - 包含 0~9 共 10 位主线角色独一无二的身体姿态、双手持牌方式与表情语言。
   - 所有图片均经过自动化透明背景抠图、Anti-aliasing alpha 平滑边缘抗锯齿与包围盒紧凑裁切。
2. **高品质图形压缩**：
   - 导出为标准无损 WebP / PNG 双格式，相比传统 GIF/PNG 体积减少 45%+，且完全无白边锯齿。
3. **10连排立绘视觉对齐校验 (`preview.png`)**：
   - 包含 0~9 全员横向一字排开的拼图校验，确保角色身高、视觉光影与卡牌数字尺寸高度统一。
4. **实时交互式 Dynamic Counter Web Showcase**：
   - 包含响应式动态拼接模拟器、一键鬼灭/御坂双主题切换、角色考据画廊以及 GitHub README 嵌入代码一键生成。

---

## 📁 目录结构

```
demon-slayer-counter/
├── scripts/
│   └── process_images.py          # 自动化图片去背景、裁切、WebP压缩与Preview拼图脚本
├── assets/
│   ├── demon-slayer/               # 鬼灭全明星 0~9 透明 WebP/PNG 资产 & preview.png
│   └── misaka-network/             # 御坂网络 0~9 透明 WebP/PNG 资产 & preview.png
├── web/                            # 动态计数器 Web 测试展示应用
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   └── assets/                      # Web 部署静态资源
└── README.md
```

---

## 🚀 启动与使用

### 1. 运行图像后处理自动化脚本
```bash
python scripts/process_images.py
```

### 2. 启动 Web 测试界面
使用任意静态 HTTP 服务器（如 Python `http.server` 或 Live Server）：
```bash
cd web
python -m http.server 8080
```
然后在浏览器中打开 `http://localhost:8080` 体验实时数字输入、手势微动与主题切换效果！
