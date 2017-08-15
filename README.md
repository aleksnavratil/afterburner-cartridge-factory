# afterburner-cartridge-factory
This is a helper program for [afterburner](https://github.com/aleksnavratil/afterburner) which makes cartridges for afterburner from Anki decks. Currently the word "program" is used in the loosest possible sense, as this is more like a recipe than a fully-automated program. We use Anki decks as the input here because they're easy to find and abundant. So far I've only done a single Anki deck, which is [this one](http://frequencylists.blogspot.com/2016/08/5000-italian-sentences-sorted-from.html).

"Cartridges" are the curriculum/lessons that you actually use to learn a language with `afterburner`. Just like in the 90's, you had to buy a Nintendo console and then also some games, which were stored on cartridges. Without the cartridges, the Nintendo was useless. So here, `afterburner` is like the Nintendo console, and the cartridge file is like the games. You can use the same console to play many games, just as you can use `afterburner` to learn many languages. 

Under the hood, a cartridge is just a zip file containing a bunch of `.mp3` files, which have names like `2203` and `24`, with no file extensions. There's also a `.csv` file in the archive, which tells `afterburner` which `.mp3` files go with which text in your target and known languages.

Anyway, the point of this program is to consume as input an Anki deck, which is a bafflingly complex bundle of `.sqlite` databases, `.json` files, and loose `.mp3` files. This program extracts the parts we need and discards the rest, emitting a cartridge file which is suitable for use in `afterburner`.

## Explanation of the files in this repo

* `reverse_engineering_the_anki_assets.txt` is a log of what I did while exploring the Anki card stack format, which turned out to just be a `.zip` archive with its file extension changed. At the very bottom of this file, there is a series of bash commands which I ran to reformat the Anki data into an input suitable for `afterburner`. This file shows how and when to run the two Python programs mentioned below, and also includes some `sqlite` operations and some other bash hacking in e.g. `sed`.

* `convert_anki_to_sane_format.py` is a little tiny Python program which consumes as input a `.json` file, which in this case is called `media`, with no file extension, and emits as output a way more readable `.csv`.

* `construct_afterburner_input_csv.py` is a slightly larger but still small Python program which emits as output the `.csv` file which is used in the cartridge file.

