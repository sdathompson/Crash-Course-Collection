import random

def coin_flip():
    heads_tails = random.getrandbits(1)

    if heads_tails == 0:
        print("Heads")
    else:
        print("Tails")

coin_flip()