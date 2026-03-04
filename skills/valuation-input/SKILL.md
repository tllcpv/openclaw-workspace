---
name: valuation-input
description: 评估项目基础资料接收与解析。用于处理评估项目的基础资料上传、信息提取、字段解析和缺失检查。触发条件：1) 用户发送评估项目资料文件（PDF、Excel、Word）2) 用户需要提取资料中的关键信息 3) 检查资料完整性。支持房产评估项目的基础信息（项目名称、地址、面积、产权证号等）自动提取。
---

# 评估资料接收解析

处理评估项目基础资料的接收、解析和信息提取。

## 核心功能

### 1. 资料上传与解析

接收以下格式的资料文件：
- **PDF** - 产权证扫描件、合同、评估委托书
- **Excel** - 测算表、信息登记表
- **Word** - 情况说明、报告草稿
- **图片** - JPG、PNG、BMP、TIFF、WebP（手机拍照资料）
- **Text/CSV** - 数据导出文件

### 2. 关键字段自动提取

自动识别并提取以下类别信息：

**基本信息**
- 项目名称、房产地址、房产类型、产权人

**物理状况**
- 建筑面积、土地面积、层数、所在楼层、建成年份、建筑结构

**权属信息**
- 产权证号、土地证号、土地用途、使用期限

**租赁信息**（租金评估）
- 当前租金、租赁起止日期、承租人

### 3. 资料完整性检查

自动检查必填字段是否缺失：
- 项目名称、项目地址（必填）
- 建筑面积（必填）
- 产权证号（必填）
- 用途（必填）
- 建成年份（如有就填写）

## 工作流程

### 标准流程

```
用户上传资料文件
      ↓
识别文件格式（PDF/Excel/Word）
      ↓
解析文档内容
      ↓
提取关键字段
      ↓
检查缺失项
      ↓
返回提取结果 + 缺失清单
```

### 使用方式

**方式一：直接调用解析脚本**

```bash
# 解析PDF
python scripts/document_parser.py "资料文件.pdf"

# 解析图片（手机拍照资料）
python scripts/document_parser.py "IMG_20240304_120000.jpg"

# 解析并检查缺失字段
python scripts/document_parser.py "资料文件.pdf" --check-missing

# 输出到文件
python scripts/document_parser.py "资料文件.pdf" -o output.json
```

**方式二：在飞书中使用**

用户发送：
```
【评估资料上传】
项目名称：XXX大厦租金评估
资料文件：[上传PDF/Excel]
```

返回：
```
资料解析完成：

✅ 已提取字段：
- 项目名称：XXX大厦
- 房产地址：XX市XX区XX路XX号
- 建筑面积：5,000平方米
- 产权证号：粤(2025)XX市不动产权第XXXX号

⚠️ 缺失字段：
- 建成年份
- 当前租金

请补充缺失资料后继续。
```

## 技术实现

### 扫描件PDF识别（OCR）

对于扫描件PDF（图片格式），会自动启用OCR识别：

1. **自动检测** - 如果PDF无法直接提取文字，自动尝试OCR
2. **中文支持** - 使用 tesseract 中文语言包识别中文字符
3. **多页处理** - 逐页识别并合并结果

**输出标识：**
```json
{
  "ocr_used": true,  // 表示使用了OCR识别
  "full_text": "..."  // 识别出的文字内容
}
```

### 依赖安装

```bash
# 基础依赖
pip install pdfplumber openpyxl python-docx

# OCR依赖（用于扫描件PDF和图片识别）
pip install pytesseract pdf2image pillow

# 系统依赖（Ubuntu/Debian）
apt-get install tesseract-ocr tesseract-ocr-chi-sim poppler-utils

# 系统依赖（macOS）
brew install tesseract tesseract-lang

# 系统依赖（Windows）
# 下载安装 tesseract-ocr：https://github.com/UB-Mannheim/tesseract/wiki
# 并添加到系统PATH
```

### 字段提取规则

详见 [references/field-definitions.md](references/field-definitions.md)

关键模式：
- `关键词：值` - 冒号分隔
- `关键词 值` - 空格分隔
- 表格单元格匹配

### 输出格式

JSON结构：
```json
{
  "file_type": "pdf",
  "file_path": "...",
  "pages": 10,
  "extracted_fields": {
    "basic_info": { "property_name": "...", ... },
    "physical_info": { ... },
    "rights_info": { ... }
  },
  "missing_fields": ["建成年份", "当前租金"],
  "tables": [...]
}
```

## 与其他步骤的衔接

解析完成后：
1. **数据存入**飞书多维表格（项目登记）
2. **触发**资料分析步骤（检查缺失、逻辑验证）
3. **通知**项目负责人补充缺失资料

## 参考文档

- **[字段定义](references/field-definitions.md)** - 具体字段提取规则和别名
- **[评估数据框架](references/valuation-data-framework.md)** - 通用信息分类标准（四类信息结构）

## 注意事项

1. **文件质量** - 扫描件需清晰，避免模糊/歪斜
2. **字段别名** - 支持多种常见表述（如"建筑面积""面积""总面积"）
3. **人工复核** - 自动提取后建议人工确认关键数据
4. **敏感信息** - 涉及产权证号等敏感信息，注意存储安全
