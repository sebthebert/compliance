"""
Compliance application
"""
import mitogen
import yaml
from yaml.loader import SafeLoader

import compare
import plugins.os

containers = (
        'centos7',
        'debian9',
        'debian10',
        'debian11',
        'fedora31',
        'fedora32',
        'fedora33',                
        'ubuntu1804',
        'ubuntu2004'
        )

key_function = {
    'os.distribution_name':     plugins.os.distribution_name,
    'os.distribution_version':  plugins.os.distribution_version,
    'os.distribution_codename': plugins.os.distribution_codename,
    'os.linux_kernel_version':  plugins.os.linux_kernel_version,
}

with open('../rules/ubuntu.yml', encoding='utf-8') as f:
    rules = yaml.load(f, Loader=SafeLoader)

@mitogen.main()
def main(router):
    """
    Main function
    """

    for host in containers:
        z = router.docker(container=host, python_path='/usr/bin/python3')
        distrib = z.call(plugins.os.distribution_name)
        version = z.call(plugins.os.distribution_version)
        codename = z.call(plugins.os.distribution_codename)
        kernel_version = z.call(plugins.os.linux_kernel_version)
        print(f"{host}: {distrib} {version} ({codename}) ({kernel_version})")

        for rule in rules['rules']:
            rule_id = rule['id']
            rule_key = rule['key']
            if 'key_args' in rule:
                key_args = rule['key_args']
                value = z.call(key_function[rule_key](key_args))
            else:
                value = z.call(key_function[rule_key])
            # print(value)
            operator = rule['comparison']['operator']
            desired = rule['comparison']['value']
            status = 'OK' if compare.compare_function[operator](value, desired) else 'KO'
            print(f"[{rule_id}] {rule_key}: {value} {operator} {desired} ? => {status}")
