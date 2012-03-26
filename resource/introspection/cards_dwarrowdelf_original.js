[
	{
		"set": "dwarrowdelf",
		"id": 0,
		"type": "iDontCare",
		"icon": "iDontCare",
		"why": "programmers count from zero"
	},
	{
		"set": "dwarrowdelf",
		"id": 1,
		"quantity": 1,
		"unique": true,
		"type": "hero",
		"title": "Elrohir",
		"icon": "leadership",
		"cost": 10,
		"strength": 2,
		"attack": 2,
		"defense": 1,
		"hp": 4,
		"traits": ["Noldor", "Noble", "Ranger"],
		"effect": {
			"normal": "While Elladan is in play, Elrohir gets +2 DEF.",
			"response": "After Elrohir is declared as a defender, pay 1 resource from his resource pool to ready him."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 2,
		"quantity": 3,
		"type": "event",
		"title": "Taking Initiative",
		"icon": "leadership",
		"cost": 0,
		"effect": {
			"action": "Discard the top card of your deck. If the discarded card's printed cost is equal to or higher than the number of characters you control, draw 2 cards and deal 2 damage to any enemy."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 3,
		"quantity": 3,
		"type": "event",
		"title": "Timely Aid",
		"icon": "leadership",
		"cost": 4,
		"effect": {
			"normal": "Secrecy 3.",
			"action": "Reveal the top 5 cards of your deck and put 1 revealed ally into play, if able. Shuffle all other revealed cards back into your deck."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 4,
		"quantity": 3,
		"type": "event",
		"title": "Unseen Strike",
		"icon": "tactics",
		"cost": 0,
		"effect": {
			"action": "Choose a character you control. Until the end of the phase, that character gets +3 ATK while attaching an enemy with a higher engagement cost than your threat."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 5,
		"quantity": 3,
		"type": "attachment",
		"title": "Keeping Count",
		"icon": "tactics",
		"cost": 0,
		"effect": {
			"normal": "Attach to a hero. Limit 1 per hero.\nAttached hero gets +1 ATK for each resource token on another copy of Keeping Count that is above the current number of resource tokens on this card.",
			"forced": "After attached hero attacks and destroys an enemy, place 1 resource token on this card."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 6,
		"quantity": 3,
		"unique": true,
		"type": "ally",
		"title": "Bofur",
		"icon": "spirit",
		"cost": 3,
		"strength": 2,
		"attack": 1,
		"defense": 1,
		"hp": 3,
		"traits": ["Dwarf"],
		"effect": {
			"quest action": "Spend 1 Spirit resource to put Bofur into play from your hand, exhausted and committed to a quest. If you quest successfully this phase and Bofur is still in play, return him to your hand."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 7,
		"quantity": 3,
		"type": "event",
		"title": "Renewed Friendship",
		"icon": "spirit",
		"cost": 0,
		"effect": {
			"response": "After another player plays an attachment on a hero you control, you may (choose 1): ready 1 of that player's heroes, have that player draw 1 card, or lower that player's threat by 2."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 8,
		"quantity": 3,
		"type": "ally",
		"title": "Ravenhill Scout",
		"icon": "lore",
		"cost": 3,
		"strength": 0,
		"attack": 1,
		"defense": 1,
		"hp": 3,
		"traits": ["Dale", "Scout"],
		"effect": {
			"action": "Exhaust Ravenhill Scout to move up to 2 progress tokens from 1 location to another location."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 9,
		"quantity": 3,
		"type": "event",
		"title": "Needful to Know",
		"icon": "lore",
		"cost": 2,
		"effect": {
			"normal": "Secrecy 2.",
			"action": "Raise your threat by 1 to look at the top card of the encounter deck. Then, reduce your threat by X, where X is the threat of that card."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 10,
		"quantity": 3,
		"type": "attachment",
		"title": "Good Meal",
		"icon": "neutral",
		"cost": 0,
		"effect": {
			"normal": "Attach to a Hobbit hero.",
			"action": "Discard Good Meal to lower the cost of the next event you play this round that matches attached hero's sphere by 2."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 11,
		"quantity": 1,
		"type": "quest",
		"title": "Up the Pass",
		"icon": "redhorn",
		"hp": 9,
		"effect": {
			"A": {
				"normal": "Celeborn has bid you escort Arwen to visit her father in Rivendell. Your journey takes you through the Redhorn Gate...",
				"setup": "Add Caradhras to the staging area. Remove all copies of Snowstorm from the encounter deck and set them aside, out of play. Put Arwen Undomiel into play under the control of the first player."
			},
			"B": {
				"when revealed": "Reveal 1 card from the encounter deck per player, and add it to the staging area."
			}
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 12,
		"quantity": 1,
		"type": "quest",
		"title": "Snowdrifts",
		"icon": "redhorn",
		"hp": 11,
		"effect": {
			"A": {
				"normal": "Progress slows as you meet the fury of the mountains. Sudden snows fall heavy around you, and a bitter wind howls down from the peaks. You uncover a shallow depression in the snow, filled with frozen remains. Some of them bear strange markings, as if they had been burned with flame. How many other doomed souls lie beneath the quickly rising drifts?"
			},
			"B": {
				"when revealed": "Shuffle 1 more copy of Snowstorm into the encounter deck than the number of players in the game.",
				"forced": "After placing the 11th progress token on Snowdrifts, discard any active location. Caradhras becomes the active location."
			}
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 13,
		"quantity": 1,
		"type": "quest",
		"title": "The Mountains' Peaks",
		"icon": "redhorn",
		"hp": 13,
		"effect": {
			"A": {
				"normal": "The mountain peaks are almost in reach, but the swirling snows make it difficult to see, and your strength begins to drain away with the daunting final push to the pinnacle."
			},
			"B": {
				"when revealed": "Shuffle all copies of Snowstorm in the encounter discard pile back into the encounter deck.\nCharacters are discarded from play if their Willpower is ever 0.\nPlayers cannot defeat this stage unlress they have 5 victory points. If the players defeat this stage, they have won the game."
			}
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 14,
		"quantity": 1,
		"unique": true,
		"type": "objective",
		"title": "Arwen Undomiel",
		"icon": "redhorn",
		"traits": ["Noldor", "Noble", "Ally"],
		"effect": {
			"normal": "The first player gains control of Arwen Undomiel, as an ally.\nIf Arwen Undomiel leaves play, the players are defeated.",
			"response": "After Arwen Undomiel exhausts, choose a hero. Add 1 resource to that hero's resource pool."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 15,
		"quantity": 1,
		"unique": true,
		"type": "location",
		"title": "Caradhras",
		"icon": "redhorn",
		"strength": 3,
		"hp": 9,
		"traits": ["Mountain", "Snow"],
		"effect": {
			"normal": "While Caradhras is the active location, questing characters get -1 Willpower.\nPlayers cannot travel to Caradhras except by quest card effects."
		},
		"victory": 3
	},
	{
		"set": "dwarrowdelf",
		"id": 16,
		"quantity": 1,
		"unique": true,
		"type": "location",
		"title": "Fanuidhol",
		"icon": "redhorn",
		"strength": 3,
		"hp": 7,
		"traits": ["Mountain", "Snow"],
		"effect": {
			"normal": "While Fanuidhol is the active loction, heroes must spend 1 resource from their resource pool to count their Willpower during the quest phase."
		},
		"victory": 2
	},
	{
		"set": "dwarrowdelf",
		"id": 17,
		"quantity": 1,
		"unique": true,
		"type": "location",
		"title": "Celebdil",
		"icon": "redhorn",
		"strength": 3,
		"hp": 7,
		"traits": ["Mountain", "Snow"],
		"effect": {
			"normal": "While Celebdil is the active location, remove 2 progress tokens from it at the end of each round."
		},
		"victory": 2
	},
	{
		"set": "dwarrowdelf",
		"id": 18,
		"quantity": 1,
		"unique": true,
		"type": "location",
		"title": "The Dimrill Stair",
		"icon": "redhorn",
		"strength": 2,
		"hp": 3,
		"traits": ["Stair"],
		"effect": {
			"travel": "Reshuffle all locations in the discard pile and victory display back into the encounter deck. If you reshuffled at least two locations, reduce each player's threat by 11 and discard all copies of Freezing Cold from play."
		},
		"victory": 1
	},
	{
		"set": "dwarrowdelf",
		"id": 19,
		"quantity": 3,
		"type": "location",
		"title": "Rocky Crags",
		"icon": "redhorn",
		"strength": 4,
		"hp": 2,
		"traits": ["Mountain"],
		"effect": {
			"travel": "Each player must deal 2 damage to 1 character he controls to travel here.",
			"shadow": "Attacking enemy gets +1 ATK for each progress token on the active location."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 20,
		"quantity": 2,
		"type": "treachery",
		"title": "Fell Voices",
		"icon": "redhorn",
		"effect": {
			"when revealed": "Return the top 2 Snow cards in the encounter discard pile to the top of the encounter deck. If this effect returned less than 2 Snow treachery cards, Fell Voices gains surge."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 21,
		"quantity": 2,
		"type": "treachery",
		"title": "Fallen Stones",
		"icon": "redhorn",
		"effect": {
			"when revealed": "The first player (choose 1): removes all progress tokens from play, or reveals 2 cards from the encounter deck and adds them to the staging area.",
			"shadow": "Attacking enemy gets +1 ATK for each progress token on the active location."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 22,
		"quantity": 5,
		"type": "treachery",
		"title": "Snowstorm",
		"icon": "redhorn",
		"traits": ["Snow"],
		"effect": {
			"when revealed": "Each questing character gets -1 Willpower until the end of the phase.",
			"shadow": "Until the end of the phase, characters defending this attack get -1 Willpower and are discarded if their Willpower is 0."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 23,
		"quantity": 3,
		"type": "treachery",
		"title": "Freezing Cold",
		"icon": "redhorn",
		"traits": ["Snow"],
		"effect": {
			"when revealed": "The first player attaches this card to a hero he controls. Counts as a Condition Attachment with the text: \"Attached hero gets -2 Willpower and cannot commit to a quest. If attached hero has more than 1 copy of Freezing Cold attached, discard attached hero from play.\""
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 24,
		"quantity": 1,
		"type": "treachery",
		"title": "Avalanche!",
		"icon": "redhorn",
		"traits": ["Snow"],
		"effect": {
			"when revealed": "Exhaust each ready character and if it is the quest phase commit them to the quest."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 25,
		"quantity": 3,
		"type": "enemy",
		"title": "Mountain Goblin",
		"icon": "redhorn",
		"cost": 25,
		"strength": 1,
		"attack": 2,
		"defense": 2,
		"hp": 3,
		"traits": ["Goblin", "Orc"],
		"effect": {
			"normal": "Mountain Goblin gets +1 ATK for each Mountain location in the staging area.",
			"shadow": "Attacking enemy gets +1 ATK. (+2 ATK instead if the active location is a Mountain.)"
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 26,
		"quantity": 2,
		"type": "enemy",
		"title": "Mountain Troll",
		"icon": "redhorn",
		"cost": 35,
		"strength": 2,
		"attack": 5,
		"defense": 5,
		"hp": 7,
		"traits": ["Troll"],
		"effect": {
			"normal": "Mountain Troll gets +1 ATK for each Mountain location in the staging area.",
			"shadow": "Attacking enemy gets +1 ATK. (+2 ATK instead if the active location is a Mountain.)"
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 27,
		"quantity": 3,
		"type": "enemy",
		"title": "Snow Warg",
		"icon": "redhorn",
		"cost": 28,
		"strength": 3,
		"attack": 3,
		"defense": 1,
		"hp": 4,
		"traits": ["Creature", "Snow"],
		"effect": {
			"normal": "Allies cannot defend while Snow Warg is attacking.",
			"forced": "When Snow Warg attacks, deal 1 damage to the defending character, if able."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 28,
		"quantity": 1,
		"unique": true,
		"type": "hero",
		"title": "Elladan",
		"icon": "tactics",
		"cost": 10,
		"strength": 2,
		"attack": 1,
		"defense": 2,
		"hp": 4,
		"traits": ["Noldor", "Noble", "Ranger"],
		"effect": {
			"normal": "While Elrohir is in play, Elladan gets +2 ATK.",
			"response": "After Elladan is declared as an attacker, pay 1 resource from his resource pool to ready him."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 29,
		"quantity": 3,
		"type": "ally",
		"title": "Dunedain Wanderer",
		"icon": "leadership",
		"cost": 5,
		"strength": 1,
		"attack": 2,
		"defense": 2,
		"hp": 2,
		"traits": ["Dunedain", "Ranger"],
		"effect": {
			"normal": "Ranged. Sentinel. Secrecy 3."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 30,
		"quantity": 3,
		"type": "event",
		"title": "Lure of Moria",
		"icon": "leadership",
		"cost": 3,
		"effect": {
			"action": "Ready all Dwarf characters."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 31,
		"quantity": 3,
		"type": "attachment",
		"title": "Rivendell Blade",
		"icon": "tactics",
		"cost": 1,
		"traits": ["Item", "Weapon"],
		"effect": {
			"normal": "Attach to a Noldor or Silvan character.\nRestricted.\nWhen attached character attacks an enemy, that enemy gets -2 DEF until the end of the phase."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 32,
		"quantity": 3,
		"type": "event",
		"title": "Hail of Stones",
		"icon": "tactics",
		"cost": 1,
		"effect": {
			"action": "Exhaust X characters to deal X damage to an enemy in the staging area."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 33,
		"quantity": 3,
		"type": "ally",
		"title": "Rider of the Mark",
		"icon": "spirit",
		"cost": 3,
		"strength": 2,
		"attack": 1,
		"defense": 1,
		"hp": 2,
		"traits": ["Rohan"],
		"effect": {
			"action": "Spend 1 Spirit resource to give control of Rider of the Mark to another player. (Limit once per round.)",
			"response": "After Rider of the Mark changes control, discard a shadow card dealt to an enemy you are engaged with."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 34,
		"quantity": 3,
		"type": "attachment",
		"title": "Song of Earendil",
		"icon": "spirit",
		"cost": 1,
		"traits": ["Song"],
		"effect": {
			"normal": "Attach to a Spirit hero.",
			"response": "After Song of Earendil enters play, draw 1 card.\nAfter another player raises his threat, raise your threat by 1 to reduce that player's threat by 1."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 35,
		"quantity": 3,
		"unique": true,
		"type": "ally",
		"title": "Bombur",
		"icon": "lore",
		"cost": 3,
		"strength": 0,
		"attack": 0,
		"defense": 1,
		"hp": 3,
		"traits": ["Dwarf"],
		"effect": {
			"action": "Exhaust Bombur to choose a location. That location gets -1 Threat until the end of the phase. (That location does not contribute its Threat instead if it is an Underground location.)"
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 36,
		"quantity": 3,
		"type": "event",
		"title": "Out of the Wild",
		"icon": "lore",
		"cost": 3,
		"effect": {
			"normal": "Secrecy 2.",
			"action": "Search the top 5 cards of the encounter deck for any 1 non-objective card worth no victory points and add it to your victory display. Shuffle the encounter deck."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 37,
		"quantity": 3,
		"type": "event",
		"title": "The End Comes",
		"icon": "neutral",
		"cost": 0,
		"effect": {
			"response": "After a Dwarf character leaves play, shuffle the encounter discard pile back into the encounter deck."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 38,
		"quantity": 1,
		"type": "quest",
		"title": "Along the Misty Mountains",
		"icon": "rivendell",
		"hp": 20,
		"effect": {
			"A": {
				"normal": "Your party has braved the snows of the pass, but now must travel North along the Misty Mountains for league upon league as you escort Arwen to her father's house.",
				"setup": "Put Arwen Undomiel into play under the control of the first player. Shuffle the encounter deck. Reveal 1 card from the encounter deck per player, and add them to the staging area."
			},
			"B": {
				"normal": "This is a wild and perilous country, and it is dangerous to follow the roads. The mountains rise up on the right, impassively watching your slow trek among their foothills."
			}
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 39,
		"quantity": 1,
		"type": "quest",
		"title": "Orc Outpost",
		"icon": "rivendell",
		"hp": 7,
		"effect": {
			"A": {
				"normal": "Heavy rain drives you to seek shelter among the caves of the mountains. They are dry, and the fire you start seeps into your bones and restores your spirit. Your eyes are heavy when teh soft clatter of falling pebbles reaches your ears. Perhaps you are not alone."
			},
			"B": {
				"when revealed": "Search the encounter deck and discard pile for Goblin Gate and add it to the staging area, if able. Then, if there is no active location, Goblin Gate becomes the active location."
			}
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 40,
		"quantity": 1,
		"type": "quest",
		"title": "Approaching Rivendell",
		"icon": "rivendell",
		"hp": 13,
		"effect": {
			"A": {
				"normal": "Orcs and other creatures have hounded you since fighting your way free of the orc outpost. Soon you will reach the safety of Rivendell's borders, but supplies have dwindled and you are dead weary from sleepless nights of keeping watch, as dark forms shadow your camp."
			},
			"B": {
				"when revealed": "Reveal 1 card from the encounter deck per player, and add it to the staging area.\nCharacters cannot be healed.\nIf the players defeat this stage, they have won the game."
			}
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 41,
		"quantity": 1,
		"unique": true,
		"type": "objective",
		"title": "Arwen Undomiel",
		"icon": "rivendell",
		"traits": ["Noldor", "Noble", "Ally"],
		"effect": {
			"normal": "The first player gains control of Arwen Undomiel, as an ally.\nIf Arwen Undomiel leaves play, the players are defeated.",
			"response": "After Arwen Undomiel exhausts, choose a hero. Add 1 resource to that hero's resource pool."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 42,
		"quantity": 2,
		"type": "location",
		"title": "Ruined Road",
		"icon": "rivendell",
		"strength": 1,
		"hp": 5,
		"traits": ["Road"],
		"effect": {
			"response": "After you travel to Ruined Road, the first player places 2 progress tokens on it or readies 1 hero he controls.",
			"shadow": "Return attacking enemy to the staging area after it attacks."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 43,
		"quantity": 1,
		"type": "location",
		"title": "Goblin Gate",
		"icon": "rivendell",
		"strength": 5,
		"hp": 4,
		"traits": ["Gate"],
		"effect": {
			"normal": "While Goblin Gate is the active location, the first enemy revealed from the encounter deck each round gains ambush. If that enemy engages a player, it makes an immediate attack (deal and resolve a shadow card)."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 44,
		"quantity": 3,
		"type": "location",
		"title": "Pathless Country",
		"icon": "rivendell",
		"strength": 3,
		"hp": 5,
		"traits": ["Hills"],
		"effect": {
			"forced": "After at least 1 progress token is placed on Pathless Country, remove 1 progress token from it.",
			"shadow": "Deal 1 damage to each ally in play."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 45,
		"quantity": 2,
		"type": "location",
		"title": "Barren Hills",
		"icon": "rivendell",
		"strength": 2,
		"hp": 4,
		"traits": ["Hills"],
		"effect": {
			"normal": "While Barren Hills is the active location, ignore ambush.",
			"shadow": "Return attacking enemy to the staging area after it attacks."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 46,
		"quantity": 2,
		"type": "treachery",
		"title": "Sleeping Sentry",
		"icon": "rivendell",
		"effect": {
			"when revealed": "Deal 1 damage to each exhausted character. Then, exhaust all ready characters.",
			"shadow": "Defending player must discard all exhausted characters he controls."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 47,
		"quantity": 3,
		"type": "treachery",
		"title": "Followed by Night",
		"icon": "rivendell",
		"effect": {
			"when revealed": "The first player (choose 1): deals 1 damage to all allies in play and Followed by Night gains surge, or all enemies engaged with players make an immediate attack, if able.",
			"shadow": "Return attacking enemy to the staging area after it attacks."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 48,
		"quantity": 2,
		"type": "treachery",
		"title": "Orc Ambush",
		"icon": "rivendell",
		"effect": {
			"normal": "Surge.",
			"when revealed": "All Orc enemies in the staging area engage the first player. If there are no Orc enemies in the staging area, return all Orc enemies in the encounter discard pile to the staging area, if able."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 49,
		"quantity": 4,
		"type": "enemy",
		"title": "Goblin Taskmaster",
		"icon": "rivendell",
		"cost": 27,
		"strength": 2,
		"attack": 2,
		"defense": 2,
		"hp": 4,
		"traits": ["Goblin", "Orc"],
		"effect": {
			"normal": "Ambush (After this enemy enters play, each player makes an engagement check against it.)",
			"forced": "After Goblin Taskmaster engages a player, that player deals 2 damage to 1 character he controls."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 50,
		"quantity": 3,
		"type": "enemy",
		"title": "Orc Raiders",
		"icon": "rivendell",
		"cost": 21,
		"strength": 1,
		"attack": 3,
		"defense": 1,
		"hp": 3,
		"traits": ["Orc"],
		"effect": {
			"normal": "Ambush (After this enemy enters play, each player makes an engagement check against it.)",
			"forced": "After Orc Raiders engages a player, that player discards 2 attachments he controls, if able."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 51,
		"quantity": 3,
		"type": "enemy",
		"title": "Crebain",
		"icon": "rivendell",
		"cost": 35,
		"strength": 2,
		"attack": 0,
		"defense": 0,
		"hp": 3,
		"traits": ["Creature"],
		"effect": {
			"normal": "Surge.\nWhile Crebain is in the staging area, encounter card effects cannot be canceled.",
			"shadow": "Return attacking enemy to the staging area after it attacks."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 52,
		"quantity": 3,
		"type": "enemy",
		"title": "Wild Bear",
		"icon": "rivendell",
		"cost": 34,
		"strength": 0,
		"attack": 2,
		"defense": 3,
		"hp": 5,
		"traits": ["Creature"],
		"effect": {
			"normal": "Ambush (After this enemy enters play, each player makes an engagement check against it.)",
			"forced": "After Wild Bear engages a player, it makes an immediate attack."
		}
	}
]