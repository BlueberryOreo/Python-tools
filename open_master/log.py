import os
import datetime

log_file_path = "./log"

if not os.path.exists(log_file_path):
    file = open(log_file_path, "wt", encoding="utf-8")
else:
    file = open(log_file_path, "a", encoding="utf-8")


def get_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def write(info):
    time = get_time()
    file.write(time + " " + info + "\n")


def error(exception, *info):
    time = get_time()
    tp = type(exception)
    file.write(time + " ERROR\n" + str(tp) + "\n" + str(exception) + "\n")
    file.write("infos:\n")
    for i in info:
        file.write(i + "\n")


def divide():
    file.write("=" * 90 + "\n")


def new_line():
    file.write("\n")
