import datetime # เพิ่มบรรทัดนี้

import config

def say_hello(name):
    now = datetime.datetime.now() # เพิ่มบรรทัดนี้
HEAD
    print(f"Hi, {name} from {config.APP_NAME}!")#เเก้ไขตรงนี้

    print(f"Hello again, {name} from {config.APP_NAME}!")# แก้ไขถูกต้อง
feature-farewell
    print(f"Today is {now.strftime('%Y-%m-%d')}.") # เพิ่มบรรทัดนี้
def greet_user():
    name = input("Please enter your name: ")
    say_hello(name)

if __name__ == "__main__":
    greet_user()

