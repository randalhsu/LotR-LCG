[
	{
		"set": "dwarrowdelf",
		"id": 0,
		"type": null,
		"icon": null,
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
		"icon": "neural",
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
	}
]