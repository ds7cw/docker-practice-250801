import datetime

if __name__ == "__main__":
    print("Hello World!")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current time & date: {}".format(now))
