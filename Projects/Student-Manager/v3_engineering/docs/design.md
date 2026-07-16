# Student Manager v3 设计文档

## 目录结构
- models/：数据模型（Student）
- services/：业务逻辑（StudentManager, StudentStatistics）
- storage/：数据持久化（JsonStorage）

## 设计原则
- SRP：单一职责，storage 独立于 manager
- 封装：main.py 不直接调用 storage
- 低耦合：StudentStatistics 只接收数据，不依赖 manager

## 新增功能
- StudentStatistics：总人数、平均年龄、性别比例
- 向后兼容：旧数据无 gender 字段，默认归入"未知"