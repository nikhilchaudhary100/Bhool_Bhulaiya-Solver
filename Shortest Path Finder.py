import curses
from curses import wrapper
import queue
import time

bhool_bhulaiya = [
    ["|", "|", "|", "|", "|", "S", "|", "|", "|", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", "|", "|", "|", "|", "|", "|", "|", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", "|", " ", "|"],
    ["|", " ", "|", "|", "|", "|", " ", "|", " ", "|"],
    ["|", " ", "|", " ", " ", " ", " ", "|", " ", "|"],
    ["|", " ", "|", " ", "|", "|", " ", "|", " ", "|"],
    ["|", " ", "|", " ", "|", " ", " ", " ", " ", "|"],
    ["|", " ", "|", " ", "|", " ", "|", "|", "|", "|"],
    ["|", "|", "|", "|", "|", "|", "|", "E", "|", "|"]
]
def printing_bhool_bhulaiya(bhool_bhulaiya, stdscr, path=[]):
    white= curses.color_pair(1)
    red= curses.color_pair(2)

    for i, row in enumerate(bhool_bhulaiya):
        for j, value in enumerate(row):
            stdscr.addstr(i,j,value, white)

def find_start(bhool_bhulaiya, start):
    for i, row in enumerate(bhool_bhulaiya):
        for j, value in enumerate(row):
            if value == start:
                return i,j
    return None

def find_path(bhool_bhulaiya, stdscr):
    start = "S"
    end = "E"
    start_pos = find_start(bhool_bhulaiya, start)


    q= queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()
    while not q.empty():
        current_pos, path = q.get()
        row, col =current_pos

        if bhool_bhulaiya[row][col] == end:
            return path
    
def main (stdscr):
    curses.init_pair (1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair (1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.clear()
    stdscr.addstr(0 , 0)
    stdscr.refresh()
    stdscr.getch()


wrapper(main)