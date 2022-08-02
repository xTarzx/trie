#!/usr/bin/env python3

import sys
import curses

from main import Trie


def main(stdscr):

    stdscr.clear()
    stdscr.refresh()

    term = ""

    while True:

        stdscr.erase()
        stdscr.addstr(term)
        stdscr.addstr("\n\n")

        words = trie.autocomplete(term)

        rows, cols = stdscr.getmaxyx()
        m = min(len(words), rows-5)
        for word in words[:m]:
            stdscr.addstr(f"{word}\n")

        stdscr.move(0, len(term))
        key = stdscr.getch()
        isenter = key == curses.KEY_ENTER or key == 13 or key == 10
        if isenter:
            break

        elif key == curses.KEY_BACKSPACE:
            term = term[:-1]

        elif (ord("a") <= key <= ord("z")) or (ord("A") <= key <= ord("Z")):
            term += chr(key)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("please provide a word list")
        exit()

    with open(sys.argv[1], "r") as f:
        words = f.read().split("\n")

    trie = Trie()

    for word in words:
        trie.insert(word)

    curses.wrapper(main)
