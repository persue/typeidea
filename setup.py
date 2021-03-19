# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='typeidea',
    version='${version}',
    description='Blog System base on Django',
    author='robin',
    author_email='robin@hotmail.com',
    url='https://www.robin.com',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    #package_data={'':[
    #    'themes/*/*/*/*',
    #]},
    include_package_data=True,
    install_requires=[
        'django~=1.11',
        'gunicorn==19.8.1',
        'xadmin==0.6.1 ',
        'supervisor==4.0.0dev0',
        'mysqlclient==1.4.6',
        'django-ckeditor==5.4.0',
        'django-rest-framework==0.1.0',
        'django-redis==4.9.0',
        'django-autocomplete-light==3.2.10',
        'mistune==0.8.4',
        'Pillow==8.1.1',
        'coreapi==2.3.3',
        'hiredis==0.2.0',
        # debug
        'django-debug-toolbar==1.9.1',
    ],
    extras_require={'ipython': ['ipython==6.2.1']},
    scripts=[
        'typeidea/manage.py',
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage:main',
        ]
    },
    classifiers=[
        #软件成熟度 3-Alpha，4-Beta，5-Production/stable
        'Development Status :: 3 - Alpha',

        #指明项目受众
        'Intended Audience :: Developers',
        'Topic :: Blog :: Django Blog',

        #选择项目许可证
        'License :: OSI Approved :: MIT License',

        #指定项目需要使用的python版本
        'Programming Language :: Python :: 3.6',
    ],
)