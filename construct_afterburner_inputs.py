## In this program, we attempt to construct the input .csv for afterburner. This .csv will later be converted into a sqlite db.

import pandas as pd ## For importing data from file as a dataframe

## Prevent pandas from being stupidly narrow
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

## First, load our data from file
data = pd.read_csv('/Users/aleks/repos/afterburner/assets/15000_Italian_sentences_sorted_from_easy_to_hard__part1/afterburner_intermediate_table.csv')


## Now, let's rename the columns to match what afterburner.py expects, which looks like this:

# | phrase_uuid | lesson | phrase_in_known_language                   | literal_translation_from_target_language_to_known_language | idiomatic_translation_to_target_language | timestamp_when_phrase_is_due_for_study |
# | ----------- | ------ | ------------------------------------------ | ---------------------------------------------------------- | ---------------------------------------- | -------------------------------------- |
# |           0 |  False |  With my best friend                       |  With the my best friend                                   |  Con la mia migliore amica               |                                     -1 |
# |           1 |  False |  On Thursday we're going to hear the opera |  Thursday we go to hear the opera                          |  Giovedi andiamo a sentire l'opera       |                                     -1 |
# |           2 |   True |  This is lesson 1                          |  Thursday we go to hear the opera                          |  Giovedi andiamo a sentire l'opera       |                                     -1 |
# |           3 |   True |  This is also lesson 1                     |  Thursday we go to hear the opera                          |  Giovedi andiamo a sentire l'opera       |                                     -1 |

## Next, let's assign lesson numbers. We'll give the same number in batches of N phrases.
data['lesson'] = 0 ## Fill a new column with 0's

## Define a top and bottom of our range
n = 10 ## This is the number of phrases per lesson
bottom = 0
top = n ## I repeat this here because we'll later adjust it in the body of the for loop

number_of_lessons_in_dataset = len(data) / n ## This is integer division and words for 5000, which is what we have now. Eventually it will not work and we'll have to do something better. 

for i in range(0, number_of_lessons_in_dataset):
    data['lesson'][bottom : top] = i ## Presumably this should be refactored to use data.loc() at some point
    bottom = bottom + n
    top = top + n 
    
## That seems to be working well.
## Next, let's populate the "timestamp when due for study" column with all -1's

data['timestamp_when_phrase_is_due_for_study'] = -1

## We'll also handle the idiomatic translation column
data['literal_translation_from_target_language_to_known_language'] = 'foobar' ## TODO: Try to figure out how to do this with machine translation

## Now reorder the columns and dump to .csv:
data = data[['phrase_uuid', 'lesson', 'phrase_in_known_language', 'literal_translation_from_target_language_to_known_language', 'idiomatic_translation_to_target_language', 'timestamp_when_phrase_is_due_for_study']]
# data.to_csv('/Users/aleks/repos/afterburner/assets/15000_Italian_sentences_sorted_from_easy_to_hard__part1/afterburner_inputs_english_to_italian_part_1.csv', encoding='utf-8')
conn = sqlite3.connect('afterburner_english_to_italian_1')
data.to_sql('afterburner_english_to_italian_1', conn, if_exists = 'fail') ## We don't want to overwrite the user's progress

