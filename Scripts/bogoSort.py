import random
import time
import sys

 #do not change nums

def bogo(sort_amount, delay):
    nums = list(range(1, sort_amount+1))
    while True:
        bogo_rand_list = random.sample(nums, sort_amount)
        print(bogo_rand_list)
        if bogo_rand_list == nums:
            print("successfully bogo'd it")
            print('imput anything in terminal to exit')
            input()
            sys.exit()
        time.sleep(delay)

print('how many items to sort?')
sort_amount = int(input())
print('how long of a delay in between?')
delay = input()
bogo(sort_amount, delay)
