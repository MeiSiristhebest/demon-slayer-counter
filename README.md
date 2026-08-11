<div align="center">

# 🔥 《鬼灭之刃全明星》动态 Profile 计数器

<p align="center">
  <b>精美的二次元 Q 版鬼灭之刃 0~9 举牌数字动态计数器，专为 GitHub Profile README 与个人主页量身打造</b>
</p>

<p align="center">
  <a href="https://vercel.com/new/import?s=https://github.com/MeiSiristhebest/demon-slayer-counter">
    <img src="https://vercel.com/button" alt="Deploy with Vercel" height="36" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Style-Cel--Shading%20Anime-ff4757.svg?style=for-the-badge&logo=anime" alt="Anime Style" />
  <img src="https://img.shields.io/badge/Format-Transparent%20WebP-2ed573.svg?style=for-the-badge" alt="WebP Format" />
  <img src="https://img.shields.io/badge/Deploy-Vercel%20%2F%20Serverless-1e90ff.svg?style=for-the-badge&logo=vercel" alt="Serverless" />
  <img src="https://img.shields.io/badge/License-MIT-ffa502.svg?style=for-the-badge" alt="License" />
</p>

<br />

<!-- 10连排立绘视觉全景图 -->
<img src="assets/demon-slayer/preview.png" alt="鬼灭全明星 0~9 全景预览" width="100%" style="border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.5);" />

</div>

---

## 📖 简介 (Overview)

**Demon Slayer Profile Counter** 是一款兼具高颜值与炫技二次元画风的 GitHub 个人主页（Profile README）动态 View Counter。结合 ufotable 官方 SD/Q版姿态考据，为 0~9 的每一位数字量身定制了独一无二的鬼灭角色性格立绘。

通过定制的 **FloodFill 智能抠图算法** 与 **SVG Base64 内嵌 Serverless API**，即使在 GitHub Camo 图片代理保护下，也能零延迟输出清晰不卡顿的矢量拼接计数器！

---

## ✨ 核心特色 (Features)

- 🎭 **0~9 官方考据性格立绘**：告别同质化僵硬站姿，包含炭治郎 3/4 英姿、祢豆子软萌蹲姿、善逸泪奔抖姿、伊之助踩石咆哮等 10 位角色专属动作！
- ✂️ **FloodFill 边缘抗锯齿抠图**：独家外围连通域算法，彻底抠除外围白背景，同时 100% 完整保留角色手中拿持的纯白数字卡牌！
- ⚡ **零依赖 1-Click Serverless 部署**：后端内置 Base64 WebP 压缩流，无需配置数据库或外部图片存储，部署在 Vercel / Cloudflare 即可秒速响应。
- 🎨 **内置实时测试 Playground**：包含本地与 Web 端图形交互测试系统，支持即时输入测试数字与动态卡牌悬停动效。

---

## 🚀 1-Click 快速部署 (Quick Start)

### 步骤 1：一键部署到 Vercel

点击下方按钮直接将项目一键导入并部署至你的 Vercel 账号：

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/MeiSiristhebest/demon-slayer-counter)

### 步骤 2：在 GitHub Profile README 中插入代码

部署完成后，在你的 GitHub 个人主页 `README.md` 中粘贴以下代码：

```markdown
[![Demon Slayer View Counter](https://YOUR_VERCEL_APP.vercel.app/api/counter?name=YOUR_GITHUB_USERNAME)](https://github.com/YOUR_GITHUB_USERNAME)
```

> **📌 注意**：请将 `YOUR_VERCEL_APP.vercel.app` 替换为你部署后获得的真实 Vercel 域名，`YOUR_GITHUB_USERNAME` 替换为你的 GitHub 用户名。

---

## 🛠️ API 参数说明 (API Query Parameters)

| 参数 (Parameter) | 类型 (Type) | 默认值 (Default) | 说明 (Description) |
|---|---|---|---|
| `name` | `string` | `visitor` | 计数器标识键（如你的 GitHub 用户名） |
| `length` | `number` | `6` | 最小数字显示位数（不足时自动补 0，如 `001234`） |
| `theme` | `string` | `demon-slayer` | 主题名称（默认 `demon-slayer`） |

---

## 🎭 0 ~ 9 鬼灭全明星角色图鉴 (Roster Showcase)

| 数字 | 角色 | 官方考据 pose 与性格说明 | 姿态亮点 |
|:---:|:---:|:---|:---|
| **0** | **灶门炭治郎** | 3/4 侧身坚毅站姿，阳光温和微笑 | 单手端牌，单手抚于腰间日轮刀 |
| **1** | **灶门祢豆子** | 软萌鸭子蹲姿，头斜歪眨眼 | 双小爪将白色数字卡牌斜贴在小脸蛋旁 |
| **2** | **我妻善逸** | 膝盖内八字打颤蹲姿，瀑布动漫眼泪 | 瑟瑟发抖将卡牌挡在脸前露出一双大眼 |
| **3** | **嘴平伊之助** | 单脚霸气踩在小岩石上，野猪头套仰天 | 单手豪横地把数字卡牌向头顶上方高高举起 |
| **4** | **栗花落香奈乎** | 优雅侧身伫立，右手抛金币（带金粉轨迹） | 左手侧持卡牌放在胸前，清澈紫眼轻微笑 |
| **5** | **富冈义勇** | 侧身单手藏在半半羽织袖口里 | 死鱼眼冷酷瞥视，两根手指冷酷夹牌 |
| **6** | **胡蝶忍** | 单脚轻盈踮立（如蝴蝶栖息） | 一手拉起羽织展露蝶翼，闭眼眯眯甜笑 |
| **7** | **煉獄杏寿郎** | 双腿豪迈跨开，昂头大笑（“UMAI!”） | 胸膛高高挺起，充满爆发力向前展示拍牌 |
| **8** | **甘露寺蜜璃** | 灵动前倾 S 型曲线，粉红脸颊爱心眼 | 双手合十捧着卡牌贴在红晕脸蛋旁 |
| **9** | **时透无一郎** | 懒散单腿屈膝坐姿，薄荷绿双眼仰望天空 | 宽大袖子下垂，随性用两根手指挂牌发呆 |

---

## 💻 本地运行与开发 (Local Development)

```bash
# 1. 克隆仓库
git clone https://github.com/MeiSiristhebest/demon-slayer-counter.git
cd demon-slayer-counter

# 2. 启动本地交互测试服务器
python server.py

# 3. 访问本地测试界面
# 网页界面: http://localhost:8080/
# 动态 SVG API: http://localhost:8080/api/counter?name=test
```

---

## 📄 开源协议 (License)

本项目采用 [MIT License](LICENSE) 开源协议。欢迎 Star ⭐ 与 Fork！
