#!/usr/bin/python3

class LockedClass:
    """LockedClass allows creating instances with a 'first_name' attribute.
    It prevents the dynamic creation of new instance attributes.
    """

    __slots__ = ("first_name",)

    def __init__(self, first_name):
        self.first_name = first_name
