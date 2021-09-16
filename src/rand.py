from random import randint

if randint(1, 4) == 1:
    print("Continue to run")
    exit(0)
else:
    print("Skipped")
    exit(1)