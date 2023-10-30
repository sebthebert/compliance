"""
Compliance Plugin for Operating System information.
"""
import os
import re

PARSERS = {
    '/etc/lsb-release': {
        'distribution': re.compile(r'^DISTRIB_ID=(.+)'),
        'version':      re.compile(r'^DISTRIB_RELEASE=(.+)'),
        'codename':     re.compile(r'^DISTRIB_CODENAME=(.+)') 
    },
    '/etc/os-release': {
        'distribution': re.compile(r'^ID="?(.*?)"?$'),
        'version':      re.compile(r'^VERSION_ID="?([^"]+?)"?$'),
        'codename':     re.compile(r'^VERSION_CODENAME="?([^"]+?)"?$')
    }
}

def distribution_name() -> str:
    """
    Function returning OS distribution name in lower string (ex.: 'ubuntu')
    """
    for path, regex in PARSERS.items():
        if os.path.exists(path):
            with open(path, encoding='utf-8') as f:
                for line in f.readlines():
                    match = re.match(regex['distribution'], line)
                    if match:
                        return match.group(1).lower()
    return 'n/a'

def distribution_version() -> str:
    """
    Function returning OS distribution version in lower string (ex.: '20.04')
    """
    for path, regex in PARSERS.items():
        if os.path.exists(path):
            with open(path, encoding='utf-8') as f:
                for line in f.readlines():
                    match = re.match(regex['version'], line)
                    if match:
                        return match.group(1).lower()
    return 'n/a'

def distribution_codename() -> str:
    """
    Function returning OS distribution codename in lower string (ex.: 'focal')
    """
    for path, regex in PARSERS.items():
        if os.path.exists(path):
            with open(path, encoding='utf-8') as f:
                for line in f.readlines():
                    match = re.match(regex['codename'], line)
                    if match:
                        return match.group(1).lower()
    return 'n/a'

def linux_kernel_version() -> str:
    """
    Function returning OS Linux Kernel version (ex.: '5.19.0-46-generic')
    """
    with open('/proc/version', encoding='utf-8') as f:
        for line in f.readlines():
            match = re.match(r'^Linux version (\S+)', line)
            if match:
                return match.group(1)
    return 'n/a'
