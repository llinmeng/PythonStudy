# -*- coding: utf-8 -*-
"""
下载并安装python 2.7 32 bit
下载并安装easy_install windows installer (python 2.7 32bit)
安装 lpthw.web(库)
   windows 命令行：  cd C:\Python27\Scripts\
                    pip install lpthw.web
创建目录 C:\Users\plg519\Maizi\TeachingPython\gotoweb\bin
目录下创建 app.py:
"""

import web

urls = (
  '/', 'index'
)

app = web.application(urls, globals())


class index:
    def GET(self):
        greeting = "Hello World"
        return greeting

if __name__ == "__main__":
    app.run()
"""
Windows cmd 运行：//在下方的Terminal中运行
cd  C:\Users\plg519\Maizi\TeachingPython\gotoweb\bin
C:\python27\python27 app.py

打开浏览器：localhost：8080
"""

