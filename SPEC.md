# 业务管理系统规格说明书

## 1. 项目概述

- **项目名称**: Business Management System (BMS)
- **项目类型**: 前后端分离的Web管理系统
- **核心功能**: 会员管理、产品管理、物料管理三大模块
- **目标用户**: 企业内部管理人员

## 2. 技术栈

### 后端
- **框架**: Python FastAPI
- **数据库**: SQLite (SQLAlchemy ORM)
- **API风格**: RESTful API

### 前端
- **框架**: Vue 3 + Element Plus
- **构建工具**: Vite
- **HTTP客户端**: Axios

## 3. 功能模块

### 3.1 会员功能

#### 3.1.1 会员信息
- 会员列表展示（分页、搜索）
- 新增会员
- 编辑会员信息
- 删除会员
- 会员字段：编号、姓名、手机号、会员等级、积分、备注、创建时间

#### 3.1.2 消费记录
- 消费记录列表（分页、筛选）
- 新增消费记录
- 查看消费详情
- 消费字段：会员、金额、商品、数量、消费时间、备注

### 3.2 产品功能

#### 3.2.1 产品类别
- 类别列表
- 新增类别
- 编辑类别
- 删除类别
- 类别字段：编号、类别名称、描述

#### 3.2.2 产品详情
- 产品列表（分页、搜索、按类别筛选）
- 新增产品
- 编辑产品
- 删除产品
- 产品字段：编号、产品名称、类别、价格、库存、描述、创建时间

### 3.3 物料功能

#### 3.3.1 物品信息
- 物品列表（分页、搜索）
- 新增物品
- 编辑物品
- 删除物品
- 物品字段：编号、物品名称、规格、单位、当前库存、备注

#### 3.3.2 物品记录
- 记录列表（分页、筛选）
- 新增物品记录（入库/出库）
- 记录字段：物品、操作类型（入库/出库）、数量、经手人、时间、备注

## 4. 数据模型

### Member (会员)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| code | String | 会员编号 |
| name | String | 姓名 |
| phone | String | 手机号 |
| level | String | 会员等级 |
| points | Integer | 积分 |
| remark | String | 备注 |
| created_at | DateTime | 创建时间 |

### Consumption (消费记录)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| member_id | Integer | 会员ID |
| amount | Float | 金额 |
| product_name | String | 商品名称 |
| quantity | Integer | 数量 |
| consume_time | DateTime | 消费时间 |
| remark | String | 备注 |

### Category (产品类别)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| code | String | 类别编号 |
| name | String | 类别名称 |
| description | String | 描述 |

### Product (产品详情)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| code | String | 产品编号 |
| name | String | 产品名称 |
| category_id | Integer | 类别ID |
| price | Float | 价格 |
| stock | Integer | 库存 |
| description | String | 描述 |
| created_at | DateTime | 创建时间 |

### Material (物品信息)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| code | String | 物品编号 |
| name | String | 物品名称 |
| spec | String | 规格 |
| unit | String | 单位 |
| current_stock | Integer | 当前库存 |
| remark | String | 备注 |

### MaterialRecord (物品记录)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| material_id | Integer | 物品ID |
| operation_type | String | 操作类型(in/out) |
| quantity | Integer | 数量 |
| operator | String | 经手人 |
| record_time | DateTime | 时间 |
| remark | String | 备注 |

## 5. API接口

### 会员模块
- `GET /api/members` - 获取会员列表
- `POST /api/members` - 新增会员
- `PUT /api/members/{id}` - 更新会员
- `DELETE /api/members/{id}` - 删除会员

### 消费记录模块
- `GET /api/consumptions` - 获取消费记录列表
- `POST /api/consumptions` - 新增消费记录
- `GET /api/consumptions/{id}` - 获取消费详情

### 产品类别模块
- `GET /api/categories` - 获取类别列表
- `POST /api/categories` - 新增类别
- `PUT /api/categories/{id}` - 更新类别
- `DELETE /api/categories/{id}` - 删除类别

### 产品模块
- `GET /api/products` - 获取产品列表
- `POST /api/products` - 新增产品
- `PUT /api/products/{id}` - 更新产品
- `DELETE /api/products/{id}` - 删除产品

### 物料模块
- `GET /api/materials` - 获取物品列表
- `POST /api/materials` - 新增物品
- `PUT /api/materials/{id}` - 更新物品
- `DELETE /api/materials/{id}` - 删除物品

### 物品记录模块
- `GET /api/material-records` - 获取物品记录列表
- `POST /api/material-records` - 新增物品记录

## 6. 项目结构

```
/workspace/
├── backend/                 # Python FastAPI 后端
│   ├── app/
│   │   ├── main.py        # 主入口
│   │   ├── database.py    # 数据库配置
│   │   ├── models.py      # 数据模型
│   │   ├── schemas.py     # Pydantic模型
│   │   └── routers/       # 路由模块
│   │       ├── members.py
│   │       ├── consumptions.py
│   │       ├── categories.py
│   │       ├── products.py
│   │       ├── materials.py
│   │       └── material_records.py
│   └── requirements.txt
├── frontend/               # Vue 3 前端
│   ├── src/
│   │   ├── App.vue
│   │   ├── main.js
│   │   ├── api/          # API调用
│   │   └── views/        # 页面组件
│   └── package.json
└── SPEC.md
```

## 7. 验收标准

1. 后端API能正常启动并响应请求
2. 前端页面能正常加载并显示数据
3. 各模块的增删改查功能正常运行
4. 前后端数据交互正常
5. 界面美观，交互流畅
