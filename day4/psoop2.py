class PackageManager:
    def __init__(self):
        print(self, 'am in constructor')

    def __del__(self):
        print(self, 'getting destroyed...')


pm = PackageManager()
print(pm)
