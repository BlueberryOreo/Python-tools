import curses
import os
from pypinyin import lazy_pinyin
from trie import Trie
import log

KEY_BACKSPACE = 8
START_ICON = ">"
K = 15
TMP_BUFF = ""

stdscr = curses.initscr()
stdscr.keypad(True)
# curses.cbreak(True)

upperwin = stdscr.subwin(0, 0)
lowerwin = stdscr.subwin(2, 0)
testwin = stdscr.subwin(2 + K, 0)

tree = Trie()


def get_dir(path: str):
    if not os.path.exists(path):
        return
    dirs = os.listdir(path)
    tree.clear()

    for d in dirs:
        if d != lazy_pinyin(d)[0]:
            # 中文
            pinyin = "".join(lazy_pinyin(d))
            tree.insert(pinyin, d)
        else:
            # 英文
            target = d
            d = d.lower()
            tree.insert(d, target)


def back_space(buff):
    buff = buff[:-1]
    now = upperwin.getyx()[1]
    upperwin.addch(" ")
    upperwin.move(upperwin.getyx()[0], now)
    upperwin.refresh()
    return buff


def tab(buff, tmp):
    upperwin.clear()
    upperwin.addstr(START_ICON)
    buff = "/".join("".join(buff).split("/")[:-1] + [tmp])
    upperwin.addstr(buff)
    upperwin.refresh()
    return list(buff)


def show(buff):
    tmp = "".join(buff).split("/")[-1].lower()
    test_show(len(tmp))
    sub_tree = tree.get_sub_tree(tmp)
    lowerwin.clear()
    lowerwin.addstr("\n".join(sub_tree[:K]))
    lowerwin.refresh()
    return sub_tree


def test_show(*info):
    testwin.clear()
    testwin.addstr(str(info))
    testwin.refresh()


def main():
    is_exit = False
    global TMP_BUFF
    while True:
        buff = []
        tmp_sub = []
        upperwin.addstr(START_ICON)
        while True:

            # testwin.clear()
            # testwin.addstr("".join(buff))
            # testwin.refresh()

            char = upperwin.getch()

            if char == ord("\n"):
                # 按下回车的操作：打开文件/文件夹
                path = "".join(buff)
                if path == "exit":
                    is_exit = True
                elif os.path.exists(path):
                    os.startfile(path)
                    # log.write("Open directory/file: " + path)
                    # log.new_line()
                else:
                    test_show("Directory/File not found!")
                    log.write("Directory/File not found!" + " path: " + path)
                    log.new_line()
                break

            if char == KEY_BACKSPACE:
                # 按下退格的操作：退格
                if len(buff) != 0:
                    buff = back_space(buff)
                    tmp_sub = show(buff)
                else:
                    upperwin.move(upperwin.getyx()[0], upperwin.getyx()[1] + 1)
                continue

            if char == ord("\t"):
                # 按下tab的操作：自动补全
                if not tmp_sub:
                    continue
                buff = tab(buff, tmp_sub[0])
                front = tmp_sub[0]
                del tmp_sub[0]
                tmp_sub.append(front)
                continue

            buff.append(chr(char))
            TMP_BUFF = "".join(buff)
            upperwin.refresh()

            if char == ord("/"):
                # 按下/的操作
                # test_show("".join(buff))
                get_dir("".join(buff))

            tmp_sub = show(buff)

            # test_show("".join(buff))

        upperwin.clear()
        upperwin.refresh()
        if is_exit:
            break


if __name__ == "__main__":
    log.write("Progress start.")
    try:
        main()
    except Exception as e:
        # info = str(stdscr.getyx()[0]) + " " + str(stdscr.getyx()[1])
        log.error(e, "y: " + str(stdscr.getyx()[0]), "x: " + str(stdscr.getyx()[1]), "buff: " + TMP_BUFF)
    log.write("Progress terminated.")
    log.divide()
