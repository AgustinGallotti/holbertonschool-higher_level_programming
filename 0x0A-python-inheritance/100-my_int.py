#!/usr/bin/python3
"""function to reverse == and !="""


class MyInt(int):
    """new class"""

    def __init__(self, myint):
        """engine"""
        self.myint = myint

    def __eq__(a1, b2):
        """method that compare"""
        return a1.myint != b2

    def __ne__(a1, b2):
        """method that distint"""
        return a1.myint == b2
