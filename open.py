import curses
import os
from pypinyin import lazy_pinyin
from trie import Trie
import time

KEY_BACKSPACE = 8
START_ICON = ">"

stdscr = curses.initscr()
stdscr.keypad(True)
# curses.cbreak(True)

upperwin = stdscr.subwin(0, 0)
lowerwin = stdscr.subwin(2, 0)

tree = Trie()


def get_dir(path: str):
    dirs = os.listdir(path)
    tree.clear()

    for d in dirs:
        if d != lazy_pinyin(d)[0]:
            # 中文
            pinyin = "".join(lazy_pinyin(d))
            tree.insert(pinyin, d)
        else:
            # 英文
            tree.insert(d)


def back_space(buff):
    buff = buff[:-1]
    now = upperwin.getyx()[1]
    upperwin.addch(" ")
    upperwin.move(upperwin.getyx()[0], now)
    upperwin.refresh()
    return buff


def tab(buff):
    upperwin.clear()
    upperwin.addstr(START_ICON)
    upperwin.addstr("".join(buff))
    upperwin.refresh()


def main():
    is_exit = False
    while True:
        buff = []
        upperwin.addstr(START_ICON)
        while True:

            lowerwin.clear()
            lowerwin.addstr("".join(buff))
            lowerwin.refresh()

            char = upperwin.getch()

            if char == ord("\n"):
                # 按下回车的操作
                if "".join(buff) == "exit":
                    is_exit = True
                break

            if char == KEY_BACKSPACE:
                # 按下退格的操作
                if len(buff) != 0:
                    buff = back_space(buff)
                else:
                    upperwin.move(upperwin.getyx()[0], upperwin.getyx()[1] + 1)
                continue

            if char == ord("\t"):
                # 按下tab的操作
                tab(buff)
                continue

            if char == ord("/"):
                # 按下/的操作
                get_dir("".join(buff))

            buff.append(chr(char))
            upperwin.refresh()

        upperwin.clear()
        upperwin.refresh()
        if is_exit:
            break


if __name__ == "__main__":
    main()
