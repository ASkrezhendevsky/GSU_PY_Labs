IP = '192.168.1.5'.split('.')
print(''.join(format(int(i), '10d') for i in IP))
print('\n')
print(''.join(format(int(i), '10b') for i in IP))


