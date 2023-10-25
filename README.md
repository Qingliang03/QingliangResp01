# **Wechat-Message-To-My-Heart**

# 前言
Hello there.
This is a small gift for Mrs.Zhao.
It's just for fun. 
Be Happy.

# 功能
每日微信公众号消息定向推送。
使用预设的模板向心上人表达心意。
是否会小鹿乱撞呢？

# 使用
使用步骤目前暂时还懒得写，测试公众号申请及模板使用，可以参考下列链接（或自行百度）。除了代码不一样，其他都是一样的。
**https://zhuanlan.zhihu.com/p/558254580**
关键注释已在main.py中注明。

# 模板内容
```
今天是{{date.DATA}} 
城市：{{city.DATA}} 
天气：{{weather.DATA}} 
最低气温: {{min_temperature.DATA}} 
最高气温: {{max_temperature.DATA}} 
今天是我们恋爱的第{{love_day.DATA}}天 
notice：{{notice.DATA}}
```

# Workflows
这部分的配置网上找的都不太清楚，贴一下我自己的。
因为github的workflow会排队，所以时间都不太一致，大致在七点多左右，时区设置了上海不管用我也不知道为什么。
如果自己改时间的话，一定要避开8点、0点等时间点，很拥挤，已亲测。
```
name: wechat blog auto

on: # workflow_dispatch
  schedule:
    - cron: '2 23 * * *'

jobs:
  build-linux:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 5

    steps:
    - uses: actions/checkout@v3
    - uses: szenius/set-timezone@v1.0
      with:
         timezoneLinux: "Asia/Shanghai"
    
    - name: Set up Python 3.7 # 安装环境
      uses: actions/setup-python@v3
      with:
        python-version: '3.7'
      #  cache: 'pip' # 设置缓存
        
    - name: Install dependencies # 安装依赖
      run: pip install requests
      
    - name: Test # 执行
      run: python main.py
```
