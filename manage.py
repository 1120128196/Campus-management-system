#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.
控制台输入python manage.py startapp (项目名字)   来生成项目
"""
import os
import sys
# 项目管理文件 运行启动等

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
