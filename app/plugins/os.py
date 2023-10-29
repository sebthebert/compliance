"""
Compliance Plugin for Operating System information.
"""
import os
import re

PARSERS = {
    '/etc/lsb-release': {
        'distribution': re.compile('^DISTRIB_ID=(.+)'),
        'version':      re.compile('^DISTRIB_RELEASE=(.+)'),
        'codename':     re.compile('^DISTRIB_CODENAME=(.+)') 
    },
    '/etc/os-release': {
        'distribution': re.compile('^ID=(.+)'),
        'version':      re.compile('^VERSION_ID="?(.+)"?'),
        'codename':     re.compile('^VERSION_CODENAME=(.+)') 
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
                        return(match.group(1).lower())
    return 'unknown'                  

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
                        return(match.group(1).lower())
    return 'unknown'

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
                        return(match.group(1).lower())
    return 'unknown'
