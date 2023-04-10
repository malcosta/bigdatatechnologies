#!/usr/bin/env python
import sys


TAB_CHAR = '\t'

for line in sys.stdin:
    id, description = line.strip().split(TAB_CHAR)
    id = int(id)
    
    if (id % 2):
        print(description + TAB_CHAR + "even")
    else:
        print(description[::-1] + TAB_CHAR + "odd")
