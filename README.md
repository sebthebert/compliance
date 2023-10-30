# Compliance

Check your hosts against compliancy rules

## Configuration

### Checks

| Name                       | Description              | Example             |
|----------------------------|--------------------------|---------------------|
| Operating System (OS)      |                          |                     |
| `os.distribution_name`     | OS distribution name     | `ubuntu`            |
| `os.distribution_version`  | OS distribution version  | `20.04`             |
| `os.distribution_codename` | OS distribution codename | `focal`             |
| `os.linux_kernel_version`  | OS Linux kernel version  | `5.19.0-46-generic` |

### Comparison Operators

| Name                       | Description                             |
|----------------------------|-----------------------------------------|
| `equal`                    | Check if 2 values are equal             |
| `in`                       | Check if 1 value is in a list of values |
| `version_greater_or_equal` | Check if a version is greater or equal  |

### Supported Distributions

| Distribution  | Versions                   |
|---------------|----------------------------|
| CentOS        | 7                          |
| Debian        | 9, 10, 11                  |
| Fedora        | 31, 32, 33, 34, 35, 36, 37 |
| Ubuntu        | 18.04, 20.04, 22.04, 22.10 |
