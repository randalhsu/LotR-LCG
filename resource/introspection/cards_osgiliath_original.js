[
	{
		"set": "osgiliath",
		"id": 0,
		"type": null,
		"icon": null,
		"why": "programmers count from zero"
	},
	{
		"set": "osgiliath",
		"id": 1,
		"quantity": 1,
		"unique": true,
		"type": "enemy",
		"title": "The Witch-king",
		"icon": "osgiliath",
		"cost": 40,
		"strength": 6,
		"attack": 6,
		"defense": 6,
		"hp": 11,
		"traits": ["Nasgul", "Captain"],
		"effect": {
			"normal": "Players cannot play attachments on The Witch-king.\nWhile The Witch-king is in the staging area, each character gets -1 Willpower.",
			"forced": "After The Witch-king attacks, he returns to the staging area unless the defending player raises his threat by 3."
		}
	},
	{
		"set": "osgiliath",
		"id": 2,
		"quantity": 4,
		"type": "enemy",
		"title": "Snaga Scouts",
		"icon": "osgiliath",
		"cost": 1,
		"strength": 1,
		"attack": 1,
		"defense": 0,
		"hp": 2,
		"traits": ["Orc", "Scout"],
		"effect": {
			"forced": "At the beginning of the encounter phase, all copies of Snaga Scouts engage the player with the lowest threat. (The first player chooses in the case of a tie.)"
		}
	},
	{
		"set": "osgiliath",
		"id": 3,
		"quantity": 4,
		"type": "enemy",
		"title": "Wolves from Mordor",
		"icon": "osgiliath",
		"cost": 27,
		"strength": 1,
		"attack": 4,
		"defense": 1,
		"hp": 3,
		"traits": ["Creature", "Scout"],
		"effect": {
			"forced": "After Wolves from Mordor attack and destroy a character, shuffle Wolves from Mordor into the encounter deck.",
			"shadow": "Deal 2 damage to the defending character."
		}
	},
	{
		"set": "osgiliath",
		"id": 4,
		"quantity": 4,
		"type": "enemy",
		"title": "Wainriders",
		"icon": "osgiliath",
		"cost": 35,
		"strength": 2,
		"attack": 3,
		"defense": 1,
		"hp": 4,
		"traits": ["Easterling", "Scout"],
		"effect": {
			"normal": "Each damage dealt by Wainriders raises the defending player's threat by 1."
		}
	},
	{
		"set": "osgiliath",
		"id": 5,
		"quantity": 3,
		"type": "enemy",
		"title": "Wainrider Captain",
		"icon": "osgiliath",
		"cost": 40,
		"strength": 3,
		"attack": 3,
		"defense": 3,
		"hp": 4,
		"traits": ["Easterling", "Captain"],
		"effect": {
			"when revealed": "Move the top Scout enemy from the encounter discard pile to the staging area. (Top 2 Scout enemies instead if the players have crossed the Anduin.)",
			"shadow": "If this attack is undefended, attacking enemy gets +2 ATK if it is a Scout."
		}
	},
	{
		"set": "osgiliath",
		"id": 6,
		"quantity": 3,
		"type": "enemy",
		"title": "Uruk Vanguard",
		"icon": "osgiliath",
		"cost": 45,
		"strength": 2,
		"attack": 2,
		"defense": 1,
		"hp": 8,
		"traits": ["Uruk", "Orc"],
		"effect": {
			"normal": "If the players have crossed the Anduin, Uruk Vanguard gets +3 ATK.",
			"shadow": "Attacking enemy gets +1 ATK. (+2 ATK instead if players have crossed the Anduin)."
		}
	},
	{
		"set": "osgiliath",
		"id": 7,
		"quantity": 3,
		"type": "location",
		"title": "Captured Watchtower",
		"icon": "osgiliath",
		"strength": 1,
		"hp": 2,
		"traits": ["West Bank"],
		"effect": {
			"normal": "If the players have crossed the Anduin, Captured Watchtower gets +3 Threat.",
			"shadow": "Remove all defending characters from combat. This attack is considered undefended."
		}
	},
	{
		"set": "osgiliath",
		"id": 8,
		"quantity": 1,
		"type": "location",
		"title": "Emyn Arnen Overlook",
		"icon": "osgiliath",
		"strength": 2,
		"hp": 5,
		"traits": ["East Bank", "Highlands"],
		"effect": {
			"normal": "The first Scout enemy revealed from the encounter deck each round gains surge and doomed 2."
		}
	},
	{
		"set": "osgiliath",
		"id": 9,
		"quantity": 2,
		"type": "location",
		"title": "Morgulduin",
		"icon": "osgiliath",
		"strength": 1,
		"hp": 3,
		"traits": ["East Bank", "Polluted"],
		"effect": {
			"normal": "While Morgulduin is the active location, it gains: \"Forced: When a character commits to a quest, deal 1 damage to that character.\"",
			"shadow": "If the players have not yet crossed the Anduin, return any current active location to the staging area, Morgulduin becomes the active location."
		}
	},
	{
		"set": "osgiliath",
		"id": 10,
		"quantity": 2,
		"type": "location",
		"title": "Pelennor Fields",
		"icon": "osgiliath",
		"strength": 1,
		"hp": 7,
		"traits": ["West Bank"],
		"effect": {
			"normal": "If the players have crossed the Anduin, Pelennor Fields gains: \"When faced with the option to travel, the players must either travel to Pelennor Fields or raise each players threat by 3.\""
		},
		"victory": 1
	},
	{
		"set": "osgiliath",
		"id": 11,
		"quantity": 3,
		"type": "location",
		"title": "Ruins of Osgiliath",
		"icon": "osgiliath",
		"strength": 1,
		"hp": 2,
		"traits": ["East Bank"],
		"effect": {
			"normal": "If the players have not crossed the Anduin, Ruins of Osgiliath gets +3 Threat."
		}
	},
	{
		"set": "osgiliath",
		"id": 12,
		"quantity": 4,
		"type": "treachery",
		"title": "Cut Off",
		"icon": "osgiliath",
		"effect": {
			"normal": "Doomed 1.",
			"when revealed": "Each player must discard all ally cards from his hand, if able.",
			"shadow": "Defending player must discard 1 ally card from his hand or attacking enemy gets +3 ATK. (2 allies instead if this attack is undefended.)"
		}
	},
	{
		"set": "osgiliath",
		"id": 13,
		"quantity": 2,
		"type": "treachery",
		"title": "Dark Pursuit",
		"icon": "osgiliath",
		"effect": {
			"when revealed": "Raise the total Threat of the staging area by 1 for each Scout enemy in play. If there are no Scout enemies in play, Dark Pursuit gains surge."
		}
	},
	{
		"set": "osgiliath",
		"id": 14,
		"quantity": 3,
		"type": "treachery",
		"title": "Massing at Osgiliath",
		"icon": "osgiliath",
		"effect": {
			"normal": "Surge.",
			"when revealed": "Until the end of the phase, each card revealed by the encounter deck gains doomed 1. (Doomed 3 instead if the players have crossed the Anduin.)"
		}
	},
	{
		"set": "osgiliath",
		"id": 15,
		"quantity": 2,
		"type": "objective",
		"title": "Ranger of Ithilien",
		"icon": "osgiliath",
		"strength": 2,
		"attack": 2,
		"defense": 1,
		"hp": 2,
		"traits": ["Gondor", "Ranger", "Ally"],
		"effect": {
			"when revealed": "The first player takes control of Ranger of Ithilien, exhausted and committed to the quest. Then, Ranger of Ithilien gains surge.",
			"shadow": "Deal 2 damage to attacking enemy. The defending player may exhaust a character he controls to take control of Ranger of Ithilien."
		}
	},
	{
		"set": "osgiliath",
		"id": 16,
		"quantity": 1,
		"type": "quest",
		"title": "Beyond Expectations",
		"icon": "osgiliath",
		"hp": 7,
		"effect": {
			"A": {
				"normal": "There are reports of increased Orc activity around Ithilien, and you have been sent to investigate. You enter Osgiliath and cross the river. On the outskirts of the city, you see a horde that surpassses all expectations coming down the Morgul Road.",
				"setup": "Search the encounter deck for 12 Scout cards, and add 3 per player (one of each title), to the staging area. Remove The Witch-king from the encounter deck and set him aside, out of play. Shuffle any unused Scout cards back into the encounter deck."
			},
			"B": {
				"normal": "Players cannot travel to West Bank locations.\nAs the van of the army enters the city, some of the horde's outriders are aware of your presence, and head in your direction. Drawing back, you make a hasty retreat towards the river."
			}
		}
	},
	{
		"set": "osgiliath",
		"id": 17,
		"quantity": 1,
		"type": "quest",
		"title": "Through the Ruins",
		"icon": "osgiliath",
		"hp": 5,
		"effect": {
			"A": {
				"normal": "The outriders and scouts of the army have cut you off from the bridge. You desperately seek the likeliest place to cross the Anduin."
			},
			"B": {
				"normal": "Players cannot travel to West Bank locations.\nEach player cannot play or put into play more than 1 card from his hand each round."
			}
		}
	},
	{
		"set": "osgiliath",
		"id": 18,
		"quantity": 1,
		"type": "quest",
		"title": "Anduin Crossing",
		"icon": "osgiliath",
		"hp": 1,
		"effect": {
			"A": {
				"normal": "The cold waters of the Anduin river rush before you, but the current is weaker here and you have to cross. The outriders and van of the Dark Lord's army are closing fast behind, and their archers will make the attempted crossing even more dangerous. The bravest members of your band turn back to distract the oncoming horde, so that the rest of you might escape."
			},
			"B": {
				"normal": "Progress tokens from card effects cannot be placed on this quest card or the active location.\nPlayers cannot travel to East Bank or West Bank locations.\nIn order to commit characters to the quest, a player must first choose a hero or 1 Ranger of Ithilien card he controls. Discard each chosen card from play."
			}
		}
	},
	{
		"set": "osgiliath",
		"id": 19,
		"quantity": 1,
		"type": "quest",
		"title": "Race to Minas Tirith",
		"icon": "osgiliath",
		"hp": 15,
		"effect": {
			"A": {
				"normal": "You made it across the Anduin and are leaving Osgiliath when a fell shriek splits the air. You begin the race across the Pelennor Fields to the safety of Minas Tirith, but a new enemy follows behind."
			},
			"B": {
				"when revealed": "Add The Witch-king to the staging area.",
				"normal": "Players have now crossed the Anduin. Players cannot travel to East Bank locations.\nIf the players defeat this stage, they have won the game."
			}
		}
	}
]