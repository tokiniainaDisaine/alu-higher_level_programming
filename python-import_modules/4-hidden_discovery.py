#!/usr/bin/python3

if __name__ == "__main__":
    from hidden_4 import * as hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
