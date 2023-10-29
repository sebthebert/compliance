"""
Compliance module for comparison
"""
from pkg_resources import parse_version

def compare_equal(value, desired_value):
    """
    Function returning True if the 2 values are equal
    """
    if value == desired_value:
        return True
    return False

def compare_in(value, desired_values):
    """
    Function returning True if 'value' is in 'desired_value' list
    """
    if value in desired_values:
        return True
    return False

def compare_version_gte(value, desired_value):
    """
    Function returning True if 'value' is greater or equal to 'desired_value'
    """
    if parse_version(str(value)) >= parse_version(str(desired_value)):
        return True
    return False

compare_function = {
    'equal': compare_equal,
    'in': compare_in,
    'version_greater_or_equal': compare_version_gte
}
