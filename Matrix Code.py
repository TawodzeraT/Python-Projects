import os
import random
import time
import msvcrt

# Enable ANSI color codes on Windows
if os.name == "nt":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

GREEN = "\033[92m"       # normal green
BRIGHT_GREEN = "\033[92;1m"  # bright/bold green
RESET = "\033[0m"

def clear():
    os.system("cls")

def matrix_rain():
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    chars = "01"

    # track where drops are in each column
    drops = [random.randint(0, height) for _ in range(width)]

    print("Press 'X' to stop.\n")

    while True:
        # check keypress
        if msvcrt.kbhit():
            key = msvcrt.getch().decode("utf-8").lower()
            if key == "x":
                break

        line = ""
        for i in range(width):
            if drops[i] == 0:
                # randomly start a new drop
                if random.random() > 0.98:
                    drops[i] = 1
                line += " "
            elif drops[i] < height:
                # bright green leading digit
                if drops[i] == 1:
                    line += BRIGHT_GREEN + random.choice(chars) + RESET
                else:
                    line += GREEN + random.choice(chars) + RESET
                drops[i] += 1
            else:
                drops[i] = 0
                line += " "

        print(line)
        time.sleep(0.05)

if __name__ == "__main__":
    clear()
    matrix_rain()




