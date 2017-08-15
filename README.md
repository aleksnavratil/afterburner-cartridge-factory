# afterburner-cartridge-factory
A helper program which makes cartridges for afterburner.

"Cartridges" are the curriculum/lessons that you actually use to learn a language with `afterburner`. Just like in the 90's, you had to buy a Nintendo console and then also some games, which were stored on cartridges. Without the cartridges, the Nintendo was useless. So here, `afterburner` is like the Nintendo console, and the cartridge file is like the games. You can use the same console to play many games, just as you can use `afterburner` to learn many languages. 

Under the hood, a cartridge is just a zip file containing a bunch of `.mp3` files, which have names like `2203` and `24`, with no file extensions. There's also a .csv file in the archive, which tells `afterburner` which `.mp3` files go with which text in your target and known languages.

Anyway, the point of this program is to consume as input an Anki deck, which is a bafflingly complex bundle of .sqlite databases, .json files, and loose .mp3 files. This program extracts the parts we need and discards the rest, emitting a cartridge file which is suitable for use in `afterburner`.