import os
from pathlib import Path


def test():
    base = Path(__file__).resolve().parent

    print(base)

test()