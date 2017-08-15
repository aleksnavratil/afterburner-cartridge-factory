## In this file, we attempt to convert the Anki data format into something much more minimal and sane.

import json ## For loading the "media" .json file fron disk, which contains a key-value mapping of correct filenames to current filenames
import os ## For renaming files
import csv ## For emitting a csv file which contains the same info as the "media" json file, but in an easier-to-understand way

## First, load our key-value map from file. It's currently in a .json file called "media," with no extension

with open('./assets/15000_Italian_sentences_sorted_from_easy_to_hard__part1/media') as audio_filename_map:
    d = json.load(audio_filename_map)
    

## Note that here we assume there are no missing files. In fact this turns out to be true in this case. Later I might add try catch or whatever to handle the inevitable mistakes. 
# os.chdir('./assets/15000_Italian_sentences_sorted_from_easy_to_hard__part1/')
# for key, value in d.items():
#     print("Now renaming ", key, " to ", value)
#     os.rename(key, value)
#     print()
#     print()

## This will work, but the filenames are gross. I propose instead that we use the existing integer filenames, and do the lookup the other way around.
## In that case, I think it'll be easier to emit this key-value dict into a .csv file, then dump that .csv file into sqlite and do the join there.

with open('./assets/15000_Italian_sentences_sorted_from_easy_to_hard__part1/mp3_filename_map.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["phrase_uuid", "dirty_filename"])
    for key, value in d.items():
       writer.writerow([key, value])