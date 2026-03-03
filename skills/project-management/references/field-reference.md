# 项目管理表格字段说明

表格地址：https://pg-tanll.feishu.cn/base/MWT8bBCR3ai80QsLwjwc3ACvnJg

## 项目表（🚩 项目）字段列表

### 基础信息

| 字段名 | 字段ID | 类型 | 说明 | 可编辑 |
|--------|--------|------|------|--------|
| 项目名称 | fld2pPEYpg | Text | 主键，项目唯一标识 | ✅ |
| 文本 5 | flddH3Sqb1 | SingleSelect | 项目类型 | ✅ |
| 项目单位 | fldCjsprqU | SingleSelect | 执行单位 | ✅ |
| 项目负责人 | fldo1NOChC | User | 飞书用户 | ✅ |
| 项目情况概述 | fldIo0kKua | Text | 项目简介 | ✅ |
| 目标来源 | fld3HR9UXo | Text | 客户来源 | ✅ |
| 项目开始时间 | fldD78NnTo | DateTime | 登记时间 | ✅ |
| 合同金额万元 | fldy39bSDS | Number | 金额（万元） | ✅ |

### 项目类型选项
- 评估项目
- 咨询项目
- 可研项目
- 尽调项目
- 投标项目

### 项目单位选项
- 大陆
- 同致信德
- 国德
- 中财宝信
- 江苏昌宏
- 其他

---

### 进度跟踪

| 字段名 | 字段ID | 类型 | 说明 | 可编辑 |
|--------|--------|------|------|--------|
| 合同 | fldZuO6JUA | SingleSelect | 合同状态 | ✅ |
| 现场 | fld6i8aa6o | MultiSelect | 现场工作阶段 | ✅ |
| 报告 | flddXnaMPU | SingleSelect | 报告状态 | ✅ |
| 收款 | fld5xRy3Kg | SingleSelect | 收款状态 | ✅ |
| 归档 | fld941EsAh | DateTime | 归档日期 | ✅ |

### 合同状态选项
- 意向
- 商谈中
- 合同定稿
- 签订完成
- 收到纸质

### 现场阶段选项（多选）
- 资料准备
- 现场勘查
- 资料收集
- 资料盖章

### 报告状态选项
- 测算结果
- 初步结果沟通
- 初步结果确定
- 报告初稿完成
- 报告审核通过
- 报告出具提交

### 收款状态选项
- 已开发票
- 款项收到
- 结算回公司

---

### 最新动态

| 字段名 | 字段ID | 类型 | 说明 | 可编辑 |
|--------|--------|------|------|--------|
| 最新消息 | fldn48SjoB | Text | 简短更新 | ✅ |
| 最新情况 | fldoYsDQRB | Text | 当前状态描述 | ✅ |

---

### 报告出具信息（新增）

| 字段名 | 类型 | 说明 | 可编辑 |
|--------|------|------|--------|
| 报告编号 | Text | 报告唯一编号 | ✅ |
| 出具时间 | DateTime | 报告出具日期 | ✅ |
| 报告结论 | Text | 评估结果/结论 | ✅ |

**报告结论示例**：
- 年租金评估值为120万元
- 资产评估值为5000万元
- 项目可行，建议投资

---

### 关联字段（自动计算）

| 字段名 | 字段ID | 类型 | 说明 |
|--------|--------|------|------|
| 特别任务 | fldS3MKJkW | Lookup | 关联任务表计数 |
| 任务完成度 | fldw8fLiXH | Formula | 已完成任务百分比 |
| 成员 | fldgWvqwtV | Lookup | 关联成员表 |
| 对应任务 | fld7v0WFJ9 | DuplexLink | 双向关联任务表 |
| 项目进展 | fldVDZU9qI | SingleLink | 关联周报表 |
| 父记录 2 | fld2l9epgp | SingleLink | 父子项目关联 |

**注意**：关联字段为自动计算，不可直接编辑。

---

## API 调用参数

```javascript
const APP_TOKEN = "MWT8bBCR3ai80QsLwjwc3ACvnJg";
const TABLE_ID = "tblmlBjhA1DDsZd4";

// 创建记录示例
feishu_bitable_create_record({
  app_token: APP_TOKEN,
  table_id: TABLE_ID,
  fields: {
    "项目名称": "XXX",
    "文本 5": "咨询项目",
    "项目单位": "大陆",
    "最新情况": "报告初稿",
    "合同金额万元": 6.1,
    "目标来源": "金",
    "项目情况概述": "...",
    "项目开始时间": 1740969600000,  // 时间戳毫秒
    "项目负责人": [{ id: "ou_xxx" }]  // 用户ID数组
  }
});
```

---

## 字段值格式参考

### 单选字段
直接传选项名称字符串：
```javascript
{ "文本 5": "咨询项目" }
```

### 多选字段
传选项名称数组：
```javascript
{ "现场": ["资料准备", "现场勘查"] }
```

### 日期时间
传时间戳（毫秒）：
```javascript
{ "项目开始时间": 1740969600000 }
```

### 用户字段
传用户对象数组：
```javascript
{ "项目负责人": [{ id: "ou_7e397a9e5453a1efb93d5caabf1d31ba" }] }
```

### 数字字段
```javascript
{ "合同金额万元": 6.1 }
```
