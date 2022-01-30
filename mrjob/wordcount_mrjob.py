from mrjob.job import MRJob
from mrjob.step import MRStep

MAX_NUMBER = 1000000000

class WordCount(MRJob):

	def mapper1(self, _, line):
		# tokenize words and generate one line per word with a pair (word, 1)
		for word in line.strip().split(" "):
			if word:
				yield word, 1

	def reducer1(self, word, counts):
		# sum all 1 by word
		yield word, sum(counts)
		
		
	def mapper2(self, word, count):
		# swap word and count, and format count as a long string (20 chars) for sorting by count in descending order
		yield '%020d' % (MAX_NUMBER - int(count)), word
			
	def reducer2(self, count, words):
		# swap again and generate a line per word with the same count
		for word in words:
        		yield word, (MAX_NUMBER - int(count))
				
	def steps(self):
		# pipeline of map reduce tasks
		return [
			MRStep(mapper=self.mapper1, reducer=self.reducer1),
			MRStep(mapper=self.mapper2, reducer=self.reducer2)
		]


if __name__ == '__main__':
     WordCount.run()
