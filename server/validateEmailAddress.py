import re


def validateEmailAddress(String_url):
    c = re.compile(r'^\w+@(\w+\.)+(com|cn|net)$')
    s = c.search(String_url)
    if s:
        print("邮箱格式正确")
        return True
    else:
        print('邮箱格式不正确')
        return False
