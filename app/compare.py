from pkg_resources import parse_version

def compare_equal(value, desired_value):
    if value == desired_value:
        return True
    return False

def compare_in(value, desired_value):
    if value in desired_value:
        return True
    return False

def compare_version_gte(value, desired_value):
    if parse_version(str(value)) >= parse_version(str(desired_value)):
        return True
    return False

compare_function = {
    'equal': compare_equal,
    'in': compare_in,
    'version_greater_or_equal': compare_version_gte
}
