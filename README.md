# Employee Table Management System

一个基于Django框架开发的员工管理系统，提供完整的员工信息管理、部门管理、任务分配、订单管理等功能。

## 🚀 功能特性

### 核心功能

- **员工管理** - 员工信息的增删改查，包括姓名、年龄、性别、薪资、入职日期等
- **部门管理** - 部门信息管理，支持员工与部门的关联
- **用户认证** - 基于Session的用户登录/登出系统，支持验证码
- **权限控制** - 自定义中间件实现访问权限控制
- **分页功能** - 自定义分页组件，提供良好的数据浏览体验

### 扩展功能

- **电话号码管理** - 电话号码库管理，支持级别和状态分类
- **任务管理** - 任务分配和跟踪系统
- **订单管理** - 订单信息管理和状态跟踪
- **数据图表** - 数据可视化展示
- **密码加密** - 使用MD5加密存储用户密码

## 🛠️ 技术栈

- **后端框架**: Django 3.2.21
- **数据库**: MySQL 
- **前端**: HTML + CSS + Bootstrap + JavaScript
- **Python版本**: Python 3.x
- **数据库驱动**: PyMySQL

## 📋 系统要求

- Python 3.6+
- Django 3.2.21
- MySQL 5.7+
- PyMySQL
- Pillow（用于验证码生成）

## 🔧 安装和配置

### 1. 克隆项目

```bash
git clone https://github.com/which-W/employee_table.git
cd employee_table
```

### 2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
pip install -f requirements.txt
```

### 4. 数据库配置

在 `employee_table/settings.py` 中配置数据库连接：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employee-table',  # 数据库名
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
```

### 5. 创建数据库

```sql
CREATE DATABASE `employee-table` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 6. 数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. 创建超级用户（可选）

```bash
python manage.py createsuperuser
```

### 8. 运行服务器

```bash
python manage.py runserver
```

访问 `http://127.0.0.1:8000` 即可使用系统。

## 📁 项目结构

```
employee_table/
├── app01/                          # 主应用
│   ├── middleware/                 # 中间件
│   │   └── auth.py                # 认证中间件
│   ├── migrations/                 # 数据库迁移文件
│   ├── uels/                      # 工具类
│   │   ├── bootstrap.py           # Bootstrap表单基类
│   │   ├── font_virity.py         # 验证码生成
│   │   ├── model_form.py          # 模型表单
│   │   ├── pageform.py            # 分页组件
│   │   └── pwd_md5.py             # 密码加密
│   ├── view/                      # 视图模块
│   ├── models.py                  # 数据模型
│   └── ...
├── employee_table/                 # 项目配置
│   ├── settings.py                # 项目设置
│   ├── urls.py                    # URL路由
│   └── ...
├── static/                        # 静态文件
├── templates/                     # 模板文件
├── manage.py                      # Django管理脚本
├── requirements.txt               # 依赖包列表
└── README.md                      # 项目说明
```

## 🗄️ 数据模型

### 主要模型

1. **Admin** - 管理员用户
   - username: 用户名
   - password: 密码（MD5加密）

2. **Department** - 部门
   - title: 部门名称

3. **Employee_Table** - 员工信息
   - name: 姓名
   - age: 年龄
   - gender: 性别
   - salary: 薪资
   - date: 入职日期
   - depart: 所属部门（外键）

4. **Telephone_User** - 电话号码管理
   - mobile: 电话号码
   - price: 价格
   - level: 级别（1-4级）
   - status: 状态（已出售/未出售）

5. **Task** - 任务管理
   - level: 任务级别
   - name: 任务名称
   - description: 任务描述
   - user: 接收人（外键到Admin）

6. **Order** - 订单管理
   - user: 处理者（外键到Admin）
   - name: 商品名称
   - price: 价格
   - sale_situation: 销售状态

## 🔗 主要URL路由

| 功能模块 | URL路径             | 描述       |
| -------- | ------------------- | ---------- |
| 部门管理 | `/depart/show`      | 部门列表   |
|          | `/depart/add`       | 添加部门   |
|          | `/depart/<id>/edit` | 编辑部门   |
| 员工管理 | `/user/show`        | 员工列表   |
|          | `/user/add/info`    | 添加员工   |
|          | `/user/<id>/edit`   | 编辑员工   |
| 电话管理 | `/telephone/list`   | 电话列表   |
|          | `/telephone/add`    | 添加电话   |
| 管理员   | `/admin/list`       | 管理员列表 |
|          | `/admin/add`        | 添加管理员 |
| 认证     | `/account/login`    | 用户登录   |
|          | `/account/logout`   | 用户登出   |
| 任务管理 | `/task/list`        | 任务列表   |
|          | `/task/add`         | 添加任务   |
| 订单管理 | `/order/list`       | 订单列表   |
|          | `/order/add`        | 添加订单   |
| 数据图表 | `/chart/list`       | 图表展示   |

## 🔐 安全特性

- **密码加密**: 使用MD5对用户密码进行加密存储
- **Session认证**: 基于Django Session的用户认证
- **访问控制**: 自定义中间件控制页面访问权限
- **验证码**: 登录页面支持图形验证码
- **CSRF保护**: Django内置CSRF防护

## 🎨 自定义组件

### 1. 分页组件 (`pageform.py`)

```python
# 使用示例
page_object = Pagination(request, user_list, page_size=10)
context = {
    'user_list': page_object.queryset,
    'page_str': page_object.html()
}
```

### 2. Bootstrap表单基类 (`bootstrap.py`)

自动为表单字段添加Bootstrap样式类和占位符。

### 3. 验证码生成 (`font_virity.py`)

生成带干扰线和干扰点的图形验证码。

## 🚀 部署说明

### 生产环境配置

1. 修改 `settings.py` 中的 `DEBUG = False`

2. 配置 `ALLOWED_HOSTS`

3. 配置静态文件收集：

   ```bash
   python manage.py collectstatic
   ```

4. 使用 Gunicorn 或其他WSGI服务器部署

### Docker部署（可选）

```dockerfile
FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 🤝 贡献指南

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📝 更新日志

- **v1.0.0** - 初始版本发布
  - 基础员工管理功能
  - 部门管理
  - 用户认证系统

## 📄 许可证

本项目采用 Apache License 2.0 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 创建 [Issue](../../issues)
- 发送邮件至：[wengzu728.love@gmail.com]

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者们！

---

⭐ 如果这个项目对您有帮助，请给它一个星标！
