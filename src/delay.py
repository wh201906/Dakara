from random import randint
from time import sleep

print("Random delay starts")
sleep(randint(10, 5 * 60))
print("Random delay ends")