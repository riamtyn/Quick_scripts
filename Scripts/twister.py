import random

colors = ["red", "yellow", "blue", "green"]
limbs = ["left hand", "right hand", "left leg", "right leg"]
extras = ["fold mat edges", "spinner's choice"]

def spin():
    spinResult = random.randint(0,18)
    limbResult = random.randint(0,3)
    colorResult = random.randint(0,3)

    if spinResult == 0:
        print(extras[0])
    elif spinResult == 1:
        print(extras[1])
    elif spinResult in range(2,19):
        print(limbs[limbResult], colors[colorResult])
    
print("\nfor when you want to play twister \n \
    but their spinners are way to low quality: \n \
        just input anything to spin again!")

while True:
    spin()
    input()
