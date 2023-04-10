import sys


TAB_CHAR = '\t'

for line in sys.stdin:
    key, value = line.strip().split(TAB_CHAR)
    print(value + TAB_CHAR + key)
