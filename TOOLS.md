# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

### Cron 定时任务原则

**核心经验：定时任务不能太复杂**

- **单一职责**：每个任务只做一件事，不要把多个股票/多个搜索塞进一个任务
- **超时控制**：搜索类任务超时设为 180-300 秒，避免默认 120 秒超时
- **错峰执行**：多个相关任务间隔 5-10 分钟，避免同时触发资源竞争
- **失败隔离**：拆分后单个任务失败不影响其他任务

**反面教材**：
❌ 一个任务同时搜索3只股票 → 超时失败
✅ 拆成3个独立任务，每个搜索1只股票 → 稳定执行

---

### 搜索类任务经验

**web_search / kimi_search**
- **控制结果数量**：默认5条足够，除非明确要求深度调研
- **指定时间范围**：用 `freshness` 参数限定（如 `past week`），避免过时信息
- **分批搜索**：多个主题分开调用，不要一次性搜太多关键词
- **超时预留**：复杂搜索至少设 60-120 秒超时

**反面教材**：
❌ 一次搜索10个关键词 → 超时/结果杂乱
✅ 分3次搜索，每次3个关键词 → 结果清晰可控

---

### Feishu 消息发送规范

**文件发送**
- 优先使用 `message` 工具的 `filePath` 参数
- 避免直接发绝对路径（`/root/...`），使用相对路径或 media 路径
- 大文件（>10MB）先确认对方是否需要

**消息格式**
- 支持 Markdown，但表格在移动端显示不佳，长列表用分段代替
- 重要信息放在前3行（折叠后可见）
- `@用户` 功能可用，但不要滥用

---

### 文件处理经验

**读取大文件**
- 超过 2000 行用 `offset` + `limit` 分页读取
- 二进制文件（如 .doc/.xls）先用工具转换，不要直接读
- 图片文件用 `read` 工具可直接查看

**编辑文件**
- `edit` 工具要求精确匹配 `oldText`，建议先 `read` 再复制修改
- 大段替换用 `write`，但注意会覆盖原文件
- 代码文件注意缩进和换行符一致性

---

### 跨会话通信

**正确方式**
- 使用 `sessions_send` 向其他会话发送消息
- 使用 `sessions_spawn` 启动后台子代理
- 不要直接用 `message` 工具处理跨会话任务

**注意事项**
- 子代理任务设合理的 `timeoutSeconds`（默认可能不够）
- 复杂任务用 `runTimeoutSeconds` 控制总执行时间
- 子代理结果会自动回传，无需手动监听

---

### 内存管理提醒

**定期整理**
- 每周回顾 `memory/YYYY-MM-DD.md`，合并到 `MEMORY.md`
- 删除已完成的 TODO，更新进行中的任务状态
- 过期股票/基金信息及时清理，避免干扰新决策

**记录原则**
- 关键决策必须写进 `MEMORY.md`（价格、理由、时间）
- 临时想法先写进当日日记，确认重要后再归档
- 财务相关操作（买入/卖出）必须记录成本价和理由

---

Add whatever helps you do your job. This is your cheat sheet.
