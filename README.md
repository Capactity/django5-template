# django5 模版项目

### 项目结构

```
django5-template-2024autumn
|  .env                              <-- 项目环境变量文件
├─ .vscode                           <-- VSCode配置目录
│  └─ settings.json
└─ requirements.txt                  <-- Django项目依赖包
├─ db.sqlite3                        <-- 临时SQLite数据库文件
├─ manage.py                         <-- 项目启动文件
├─ mysite                            <-- 项目主目录
│  ├─ __init__.py
│  ├─ __pycache__
│  │  ├─ __init__.cpython-312.pyc
│  │  ├─ settings.cpython-312.pyc
│  │  ├─ urls.cpython-312.pyc
│  │  └─ wsgi.cpython-312.pyc
│  ├─ asgi.py
│  ├─ settings.py                    <-- 项目配置文件
│  ├─ urls.py                        <-- 项目URL配置文件
│  └─ wsgi.py
├─ project-structure.txt
└─ venv                             <-- 虚拟环境目录
   └─ venv-3.12.4
      ├─ bin
      ├─ include
      │  └─ python3.12
      ├─ lib
      └─ pyvenv.cfg

```

### 常用命令

```shell
# 创建虚拟环境
python -m venv venv
# 激活虚拟环境
source venv/bin/activate
# 安装依赖包
pip install -r requirements.txt
# 更新依赖
pip freeze > requirements.txt
# 运行开发服务器
python manage.py runserver

```
