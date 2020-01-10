
'''
1. 创建函数模块（模块就是文件）

2. 创建setup.py文件

3. 将函数模块和setup.py文件放到一个文件夹中

4. 构建发布（发布就是一个文件集合，sdist = Source Distribution）

   python setup.py sdist

5. 将发布安装到python本地副本中				

   python setup.py install

6. 给命令行上传工具提供pypi账号和密码

   python setup.py register

6. 上传到pypi				

   python setup.py sdist upload


7. setup.py的代码如下

from distutils.core import setup

setup(
    name = 'fcq_nester',
    version = '1.1.0',
    py_modules = ['fcq_nester'],
    author = 'hbzgfcq',
    author_email = 'hbzgfcq@163.com',
    url = 'http://www.zgzjzx.com',
    description = 'A simple printer of nester lists',
    )
'''