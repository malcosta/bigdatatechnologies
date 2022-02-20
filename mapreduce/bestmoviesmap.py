#!/usr/bin/python
import sys

TAB_CHAR = '\t'

for line in sys.stdin:
  user_id, movie_id, rating, timestamp = line.split(TAB_CHAR)
  print(movie_id + TAB_CHAR + rating)
