import json
import hashlib

def login(name, pw):
    try:
        handle = open('test.txt', 'r')
    except FileNotFoundError:
        print("User name not exist")
        return False
    else:
        js = handle.read()
        dic = json.loads(js)
        handle.close()
    hashpw = hashlib.md5()
    hashpw.update(pw.encode(encoding='utf-8'))

    if name == "" or pw == "":
        print("Enter your email or mobile phone number!")
    elif name not in dic.keys():
        print("User name not exist!")
    elif name in dic.keys() and dic[name][1] == 0:
        print("%sThis account is locked! Please contact administrator" % name)
    elif name in dic.keys() and dic[name][1] != 0:
        if hashpw.hexdigest() != dic[name][0]:
            dic[name][1] = dic[name][1] - 1
            if dic[name][1] == 0:
                print("%sThis account is locked!Please contact administrator" % name)
            else:
                print("Password is incorrect!You still have %s chance" % (dic[name][1]))
        else:
            print("%s Log in successful!" % name)
            return True

while True:
    name = input("name:")
    pw = input("password:")

    check = login(name, pw)
    if check:
        break