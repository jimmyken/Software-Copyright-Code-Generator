# SCCG：软件著作权代码生成器
# Software Copyright Code Generator：计算机软件著作权程序鉴别材料生成器

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.txt)

自动从源代码生成符合软件著作权申请要求的程序鉴别材料（DOCX格式）。

## 目录

  * [特性](#特性)
  * [运行环境](#运行环境)
  * [安装](#安装)
  * [快速开始](#快速开始)
  * [背景](#背景)
  * [详细使用](#详细使用)
     * [程序鉴别材料要求](#程序鉴别材料要求)
     * [如何实现每页50行](#如何实现每页50行)
     * [命令行参数](#命令行参数)
     * [使用示例](#使用示例)
  * [常见问题](#常见问题)
  * [开发说明](#开发说明)
  * [许可证](#许可证)

## 特性

- ✅ 自动删除注释和空行
- ✅ 自动添加符合规范的页眉（软件名+版本号+页码）
- ✅ 自动调整格式，确保每页50行
- ✅ 支持多个源代码目录
- ✅ 支持多种编程语言（Python、Java、JavaScript、HTML、CSS等）
- ✅ 支持自定义注释风格
- ✅ 支持排除指定文件或文件夹
- ✅ 支持自定义字体和排版参数

## 运行环境

- **Python**: 3.11 或更高版本（推荐 **Python 3.11+**）
- **操作系统**: Windows、macOS、Linux

## 安装

### 方式一：从 PyPI 安装（推荐）

```bash
pip install sccg
```

### 方式二：从源码安装

```bash
# 克隆仓库
git clone https://github.com/kenley2021/sccg.git
cd sccg

# 创建虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 安装到系统
pip install -e .
```

## 快速开始

```bash
# 最简单的用法：处理当前目录的 Python 代码
sccg -o output.docx

# 指定源代码目录
sccg -i ./src -o output.docx

# 指定软件名称和版本（用于生成页眉）
sccg -t "我的项目V1.0" -i ./src -o output.docx

# 处理多种语言的代码
sccg -i ./src -e py -e js -e html -e css -o output.docx
```

## 背景

申请软件著作权时需要提交以下材料：

| 材料类型 | 说明 | 准备难度 |
|---------|------|---------|
| 申请表 | 官网在线生成 | ⭐ 简单 |
| 身份证明 | 营业执照或身份证 | ⭐ 简单 |
| **程序鉴别材料** | **源代码文档（本工具生成）** | ⭐⭐⭐ 复杂 |
| 文档鉴别材料 | 软件操作手册 | ⭐⭐ 中等 |

程序鉴别材料需要整理源代码并满足特定格式要求（每页50行、无注释、带页眉等），手动处理非常繁琐。**sccg** 工具可以自动完成这一过程，几秒钟内生成符合规范的 DOCX 文档。

## 详细使用

### 程序鉴别材料要求

根据国家版权局要求，程序鉴别材料必须满足：

| 要求项 | 具体规范 | sccg 实现方式 |
|-------|---------|--------------|
| 代码行数 | 每页至少50行 | ✅ 自动调整格式参数 |
| 代码内容 | 不能含有注释、空行 | ✅ 自动过滤 |
| 页眉格式 | 软件名+版本号（居中），页码（右对齐） | ✅ 自动生成 |

### 如何实现每页50行

经过精确测试，以下参数组合可确保每页恰好50行：

| 参数 | 数值 | 说明 |
|-----|------|------|
| 字号 | 10.5pt | 五号字体 |
| 行间距 | 10.5pt | 固定值 |
| 段前间距 | 0pt | 无间距 |
| 参数 | 简写 | 类型 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--title` | `-t` | TEXT | 软件著作权程序鉴别材料生成器V1.0 | 软件名称+版本号（生成页眉） |
| `--indir` | `-i` | PATH | 当前目录 | 源码所在文件夹（可多个） |
| `--ext` | `-e` | TEXT | py | 源代码文件扩展名（可多个） |
| `--comment-char` | `-c` | TEXT | #, // | 注释字符（可多个） |
| `--font-name` | - | TEXT | 宋体 | 字体名称 |
| `--font-size` | - | FLOAT | 10.5 | 字号（五号字） |
| `--space-before` | - | FLOAT | 0.0 | 段前间距 |
| `--space-after` | - | FLOAT | 2.3 | 段后间距 |
| `--line-spacing` | - | FLOAT | 10.5 | 行间距 |
| `--exclude` | - | PATH | - | 排除的文件或路径（可多个） |
| `--outfile` | `-o` | PATH | code.docx | 输出文件名 |
| `--verbose` | `-v` | FLAG | - | 显示调试信息 |
| `--help` | - | - | - | 显示帮助信息 |

查看完整帮助：
```bash
sccg --help
```

### 使用示例

#### 示例 1：基本用法

```bash
# 处理当前目录的 Python 代码
sccg -o my_software.docx
```

#### 示例 2：指定项目目录和标题

```bash
# 处理指定目录
sccg -t "我的Web应用V2.0" -i ./src -o output.docx
```

#### 示例 3：处理多种编程语言

```bash
# 支持 Python、JavaScript、HTML、CSS
sccg -i ./project \
   常见问题

### Q1: 支持哪些编程语言？

支持所有文本格式的代码文件，常见的包括：
- Python (`.py`)
- Java (`.java`)
- JavaScript (`.js`)
- HTML (`.html`)
- CSS (`.css`)
- C/C++ (`.c`, `.cpp`, `.h`)
- Go (`.go`)
- Rust (`.rs`)
- 等等...

通过 `-e` 参数指定文件扩展名即可。

### Q2: 如何自定义页眉标题？

```bash
sccg -t "我的软件名称V1.0" -i ./src -o output.docx
```

### Q3: 如何处理多行注释？

目前仅支持单行注释（如 `#`、`//`）。对于多行注释（如 `/* */`、`"""`），建议：
- Python: 使用 `-c '"""'` 删除文档字符串开头
- Java/C++: 暂不完全支持 `/* */` 块注释

### Q4: 为什么生成的文档不是每页恰好50行？

请确保使用默认参数（不要修改字号、行距等）。如果仍有问题，可能是：
- 代码行过长导致自动换行
- 字体在不同系统上渲染差异
- Word 版本差异

### Q5: 如何调整字体？

```bash
# 使用等宽字体（推荐用于代码）
sccg -i ./src --font-name "Consolas" -o output.docx

# macOS 系统
sccg -i ./src --font-name "Menlo" -o output.docx
```

⚠️ **注意**：修改字体后可能需要重新调整字号和行距以保持每页50行。

### Q6: 生成的文档太大怎么办？

```bash
# 排除测试、文档、示例等非核心代码
sccg -i ./src \
     --exclude ./tests \
     --exclude ./docs \
     --exclude ./examples \
     -o output.docx
```

### Q7: 如何查看处理了哪些文件？

```bash
# 使用 -v 参数显示详细日志
sccg -i ./src -o output.docx -v
```

输出示例：
```
DEBUG:__main__:在/path/to/project/src目录下找到25个代码文件.
DEBUG:__main__:在/path/to/project目录下找到30个代码文件.
```

### Q8: Python 3.11+ 兼容性

本工具已针对 Python 3.11+ 优化，主要改进：
- ✅ 移除过时的 `scandir` 依赖（已内置）
- ✅ 使用现代的 `importlib.resources` API
- ✅ 改进 UTF-8 编码处理
- ✅ 支持 Python 3.7 - 3.14+

## 开发说明

### 本地开发环境设置

```bash
# 克隆项目
git clone https://github.com/kenley2021/sccg.git
cd sccg

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate  # Windows

# 安装开发依赖
pip install -r requirements.txt

# 以开发模式安装
pip install -e .

# 运行测试
python -m sccg.sccg --help
```

### 项目结构

```
sccg/
├── sccg/
│   ├── __init__.py
│   ├── sccg.py          # 主程序
│   └── template.docx    # Word 模板
├── setup.py             # 安装配置
├── requirements.txt     # 依赖列表
├── README.md            # 说明文档
├── LICENSE.txt          # MIT 许可证
└── MANIFEST.in          # 打包配置
```

## 许可证

本项目采用 [MIT License](LICENSE.txt) 开源协议。

## 贡献

欢迎提交 Issue 和 Pull Request！

## ☕️ 请喝一杯咖啡

如果这个工具帮您节省了时间，欢迎请作者喝杯咖啡！您的支持是我持续维护和改进这个项目的动力。

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="images/weixin.jpg" width="200px" alt="微信支付" />
        <br />
        <b>微信支付</b>
      </td>
      <td align="center">
        <img src="images/alipay.jpg" width="200px" alt="支付宝支付" />
        <br />
        <b>支付宝支付</b>
      </td>
    </tr>
  </table>
</div>

感谢您的支持！🙏

---

**作者**: jimmy  
**邮箱**: four498@gmail.com  
**项目地址**: https://github.com/jimmyken/Software-Copyright-Code-Generator.git
