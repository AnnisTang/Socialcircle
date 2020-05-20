import json
import hashlib

def registor(name, pw):
    try:
        handle = open('test.txt', 'r')
    except FileNotFoundError:
        dic = {}
    else:
        js = handle.read()
        dic = json.loads(js)
        handle.close()
    if name in dic.keys():
        print("This user name is exist")
        return False
    if len(pw) < 6:
        print("Passwords must be at least 6 characters")
        return False
    hashpw = hashlib.md5()
    hashpw.update(pw.encode(encoding='utf-8'))
    dic[name] = [hashpw.hexdigest(), 3]
    js = json.dumps(dic)
    file = open('test.txt', 'w')
    file.write(js)
    file.close()
    print("registration success!!!")
    return True

while True:
    name = input("name:")
    pw = input("password:")

    registor(name, pw)