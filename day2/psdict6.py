info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

print(info.keys())
print()
print(info.values())
print()
print(info.items())
print()
# iterate for its key -> value pair

for key, value in sorted(info.items()):
    print(key, '->', value)

    #  20 : 40 IST