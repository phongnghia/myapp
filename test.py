import os
import random
from pathlib import Path


def test():
    id = set(range(10000000, 100000000))
    new_id = random.choice(tuple(id))

    print(new_id)

    return new_id


test()
