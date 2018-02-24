# http://tinyurl.com/jmak8tr

import time

qs = ["what is your name? ",
      "what is your favorite color? ",
      "what is your quest? "]

n = 0

while True:
    print("--------------")
    print("Type q to quit ")
    print("--------------")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3

