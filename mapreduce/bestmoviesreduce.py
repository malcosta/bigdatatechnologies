#!/usr/bin/python
import sys
import csv

TAB_CHAR = '\t'
MIN_COUNT = 100


def movie_title(movie_id, avg_ratings):
	'''
	Convert from movie id to movie title
	'''
	with open("/root/input/u.item", "r") as infile:
		reader = csv.reader(infile, delimiter='|')
		next(reader)
		movie_title = "NOT_FOUND"
		for line in reader:
			if int(movie_id) == int(line[0]):
				movie_title = line[1]      
	print(str(avg_ratings) + TAB_CHAR + str(movie_id) + " , " + movie_title)


last_id = None
sum_ratings = 0
count = 0
for line in sys.stdin:
	movie_id, rating = line.split(TAB_CHAR, 1)
	if last_id and last_id != movie_id:
		if count >= MIN_COUNT:
			movie_title(int(last_id), sum_ratings/float(count))
		sum_ratings = int(rating)
		count = 1
	else:
		sum_ratings += int(rating)
		count += 1
	last_id = movie_id

if count >= MIN_COUNT:
	movie_title(int(last_id), sum_ratings/float(count))
