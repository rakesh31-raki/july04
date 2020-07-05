info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

value = info.pop('domain')  # delete
del info['host']
print(value)
print(info)