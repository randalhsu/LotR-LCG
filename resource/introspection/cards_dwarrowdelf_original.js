[
	{
		"set": "dwarrowdelf",
		"id": 0,
		"quantity": 4,
		"type": "treachery",
		"title": "Wrapped!",
		"icon": "watcher",
		"effect": {
			"when revealed": "The first player attaches Wrapped! to a hero he controls. (Counts as a Tentacle attachment with the text: \"Limit 1 per hero. Attached hero cannot exhaust or ready. At the end of the round, discard attached hero from play. Combat Action: Exhaust a hero you control without a Tentacle attachment to discard Wrapped!.\")"
		}
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
	},
	{
		"set": "dwarrowdelf",
		"id": 53,
		"quantity": 1,
		"unique": true,
		"type": "hero",
		"title": "Aragorn",
		"icon": "lore",
		"cost": 12,
		"strength": 2,
		"attack": 3,
		"defense": 2,
		"hp": 5,
		"traits": ["Dunedain", "Ranger"],
		"effect": {
			"normal": "Sentinel.",
			"refresh action": "Reduce your threat to your starting threat level. (Limit once per game.)"
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 54,
		"quantity": 3,
		"type": "event",
		"title": "Grave Cairn",
		"icon": "leadership",
		"cost": 1,
		"effect": {
			"response": "After a character leaves play, add its Attack to another characters Attack until the end of the round."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 55,
		"quantity": 3,
		"type": "attachment",
		"title": "Sword that was Broken",
		"icon": "leadership",
		"cost": 3,
		"traits": ["Artifact"],
		"effect": {
			"normal": "Attach to a hero.\nAttached hero gains a Leadership resource icon.\nIf attached hero is Aragorn, each character you control gets +1 Willpower."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 56,
		"quantity": 3,
		"type": "ally",
		"title": "Watcher of the Bruinen",
		"icon": "tactics",
		"cost": 2,
		"strength": 0,
		"attack": 1,
		"defense": 2,
		"hp": 2,
		"traits": ["Noldor", "Warrior"],
		"effect": {
			"normal": "Sentinel.\nWatcher of the Bruinen does not exhaust to defend.",
			"forced": "After Watcher of the Bruinen defends, either discard it from play or discard 1 card from your hand."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 57,
		"quantity": 3,
		"type": "attachment",
		"title": "Rivendell Bow",
		"icon": "tactics",
		"cost": 1,
		"traits": ["Item", "Weapon"],
		"effect": {
			"normal": "Attach to a Noldor or Silvan character, or to Aragorn. Limit 1 per character.\nAttached character gains ranged.\nIf attached character has a printed ranged keyword, it gets +1 Attack during a ranged attack."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 58,
		"quantity": 3,
		"type": "ally",
		"title": "Arwen Undomiel",
		"icon": "spirit",
		"cost": 2,
		"strength": 2,
		"attack": 0,
		"defense": 1,
		"hp": 2,
		"traits": ["Noldor", "Noble"],
		"effect": {
			"response": "After Arwen Undomiel exhausts, choose a character. That character gains sentinel and +1 Defense until the end of the round."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 59,
		"quantity": 3,
		"type": "event",
		"title": "Elrond's Counsel",
		"icon": "spirit",
		"cost": 0,
		"effect": {
			"action": "If you control a unique Noldor character, give another character +1 Willpower until the end of the phase and lower your threat by 3."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 60,
		"quantity": 3,
		"type": "event",
		"title": "Short Cut",
		"icon": "lore",
		"cost": 1,
		"effect": {
			"response": "After a location enters play, exhaust a Hobbit character to shuffle that location back into the encounter deck. Then, reveal 1 card from the encounter deck and add it to the staging area."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 61,
		"quantity": 3,
		"type": "attachment",
		"title": "Legacy of Durin",
		"icon": "lore",
		"cost": 1,
		"traits": ["Condition"],
		"effect": {
			"normal": "Attach to a Dwarf hero.",
			"response": "After you play a Dwarf character from your hand, draw 1 card."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 62,
		"quantity": 3,
		"type": "attachment",
		"title": "Resourceful",
		"icon": "neutral",
		"cost": 4,
		"effect": {
			"normal": "Secrecy 3.\nAttach to a hero you control.\nAttached hero collects 1 additional resource during the resource phase each round."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 63,
		"quantity": 1,
		"type": "quest",
		"title": "To the West-Door",
		"icon": "watcher",
		"hp": 13,
		"effect": {
			"A": {
				"normal": "Elrond has asked you to scout the Mines of Moria on your return to Lorien, hoping to discover if it is the source of increased Orc activity along the Misty Mountains.",
				"setup": "Remove The Watcher and Doors of Durin from the encounter deck and set them aside, out of play."
			},
			"B": {
				"when revealed": "Reveal cards from the top of the encounter deck and add them to the staging area until there is at least X Threat in the staging area. X is twice the number of players in the game."
			}
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 64,
		"quantity": 1,
		"type": "quest",
		"title": "The Seething Lake",
		"icon": "watcher",
		"hp": 5,
		"effect": {
			"A": {
				"normal": "The others swung round and saw the waters of the lake seething, as if a host of snakes were swimming up from the southern end. - The Fellowship of the Ring\nThe Doors of Durin are blocked by an ancient spell. You must figure out a way into the mines before the Seething bog and its Watcher consumes you all."
			},
			"B": {
				"when revealed": "Add The Watcher to the staging area. Doors of Durin becomes the active location, moving any previous active location to the staging area. Shuffle all Tentacle cards in the encounter discard pile back into the encounter deck.\nIf the players have at least 3 victory points and defeat this stage, they have won the game."
			}
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 65,
		"quantity": 1,
		"unique": true,
		"type": "location",
		"title": "Doors of Durin",
		"icon": "watcher",
		"strength": 2,
		"hp": -1,
		"traits": ["Gate"],
		"effect": {
			"normal": "Progress tokens that would be placed on Doors of Durin are instead placed on the current quest card.",
			"action": "Each player may discard any number of cards from his hand. Then, discard the top card of the encounter deck. If the first letter of the encounter card's title matches that of one of the discarded player cards, add Doors of Durin to your victory display. (Limit once per round.)"
		},
		"victory": 3
	},
	{
		"set": "dwarrowdelf",
		"id": 66,
		"quantity": 1,
		"type": "location",
		"title": "Stair Falls",
		"icon": "watcher",
		"strength": 2,
		"hp": 4,
		"traits": ["Stair"],
		"effect": {
			"travel": "The first player must exhaust 2 characters to travel here.",
			"shadow": "Remove 1 progress token from the current quest."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 67,
		"quantity": 2,
		"type": "location",
		"title": "Perilous Swamp",
		"icon": "watcher",
		"strength": 4,
		"hp": 2,
		"traits": ["Swamp"],
		"effect": {
			"normal": "No more than 1 progress token can be placed on Perilous Swamp each round.",
			"shadow": "Remove 1 progress token from the current quest."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 68,
		"quantity": 2,
		"type": "location",
		"title": "Makeshift Passage",
		"icon": "watcher",
		"strength": 1,
		"hp": 5,
		"traits": ["Swamp"],
		"effect": {
			"forced": "After you travel to Makeshift Passage, place 2 progress tokens on the current quest card, bypassing any active location."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 69,
		"quantity": 3,
		"type": "location",
		"title": "Stagnant Creek",
		"icon": "watcher",
		"strength": 3,
		"hp": 3,
		"traits": ["Swamp"],
		"effect": {
			"when revealed": "Discard the top card of the encounter deck. If the discarded card is a Tentacle enemy, add that card to the staging area and raise each player's threat by 5."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 70,
		"quantity": 1,
		"type": "treachery",
		"title": "Ill Purpose",
		"icon": "watcher",
		"effect": {
			"when revealed": "All enemies in the staging area engage the player with the highest threat. Then, each player raises his threat by the total Threat of all cards in the staging area.",
			"shadow": "Attacking enemy gets +1 Attack. (+3 Attack instead of it is a Tentacle.)"
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 71,
		"quantity": 3,
		"type": "treachery",
		"title": "Disturbed Waters",
		"icon": "watcher",
		"effect": {
			"normal": "Doomed 5."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 72,
		"quantity": 1,
		"unique": true,
		"type": "enemy",
		"title": "The Watcher",
		"icon": "watcher",
		"cost": 48,
		"strength": 4,
		"attack": 5,
		"defense": 7,
		"hp": 9,
		"traits": ["Creature", "Tentacle"],
		"effect": {
			"normal": "Regenerate 2. While there is another Tentacle enemy in play, The Watcher cannot be optionally engaged.\nIf The Watcher is in the staging area at the end of the combat phase, each player must deal 3 damage to 1 character he controls."
		},
		"victory": 3
	},
	{
		"set": "dwarrowdelf",
		"id": 73,
		"quantity": 4,
		"type": "enemy",
		"title": "Grasping Tentacle",
		"icon": "watcher",
		"cost": 12,
		"strength": 2,
		"attack": 3,
		"defense": 0,
		"hp": 3,
		"traits": ["Tentacle"],
		"effect": {
			"forced": "When Grasping Tentacle is attacked, discard the top card of the encounter deck. If that card has a shadow effect or is a Tentacle enemy, attach this card to an attacking character as a Tentacle attachment with the text: \"Attached character's Attack and Defense are reduced to 0.\""
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 74,
		"quantity": 4,
		"type": "enemy",
		"title": "Trashing Tentacle",
		"icon": "watcher",
		"cost": 12,
		"strength": 2,
		"attack": 3,
		"defense": 0,
		"hp": 3,
		"traits": ["Tentacle"],
		"effect": {
			"forced": "When Thrashing Tentacle is attacked, discard the top card of the encounter deck. If that card has a shadow effect or is a Tentacle enemy, deal the damage from the attack to 1 character an attacking player controls (ignoring defense)."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 75,
		"quantity": 4,
		"type": "enemy",
		"title": "Striking Tentacle",
		"icon": "watcher",
		"cost": 18,
		"strength": 2,
		"attack": 4,
		"defense": 1,
		"hp": 3,
		"traits": ["Tentacle"],
		"effect": {
			"forced": "When Striking Tentacle attacks, discard the top card of the encounter deck. If that card has a shadow effect or is a Tentacle enemy, this attack is considered undefended."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 76,
		"quantity": 1,
		"unique": true,
		"type": "hero",
		"title": "Hama",
		"icon": "tactics",
		"cost": 9,
		"strength": 1,
		"attack": 3,
		"defense": 1,
		"hp": 4,
		"traits": ["Rohan", "Warrior"],
		"effect": {
			"response": "After Hama is declared as an attacker, return a Tactics event from your discard pile to your hand. Then, choose and discard 1 card from your hand."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 77,
		"quantity": 3,
		"type": "ally",
		"title": "Erestor",
		"icon": "leadership",
		"cost": 4,
		"strength": 2,
		"attack": 0,
		"defense": 1,
		"hp": 3,
		"traits": ["Noldor"],
		"effect": {
			"action": "Choose and discard 1 card from your hand to draw 1 card. (Limit once per round.)"
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 78,
		"quantity": 3,
		"type": "event",
		"title": "Fresh Tracks",
		"icon": "leadership",
		"cost": 1,
		"effect": {
			"response": "After an enemy is added to the staging area, deal 1 damage to that enemy. Players ignore that enemy while making engagement checks this round."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 79,
		"quantity": 3,
		"type": "ally",
		"title": "Erebor Battle Master",
		"icon": "tactics",
		"cost": 3,
		"strength": 0,
		"attack": 1,
		"defense": 1,
		"hp": 2,
		"traits": ["Dwarf", "Warrior"],
		"effect": {
			"normal": "Erebor Battle Master gets +1 Attack for each other Dwarf character you control."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 80,
		"quantity": 3,
		"type": "attachment",
		"title": "Ring Mail",
		"icon": "tactics",
		"cost": 2,
		"traits": ["Item", "Armor"],
		"effect": {
			"normal": "Attach to a Dwarf or Hobbit character.\nRestricted.\nAttached character gets +1 hit point and +1 Defense."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 81,
		"quantity": 3,
		"type": "event",
		"title": "Out of Sight",
		"icon": "spirit",
		"cost": 5,
		"effect": {
			"normal": "Secrecy 3.",
			"action": "Enemies engaged with you cannot attack this phase."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 82,
		"quantity": 3,
		"type": "attachment",
		"title": "Ever My Heart Rises",
		"icon": "spirit",
		"cost": 0,
		"traits": ["Condition"],
		"effect": {
			"normal": "Attach to a Dwarf character.",
			"response": "After you travel to a Mountain or Underground location, ready attached character and reduce your threat by 1."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 83,
		"quantity": 3,
		"type": "ally",
		"title": "Warden of Healing",
		"icon": "lore",
		"cost": 2,
		"strength": 1,
		"attack": 0,
		"defense": 1,
		"hp": 1,
		"traits": ["Gondor", "Healer"],
		"effect": {
			"action": "Exhaust Warden of Healing to heal 1 damage on up to 2 different characters. Then, you may pay 2 Lore resources to ready Warden of Healing."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 84,
		"quantity": 3,
		"type": "event",
		"title": "Word of Command",
		"icon": "lore",
		"cost": 1,
		"effect": {
			"action": "Exhaust an Istari character to search your deck for 1 card and add it to your hand. Shuffle your deck."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 85,
		"quantity": 3,
		"type": "attachment",
		"title": "Love of Tales",
		"icon": "lore",
		"cost": 0,
		"traits": ["Condition"],
		"effect": {
			"normal": "Attach to a Lore hero. Limit 1 per hero.",
			"response": "After a Song card is played, add 1 resource to attached hero's resource pool."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 86,
		"quantity": 1,
		"type": "quest",
		"title": "Journey in the Black Pit",
		"icon": "dark",
		"hp": 13,
		"effect": {
			"A": {
				"normal": "Your party is scouting the Mines of Moria, searching for signs of Orcs. Dark tunnels and twisting passages spread out in all directions, a labyrinthine maze that you could wander in forever if you take the wrong path.",
				"setup": "The first player attaches Cave Torch to a hero of his choice."
			},
			"B": {
				"when revealed": "Discard cards from the top of the encounter deck until you discard X locations, where X is one less than the number of players in the game (minimum of 1). Add those locations to the staging area, and shuffle the other discarded cards back into the encounter deck.\nEach location gets +1 Threat. If the players quest unsuccessfully, trigger all \"Lost:\" effects in play."
			}
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 87,
		"quantity": 1,
		"type": "quest",
		"title": "Continuing Eastward",
		"icon": "dark",
		"hp": 17,
		"effect": {
			"A": {
				"normal": "Time carries no weight in the darkness, and the hours creep by with no end in sight. The number of Orcs in the mines increase as you head toward the East-gate, but there appears to be little real organization within their ranks. You press onward."
			},
			"B": {
				"when revealed": "The first player makes a locate test. If this test is failed, reveal cards from the encounter deck equal to the number of players in the game and add them to the staging area. Then, trigger all \"Lost:\" effects in play.\nIf the players quest unsuccessfully, trigger all \"Lost:\" effects in play.\nIf the players defeat this stage, they have won the game."
			}
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 88,
		"quantity": 1,
		"unique": true,
		"type": "objective",
		"title": "Durin's Greaves",
		"icon": "dark",
		"traits": ["Artifact", "Armour"],
		"effect": {
			"when revealed": "The first player attaches Durin's Greaves to a hero of his choice as an attachment.\nAttached hero gains +1 Defense."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 89,
		"quantity": 3,
		"type": "location",
		"title": "Abandoned Mine",
		"icon": "dark",
		"strength": 3,
		"hp": 3,
		"traits": ["Underground", "Dark"],
		"effect": {
			"normal": "Lost: Return the top 2 Goblin enemies in the encounter discard pile to the staging area, if able.\nPASS"
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 90,
		"quantity": 2,
		"type": "location",
		"title": "Dwarven Forge",
		"icon": "dark",
		"strength": 2,
		"hp": 4,
		"traits": ["Underground", "Dark"],
		"effect": {
			"normal": "Lost: Each player must choose and discard 1 card from his hand.\nPASS"
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 91,
		"quantity": 2,
		"type": "location",
		"title": "Silent Caverns",
		"icon": "dark",
		"strength": 1,
		"hp": 3,
		"traits": ["Underground"],
		"effect": {
			"normal": "Lost: Exhaust all characters.\nPASS"
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 92,
		"quantity": 2,
		"type": "location",
		"title": "Twisting Passage",
		"icon": "dark",
		"strength": 3,
		"hp": 5,
		"traits": ["Underground", "Dark"],
		"effect": {
			"normal": "PASS",
			"forced": "Before placing progress tokens on Twisting Passage, the first player must make a locate test. If this test is failed, do not place any progress tokens on Twisting Passage and trigger all \"Lost:\" effects in play."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 93,
		"quantity": 2,
		"type": "treachery",
		"title": "Fatigue",
		"icon": "dark",
		"effect": {
			"when revealed": "Each player must exhaust 1 character he controls, if able. Then, if any player controls no unexhausted characters, Fatigue gains surge.",
			"shadow": "The defending player must exhaust 1 character he controls, if able."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 94,
		"quantity": 4,
		"type": "treachery",
		"title": "Foul Air",
		"icon": "dark",
		"effect": {
			"when revealed": "The first player makes a locate test. If this test is failed, deal 2 damage to all characters and trigger all \"Lost:\" effects in play."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 95,
		"quantity": 1,
		"type": "treachery",
		"title": "Gathering Ground",
		"icon": "dark",
		"effect": {
			"normal": "PASS",
			"when revealed": "Attach this card to a location in the staging area with the highest combined threat and remaining quest points. (Counts as a Condition attachment with the text: \"Each enemy revealed from the encounter deck gains surge.\")"
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 96,
		"quantity": 2,
		"type": "treachery",
		"title": "Vast and Intricate",
		"icon": "dark",
		"effect": {
			"when revealed": "The first player makes a locate test. If this test is failed, raise each player's threat by 7, remove all progress tokens from play, and trigger all \"Lost:\" effects in play."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 97,
		"quantity": 3,
		"type": "enemy",
		"title": "Cave Spider",
		"icon": "dark",
		"cost": 31,
		"strength": 3,
		"attack": 2,
		"defense": 1,
		"hp": 4,
		"traits": ["Spider", "Creature"],
		"effect": {
			"when revealed": "The first player draws 1 card. Then, that player must choose and discard 4 cards from his hand, if able.",
			"forced": "After Cave Spider engages a player, that player must choose and discard 1 card from his hand, if able."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 98,
		"quantity": 4,
		"type": "enemy",
		"title": "Goblin Sneak",
		"icon": "dark",
		"cost": 15,
		"strength": 2,
		"attack": 1,
		"defense": 1,
		"hp": 2,
		"traits": ["Goblin", "Orc"],
		"effect": {
			"forced": "After Goblin Sneak engages a player, discard the top card of the encounter deck. If it is a treachery card, Goblin Sneak engages the next player, if able.",
			"shadow": "Add Goblin Sneak to the staging area."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 99,
		"quantity": 1,
		"type": "enemy",
		"title": "Goblin Warlord",
		"icon": "dark",
		"cost": 39,
		"strength": 4,
		"attack": 3,
		"defense": 3,
		"hp": 5,
		"traits": ["Goblin", "Orc"],
		"effect": {
			"normal": "Lost: Each player must choose and discard 1 ally he controls from play, if able.",
			"shadow": "Trigger all \"Lost:\" effects in play."
		}
	},
	{
		"set": "dwarrowdelf",
		"id": 100,
		"quantity": 3,
		"type": "enemy",
		"title": "Rock Adder",
		"icon": "dark",
		"cost": 20,
		"strength": 1,
		"attack": 3,
		"defense": 0,
		"hp": 3,
		"traits": ["Creature"],
		"effect": {
			"normal": "Rock Adder cannot be attacked unless it has dealt at least 1 damage this round.",
			"shadow": "If this attack is undefended, the defending player must discard 1 character he controls from play."
		}
	}
]