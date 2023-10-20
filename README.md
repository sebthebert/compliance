# Compliance

Check your hosts against compliancy rules

## Configuration

### Checks

| Name                       | Description              | Example  |
|----------------------------|--------------------------|----------|
| Operating System (OS)      | | |
| `os.distribution_name`'    | OS distribution name     | `ubuntu` |
| `os.distribution_version`  | OS distribution version  | `20.04`  |      
| `os.distribution_codename` | OS distribution codename | `focal`  |

### Comparison Operators

| Name                       | Description                             |
|----------------------------|-----------------------------------------|
| `equal`                    | Check if 2 values are equal             |
| `in`                       | Check if 1 value is in a list of values |
| `version_greater_or_equal` | Check if a version is greater or equal  |

