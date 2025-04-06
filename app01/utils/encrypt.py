'''
密码加密
'''
from django.conf import settings
import hashlib

def md5(data_string):
    # 可以在md5中调用django中setting里的自带加密盐
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()