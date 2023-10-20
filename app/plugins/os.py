import os
import re

parsers = {
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
    for p in parsers:
        if os.path.exists(p):
            with open(p) as f:
                for line in f.readlines():
                    match = re.match(parsers[p]['distribution'], line)
                    if match: 
                        return(match.group(1).lower())

def distribution_version() -> str:
    for p in parsers:
        if os.path.exists(p):
            with open(p) as f:
                for line in f.readlines():
                    match = re.match(parsers[p]['version'], line)
                    if match: 
                        return(match.group(1).lower())

def distribution_codename() -> str:
    for p in parsers:
        if os.path.exists(p):
            with open(p) as f:
                for line in f.readlines():
                    match = re.match(parsers[p]['codename'], line)
                    if match: 
                        return(match.group(1).lower())
