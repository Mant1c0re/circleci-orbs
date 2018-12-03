import sys
print('Escaped string:')
for line in sys.stdin:
    sys.stdout.write(line.strip() + r'\n')
print('')

