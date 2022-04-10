import os
import shutil
import sys

if __name__ == "__main__":
    count = 0
    new_name = None
    while True:
        print("python作业转换程序")
        print("注意！不要把该程序放在需要进行转换的文件所在文件夹中！")
        print("Ctrl+c中断程序")
        root = input("输入文件夹路径：")
        out = input("输出文件夹路径：")
        if not os.path.exists(out):
            os.mkdir(out)
        file_list = os.listdir(root)

        if count == 0:
            new_name = input("请输入你的学号：") + ".py"
            count += 1
        else:
            j = input("你的学号是" + new_name[:-3] + "，是否正确？[Y/N]")
            if j in ["Y", "y", "Yes", "YES"]:
                pass
            elif j in ["N", "n", "No", "NO"]:
                new_name = input("请重新输入你的学号：") + ".py"
            else:
                print("输入格式错误，三秒后退出程序")
                os.system("@timeout 3")
                break

        for i in range(len(file_list)):
            if file_list[i].endswith(".py"):
                output = out + "\\" + file_list[i][:-3]
                old_path = root + "\\" + file_list[i]
                new_path = output + "\\" + new_name
                # print("old path =", old_path, "new path =", new_path)
                if not os.path.isdir(output):
                    os.mkdir(output)
                shutil.copy(old_path, new_path)
                print(old_path, "-->", new_path)

        print("转换成功！")
        judge = input("是否继续转换？[Y/N]")
        if judge in ["Y", "y", "Yes", "YES"]:
            continue
        elif judge in ["N", "n", "No", "NO"]:
            break
        else:
            print("输入格式错误，三秒后退出程序")
            os.system("@timeout 3")
            break
    os.system("pause")
# E:\Progress\PythonProjects\Python学习\学校\作业与考试\备份\第二章
# E:\Progress\PythonProjects\Python学习\学校\作业与考试\备份\第二章\x
