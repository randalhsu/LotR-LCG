## LotR LCG

An implementation of Fantasy Flight Games' board game: <a href="http://www.fantasyflightgames.com/edge_minisite.asp?eidm=129">The Lord of the Rings: The Card Game</a>

This program provides auto Scenario setting and Card/Token dragging.

Players must resolve Phases/Damage/Card effects etc. by themselves.

Currently SOLO game only. Multiplayer mode will be done when I have time (Maybe. I do not guarantee anything).


### Prerequisites:

* Card image files are required but NOT included. Look for `resource/card_image_path_*.txt` for some clues.

* Each Quest Card image `*.jpg` must also be splited to `*-A.jpg` and `*-B.jpg`. `resource/quest_cards_splitter.py` is doing this.


### Usage:

`python Launcher.py`


### Tested dependencies:

* Python 2.7.2

* PyQt   4.9

* PIL    1.1.7  (optional, for splitting Quest Cards)


### License:

* Python codes are licensed under GNU GPL v2.

* All image art is copyrighted by Fantasy Flight Games.


https://github.com/amulet-tw/LotR-LCG