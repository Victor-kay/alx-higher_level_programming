#!/usr/bin/python3

def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible. If the object cannot
    have new attributes, it raises a TypeError exception.

    Args:
        obj: The object to which the attribute should be added.
        attr_name: The name of the new attribute.
        attr_value: The value of the new attribute.

    Raises:
        TypeError: If the object cannot have new attributes.

    Example:
        >>> obj = {}
        >>> add_attribute(obj, 'new_attr', 42)
        >>> obj['new_attr']
        42

        >>> obj = 42
        >>> add_attribute(obj, 'new_attr', 'value')
        Traceback (most recent call last):
            ...
        TypeError: can't add new attribute
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    elif hasattr(obj, '__slots__') or isinstance(obj, (int, str, float, list, tuple, set, frozenset)):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
