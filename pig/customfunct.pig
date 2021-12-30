register '/root/pigudf.py' using jython as myfuncs;

professions = LOAD '/root/input/professions.tsv' USING PigStorage('\t') AS (id:int, description:chararray);
DUMP professions;
transformed_professions = FOREACH professions GENERATE myfuncs.even_odd(id, description);
DUMP transformed_professions;
