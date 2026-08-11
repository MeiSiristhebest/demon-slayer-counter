# GitHub Profile 动态计数器部署指南 (Vercel & Cloudflare Workers)

本目录提供了零成本、高性能的二次元动态计数器 API 部署服务包。

---

## 🚀 方式 A：1 分钟部署至 Vercel (推荐，零成本)

### 步骤：
1. 安装 Vercel CLI（若未安装）：
   ```bash
   npm i -g vercel
   ```
2. 进入 `server` 目录并运行一键部署：
   ```bash
   cd demon-slayer-counter/server
   vercel --prod
   ```
3. 部署完成后，你将获得一个生产环境域名，如 `https://your-app.vercel.app`。

---

## ⚡ 方式 B：部署至 Cloudflare Workers

### 步骤：
1. 安装 Wrangler：
   ```bash
   npm i -g wrangler
   ```
2. 运行一键发布：
   ```bash
   cd demon-slayer-counter/server
   wrangler deploy worker.js --name demon-slayer-counter
   ```

---

## 📝 在 GitHub Profile `README.md` 中嵌入计数器

复制下方代码并粘贴至你的 GitHub 个人主页 `README.md` 中（请将 `your-domain.vercel.app` 替换为你的真实部署域名，将 `YOUR_GITHUB_USERNAME` 替换为你的 GitHub 用户名）：

### 1. 🔥 鬼灭全明星主题 (Demon Slayer)
```markdown
[![Demon Slayer View Counter](https://your-domain.vercel.app/api/counter?name=YOUR_GITHUB_USERNAME&theme=demon-slayer)](https://github.com/YOUR_GITHUB_USERNAME)
```

### 2. ⚡ 御坂网络主题 (Misaka Network)
```markdown
[![Misaka Network View Counter](https://your-domain.vercel.app/api/counter?name=YOUR_GITHUB_USERNAME&theme=misaka-network)](https://github.com/YOUR_GITHUB_USERNAME)
```
