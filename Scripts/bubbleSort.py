import random
import time

def BubbleSort(SortItems, Delay):
    SortedList = list(range(1, SortItems + 1)) #generate the sorted list
    RandomList = random.sample(SortedList, SortItems) #randomise that list
    ListLength = len(RandomList)
    ListNum = 0
    while True:
        if ListNum >= ListLength - 1:
            ListNum = 0
        elif RandomList[ListNum] > RandomList[ListNum + 1]:
            RandomList[ListNum], RandomList[ListNum + 1] = RandomList[ListNum + 1], RandomList[ListNum]
            ListNum+=1
            print(RandomList)
        elif RandomList[ListNum] < RandomList[ListNum + 1]:
            ListNum+=1
        if RandomList == SortedList:
            print('sorted')
            print(RandomList)
            exit()
        time.sleep(Delay)

# ---------------------------------------
print('how many items to sort?')
SortItems = int(input())
print('how long of a delay in between actions? (in seconds)')
Delay = float(input())
BubbleSort(SortItems, Delay)
