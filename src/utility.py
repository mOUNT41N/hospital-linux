from flask import session, redirect, request
import functools
import hashlib

# 登录装饰器
def require_login(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if "username" not in session:
            return redirect("/login/")
        return func(*args, **kwargs)
    return wrapper


def md5_hash(string):
    m = hashlib.md5()
    m.update(bytes(string, "utf-8"))
    return m.hexdigest()

def urlencode(arg_dict):
    return request.url.encode("")