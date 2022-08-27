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

```shell
"第一次使用需要修改env.yaml中的url"
"login.py为或去token的方法  框架加入了拦截器，自动调用此方法"
"如果接口存在验签 可将验签方法封装到login.py中  在拦截器中调用 拦截器为send_method的Foo类 "
"因为验签方式存在差异 后期会尽量完善拦截器"
```