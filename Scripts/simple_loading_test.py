import time

while True:
    print("\033[H\033[2J", end="")
    print("--")
    time.sleep(.01)
    print("\033[H\033[2J", end="")
    print(" \\")
    time.sleep(.01)
    print("\033[H\033[2J", end="")
    print("|")
    time.sleep(.01)
    print("\033[H\033[2J", end="")
    print('/')
    time.sleep(.01)
    print("\033[H\033[2J", end="")
