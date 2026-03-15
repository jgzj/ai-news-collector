# 📰 AI 新闻日报

自动收集和展示最新人工智能相关新闻的 GitHub 项目。

## ✨ 功能特性

- 🤖 **自动采集**：每日自动从多个权威源收集 AI 新闻
- 📱 **响应式设计**：美观简洁的展示页面，支持移动端
- 🔄 **GitHub Actions**：定时任务自动更新
- 📊 **分类展示**：按主题分类，快速浏览
- 🔗 **来源标注**：每条新闻标注来源和发布时间

## 🚀 在线访问

[📅 查看最新 AI 新闻](https://jgzj.github.io/ai-news-collector/)

## 📋 新闻来源

- The Verge - AI 板块
- TechCrunch - AI 标签
- MIT Technology Review
- ArXiv 最新论文
- AI 研究机构博客
- 行业领先企业动态

## 🛠️ 技术栈

- **采集**: Python + Requests + BeautifulSoup
- **页面**: HTML5 + CSS3 + JavaScript
- **部署**: GitHub Pages
- **自动化**: GitHub Actions

## ⚙️ 配置说明

### GitHub Actions 配置

1. 进入 Settings → Actions → General
2. 启用 "Allow GitHub Actions to create and approve pull requests"
3. Actions 会自动运行（每天 UTC 时间 0:00）

### 自定义新闻源

编辑 `scripts/collect_news.py` 中的 `SOURCES` 列表，添加或移除新闻源。

## 📝 使用说明

### 手动运行

```bash
# 安装依赖
pip install -r requirements.txt

# 运行采集脚本
python scripts/collect_news.py

# 本地预览
python -m http.server 8000
```

### 查看历史新闻

所有历史新闻保存在 `data/` 目录，按日期归档。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

---

**最后更新**: 自动更新
**维护者**: AI Assistant
