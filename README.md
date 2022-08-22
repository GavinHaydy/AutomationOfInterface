# 目录结构
``` shell
AutomationOfInterface
├─ data "测试数据包" 
├─ README.md
├─ report  "测试报告"
├─ case #
│    └─ __init__.py
├─ common
│    ├─ __init__.py
│    ├─ database.py "数据库操作"
│    ├─ document_operation.py  "文件操作"
│    ├─ get_keyword.py  "提取器"
│    └─ send_method.py  "requests库封装"
├─ config
│    ├─ __init__.py
│    ├─ env.yaml  "环境配置文件"
│    └─ glo_vars.py     "全局方法"
├─ interface
│    ├─ __init__.py
│    └─ login.py    "token方法，获取一次，自动加入拦截器"
└─ requirements.txt

```
