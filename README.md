
[![OSCS Status](https://www.oscs1024.com/platform/badge/AutomationOfInterface.svg?size=small)](https://www.murphysec.com/accept?code=66b87a66bce3eb33eed6d0ac6683bf2f&type=1&from=2)
# 注意事项
```shell
1、本版本更新于2024年8月 开发的python版本为3.12 低版本可能会出现问题
2、推荐使用venv环境，避免依赖包版本冲突
```
# 操作说明
```shell
1、安装依赖
pip install -r requirements.txt
2、执行测试
python run.py
```

# 目录结构
``` shell
AutomationOfInterface
├─ data "测试数据包" 
├─ README.md
├─ report  "测试报告"
├─ case # 测试用例
│    └─ __init__.py
├─ common # 公共方法
│    ├─ __init__.py
│    ├─ database.py "数据库操作"
│    ├─ document_operation.py  "文件操作"
│    ├─ get_keyword.py  "提取器"
│    └─ send_method.py  "requests库封装"
├─ config # 配置文件
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
"login.py为获取token的方法  框架加入了拦截器，自动调用此方法"
"如果接口存在验签 可将验签方法封装到login.py中  在拦截器中调用 拦截器为send_method的Foo类 "
"因为验签方式存在差异 后期会尽量完善拦截器"
```