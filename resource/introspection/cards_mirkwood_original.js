[
	{
		"set": "mirkwood",
		"id": 0,
		"type": "iDontCare",
		"icon": "iDontCare",
		"why": "programmers count from zero"
	},
	{
		"set": "mirkwood",
		"id": 1,
		"quantity": 1,
		"unique": true,
		"type": "hero",
		"title": "Bilbo Baggins",
		"icon": "lore",
		"cost": 9,
		"strength": 1,
		"attack": 1,
		"defense": 2,
		"hp": 2,
		"traits": ["Hobbit"],
		"effect": {
			"normal": "The first player draws 1 additional card in the resource phase."
		},
		"quote": "\"Well, my dear fellow,\" said Bilbo, \"now you've heard the news, can't you spare me a moment? I want your help in something urgent.\" - The Fellowship of the Ring"
	},
	{
		"set": "mirkwood",
		"id": 2,
		"quantity": 3,
		"type": "attachment",
		"title": "Dunedain Mark",
		"icon": "leadership",
		"cost": 1,
		"traits": ["Signal"],
		"effect": {
			"normal": "Attach to a hero.\nAttached hero gains +1 ATK",
			"action": "Pay 1 resource from attached hero's pool to attach Dunedain Mark to another hero."
		}
	},
	{
		"set": "mirkwood",
		"id": 3,
		"quantity": 2,
		"type": "event",
		"title": "Campfire Tales",
		"icon": "leadership",
		"cost": 1,
		"effect": {
			"action": "Each player draws 1 card."
		},
		"quote": "\"It is a fair tale, though it is sad, as are all the tales of Middle-earth, and yet it may lift up your hearts.\" - Strider, The Fellowship of the Ring"
	},
	{
		"set": "mirkwood",
		"id": 4,
		"quantity": 3,
		"type": "ally",
		"title": "Winged Guardian",
		"icon": "tactics",
		"cost": 2,
		"strength": 0,
		"attack": 0,
		"defense": 4,
		"hp": 1,
		"traits": ["Creature", "Eagle"],
		"effect": {
			"normal": "Sentinel. Winged Guardian cannot have restricted attachments.",
			"forced": "After an attack in which Winged Guardian defends resolves, Pay 1 Tactics resource or discard Winged Guardian from play."
		}
	},
	{
		"set": "mirkwood",
		"id": 5,
		"quantity": 3,
		"type": "event",
		"title": "The Eagles Are Coming!",
		"icon": "tactics",
		"cost": 0,
		"traits": ["Eagle"],
		"effect": {
			"action": "Search the top 5 cards of your deck for any number of Eagle cards and add them to your hand. Shuffle the other cards back into your deck."
		},
		"quote": "\"The Eagles! The Eagles!\" - Bilbo Baggins, The Hobbit"
	},
	{
		"set": "mirkwood",
		"id": 6,
		"quantity": 3,
		"type": "ally",
		"title": "Westfold Horse-Breaker",
		"icon": "spirit",
		"cost": 2,
		"strength": 1,
		"attack": 0,
		"defense": 1,
		"hp": 1,
		"traits": ["Rohan"],
		"effect": {
			"action": "Discard Westfold Horse-Breaker to choose and ready a hero."
		},
		"quote": "\"Your own valour has done more, and the stout legs of the Westfold-men marching through the night.\" - Gandalf, The Two Towers"
	},
	{
		"set": "mirkwood",
		"id": 7,
		"quantity": 3,
		"type": "event",
		"title": "Mustering the Rohirrim",
		"icon": "spirit",
		"cost": 1,
		"effect": {
			"action": "Search the top 10 cards of your deck for any 1 Rohan ally card and add it to your hand. Then, shuffle the other cars back into your deck."
		},
		"quote": "\"More speed we cannot make, if the strength of Rohan is to be gathered.\" - Eomer, The Return of the King"
	},
	{
		"set": "mirkwood",
		"id": 8,
		"quantity": 3,
		"type": "ally",
		"title": "Rivendell Minstrel",
		"icon": "lore",
		"cost": 3,
		"strength": 2,
		"attack": 0,
		"defense": 0,
		"hp": 1,
		"traits": ["Noldor"],
		"effect": {
			"response": "After you play Rivendell Minstrell from your hand, search your deck for 1 Song card and add it to your hand. Shuffle your deck."
		},
		"quote": "As Elrond entered and went towards the seat prepared for him, Elvish minstrels began to make sweet music. - The Fellowship of the Ring"
	},
	{
		"set": "mirkwood",
		"id": 9,
		"quantity": 3,
		"type": "event",
		"title": "Strider's Path",
		"icon": "lore",
		"cost": 1,
		"effect": {
			"response": "After a location is revealed from the encounter deck, immediately travel to that location without resolving its Travel effect. If another location is currently active, return it to the staging area."
		},
		"quote": "\"My cuts, short or long, don't go wrong.\" - Strider, The Fellowship of the Ring"
	},
	{
		"set": "mirkwood",
		"id": 10,
		"quantity": 3,
		"type": "attachment",
		"title": "Song of Kings",
		"icon": "neural",
		"cost": 1,
		"traits": ["Song"],
		"effect": {
			"normal": "Attach to a hero.\nAttached hero gains a Leadership resource icon."
		},
		"quote": "From the ashes a fire shall be woken,\nA light from the shadows shall spring;\nRenewed shall be blade that was broken,\nThe crownless again shall be king. - The Fellowship of the Ring"
	},
	{
		"set": "mirkwood",
		"id": 11,
		"quantity": 1,
		"type": "quest",
		"title": "The Hunt Begins",
		"icon": "gollum",
		"hp": 8,
		"effect": {
			"A": {
				"normal": "Gandalf has requested your assistance in the search for the elusive creature known as Gollum. Your search begins in the Anduin Valley between Mirkwood Forest and the Misty Mountains.",
				"setup": "Reveal 1 card per player from the encounter deck, and add it to the staging area."
			},
			"B": {
				"normal": "You make your way along the banks of the Anduin River, a likely place for Gollum to find food.",
				"forced": "After the players quest successfully, the first player looks at the top 3 cards of the encounter deck. Reveal and add 1 of those cards to the staging area, and discard the other 2 cards."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 12,
		"quantity": 1,
		"type": "quest",
		"title": "A New Terror Abroad",
		"icon": "gollum",
		"hp": 10,
		"effect": {
			"A": {
				"normal": "The wood was full of the rumor of him, dreadful tales even among beasts and birds. The Woodmen said that there was some new terror abroad, a ghost that drank blood. - The Fellowship of the Ring"
			},
			"B": {
				"normal": "Rumors have led you to the eaves of Mirkwood Forest, where the Woodmen whisper of a new terror in the night...",
				"forced": "At the beginning of the quest phase, the first player looks at the top 2 cards of the encounter deck. Reveal and add 1 of those cards to the staging area, and discard the other."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 13,
		"quantity": 1,
		"type": "quest",
		"title": "On the Trail",
		"icon": "gollum",
		"hp": 8,
		"effect": {
			"A": {
				"normal": "\"But at the western edge of Mirkwood the trail turned away. It wandered off southwards and passed out of the Wood-elves' ken, and was lost.\" - Gandalf, The Fellowship of the Ring"
			},
			"B": {
				"normal": "Any player who does not control a hero with at least 1 Clue objective attached cannot commit characters to this quest. If there are ever no heroes with Clue objectives attached in play, reset the quest deck to stage 2B.\nIf the players defeat this stage, the players have once again found a true sign of Gollum's passing, and won the game.",
				"forced": "At the beginning of the quest phase, the first player looks at the top 2 cards of the encounter deck. Reveal and add 1 of those cards to the staging area, and discard the other."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 14,
		"quantity": 4,
		"type": "objective",
		"title": "Signs of Gollum",
		"icon": "gollum",
		"traits": ["Clue"],
		"effect": {
			"normal": "Guarded.",
			"response": "After the players quest successfully, the players may claim Signs of Gollum if it has no attached encounters. When claimed, attach Signs of Gollum to any hero committed to the quest. (Counts as a Condition attachment with: \"Forced: After attached hero is damaged or leaves play, return this card to the top of the encounter deck.\")"
		}
	},
	{
		"set": "mirkwood",
		"id": 15,
		"quantity": 2,
		"type": "location",
		"title": "The Old Ford",
		"icon": "gollum",
		"strength": -1,
		"hp": 2,
		"traits": ["Riverland"],
		"effect": {
			"normal": "X is the number of ally cards in play.",
			"shadow": "Discard from play all allies with a printed cost lower than the number of Riverland locations in play."
		}
	},
	{
		"set": "mirkwood",
		"id": 16,
		"quantity": 3,
		"type": "location",
		"title": "The Eaves of Mirkwood",
		"icon": "gollum",
		"strength": 2,
		"hp": 2,
		"traits": ["Forest"],
		"effect": {
			"normal": "While The Eaves of Mirkwood is the active location, encounter card effects cannot be canceled."
		},
		"quote": "By the afternoon they had reached the eaves of Mirkwood, and were resting almost beneath the great overhanging boughs of its outer trees. - The Hobbit"
	},
	{
		"set": "mirkwood",
		"id": 17,
		"quantity": 2,
		"type": "location",
		"title": "River Ninglor",
		"icon": "gollum",
		"strength": 2,
		"hp": 4,
		"traits": ["Riverland"],
		"effect": {
			"normal": "While River Ninglor is the active location, remove 1 progress token from it and from the current quest at the end of each round.",
			"shadow": "Remove 1 progress token from the current quest. (2 progress tokens instead if this attack is undefended.)"
		}
	},
	{
		"set": "mirkwood",
		"id": 18,
		"quantity": 2,
		"type": "location",
		"title": "The East Bank",
		"icon": "gollum",
		"strength": 3,
		"hp": 3,
		"traits": ["Riverland"],
		"effect": {
			"normal": "While The East Bank is the active location, ally cards cost 1 additional matching resource to play from hand.",
			"shadow": "If you do not control at least 1 hero with a Clue card attached, return this enemy to the staging area after its attack resolves."
		}
	},
	{
		"set": "mirkwood",
		"id": 19,
		"quantity": 2,
		"type": "location",
		"title": "The West Bank",
		"icon": "gollum",
		"strength": 3,
		"hp": 3,
		"traits": ["Riverland"],
		"effect": {
			"normal": "While The West Bank is the active location, attachment and event cards cost 1 additional matching resource to play from hand.",
			"shadow": "If you do not control at least 1 hero with a Clue card attached, double this enemy's base ATK for this attack."
		}
	},
	{
		"set": "mirkwood",
		"id": 20,
		"quantity": 2,
		"type": "enemy",
		"title": "Goblintown Scavengers",
		"icon": "gollum",
		"cost": 12,
		"strength": 1,
		"attack": 1,
		"defense": 0,
		"hp": 3,
		"traits": ["Goblin", "Orc"],
		"effect": {
			"when revealed": "Discard the top card of each player's deck. Until the end of the phase, increase Goblintown Scavenger's Threat by the total printed cost of all cards discarded in this way."
		}
	},
	{
		"set": "mirkwood",
		"id": 21,
		"quantity": 5,
		"type": "enemy",
		"title": "Hunters from Mordor",
		"icon": "gollum",
		"cost": 34,
		"strength": 2,
		"attack": 2,
		"defense": 2,
		"hp": 6,
		"traits": ["Mordor"],
		"effect": {
			"normal": "Hunters from Mordor get +2 ATK and +2 Threat for each Clue card in play.",
			"shadow": "Deal 1 damage to each hero with a Clue card attached. (3 damage instead if this attack is undefended.)"
		}
	},
	{
		"set": "mirkwood",
		"id": 22,
		"quantity": 2,
		"type": "treachery",
		"title": "False Lead",
		"icon": "gollum",
		"effect": {
			"when revealed": "The first player chooses and shuffles a card with the printed Clue trait back into the encounter deck. If there are no Clue cards in play, False Lead gains surge."
		},
		"quote": "\"There we had rumor of him, and we guess that he dwelt there long in the dark hills; but we never found him and at last I despaired.\" - Gandalf, The Fellowship of the Ring."
	},
	{
		"set": "mirkwood",
		"id": 23,
		"quantity": 2,
		"type": "treachery",
		"title": "Flooding",
		"icon": "gollum",
		"effect": {
			"normal": "Doomed 1. Surge.",
			"when revealed": "Remove all progress tokens from all Riverland locations.",
			"shadow": "Resolve the \"when revealed\" effect of this card."
		},
		"quote": "\"There we had rumor of him, and we guess that he dwelt there long in the dark hills; but we never found him and at last I despaired.\" - Gandalf, The Fellowship of the Ring."
	},
	{
		"set": "mirkwood",
		"id": 24,
		"quantity": 3,
		"type": "treachery",
		"title": "Old Wives' Tales",
		"icon": "gollum",
		"traits": ["Gossip"],
		"effect": {
			"when revealed": "Discard 1 resource from each hero's resource pool, if able. Exhaust any hero that could not discard a resource from its pool."
		},
		"quote": "It climbed trees to find nests; it crept into holes to find the young; it slipped through windows to find cradles. - The Fellowship of the Ring"
	},
	{
		"set": "mirkwood",
		"id": 25,
		"quantity": 1,
		"unique": true,
		"type": "hero",
		"title": "Frodo Baggins",
		"icon": "spirit",
		"cost": 7,
		"strength": 2,
		"attack": 1,
		"defense": 2,
		"hp": 2,
		"traits": ["Hobbit"],
		"effect": {
			"response": "After Frodo Baggins is damaged, cancel the damage and instead raise your threat by the amount of damage he would have been dealt. (Limit once per phase.)"
		},
		"quote": "Frodo began to feel restless, and the old paths seemed too well-trodden. he looked at maps and wondered what lay beyond their edges... - The Fellowship of the Ring"
	},
	{
		"set": "mirkwood",
		"id": 26,
		"quantity": 3,
		"type": "attachment",
		"title": "Dunedain Warning",
		"icon": "leadership",
		"cost": 1,
		"traits": ["Signal"],
		"effect": {
			"normal": "Attach to a hero.\nAttached hero gains +1 DEF",
			"action": "Pay 1 resource from attached hero's pool to attach Dunedain Warning to another hero."
		}
	},
	{
		"set": "mirkwood",
		"id": 27,
		"quantity": 3,
		"type": "event",
		"title": "Second Breakfast",
		"icon": "leadership",
		"cost": 1,
		"effect": {
			"action": "Each player returns the topmost attachment card from his discard pile to his hand."
		},
		"quote": "...he was just sitting down to a nice little second-breakfast in the dining room... - The Hobbit"
	},
	{
		"set": "mirkwood",
		"id": 28,
		"quantity": 3,
		"type": "ally",
		"title": "Beorning Beekeeper",
		"icon": "tactics",
		"cost": 4,
		"strength": 1,
		"attack": 2,
		"defense": 1,
		"hp": 3,
		"traits": ["Beorning"],
		"effect": {
			"action": "Discard Beorning Beekeeper from play to deal 1 damage to each enemy in the staging area."
		},
		"quote": "\"We are getting near,\" said Gandalf. \"We are on th edge of his bee pastures.\" - The Hobbit"
	},
	{
		"set": "mirkwood",
		"id": 29,
		"quantity": 3,
		"type": "attachment",
		"title": "Born Aloft",
		"icon": "tactics",
		"cost": 0,
		"traits": ["Condition"],
		"effect": {
			"normal": "Attach to an ally.",
			"action": "Discard Born Aloft from play to return attached ally to its owner's hand."
		},
		"quote": "\"Very well,\" said Gandalf. \"Take us where and as far as you will!\" - The Hobbit"
	},
	{
		"set": "mirkwood",
		"id": 30,
		"quantity": 3,
		"unique": true,
		"type": "ally",
		"title": "Eomund",
		"icon": "spirit",
		"cost": 3,
		"strength": 2,
		"attack": 1,
		"defense": 1,
		"hp": 2,
		"traits": ["Rohan"],
		"effect": {
			"response": "After Eomund leaves play, ready all Rohan characters in play."
		},
		"quote": "\"You I have not seen before, for you are young, but I have spoken with Eomund your father...\" - Aragorn, The Two Towers"
	},
	{
		"set": "mirkwood",
		"id": 31,
		"quantity": 3,
		"type": "attachment",
		"title": "Nor am I a Stranger",
		"icon": "spirit",
		"cost": 1,
		"traits": ["Title"],
		"effect": {
			"normal": "Attach to a character.\nAttached character gains the Rohan trait."
		},
		"quote": "\"Nor indeed am I a stranger; for I have been in this land before, more than once, and ridden with the host of the Rohirrim, though under other name and in other guise.\" - Aragorn, The Two Towers"
	},
	{
		"set": "mirkwood",
		"id": 32,
		"quantity": 3,
		"type": "ally",
		"title": "Longbeard Map-Maker",
		"icon": "lore",
		"cost": 3,
		"strength": 1,
		"attack": 1,
		"defense": 1,
		"hp": 3,
		"traits": ["Dwarf"],
		"effect": {
			"action": "Spend 1 Lore resource to give Longbeard Map-Maker +1 Willpower until the end of the phase."
		},
		"quote": "On the table in the light of a big lamp with a red shade he spread a piece of parchment rather like a map. - The Hobbit"
	},
	{
		"set": "mirkwood",
		"id": 33,
		"quantity": 3,
		"type": "attachment",
		"title": "A Burning Brand",
		"icon": "lore",
		"cost": 2,
		"effect": {
			"normal": "Attach to a Lore character.\nWhile attached character is defending, cancel any shadow effects on cards dealt to the attacking enemy."
		},
		"quote": "\"Keep close to the fire, with your faces outward!\" cried Strider. \"Keep some of the longer sticks ready in your hands.\" - The Fellowship of the Ring"
	},
	{
		"set": "mirkwood",
		"id": 34,
		"quantity": 3,
		"type": "attachment",
		"title": "Song of Wisdom",
		"icon": "neural",
		"cost": 1,
		"traits": ["Song"],
		"effect": {
			"normal": "Attach to a hero.\nAttached hero gains a Lore resource icon."
		},
		"quote": "I sit beside the fire and think\nof all that I have seen,\nof meadow-flowers and butterflies\nin summers that have been - The Fellowship of the Ring"
	},
	{
		"set": "mirkwood",
		"id": 35,
		"quantity": 1,
		"type": "quest",
		"title": "Grimbeorn's Quest",
		"icon": "carrock",
		"hp": 7,
		"effect": {
			"A": {
				"normal": "While searching for Gollum in the Anduin valley, you recieve word that a group of Trolls have come to the Carrock.",
				"setup": "Add The Carrock to the staging area. Remove 4 unique Troll cards and 4 copies of the \"Sacked!\" card from the encounter deck and set them aside, out of play. Then shuffle 1 \"Sacked!\" card per player back into the encounter deck."
			},
			"B": {
				"normal": "As this area is under the watch of the Beornings, you seek out their leader, Grimbeorn the Old, and discover he has already set out in a rage. You follow, hoping to find him before he confronts the Trolls.",
				"forced": "After placing the 7th progress token on Grimbeorn's Quest, The Carrock becomes the active location. Discard the previous active location from play."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 36,
		"quantity": 1,
		"type": "quest",
		"title": "Against the Trolls",
		"icon": "carrock",
		"hp": 1,
		"effect": {
			"A": {
				"normal": "You approach the Carrock, and find that the Trolls have been watching you from the top of the rocky river landmark."
			},
			"B": {
				"normal": "As you approach, the Trolls close in and attack!",
				"when revealed": "Place the unique Troll cards previously set aside into the staging area.\nPlayers cannot defeat this stage if there are any Troll enemies in play."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 37,
		"quantity": 1,
		"unique": true,
		"type": "objective",
		"title": "Grimbeorn the Old",
		"icon": "carrock",
		"strength": 2,
		"attack": 4,
		"defense": 3,
		"hp": 10,
		"traits": ["Ally"],
		"effect": {
			"normal": "Grimbeorn the Old does not exhaust to defend against Troll enemies.\nIf Grimbeorn the Old has 8 or more resource tokens on him, he joins the first player as an ally.",
			"action": "Spend 1 Leadership resource to place that resource on Grimbeorn the Old."
		}
	},
	{
		"set": "mirkwood",
		"id": 38,
		"quantity": 1,
		"unique": true,
		"type": "enemy",
		"title": "Louis",
		"icon": "carrock",
		"cost": 34,
		"strength": 2,
		"attack": 4,
		"defense": 2,
		"hp": 10,
		"traits": ["Troll"],
		"effect": {
			"normal": "While Louis is engaged with a player, all Troll enemies gain, \"Forced: After this enemy attacks, the defending player must raise his threat by 3.\"",
			"response": "After defeating Louis, you may choose and discard 1 \"Sacked!\" card from play."
		}
	},
	{
		"set": "mirkwood",
		"id": 39,
		"quantity": 1,
		"unique": true,
		"type": "enemy",
		"title": "Morris",
		"icon": "carrock",
		"cost": 34,
		"strength": 2,
		"attack": 4,
		"defense": 2,
		"hp": 10,
		"traits": ["Troll"],
		"effect": {
			"normal": "While Morris is engaged with a player, all Troll enemies get +1 ATK.",
			"response": "After defeating Morris, you may choose and discard 1 \"Sacked!\" card from play."
		}
	},
	{
		"set": "mirkwood",
		"id": 40,
		"quantity": 1,
		"unique": true,
		"type": "enemy",
		"title": "Stuart",
		"icon": "carrock",
		"cost": 34,
		"strength": 2,
		"attack": 4,
		"defense": 2,
		"hp": 10,
		"traits": ["Troll"],
		"effect": {
			"normal": "While Stuart is engaged with a player, all Troll enemies get +1 DEF.",
			"response": "After defeating Stuart, you may choose and discard 1 \"Sacked!\" card from play."
		}
	},
	{
		"set": "mirkwood",
		"id": 41,
		"quantity": 1,
		"unique": true,
		"type": "enemy",
		"title": "Rupert",
		"icon": "carrock",
		"cost": 34,
		"strength": 2,
		"attack": 4,
		"defense": 2,
		"hp": 10,
		"traits": ["Troll"],
		"effect": {
			"forced": "After Rupert attacks, shuffle all copies of the \"Sacked!\" card from the discard pile back into the encounter deck.",
			"response": "After defeating Rupert, you may choose and discard 1 \"Sacked!\" card from play."
		}
	},
	{
		"set": "mirkwood",
		"id": 42,
		"quantity": 4,
		"type": "enemy",
		"title": "Muck Adder",
		"icon": "carrock",
		"cost": 20,
		"strength": 1,
		"attack": 2,
		"defense": 0,
		"hp": 4,
		"traits": ["Creature"],
		"effect": {
			"forced": "If Muck Adder damages a character, discard that character from play.",
			"shadow": "Defending character gets -1 DEF for the duration of this attack."
		}
	},
	{
		"set": "mirkwood",
		"id": 43,
		"quantity": 1,
		"unique": true,
		"type": "location",
		"title": "The Carrock",
		"icon": "carrock",
		"strength": 2,
		"hp": 6,
		"traits": ["Riverland"],
		"effect": {
			"normal": "Immune to player card effects.\nPlayers cannot travel to The Carrock except through quest card effects.\nWhile The Carrock is the active location, Troll enemies get +1 ATK and +1 DEF."
		}
	},
	{
		"set": "mirkwood",
		"id": 44,
		"quantity": 4,
		"type": "location",
		"title": "River Langflood",
		"icon": "carrock",
		"strength": 2,
		"hp": 3,
		"traits": ["Riverland"],
		"effect": {
			"normal": "While it is in the staging area, River Langflood gets +1 Threat for each Troll enemy in play."
		}
	},
	{
		"set": "mirkwood",
		"id": 45,
		"quantity": 3,
		"type": "location",
		"title": "Bee Pastures",
		"icon": "carrock",
		"strength": 1,
		"hp": 2,
		"traits": ["Wilderlands"],
		"effect": {
			"normal": "After you travel to Bee Pastures, search the encounter deck and discard pile for Grimbeorn the Old and add him to the staging area. Then shuffle the encounter deck."
		}
	},
	{
		"set": "mirkwood",
		"id": 46,
		"quantity": 3,
		"type": "location",
		"title": "Oak-wood Grove",
		"icon": "carrock",
		"strength": 2,
		"hp": 1,
		"traits": ["Forest"],
		"effect": {
			"normal": "While Oak-wood Grove is the active location, resource tokens from any sphere may be spent as Leadership resource tokens."
		}
	},
	{
		"set": "mirkwood",
		"id": 47,
		"quantity": 3,
		"type": "treachery",
		"title": "A Frightened Beast",
		"icon": "carrock",
		"effect": {
			"when revealed": "Each player raises his threat by the total Threat of all cards in the staging area. Any player may choose to discard from play 1 Creature ally card he controls to cancel this effect."
		},
		"quote": "Then, one of the ponies took fright at nothing and bolted. - The Hobit"
	},
	{
		"set": "mirkwood",
		"id": 48,
		"quantity": 5,
		"type": "treachery",
		"title": "Sacked!",
		"icon": "carrock",
		"effect": {
			"when revealed": "Attach to a hero with no \"Sacked!\" cards attached controlled by the first player. (Cannot be canceled.) Counts as a condition attachment with the text: \"Attached hero cannot attack, defend, commit to a quest, trigger its effect, or collect resources.\"",
			"shadow": "If attacking enemy is a Troll, resolve this card's \"when revealed\" effect."
		},
		"quote": "\"There we had rumor of him, and we guess that he dwelt there long in the dark hills; but we never found him and at last I despaired.\" - Gandalf, The Fellowship of the Ring."
	},
	{
		"set": "mirkwood",
		"id": 49,
		"quantity": 2,
		"type": "treachery",
		"title": "Roasted Slowly",
		"icon": "carrock",
		"effect": {
			"when revealed": "Destroy all heroes with the card \"Sacked!\" attached. Then, shuffle Roasted Slowly back into the encounter deck.",
			"shadow": "If attacking enemy is a Troll, remove 2 damage tokens from it."
		}
	},
	{
		"set": "mirkwood",
		"id": 50,
		"quantity": 1,
		"unique": true,
		"type": "hero",
		"title": "Prince Imrahil",
		"icon": "leadership",
		"cost": 11,
		"strength": 2,
		"attack": 3,
		"defense": 2,
		"hp": 4,
		"traits": ["Gondor", "Noble"],
		"effect": {
			"response": "After a character leaves play, ready Prince Imrahil. (Limit once per round.)"
		}
	},
	{
		"set": "mirkwood",
		"id": 51,
		"quantity": 3,
		"type": "attachment",
		"title": "Dunedain Quest",
		"icon": "leadership",
		"cost": 2,
		"traits": ["Signal"],
		"effect": {
			"normal": "Attach to a hero.\nAttached hero gains +1 Willpower",
			"action": "Pay 1 resource from attached hero's pool to attach Dunedain Quest to another hero."
		}
	},
	{
		"set": "mirkwood",
		"id": 52,
		"quantity": 3,
		"type": "event",
		"title": "Parting Gifts",
		"icon": "leadership",
		"cost": 0,
		"effect": {
			"action": "Move any number of resource tokens from a Leadership hero's resource pool to any other hero's resource pool."
		}
	},
	{
		"set": "mirkwood",
		"id": 53,
		"quantity": 3,
		"unique": true,
		"type": "ally",
		"title": "Landroval",
		"icon": "tactics",
		"cost": 5,
		"strength": 1,
		"attack": 3,
		"defense": 1,
		"hp": 4,
		"traits": ["Creature", "Eagle"],
		"effect": {
			"normal": "Sentinel. Landroval cannot have restricted attachments.",
			"response": "After a hero card is destroyed, return Landroval to his owner's hand to put that hero back into play, with 1 damage token on it. (Limit once per game.)"
		}
	},
	{
		"set": "mirkwood",
		"id": 54,
		"quantity": 3,
		"type": "event",
		"title": "To the Eyrie",
		"icon": "tactics",
		"cost": 2,
		"effect": {
			"response": "After an ally is destroyed, exhaust 1 Eagle character to move that ally from the discard pile to its owner's hand."
		}
	},
	{
		"set": "mirkwood",
		"id": 55,
		"quantity": 3,
		"type": "ally",
		"title": "Escort from Edoras",
		"icon": "spirit",
		"cost": 2,
		"strength": 2,
		"attack": 0,
		"defense": 0,
		"hp": 1,
		"traits": ["Rohan"],
		"effect": {
			"normal": "While committed to a quest, Escort from Edoras gets +2 Willpower.",
			"forced": "After resolving a quest to which Escort from Edoras was committed, discard Escort from Edoras from play."
		}
	},
	{
		"set": "mirkwood",
		"id": 56,
		"quantity": 3,
		"type": "attachment",
		"title": "Ancient Mathom",
		"icon": "spirit",
		"cost": 1,
		"traits": ["Mathom"],
		"effect": {
			"normal": "Attach to a location.",
			"response": "After attached location is explored, the first player draws 3 cards."
		}
	},
	{
		"set": "mirkwood",
		"id": 57,
		"quantity": 3,
		"unique": true,
		"type": "ally",
		"title": "Haldir of Lorien",
		"icon": "lore",
		"cost": 4,
		"strength": 2,
		"attack": 2,
		"defense": 2,
		"hp": 3,
		"traits": ["Ranged", "Sentinel"]
	},
	{
		"set": "mirkwood",
		"id": 58,
		"quantity": 3,
		"type": "event",
		"title": "Infighting",
		"icon": "lore",
		"cost": 1,
		"effect": {
			"action": "Move any number of damage from one enemy to another."
		}
	},
	{
		"set": "mirkwood",
		"id": 59,
		"quantity": 3,
		"unique": true,
		"type": "ally",
		"title": "Radagast",
		"icon": "neural",
		"cost": 5,
		"strength": 2,
		"attack": 1,
		"defense": 1,
		"hp": 3,
		"traits": ["Istari"],
		"effect": {
			"normal": "Radagast collects 1 resource each resource phase. These resources can be used to pay for Creature cards played from your hand.",
			"action": "Spend X resources from Radagast's pool to heal X wounds on any 1 Creature."
		}
	},
	{
		"set": "mirkwood",
		"id": 60,
		"quantity": 1,
		"type": "quest",
		"title": "The Wounded Eagle",
		"icon": "rhosgobel",
		"hp": 8,
		"effect": {
			"A": {
				"normal": "After a fierce conflict with a group of Trolls, you come across a fallen Eagle, grievously wounded and on the verge of death...",
				"setup": "Search the encounter deck for Rhosgobel and Wilyador, and add them to the staging area with 2 damage tokens on Wilyador. Then, shuffle the encounter deck."
			},
			"B": {
				"normal": "The Eagle's wounds cannot be tended in the wilderness, so you attempt to bring the creature to Rhosgobel, where the wisdom of Radagast the Brown may be its only hope."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 61,
		"quantity": 1,
		"type": "quest",
		"title": "Radagast's Request",
		"icon": "rhosgobel",
		"hp": 12,
		"effect": {
			"A": {
				"normal": "The Eagle's health has grown worse, but you have at last arrived at Rhosgobel, where Radagast examines the bird. He then asks you to head out into the wilderness to find the healing plant, Athelas. Meantime, any healing lore or supplies your party has it its disposal could be used to assist in comforting the Eagle until you return."
			},
			"B": {
				"response": "After the quest phase begins, the first player may place X dmage tokens on Wilyador to look at the top 3 cards of the encounter deck. Reveal and add 1 of these cards to the staging area, and discard the other 2. X is the number of players in the game.",
				"forced": "After a card effect heals Wilyador, remove that card from the game."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 62,
		"quantity": 1,
		"type": "quest",
		"title": "Return to Rhosgobel",
		"icon": "rhosgobel",
		"hp": 0,
		"effect": {
			"A": {
				"normal": "Feeling that time is runnign out on Wilyador's life, you gather the Athelas you have found and head back to Rhosgobel. You arrive at night, wondering if you have found enough of the herb..."
			},
			"B": {
				"when revealed": "Heal 5 wounds from Wilyador for each Athelas objective card the players control.",
				"normal": "If Wilyador is completely healed when this effect resolves, Wilyador survives and the players have won the game. Otherwise, the players have lost the game."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 63,
		"quantity": 4,
		"type": "objective",
		"title": "Athelas",
		"icon": "rhosgobel",
		"traits": ["Item"],
		"effect": {
			"normal": "Guarded.",
			"action": "Exhaust a hero to claim this objective if it has no encounters attached. Then, attach Athelas to that hero."
		}
	},
	{
		"set": "mirkwood",
		"id": 64,
		"quantity": 1,
		"unique": true,
		"type": "objective",
		"title": "Wilyador",
		"icon": "rhosgobel",
		"traits": ["Creature", "Eagle"],
		"effect": {
			"normal": "No attachments. The first player gains control of Wilyador, as an ally.",
			"forced": "At the end of each round, Wilyador suffers 2 damage.\nWilyador cannot be healed of more than 5 wounds by a single effect. If Wilyador leaves play, the players have lost the game."
		}
	},
	{
		"set": "mirkwood",
		"id": 65,
		"quantity": 1,
		"type": "location",
		"title": "Rhosgobel",
		"icon": "rhosgobel",
		"strength": -1,
		"hp": 4,
		"traits": ["Forest"],
		"effect": {
			"normal": "X is the number of players in the game.\nWhile Rhosgobel is in the staging area, Wilyador cannot be healed.",
			"travel": "Players must complete stage one of this quest before they can travel to Rhosgobel."
		},
		"victory": 4
	},
	{
		"set": "mirkwood",
		"id": 66,
		"quantity": 4,
		"type": "location",
		"title": "Forest Grove",
		"icon": "rhosgobel",
		"strength": 2,
		"hp": 3,
		"traits": ["Forest"],
		"effect": {
			"response": "After the players explore Forest Grove, search the encounter deck and discard pile for 1 Athelas objective, and add it to the staging area. Then, shuffle the encounter deck."
		}
	},
	{
		"set": "mirkwood",
		"id": 67,
		"quantity": 4,
		"type": "treachery",
		"title": "Exhaustion",
		"icon": "rhosgobel",
		"effect": {
			"when revealed": "Deal 2 damage to each exhausted character.",
			"shadow": "Deal 1 damage to each exhausted character."
		}
	},
	{
		"set": "mirkwood",
		"id": 68,
		"quantity": 4,
		"type": "treachery",
		"title": "Swarming Insects",
		"icon": "rhosgobel",
		"effect": {
			"when revealed": "Deal 1 damage to each character without any attachments.",
			"shadow": "If a character (including Wilyador) has more damage than each other character, deal 3 additional damage to that character."
		}
	},
	{
		"set": "mirkwood",
		"id": 69,
		"quantity": 2,
		"type": "treachery",
		"title": "Festering Wounds",
		"icon": "rhosgobel",
		"effect": {
			"when revealed": "Deal 2 damage to each wounded character.",
			"shadow": "Deal 1 damage to each wounded character. (2 damage instead of this attack is undefended.)"
		}
	},
	{
		"set": "mirkwood",
		"id": 70,
		"quantity": 4,
		"type": "enemy",
		"title": "Mirkwood Flock",
		"icon": "rhosgobel",
		"cost": 32,
		"strength": 1,
		"attack": 2,
		"defense": 1,
		"hp": 3,
		"traits": ["Creature"],
		"effect": {
			"normal": "Only Eagle characters or characters with ranged can attack or defend against Mirkwood Flock.",
			"shadow": "If this attack is undefended, the damage must be placed on Wilyador."
		}
	},
	{
		"set": "mirkwood",
		"id": 71,
		"quantity": 5,
		"type": "enemy",
		"title": "Black Forest Bats",
		"icon": "rhosgobel",
		"cost": 26,
		"strength": 1,
		"attack": 1,
		"defense": 0,
		"hp": 2,
		"traits": ["Creature"],
		"effect": {
			"normal": "Only Eagle characters or characters with ranged can attack or defend against Mirkwood Flock.",
			"shadow": "If this attack is undefended, the damage must be placed on Wilyador."
		}
	},
	{
		"set": "mirkwood",
		"id": 72,
		"quantity": 1,
		"unique": true,
		"type": "hero",
		"title": "Brand son of Bain",
		"icon": "tactics",
		"cost": 10,
		"strength": 2,
		"attack": 3,
		"defense": 2,
		"hp": 3,
		"traits": ["Dale"],
		"effect": {
			"normal": "Ranged.",
			"response": "After Brand son of Bain attacks and defeats an enemy engaged with another player, choose and ready one of that player's characters."
		}
	},
	{
		"set": "mirkwood",
		"id": 73,
		"quantity": 3,
		"type": "ally",
		"title": "Keen-eyed Took",
		"icon": "leadership",
		"cost": 2,
		"strength": 1,
		"attack": 0,
		"defense": 0,
		"hp": 2,
		"traits": ["Hobbit"],
		"effect": {
			"response": "After Keen-eyed Took enters play, reveal the top card of each player's deck.",
			"action": "Return Keen-eyed Took to your hand to discard the top card of each player's deck."
		}
	},
	{
		"set": "mirkwood",
		"id": 74,
		"quantity": 3,
		"type": "event",
		"title": "Rear Guard",
		"icon": "leadership",
		"cost": 1,
		"effect": {
			"quest action": "Discard a Leadership ally to give each hero committed to this quest +1 Willpower until the end of the phase."
		}
	},
	{
		"set": "mirkwood",
		"id": 75,
		"quantity": 3,
		"type": "ally",
		"title": "Descendant of Thorondor",
		"icon": "tactics",
		"cost": 4,
		"strength": 1,
		"attack": 2,
		"defense": 1,
		"hp": 2,
		"traits": ["Creature", "Eagle"],
		"effect": {
			"normal": "Descendant of Thorondor cannot have restricted attachments.",
			"response": "After Descendant of Thorondor enters or leaves play, deal 2 damage to any 1 enemy in the staging area."
		}
	},
	{
		"set": "mirkwood",
		"id": 76,
		"quantity": 3,
		"type": "event",
		"title": "Meneldor's Flight",
		"icon": "tactics",
		"cost": 0,
		"effect": {
			"action": "Choose an Eagle ally. Return that character to its owner's hand."
		}
	},
	{
		"set": "mirkwood",
		"id": 77,
		"quantity": 3,
		"type": "ally",
		"title": "The Riddermark's Finest",
		"icon": "spirit",
		"cost": 2,
		"strength": 1,
		"attack": 1,
		"defense": 0,
		"hp": 2,
		"traits": ["Creature", "Rohan"],
		"effect": {
			"action": "Exhaust and discard The Riddermark's Finest to place 2 progress tokens on any location."
		}
	},
	{
		"set": "mirkwood",
		"id": 78,
		"quantity": 3,
		"type": "event",
		"title": "Ride to Ruin",
		"icon": "spirit",
		"cost": 1,
		"effect": {
			"action": "Discard a Rohan ally to choose a location. Place 3 progress tokens on that location."
		}
	},
	{
		"set": "mirkwood",
		"id": 79,
		"quantity": 3,
		"unique": true,
		"type": "ally",
		"title": "Gildor Inglorion",
		"icon": "lore",
		"cost": 5,
		"strength": 3,
		"attack": 2,
		"defense": 3,
		"hp": 3,
		"traits": ["Noldor"],
		"effect": {
			"action": "Exhaust Gildor Inglorion to look at the top 3 cards of your deck. Switch one of those cards with a card from your hand. Then, return the 3 cards to the top of your deck, in any order."
		}
	},
	{
		"set": "mirkwood",
		"id": 80,
		"quantity": 3,
		"type": "event",
		"title": "Gildor's Counsel",
		"icon": "lore",
		"cost": 3,
		"effect": {
			"normal": "Play during the Quest phase, before characters are committed to the Quest.",
			"action": "Reveal 1 less card from the encounter deck this phase. (To a minimum of 1.)"
		}
	},
	{
		"set": "mirkwood",
		"id": 81,
		"quantity": 3,
		"type": "attachment",
		"title": "Song of Travel",
		"icon": "neural",
		"cost": 1,
		"traits": ["Song"],
		"effect": {
			"normal": "Attach to a hero.\nAttached hero gains a Spirit resource icon"
		}
	},
	{
		"set": "mirkwood",
		"id": 82,
		"quantity": 1,
		"type": "quest",
		"title": "The Hills of Emyn Muil",
		"icon": "emynmuil",
		"hp": 1,
		"effect": {
			"A": {
				"normal": "The hunt for Gollum has led you to the south, and you are now approaching Rauros Falls and the nearby hills of Emyn Muil...",
				"setup": "Search the encounter deck for Amon Hen and Amon Lhaw, and add them to the staging area. The shuffle the encounter deck."
			},
			"B": {
				"normal": "You are certain that Gollum has fled into this area, and you must explore until you find the fresh trail.",
				"forced": "If there are no location cards in the staging area, the first treachery card revealed during the quest phase gains surge.\nPlayers cannot defeat this stage unless there are no Emyn Muil locations in play, and they have collected at least 20 victory points."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 83,
		"quantity": 1,
		"type": "location",
		"title": "Amon Hen",
		"icon": "emynmuil",
		"strength": -1,
		"hp": 5,
		"traits": ["Emyn Muil"],
		"effect": {
			"normal": "X is double the number of players in the game.\nWhile Amon Hen is the active location, players cannot play events."
		},
		"victory": 5
	},
	{
		"set": "mirkwood",
		"id": 84,
		"quantity": 1,
		"type": "location",
		"title": "Amon Lhaw",
		"icon": "emynmuil",
		"strength": -1,
		"hp": 5,
		"traits": ["Emyn Muil"],
		"effect": {
			"normal": "X is double the number of players in the game.\nWhile Amon Lhaw is the active location, treat all attachments as if their printed text boxes were blank."
		},
		"victory": 5
	},
	{
		"set": "mirkwood",
		"id": 85,
		"quantity": 2,
		"type": "location",
		"title": "The East Wall of Rohan",
		"icon": "emynmuil",
		"strength": 4,
		"hp": 2,
		"traits": ["Emyn Muil"],
		"effect": {
			"normal": "While The East Wall of Rohan is the active location, non-Rohan characters cost 2 additional matching resources to play."
		},
		"victory": 3
	},
	{
		"set": "mirkwood",
		"id": 86,
		"quantity": 2,
		"type": "location",
		"title": "The North Stair",
		"icon": "emynmuil",
		"strength": 3,
		"hp": 3,
		"traits": ["Emyn Muil"],
		"effect": {
			"forced": "After traveling to The North Stair, move the top card of the encounter discard pile to the staging area. Resolve any \"when revealed\" effects on that card."
		},
		"victory": 3
	},
	{
		"set": "mirkwood",
		"id": 87,
		"quantity": 2,
		"type": "location",
		"title": "Rauros Falls",
		"icon": "emynmuil",
		"strength": 2,
		"hp": 4,
		"traits": ["Emyn Muil"],
		"effect": {
			"normal": "While Rauros Falls is the active location, all characters must commit to the current quest during the quest phase.",
			"shadow": "After this attack resolves, return attacking enemy to the staging area."
		},
		"victory": 3
	},
	{
		"set": "mirkwood",
		"id": 88,
		"quantity": 3,
		"type": "location",
		"title": "The Shores of Nen Hithoel",
		"icon": "emynmuil",
		"strength": 2,
		"hp": 2,
		"traits": ["Emyn Muil"],
		"effect": {
			"travel": "The first player must discard 1 event card from his hand to travel to this location.",
			"shadow": "After this attack resolves, return attacking enemy to the staging area."
		},
		"victory": 2
	},
	{
		"set": "mirkwood",
		"id": 89,
		"quantity": 3,
		"type": "location",
		"title": "The Outer Ridge",
		"icon": "emynmuil",
		"strength": 2,
		"hp": 2,
		"traits": ["Emyn Muil"],
		"effect": {
			"travel": "While The Outer Ridge is the active location, each location in the staging area gets +1 Threat.",
			"shadow": "After this attack resolves, return attacking enemy to the staging area."
		},
		"victory": 2
	},
	{
		"set": "mirkwood",
		"id": 90,
		"quantity": 4,
		"type": "location",
		"title": "The Highlands",
		"icon": "emynmuil",
		"strength": 1,
		"hp": 1,
		"traits": ["Emyn Muil"],
		"effect": {
			"travel": "In order to travel to The Highlands, the players must reveal the top card of the encounter deck, and add it to the staging area."
		},
		"victory": 1
	},
	{
		"set": "mirkwood",
		"id": 91,
		"quantity": 4,
		"type": "treachery",
		"title": "Impassable Chasm",
		"icon": "emynmuil",
		"effect": {
			"when revealed": "If there is an active location, remove all progress tokens from that location and return it to the staging area. If no location is moved by this effect, this card gains surge."
		}
	},
	{
		"set": "mirkwood",
		"id": 92,
		"quantity": 3,
		"type": "treachery",
		"title": "Rockslide",
		"icon": "emynmuil",
		"traits": ["Hazard"],
		"effect": {
			"when revealed": "Deal 2 damage to each character committed to this quest.",
			"shadow": "Remove defending character from combat. This attack is considered undefended."
		}
	},
	{
		"set": "mirkwood",
		"id": 93,
		"quantity": 3,
		"type": "treachery",
		"title": "Slick Footing",
		"icon": "emynmuil",
		"traits": ["Hazard"],
		"effect": {
			"when revealed": "Remove 1 progress token from each location in play. Then, discard the top card of each player's deck for each progress token removed by this effect."
		}
	},
	{
		"set": "mirkwood",
		"id": 94,
		"quantity": 3,
		"type": "enemy",
		"title": "Orc Horse Thieves",
		"icon": "emynmuil",
		"cost": 35,
		"strength": 3,
		"attack": 1,
		"defense": 2,
		"hp": 6,
		"traits": ["Mordor", "Orc"],
		"effect": {
			"normal": "Doomed 2.\nOrc Horse Thieves get +1 ATK for each location in the staging area."
		}
	},
	{
		"set": "mirkwood",
		"id": 95,
		"quantity": 1,
		"unique": true,
		"type": "hero",
		"title": "Boromir",
		"icon": "tactics",
		"cost": 11,
		"strength": 1,
		"attack": 3,
		"defense": 2,
		"hp": 5,
		"traits": ["Gondor", "Noble", "Warrior"],
		"effect": {
			"action1": "Raise your threat by 1 to ready Boromir.",
			"action2": "Discard Boromir to deal 2 damage to each enemy engaged with a single player."
		}
	},
	{
		"set": "mirkwood",
		"id": 96,
		"quantity": 3,
		"type": "ally",
		"title": "Dunedain Watcher",
		"icon": "leadership",
		"cost": 3,
		"strength": 1,
		"attack": 1,
		"defense": 1,
		"hp": 2,
		"traits": ["Dunedain"],
		"effect": {
			"response": "Discard Dunedain Watcher from play to cancel the shadow effects of a card just triggered."
		}
	},
	{
		"set": "mirkwood",
		"id": 97,
		"quantity": 3,
		"type": "attachment",
		"title": "Dunedain Cache",
		"icon": "leadership",
		"cost": 2,
		"traits": ["Item"],
		"effect": {
			"normal": "Attach to a hero.\nAttached hero gains ranged",
			"action": "Pay 1 resource from attached hero's pool to attach Dunedain Cache to another hero."
		}
	},
	{
		"set": "mirkwood",
		"id": 98,
		"quantity": 3,
		"type": "ally",
		"title": "Vassal of the Windlord",
		"icon": "tactics",
		"cost": 1,
		"strength": 0,
		"attack": 3,
		"defense": 0,
		"hp": 1,
		"traits": ["Creature", "Eagle"],
		"effect": {
			"normal": "Ranged. Vassal of the Windlord cannot have restricted attachments.",
			"forced": "After an attack in which Vassal of the Windlord attacked resolves, discard Vassal of the Windlord from play."
		}
	},
	{
		"set": "mirkwood",
		"id": 99,
		"quantity": 3,
		"type": "attachment",
		"title": "Song of Mocking",
		"icon": "tactics",
		"cost": 1,
		"traits": ["Song"],
		"effect": {
			"normal": "Attach to a hero.",
			"action": "Exhaust Song of Mocking to choose another hero. Until the end of the phase, attached hero takes all damage assigned to the chosen hero."
		}
	},
	{
		"set": "mirkwood",
		"id": 100,
		"quantity": 3,
		"type": "ally",
		"title": "Elfhelm",
		"icon": "spirit",
		"cost": 4,
		"strength": 1,
		"attack": 2,
		"defense": 2,
		"hp": 3,
		"traits": ["Rohan", "Warrior"],
		"effect": {
			"normal": "While Elfhelm is ready, he gains: \"Response: After your threat is raised as the result of questing unsuccessfully, or by an encounter or quest card effect, reduce your threat by 1.\""
		}
	},
	{
		"set": "mirkwood",
		"id": 101,
		"quantity": 3,
		"type": "event",
		"title": "We Do Not Sleep",
		"icon": "spirit",
		"cost": 5,
		"effect": {
			"action": "Until the end of the phase, Rohan characters do not exhaust to commit to quests."
		}
	},
	{
		"set": "mirkwood",
		"id": 102,
		"quantity": 3,
		"type": "ally",
		"title": "Silvan Tracker",
		"icon": "lore",
		"cost": 3,
		"strength": 1,
		"attack": 1,
		"defense": 1,
		"hp": 3,
		"traits": ["Silvan"],
		"effect": {
			"response": "After a Silvan character readies during the refresh phase, heal 1 damage from that character."
		}
	},
	{
		"set": "mirkwood",
		"id": 103,
		"quantity": 3,
		"type": "attachment",
		"title": "Fast Hitch",
		"icon": "lore",
		"cost": 1,
		"traits": ["Skill"],
		"effect": {
			"normal": "Attach to a Hobbit character.",
			"action": "Exhaust Fast Hitch to ready attached character."
		}
	},
	{
		"set": "mirkwood",
		"id": 104,
		"quantity": 3,
		"type": "attachment",
		"title": "Song of Battle",
		"icon": "neural",
		"cost": 1,
		"traits": ["Song"],
		"effect": {
			"normal": "Attach to a hero. Attached hero gains a Tactics resource icon."
		}
	},
	{
		"set": "mirkwood",
		"id": 105,
		"quantity": 1,
		"type": "quest",
		"title": "Into the Marshes",
		"icon": "marshes",
		"hp": 12,
		"effect": {
			"A": {
				"normal": "You have followed Gollum's trail for days, and are now closing in fast pursuit. In a last ditch effort to escape you, the creature has fled to The Dead Marshes.",
				"setup": "Search the encounter deck for Gollum, and add it to the staging area. Shuffle the encounter deck, then reveal 1 card per player from the encounter deck and add it to the staging area."
			},
			"B": {
				"normal": "'Yes, yes,' said Gollum. 'All dead, all rotten. Elves and Men and Orcs. The Dead Marshes. There was a great battle long ago, yes, so they told him when Smeagol was young, when I was young before teh Precious came. It was a great battle. Tall Men with long swords, and terrible Elves and Orcses shrieking. They fought on the plain for days and months at the Black Gates. But the Marshes have grown since then, swallowed up the graves; always creeping, creeping.' - The Two Towers"
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 106,
		"quantity": 1,
		"type": "quest",
		"title": "The Capture",
		"icon": "marshes",
		"hp": 3,
		"effect": {
			"A": {
				"normal": "After a tiring pursuit through the treacherous marshland, you have cornered Gollum, and move in for the capture."
			},
			"B": {
				"forced": "After this stage is defeated, the first player chooses a player. That player must pass an Escape test, dealing 1 card from the encounter deck for each resource token on Gollum, to capture him. If Gollum is not captured at this time, reset the quest deck to stage 1B.\nIf this final Escape test is passed, the players have captured Gollum and won the game."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 107,
		"quantity": 1,
		"unique": true,
		"type": "objective",
		"title": "Gollum",
		"icon": "marshes",
		"traits": ["Gollum"],
		"effect": {
			"normal": "If Gollum ever has 8 or more resource tokens on him, shuffle him back into the encounter deck.",
			"forced": "At the end of the quest phase, the party must make an escape test, dealing 1 card per player from the encounter deck. If this test is failed, place 2 resource tokens on Gollum."
		}
	},
	{
		"set": "mirkwood",
		"id": 108,
		"quantity": 3,
		"type": "treachery",
		"title": "A Wisp of Pale Sheen",
		"icon": "marshes",
		"traits": ["Escape"],
		"effect": {
			"normal": "Escape: 4",
			"when revealed": "Place 2 resource tokens on Gollum. Any player may exhaust a Lore hero to reduce this effect to 1 resource token."
		}
	},
	{
		"set": "mirkwood",
		"id": 109,
		"quantity": 3,
		"type": "treachery",
		"title": "Nightfall",
		"icon": "marshes",
		"traits": ["Escape"],
		"effect": {
			"normal": "Escape: 2",
			"when revealed": "The first player makes an escape test, dealing 2 cards from the encounter deck. If this test is failed, place 1 resource token on Gollum and raise each player's threat by 2."
		}
	},
	{
		"set": "mirkwood",
		"id": 110,
		"quantity": 3,
		"type": "treachery",
		"title": "Through the Mist",
		"icon": "marshes",
		"traits": ["Escape"],
		"effect": {
			"normal": "Escape: 3",
			"when revealed": "The first player makes an escape test counting ATK instead of Willpower, dealing 2 cards from the encounter deck. If this test is failed, place 1 resource token on Gollum and raise each player's threat by 1."
		}
	},
	{
		"set": "mirkwood",
		"id": 111,
		"quantity": 4,
		"type": "treachery",
		"title": "The Lights of the Dead",
		"icon": "marshes",
		"traits": ["Escape"],
		"effect": {
			"normal": "Escape: 5",
			"when revealed": "Each player must make an escape test, dealing 2 cards from the encounter deck for each test. Each player that fails this test places 1 resource token on Gollum, and raises his threat by 1."
		}
	},
	{
		"set": "mirkwood",
		"id": 112,
		"quantity": 4,
		"type": "enemy",
		"title": "Giant Marsh Worm",
		"icon": "marshes",
		"cost": 36,
		"strength": 1,
		"attack": 3,
		"defense": 2,
		"hp": 6,
		"traits": ["Creature"],
		"effect": {
			"normal": "Escape: 2",
			"forced": "Remove 2 damage from Giant Marsh Worm at the end of each round."
		}
	},
	{
		"set": "mirkwood",
		"id": 113,
		"quantity": 4,
		"type": "location",
		"title": "Impassable Bog",
		"icon": "marshes",
		"strength": 1,
		"hp": 12,
		"traits": ["Dead Marshes"],
		"effect": {
			"normal": "Escape: 2",
			"when revealed": "Place 1 resource token on Gollum for each location card in the staging area."
		},
		"victory": 7
	},
	{
		"set": "mirkwood",
		"id": 114,
		"quantity": 4,
		"type": "location",
		"title": "The Heart of the Marshes",
		"icon": "marshes",
		"strength": 3,
		"hp": 4,
		"traits": ["Dead Marshes"],
		"effect": {
			"normal": "While The Heart of the Marshes is the active location, all cards dealt from the encounter deck for escape tests get +1 Escape. (Cards recieve this bonus even if they do not have a printed escape value.)\nEscape: 1"
		}
	},
	{
		"set": "mirkwood",
		"id": 115,
		"quantity": 4,
		"type": "location",
		"title": "Fens and Mires",
		"icon": "marshes",
		"strength": 2,
		"hp": 2,
		"traits": ["Dead Marshes"],
		"effect": {
			"normal": "Escape: 2",
			"forced": "After the players travel to this location, place 1 resource token on Gollum."
		}
	},
	{
		"set": "mirkwood",
		"id": 116,
		"quantity": 1,
		"unique": true,
		"type": "hero",
		"title": "Dain Ironfoot",
		"icon": "leadership",
		"cost": 11,
		"strength": 1,
		"attack": 2,
		"defense": 3,
		"hp": 5,
		"traits": ["Dwarf"],
		"effect": {
			"normal": "While Dain Ironfoot is ready, Dwarf characters get +1 ATK and +1 Willpower."
		}
	},
	{
		"set": "mirkwood",
		"id": 117,
		"quantity": 3,
		"type": "attachment",
		"title": "Dunedain Signal",
		"icon": "leadership",
		"cost": 1,
		"traits": ["Signal"],
		"effect": {
			"normal": "Attach to a hero.\nAttached hero gains sentinel",
			"action": "Pay 1 resource from attached hero's pool to attach Dunedain Signal to another hero."
		}
	},
	{
		"set": "mirkwood",
		"id": 118,
		"quantity": 3,
		"type": "event",
		"title": "Dawn Take You All",
		"icon": "leadership",
		"cost": 2,
		"effect": {
			"normal": "lay after shadow cards have been dealt, before any attacks have resloved.",
			"combat action": "Each player may choose and discard 1 facedown shadow card from an enemy with which he is engaged."
		}
	},
	{
		"set": "mirkwood",
		"id": 119,
		"quantity": 3,
		"type": "ally",
		"title": "Eagles of the Misty Mountains",
		"icon": "tactics",
		"cost": 4,
		"strength": 2,
		"attack": 2,
		"defense": 2,
		"hp": 4,
		"traits": ["Creature", "Eagle"],
		"effect": {
			"normal": "Eagles of the Misty Mountains cannot have restricted attachments. Eagles of the Misty Mountains gets +1 ATK and +1 DEF for each facedown attachment it has.",
			"response": "After another Eagle character leaves play, you may attach that card facedown to Eagles of the Misty Mountains."
		}
	},
	{
		"set": "mirkwood",
		"id": 120,
		"quantity": 3,
		"type": "attachment",
		"title": "Support of the Eagles",
		"icon": "tactics",
		"cost": 3,
		"traits": ["Boon"],
		"effect": {
			"normal": "Attach to a Tactics hero.",
			"action": "Exhaust Support of the Eagles to choose an Eagle ally. Until the end of the phase, attached hero adds that ally's ATK or DEF (choose 1) to its own."
		}
	},
	{
		"set": "mirkwood",
		"id": 121,
		"quantity": 3,
		"type": "ally",
		"title": "West Road Traveller",
		"icon": "spirit",
		"cost": 2,
		"strength": 2,
		"attack": 0,
		"defense": 0,
		"hp": 1,
		"traits": ["Rohan"],
		"effect": {
			"response": "After you play West Road Traveller from your hand, switch the active location with any other location in the staging area."
		}
	},
	{
		"set": "mirkwood",
		"id": 122,
		"quantity": 3,
		"type": "event",
		"title": "Astonishing Speed",
		"icon": "spirit",
		"cost": 3,
		"effect": {
			"action": "Until the end of the phase, all Rohan characters get +2 Willpower"
		}
	},
	{
		"set": "mirkwood",
		"id": 123,
		"quantity": 3,
		"type": "ally",
		"title": "Mirkwood Runner",
		"icon": "lore",
		"cost": 3,
		"strength": 1,
		"attack": 2,
		"defense": 0,
		"hp": 2,
		"traits": ["Silvan", "Scout"],
		"effect": {
			"normal": "While Mirkwood Runner is attacking alone, the defending enemy does not count its DEF."
		}
	},
	{
		"set": "mirkwood",
		"id": 124,
		"quantity": 3,
		"type": "event",
		"title": "Rumour from the Earth",
		"icon": "lore",
		"cost": 0,
		"effect": {
			"action": "Look at the top card of the encounter deck. Then, you may pay 1 Lore resource to return Rumour from the Earth to your hand."
		}
	},
	{
		"set": "mirkwood",
		"id": 125,
		"quantity": 3,
		"type": "event",
		"title": "Shadow of the Past",
		"icon": "neural",
		"cost": 2,
		"effect": {
			"action": "Move the top card of the encounter discard pile to the top of the encounter deck."
		}
	},
	{
		"set": "mirkwood",
		"id": 126,
		"quantity": 1,
		"type": "quest",
		"title": "Through the Forest",
		"icon": "return",
		"hp": 12,
		"effect": {
			"A": {
				"normal": "Having captured Gollum, you must now escort him through Mirkwood Forest for interrogation at Thranduil's Palace.",
				"setup": "Search the encounter deck for Gollum. Choose a player to guard Gollum at the start of the game, and place Gollum in front of that player. Then shuffle the encounter deck. Reveal 1 card per player from the encounter deck, and add it to the staging area."
			},
			"B": {
				"normal": "Mirkwood is always a dangerous place, but it is even worse with Gollum. Between the outbursts, tantrums, and the flying provisions, you are not afforded a moment's peace."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 127,
		"quantity": 1,
		"type": "quest",
		"title": "Escape Attempt",
		"icon": "return",
		"hp": 3,
		"effect": {
			"A": {
				"normal": "As soon as he thinks that no one is watching, Gollum attempts to slip his bonds and escape."
			},
			"B": {
				"normal": "The player guarding Gollum cannot commit characters to this quest (unless he is the only player remaining in the game).\nIf the players quest unsuccessfully, Gollum escapes and the players have lost the game."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 128,
		"quantity": 1,
		"type": "quest",
		"title": "To the Elvin King's Halls",
		"icon": "return",
		"hp": 7,
		"effect": {
			"A": {
				"normal": "Having thwarted Gollum's escape attempt, you tighten his rope and push on through Mirkwood, to Thranduil's palace."
			},
			"B": {
				"normal": "The player guarding Gollum cannot play cards from his hand."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 129,
		"quantity": 1,
		"type": "quest",
		"title": "Ambush",
		"icon": "return",
		"hp": 2,
		"effect": {
			"A": {
				"normal": "As you make the final push to Thranduil's Palace, your enemies make a desperate attempt to ambush your party, and seize Gollum for themselves."
			},
			"B": {
				"forced": "At the beginning of the combat phase, all enemies in play engage the player guarding Gollum.",
				"normal": "Players cannot defeat this stage if there are any enemies in play. If players defeat this stage, they have won the game."
			}
		}
	},
	{
		"set": "mirkwood",
		"id": 130,
		"quantity": 1,
		"unique": true,
		"type": "objective",
		"title": "Gollum",
		"icon": "return",
		"hp": 5,
		"traits": ["Creature"],
		"effect": {
			"normal": "Damage from undefended attacks against you must be dealt to Gollum. If Gollum is destroyed, or if the player guarding Gollum is eliminated, the players have lost the game.",
			"forced": "At the end of each round, raise the threat of the player guarding Gollum by 3. Then, that player may choose a new player to guard Gollum."
		}
	},
	{
		"set": "mirkwood",
		"id": 131,
		"quantity": 4,
		"type": "location",
		"title": "The Spider's Ring",
		"icon": "return",
		"strength": 3,
		"hp": 2,
		"traits": ["Forest"],
		"effect": {
			"normal": "While The Spider's Ring is the active location, the player guarding Gollum cannot change.",
			"shadow": "If this attack is undefended, return any current active location to the staging area. The Spider's Ring becomes the active location."
		}
	},
	{
		"set": "mirkwood",
		"id": 132,
		"quantity": 3,
		"type": "location",
		"title": "Dry Watercourse",
		"icon": "return",
		"strength": 2,
		"hp": 2,
		"traits": ["Forest"],
		"effect": {
			"normal": "While Dry Watercourse is the active location, all treachery card effects that target the player guarding Gollum also target each other player."
		}
	},
	{
		"set": "mirkwood",
		"id": 133,
		"quantity": 3,
		"type": "location",
		"title": "Woodman's Glade",
		"icon": "return",
		"strength": 2,
		"hp": 2,
		"traits": ["Forest"],
		"effect": {
			"travel": "The player guarding Gollum must exhaust a hero he controls to travel to Woodman's Glade.",
			"response": "After exploring Woodman's Glade, reduce the threat of each player not guarding Gollum by 2."
		}
	},
	{
		"set": "mirkwood",
		"id": 134,
		"quantity": 3,
		"type": "location",
		"title": "Wood Elf Path",
		"icon": "return",
		"strength": 1,
		"hp": 3,
		"traits": ["Forest"],
		"effect": {
			"response": "After the players travel to Wood Elf Path, the player guarding Gollum may choose a new player to guard him."
		}
	},
	{
		"set": "mirkwood",
		"id": 135,
		"quantity": 2,
		"type": "treachery",
		"title": "Gollum's Anguish",
		"icon": "return",
		"traits": ["Tantrum"],
		"effect": {
			"when revealed": "Raise the threat of the player guarding Gollum by 8. That player must choose a new player to guard Gollum, if able.",
			"shadow": "Raise the threat of the player guarding Gollum by 4."
		}
	},
	{
		"set": "mirkwood",
		"id": 136,
		"quantity": 2,
		"type": "treachery",
		"title": "Gollum's Bite",
		"icon": "return",
		"traits": ["Tantrum"],
		"effect": {
			"when revealed": "Deal 4 damage to a hero controlled by the player guarding Gollum. That player must choose a new player to guard Gollum, if able.",
			"shadow": "Deal 2 damage to a hero controlled by the player guarding Gollum."
		}
	},
	{
		"set": "mirkwood",
		"id": 137,
		"quantity": 3,
		"type": "treachery",
		"title": "Wasted Provisions",
		"icon": "return",
		"traits": ["Tantrum"],
		"effect": {
			"when revealed": "Discard the top 10 cards from the deck of the player guarding Gollum. That player must choose a new player to guard Gollum, if able.",
			"shadow": "Discard the top 5 cards from the deck of the player guarding Gollum."
		}
	},
	{
		"set": "mirkwood",
		"id": 138,
		"quantity": 4,
		"type": "enemy",
		"title": "Mirkwood Bats",
		"icon": "return",
		"cost": 22,
		"strength": 1,
		"attack": 1,
		"defense": 1,
		"hp": 1,
		"traits": ["Creature"],
		"effect": {
			"normal": "Surge.",
			"forced": "After Mirkwood Bats engages a player, deal 1 damage to each character controlled by the player guarding Gollum."
		}
	},
	{
		"set": "mirkwood",
		"id": 139,
		"quantity": 3,
		"type": "enemy",
		"title": "Attercop, Attercop",
		"icon": "return",
		"cost": 44,
		"strength": 2,
		"attack": 8,
		"defense": 4,
		"hp": 6,
		"traits": ["Creature", "Spider"],
		"effect": {
			"forced": "At the beginning of the encounter phase, Attercop, Attercop automatically engages the player guarding Gollum, regardless of his threat."
		}
	}
]