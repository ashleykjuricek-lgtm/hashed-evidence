#!/usr/bin/env python3
"""Terminal TUI Calculator using curses."""

import curses
import math

BUTTONS = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "^", "="],
]

KEY_MAP = {
    "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
    "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
    "+": "+", "-": "-", "*": "*", "/": "/",
    ".": ".", "(": "(", ")": ")",
    "^": "^", "c": "C", "C": "C",
}


def safe_eval(expr: str) -> str:
    """Evaluate a math expression safely."""
    expr = expr.replace("^", "**")
    allowed = set("0123456789.+-*/() ")
    cleaned = expr.replace("**", "")
    if not all(ch in allowed for ch in cleaned):
        return "Error"
    try:
        result = eval(expr, {"__builtins__": {}}, {"math": math})
        if isinstance(result, float) and result == int(result) and abs(result) < 1e15:
            return str(int(result))
        if isinstance(result, float):
            return f"{result:.10g}"
        return str(result)
    except Exception:
        return "Error"


def draw_box(win, y, x, h, w, label="", selected=False):
    attr = curses.A_REVERSE if selected else curses.A_NORMAL
    for row in range(h):
        for col in range(w):
            ch = " "
            if row == 0 or row == h - 1:
                ch = "-"
            if col == 0 or col == w - 1:
                ch = "|"
            if (row == 0 or row == h - 1) and (col == 0 or col == w - 1):
                ch = "+"
            try:
                win.addch(y + row, x + col, ch, attr)
            except curses.error:
                pass
    if label:
        lx = x + (w - len(label)) // 2
        ly = y + h // 2
        try:
            win.addstr(ly, lx, label, attr | curses.A_BOLD)
        except curses.error:
            pass


def main(stdscr):
    curses.curs_set(0)
    curses.use_default_colors()
    try:
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    except curses.error:
        pass

    expression = ""
    result = ""
    sel_row, sel_col = 0, 0

    while True:
        stdscr.erase()
        max_y, max_x = stdscr.getmaxyx()

        btn_w = 10
        btn_h = 3
        grid_w = btn_w * 4
        grid_h = btn_h * 5
        total_h = grid_h + 5
        start_x = max(0, (max_x - grid_w) // 2)
        start_y = max(0, (max_y - total_h) // 2)

        # Title
        title = " Calculator "
        tx = max(0, (max_x - len(title)) // 2)
        try:
            stdscr.addstr(start_y, tx, title, curses.A_BOLD)
        except curses.error:
            pass

        # Display
        disp_y = start_y + 1
        display_text = expression if expression else "0"
        if result:
            display_text = result
        disp = display_text[-grid_w + 2:].rjust(grid_w - 2)
        try:
            stdscr.addstr(disp_y, start_x, "+" + "-" * (grid_w - 2) + "+")
            stdscr.addstr(disp_y + 1, start_x, "|" + disp + "|", curses.A_BOLD)
            stdscr.addstr(disp_y + 2, start_x, "+" + "-" * (grid_w - 2) + "+")
        except curses.error:
            pass

        # Show expression below display when showing result
        if result and expression:
            expr_line = expression[-(grid_w - 2):]
            try:
                stdscr.addstr(disp_y + 3, start_x + 1, expr_line.rjust(grid_w - 2), curses.A_DIM)
            except curses.error:
                pass

        # Buttons
        btn_start_y = disp_y + 4
        for r, row in enumerate(BUTTONS):
            for c, label in enumerate(row):
                selected = (r == sel_row and c == sel_col)
                draw_box(stdscr, btn_start_y + r * btn_h, start_x + c * btn_w, btn_h, btn_w, label, selected)

        # Help
        help_y = btn_start_y + len(BUTTONS) * btn_h + 1
        help_text = "Arrow keys: move | Enter: press | Type digits/ops | q: quit"
        hx = max(0, (max_x - len(help_text)) // 2)
        try:
            stdscr.addstr(help_y, hx, help_text, curses.A_DIM)
        except curses.error:
            pass

        stdscr.refresh()

        key = stdscr.getch()

        if key == ord("q") or key == 27:  # q or Escape
            break
        elif key == curses.KEY_UP:
            sel_row = (sel_row - 1) % len(BUTTONS)
        elif key == curses.KEY_DOWN:
            sel_row = (sel_row + 1) % len(BUTTONS)
        elif key == curses.KEY_LEFT:
            sel_col = (sel_col - 1) % 4
        elif key == curses.KEY_RIGHT:
            sel_col = (sel_col + 1) % 4
        elif key in (curses.KEY_ENTER, 10, 13):
            btn = BUTTONS[sel_row][sel_col]
            if btn == "=":
                result = safe_eval(expression)
            elif btn == "C":
                expression = ""
                result = ""
            else:
                if result:
                    if btn in "+-*/^":
                        expression = result + btn
                    else:
                        expression = btn
                    result = ""
                else:
                    expression += btn
        elif key == 127 or key == curses.KEY_BACKSPACE:
            if result:
                result = ""
            elif expression:
                expression = expression[:-1]
        elif key == ord("\n") or key == ord("="):
            result = safe_eval(expression)
        else:
            ch = chr(key) if 0 <= key < 256 else ""
            if ch in KEY_MAP:
                btn = KEY_MAP[ch]
                if btn == "C":
                    expression = ""
                    result = ""
                elif btn == "=":
                    result = safe_eval(expression)
                else:
                    if result:
                        if btn in "+-*/^":
                            expression = result + btn
                        else:
                            expression = btn
                        result = ""
                    else:
                        expression += btn


if __name__ == "__main__":
    curses.wrapper(main)
