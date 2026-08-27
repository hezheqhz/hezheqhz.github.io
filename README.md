# Zhe He's Academic Homepage 赫哲的个人学术主页

基于 [HugoBlox Academic CV](https://github.com/HugoBlox/theme-academic-cv) 模板（Hugo + Tailwind CSS v4），部署在 GitHub Pages。

## 本地预览

```bash
hugo server --disableFastRender
# 打开 http://localhost:1313/
```

需要的环境（已安装）：Hugo Extended ≥ 0.162、Go、Node.js、`npm install`（项目依赖）、`npm i -g @tailwindcss/cli`。

## 部署到 GitHub Pages（首次）

```bash
gh auth login                       # 浏览器登录 GitHub
gh repo create hezheqhz.github.io --public --source . --push
```

然后在仓库页面 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
之后每次 `git push` 到 main 分支都会自动构建并发布到 https://hezheqhz.github.io/。

## 日常更新内容

| 要改什么 | 改哪里 |
|---|---|
| 个人简介、头衔、社交链接 | `data/authors/me.yaml` |
| 工作经历/教育/获奖/技能 | `data/authors/me.yaml`（experience / education / awards / skills） |
| 新增论文 | 复制 `content/publications/` 下任意文件夹，改 `index.md` 即可 |
| 首页板块（研究方向、经费项目表） | `content/_index.md` |
| 研究方向项目页 | `content/projects/` |
| 网站名称、简介、主题色 | `config/_default/params.yaml` |
| 导航菜单 | `config/_default/menus.yaml` |

## 待办（替换占位内容）

- ~~头像照片~~ ✅ 已添加（`assets/media/authors/me.jpg`；换照片直接替换该文件即可）
- **Google Scholar / ORCID / GitHub**：已填入，如需修改在 `data/authors/me.yaml` 的 `links` 里
- **CV 下载按钮**：把简历 PDF 放到 `static/uploads/resume.pdf`，然后取消 `content/_index.md` 中 button 的注释
- 论文的 DOI / PDF 链接可在各论文 `index.md` 里补充 `hugoblox.ids.doi` 和 `links`

## 目录说明

- `参考材料/` — 原始简历 docx 和论文页面生成脚本 `gen_pubs.py`
- `content/publications/` — 37 篇论文页面（28 期刊 + 1 学位论文 + 9 会议，其中 6 篇 featured）
