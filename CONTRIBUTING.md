# 🤝 贡献指南 (Contributing Guide)

感谢你对 **Demon Slayer Profile Counter** 项目感兴趣！

---

## 🎨 提交新功能与优化

1. **Fork 本仓库** 到你自己的 GitHub 账号。
2. **创建 Feature 分支**：
   ```bash
   git checkout -b feat/your-feature-name
   ```
3. **提交修改与 Commit**：
   请遵循常规提交规范（Conventional Commits），如 `feat: ...` 或 `fix: ...`。
4. **发起 Pull Request (PR)**：
   在 GitHub 上提交 PR，我们会第一时间审核并合并！

---

## 🛠️ 重新打包 Base64 资产

若你修改了图片资产或增加了缩放尺寸，请运行以下 Python 脚本重新构建 API 依赖包：
```bash
python scripts/generate_server_assets.py
```
然后再提交代码。
