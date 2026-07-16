# Day4 学习记录：项目工程化与 AI Pair Programming

## 今日目标
将 Student Manager 从"能跑的脚本"升级为有软件工程规范的项目。

## 完成内容

### 1. 项目工程化
- 新建 v3_engineering/ 版本
- 目录结构：models/、services/、storage/、data/、docs/
- 理解 Python Package 和 __init__.py

### 2. 模块拆分（Refactor）
- 将 JSON 持久化从 manager.py 拆分到 storage/storage.py
- 应用单一职责原则（SRP）
- 保持接口不变，main.py 零修改

### 3. StudentStatistics 模块
- 新增 services/statistics.py
- 实现：总人数、平均年龄、性别比例
- 向后兼容：旧数据无 gender 字段，默认归入"未知"
- 低耦合设计：只接收数据，不依赖 manager

### 4. Context Engineering
- 学会给 AI 写详细 Prompt
- 关键要素：目标明确 + 边界清晰 + 约束具体 + 验证标准

### 5. Code Review
- 发现 Bug：age 类型转换、self.gender 笔误、try 块范围
- 学会先发现问题，再思考修改方案

### 6. Git 进阶
- git branch / git switch / git checkout / git merge
- git log / git diff / git restore
- 创建 practice 分支练习合并流程

## 关键设计决策
- 在 Student.__init__ 中强制 int(age)，从源头解决类型问题
- StudentStatistics 接收 students 列表而非 manager 对象（低耦合）
- storage 独立后，未来可无缝替换为数据库存储

## 下一步
- Day5：main.py 过长问题（UI 层与业务逻辑分离）