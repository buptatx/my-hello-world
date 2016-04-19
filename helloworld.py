#!/usr/bin/env python
#coding=utf-8

"""
this module is using for echo helloworld
"""

import sys

def echo_hello(user):
    """
    print function
    """
    print "{u} says: helloworld~".format(u=user)


def main():
    """
    entrance for this module
    """
    if len(sys.argv) < 2:
        print "usage:" \
            "python ./helloworld.py username"
        return -1

    username = sys.argv[1]
    echo_hello(username)


if __name__ == "__main__":
    sys.exit(main())
