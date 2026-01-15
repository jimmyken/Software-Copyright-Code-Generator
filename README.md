# Software-Copyright-Code-Generator
计算机软件著作权程序鉴别材料生成器

## 简介 / Introduction

一个自动生成符合中国软件著作权申请要求的程序鉴别材料的工具。只需提供源代码文件夹，即可自动生成符合申请规范的DOCX文件。

An automated tool that generates source code documentation compliant with China's software copyright application requirements. Simply provide the source code folder, and it will automatically generate a DOCX file meeting all application specifications.

## 主要特性 / Key Features

- ✅ 自动扫描源代码目录 / Automatically scans source code directory
- ✅ 支持多种编程语言 / Supports multiple programming languages
- ✅ 符合申请规范：每页50行代码 / Compliant format: 50 lines per page
- ✅ 自动选择前30页和后30页（超过60页时） / Automatically selects first 30 and last 30 pages (when > 60 pages)
- ✅ 添加页眉页脚 / Adds headers and footers
- ✅ 生成标准DOCX文档 / Generates standard DOCX document

## 安装 / Installation

### 环境要求 / Requirements

- Python 3.6 或更高版本 / Python 3.6 or higher

### 安装依赖 / Install Dependencies

```bash
pip install -r requirements.txt
```

## 使用方法 / Usage

### 基本用法 / Basic Usage

```bash
python generator.py /path/to/source -o output.docx
```

### 完整参数 / Full Options

```bash
python generator.py /path/to/source \
  -o output.docx \
  -n "软件名称" \
  -v "V1.0"
```

### 参数说明 / Parameters

- `source_dir`: 源代码目录路径（必需） / Source code directory path (required)
- `-o, --output`: 输出DOCX文件路径（默认：copyright_code.docx） / Output DOCX file path (default: copyright_code.docx)
- `-n, --name`: 软件名称，显示在页眉（默认：软件名称） / Software name for header (default: 软件名称)
- `-v, --version`: 软件版本（默认：V1.0） / Software version (default: V1.0)

## 使用示例 / Examples

### 示例 1：基本使用 / Example 1: Basic Usage

```bash
python generator.py ./my_project -o my_copyright.docx
```

### 示例 2：指定软件名称和版本 / Example 2: With Software Name and Version

```bash
python generator.py ./my_project \
  -o my_copyright.docx \
  -n "我的管理系统" \
  -v "V2.0"
```

## 工作原理 / How It Works

1. **扫描源代码** / **Scan Source Code**: 递归扫描指定目录下的所有源代码文件
2. **收集代码** / **Collect Code**: 读取并整理所有代码文件内容
3. **格式化** / **Format**: 按每页50行的格式组织代码
4. **选择页面** / **Select Pages**: 
   - 如果总页数 ≤ 60页：包含所有页面 / If total pages ≤ 60: include all pages
   - 如果总页数 > 60页：包含前30页和后30页 / If total pages > 60: include first 30 and last 30 pages
5. **生成文档** / **Generate Document**: 创建带有页眉页脚的DOCX文档

## 支持的文件类型 / Supported File Types

程序支持以下常见源代码文件扩展名 / The tool supports the following common source code file extensions:

- **Python**: `.py`
- **Java**: `.java`
- **C/C++**: `.c`, `.cpp`, `.h`, `.hpp`
- **C#**: `.cs`
- **JavaScript/TypeScript**: `.js`, `.ts`, `.jsx`, `.tsx`
- **Go**: `.go`
- **Rust**: `.rs`
- **Ruby**: `.rb`
- **PHP**: `.php`
- **Swift**: `.swift`
- **Kotlin**: `.kt`
- **Scala**: `.scala`
- **其他 / Others**: `.sql`, `.sh`, `.xml`, `.html`, `.css`, `.json`, `.yaml`, `.yml`, 等 / etc.

## 自动排除的目录 / Automatically Excluded Directories

工具会自动跳过以下目录 / The tool automatically skips the following directories:

- `.git`, `.svn`, `.hg` (版本控制 / Version control)
- `__pycache__`, `node_modules` (依赖和缓存 / Dependencies and cache)
- `venv`, `env`, `.env` (虚拟环境 / Virtual environments)
- `dist`, `build`, `target` (构建输出 / Build outputs)
- `.idea`, `.vscode` (IDE配置 / IDE configurations)

## 注意事项 / Notes

1. 确保源代码目录包含实际的源代码文件 / Ensure the source directory contains actual source code files
2. 生成的DOCX文件符合中国软件著作权申请的格式要求 / The generated DOCX file complies with China's software copyright application format requirements
3. 建议在提交前检查生成的文档 / It's recommended to review the generated document before submission
4. 对于大型项目，处理可能需要一些时间 / For large projects, processing may take some time

## 许可证 / License

MIT License

## 贡献 / Contributing

欢迎提交问题和拉取请求 / Issues and pull requests are welcome!
