import curses
from curses import wrapper
import queue
import time

bhool_bhulaiya = [
    ["|", "|", "|", "|", "|", "S", "|", "|", "|"],
    ["|", " ", " ", " ", "|", " ", " ", "|", "|"],
    ["|", " ", " ", " ", "|", " ", " ", " ", "|"],
    ["|", " ", "|", " ", "|", " ", "|", " ", "|"],
    ["|", " ", "|", " ", " ", " ", "|", " ", "|"],
    ["|", " ", "|", " ", "|", " ", "|", " ", "|"],
    ["|", " ", "|", " ", "|", " ", "|", " ", "|"],
    ["|", " ", "|", " ", "|", " ", "|", " ", "|"],
    ["|", "E", "|", "|", "|", "|", "|", "|", "|"]
]
def printing_bhool_bhulaiya(bhool_bhulaiya, stdscr, path=[]):
    white= curses.color_pair(1)
    red= curses.color_pair(2)

    for i, row in enumerate(bhool_bhulaiya):
        for j, value in enumerate(row):
            if (i, j) in path:
               stdscr.addstr(i, j*2,"X", red) 
            else:
                stdscr.addstr(i, j*2,value, white)

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

        stdscr.clear()
        printing_bhool_bhulaiya(bhool_bhulaiya, stdscr, path)
        stdscr.refresh()
        time.sleep(0.3)   # pause 0.3 seconds
        if bhool_bhulaiya[row][col] == end:
            return path
        
        neighbors = find_neighbors(bhool_bhulaiya, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            r, c = neighbor
            if bhool_bhulaiya[r][c] == "|":
                continue
            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor) 


def find_neighbors(bhool_bhulaiya, row, col):
        neighbors = []
        if row > 0 : #up
            neighbors.append((row-1, col))
        if row+1 < len(bhool_bhulaiya): #down
            neighbors.append((row+1, col))
        if col > 0 : #left
            neighbors.append((row, col-1))
        if col+1 < len(bhool_bhulaiya): #right
            neighbors.append((row, col+1))

        return neighbors        

    
def main (stdscr):
    curses.init_pair (1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair (2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    find_path(bhool_bhulaiya, stdscr)
    stdscr.getch()


wrapper(main)
