/*
Word Count example
*/

-- load input from text files in directory
lines = LOAD '/root/input/' AS (line:chararray);

-- splits the line into words and flatten to get a word per row
words = FOREACH lines GENERATE FLATTEN(TOKENIZE(line,' ')) as word;

-- group by word
word_group = GROUP words BY word;

-- count words
word_count = FOREACH word_group GENERATE group, COUNT(words) as cnt;

-- order words by count
word_count_sorted = ORDER word_count BY cnt DESC;

-- limit number of results
word_count_sorted_limit = LIMIT word_count_sorted 10;

-- print results
DUMP word_count_sorted_limit;
