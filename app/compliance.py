import mitogen
import yaml
from yaml.loader import SafeLoader

from compare import compare_function
from plugins.os import distribution_name, distribution_version, distribution_codename

key_function = {
    'os.distribution_name':            distribution_name,
    'os.distribution_version':         distribution_version,
    'os.distribution_codename':        distribution_codename,
}

with open('../rules/ubuntu.yml') as f:
    rules = yaml.load(f, Loader=SafeLoader)

@mitogen.main()
def main(router):

    containers = (
        'ubuntu1804',
        'ubuntu2004',
        )

    for host in containers:
        z = router.docker(container=host, python_path='/usr/bin/python3')
        print(f"{host}: {z.call(distribution_name)} {z.call(distribution_version)} ({z.call(distribution_codename)})")

        for rule in rules['rules']:
            id = rule['id']
            key = rule['key']
            if 'key_args' in rule:
                key_args = rule['key_args']
                value = z.call(key_function[key](key_args))
            else:
                value = z.call(key_function[key])
            # print(value)
            operator = rule['comparison']['operator']
            desired = rule['comparison']['value']
            status = compare_function[operator](value, desired)
            print(f"[{id}] {key}: {value} {operator} {desired} ? => {('OK' if status else 'KO')}")
