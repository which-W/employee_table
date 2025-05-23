import hashlib
from django.conf import settings


def md5_pwd(pwd):
    """
    md5加密
    :param pwd:
    :return:
    """
    md5 = hashlib.md5(settings.SECRET_KEY.encode("utf-8"))
    md5.update(pwd.encode("utf-8"))
    return md5.hexdigest()
