# DeepSeek 提示词管理器 [PromptBox]

一个优雅的 AI 提示词管理工具，帮助用户快速查找和使用各类 AI 提示词模板。

![DeepSeek 提示词管理器](screenshot.png) PromptBox

## 功能特点

- 🎯 分类管理：按照不同场景和用途对提示词进行分类
- 🔍 实时搜索：快速搜索并定位所需的提示词
- 🔗 导航链接：快速访问常用的 AI 相关网站
- 📋 一键复制：便捷的提示词复制功能
- 💫 魔法效果：精美的动画和交互效果
- 📱 响应式设计：完美支持各种设备

## 技术栈

- 后端：Python + Flask
- 前端：HTML5 + CSS3 + JavaScript
- 配置：INI 文件格式

## 快速开始

1. 安装依赖：

 DeepSeek 提示词应用。

```markdown:README.md
# DeepSeek 提示词管理器

一个优雅的 AI 提示词管理工具，帮助用户快速查找和使用各类 AI 提示词模板。

![DeepSeek 提示词管理器](screenshot.png)

## 功能特点

- 🎯 分类管理：按照不同场景和用途对提示词进行分类
- 🔍 实时搜索：快速搜索并定位所需的提示词
- 🔗 导航链接：快速访问常用的 AI 相关网站
- 📋 一键复制：便捷的提示词复制功能
- 💫 魔法效果：精美的动画和交互效果
- 📱 响应式设计：完美支持各种设备

## 技术栈

- 后端：Python + Flask
- 前端：HTML5 + CSS3 + JavaScript
- 配置：INI 文件格式

## 快速开始

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 配置提示词：
编辑 `deepseek_config.ini` 文件，添加或修改提示词模板。

3. 启动应用：
```bash
python app.py
```

4. 访问应用：
打开浏览器访问 `http://localhost:5000`

## 配置文件说明

`deepseek_config.ini` 支持以下配置：

```ini
[导航链接]
网站名称 = 网址

[分类名称]
提示词名称 = 提示词模板
```

## 项目结构

```
.
├── app.py              # Flask 应用主文件
├── requirements.txt    # 项目依赖
├── deepseek_config.ini # 配置文件
└── static/            
    └── index.html     # 前端页面
```

## 开发说明

- 提示词模板支持动态更新，修改配置文件后自动生效
- 前端采用模块化设计，易于扩展和维护
- 支持自定义样式和主题

## 贡献指南

1. Fork 本仓库
2. 创建新的功能分支
3. 提交您的更改
4. 发起 Pull Request

## 许可证

MIT License

## 联系方式

如有问题或建议，欢迎提交 Issue 或 Pull Request。

## 致谢

感谢所有为本项目做出贡献的开发者。
```

这个 README.md 包含了：


