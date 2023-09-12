#!/usr/bin/python3

"""module contains  function"""


def add_new_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible; raises a TypeError
    exception if the object cannot have new attributes.

    Args:
        obj: The object to which the attribute should be added.
        attr_name: The name of the new attribute.
        attr_value: The value of the new attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
