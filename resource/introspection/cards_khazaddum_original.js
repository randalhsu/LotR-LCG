[
	{
		"set": "khazaddum",
		"id": 0,
		"type": "iDontCare",
		"icon": "iDontCare",
		"why": "programmers count from zero"
	},
	{
		"set": "khazaddum",
		"id": 1,
		"quantity": 1,
		"unique": true,
		"type": "hero",
		"title": "Dwalin",
		"icon": "spirit",
		"cost": 9,
		"strength": 1,
		"attack": 2,
		"defense": 2,
		"hp": 4,
		"traits": ["Dwarf"],
		"effect": {
			"response": "After Dwalin attacks and destroys an Orc enemy, lower your threat by 2."
		}
	},
	{
		"set": "khazaddum",
		"id": 2,
		"quantity": 1,
		"unique": true,
		"type": "hero",
		"title": "Bifur",
		"icon": "lore",
		"cost": 7,
		"strength": 2,
		"attack": 1,
		"defense": 2,
		"hp": 3,
		"traits": ["Dwarf"],
		"effect": {
			"action": "Pay 1 resource from a hero's resource pool to add 1 resource to Bifur's resource pool. Any player may trigger this ability. (Limit once per round.)"
		}
	},
	{
		"set": "khazaddum",
		"id": 3,
		"quantity": 3,
		"type": "attachment",
		"title": "Narvi's Belt",
		"icon": "leadership",
		"cost": 2,
		"traits": ["Item"],
		"effect": {
			"normal": "Attach to a Dwarf hero.",
			"action": "Exhaust Narvi's Belt to give attached hero a resource icon of your choice until the end of the phase."
		}
	},
	{
		"set": "khazaddum",
		"id": 4,
		"quantity": 3,
		"type": "event",
		"title": "Durin's Song",
		"icon": "leadership",
		"cost": 1,
		"traits": ["Song"],
		"effect": {
			"action": "Choose a Dwarf hero. That hero gets +2 Willpower, +2 ATK, and +2 DEF until the end of the round."
		}
	},
	{
		"set": "khazaddum",
		"id": 5,
		"quantity": 3,
		"type": "event",
		"title": "Ever Onward",
		"icon": "leadership",
		"cost": 3,
		"effect": {
			"response": "After players quest unsuccessfully, choose a player. That player does not raise his threat."
		}
	},
	{
		"set": "khazaddum",
		"id": 6,
		"quantity": 3,
		"type": "ally",
		"title": "Veteran of Nanduhirion",
		"icon": "tactics",
		"cost": 4,
		"strength": 0,
		"attack": 3,
		"defense": 2,
		"hp": 3,
		"traits": ["Dwarf", "Warrior"],
		"effect": {
			"normal": "Veteran of Nanduhirion enters play with 1 damage on it."
		}
	},
	{
		"set": "khazaddum",
		"id": 7,
		"quantity": 3,
		"type": "attachment",
		"title": "Drarrowdelf Axe",
		"icon": "tactics",
		"cost": 1,
		"traits": ["Item", "Weapon"],
		"effect": {
			"normal": "Attach to a Dwarf character. Restricted.\nAttached character gets +1 ATK.",
			"response": "After attached character attacks, deal 1 damage to the defending enemy."
		}
	},
	{
		"set": "khazaddum",
		"id": 8,
		"quantity": 3,
		"type": "event",
		"title": "Khazad! Khazad!",
		"icon": "tactics",
		"cost": 0,
		"effect": {
			"action": "Choose a Dwarf character. Until the end of the phase, that character gets +3 ATK."
		}
	},
	{
		"set": "khazaddum",
		"id": 9,
		"quantity": 3,
		"type": "ally",
		"title": "Zigil Miner",
		"icon": "spirit",
		"cost": 2,
		"strength": 1,
		"attack": 1,
		"defense": 1,
		"hp": 1,
		"traits": ["Dwarf"],
		"effect": {
			"action": "Exhaust Zigil Miner and name a number to discard the top 2 cards of your deck. If at least one of those cards has a cost equal to the named number, choose a hero you control. That hero adds resources to his resource pool equal to the named number."
		}
	},
	{
		"set": "khazaddum",
		"id": 10,
		"quantity": 3,
		"type": "event",
		"title": "Untroubled by Darkness",
		"icon": "spirit",
		"cost": 2,
		"effect": {
			"action": "Each Dwarf character gets +1 Willpower until the end of the phase. (+2 Willpower instead if the active location is an Underground or Dark location.)"
		}
	},
	{
		"set": "khazaddum",
		"id": 11,
		"quantity": 3,
		"type": "ally",
		"title": "Erebor Record Keeper",
		"icon": "lore",
		"cost": 1,
		"strength": 1,
		"attack": 0,
		"defense": 0,
		"hp": 1,
		"traits": ["Dwarf"],
		"effect": {
			"normal": "Erebor Record Keeper cannot attack or defend.",
			"action": "Exhaust Erebor Record Keeper and pay 1 Lore resource to choose and ready a Dwarf character."
		}
	},
	{
		"set": "khazaddum",
		"id": 12,
		"quantity": 3,
		"type": "event",
		"title": "Ancestral Knowledge",
		"icon": "lore",
		"cost": 1,
		"effect": {
			"action": "Exhaust a Dwarf character to place 2 progress tokens on the active location. (4 progress tokens instead if it is an Underground or Mountain location.)"
		}
	},
	{
		"set": "khazaddum",
		"id": 13,
		"quantity": 3,
		"type": "attachment",
		"title": "Boots from Erebor",
		"icon": "neural",
		"cost": 0,
		"traits": ["Item"],
		"effect": {
			"normal": "Attach to a Dwarf or Hobbit character.\nLimit 1 Boots from Erebor per character.\nAttached character gets +1 hit point."
		}
	},
	{
		"set": "khazaddum",
		"id": 14,
		"quantity": 2,
		"type": "enemy",
		"title": "Patrol Leader",
		"icon": "pit",
		"cost": 30,
		"strength": 3,
		"attack": 4,
		"defense": 3,
		"hp": 4,
		"traits": ["Goblin", "Orc"],
		"effect": {
			"forced": "Before Patrol Leader is dealt damage, discard the top card of the encounter deck. If the discarded card is an enemy, cancel the damage.",
			"shadow": "Cancel all damage dealt to this enemy."
		}
	},
	{
		"set": "khazaddum",
		"id": 15,
		"quantity": 5,
		"type": "treachery",
		"title": "Signs of Conflict",
		"icon": "pit",
		"effect": {
			"normal": "Doomed 2. Surge.",
			"shadow": "Defending player raises his threat by 2."
		}
	},
	{
		"set": "khazaddum",
		"id": 16,
		"quantity": 1,
		"unique": true,
		"type": "location",
		"title": "East-gate",
		"icon": "pit",
		"strength": 7,
		"hp": 7,
		"traits": ["Gate"],
		"effect": {
			"normal": "Immune to card effects.\nPlayers cannot optionally engage enemies and no engagement checks are made.",
			"forced": "After East-gate leaves play as an explored location, add First Hall to the staging area."
		},
		"victory": 1
	},
	{
		"set": "khazaddum",
		"id": 17,
		"quantity": 1,
		"unique": true,
		"type": "location",
		"title": "First Hall",
		"icon": "pit",
		"strength": 2,
		"hp": 2,
		"traits": ["Underground"],
		"effect": {
			"travel": "Each player must raise his threat by 3 to travel here.",
			"forced": "After First Hall leaves play as an explored location, add Bridge of Khazad-dum to the staging area."
		},
		"victory": 1
	},
	{
		"set": "khazaddum",
		"id": 18,
		"quantity": 1,
		"unique": true,
		"type": "location",
		"title": "Bridge of Khazad-dum",
		"icon": "pit",
		"strength": 3,
		"hp": 3,
		"traits": ["Underground", "Bridge"],
		"effect": {
			"normal": "While Bridge of Khazad-dum is the active location, players cannot play cards."
		},
		"victory": 2
	},
	{
		"set": "khazaddum",
		"id": 19,
		"quantity": 2,
		"type": "location",
		"title": "Stairs of Nain",
		"icon": "pit",
		"strength": 2,
		"hp": 4,
		"traits": ["Underground"],
		"effect": {
			"travel": "The first player must exhaust 1 character he controls to travel here.",
			"shadow": "Defending player must choose and exhaust 1 character he controls."
		}
	},
	{
		"set": "khazaddum",
		"id": 20,
		"quantity": 2,
		"type": "enemy",
		"title": "Cave-troll",
		"icon": "seventh",
		"cost": 33,
		"strength": 4,
		"attack": 6,
		"defense": 4,
		"hp": 7,
		"traits": ["Troll"],
		"effect": {
			"normal": "For each excess point of combat damage dealt by Cave-troll (damage that is dealt beyond the remaining hit points of the character damaged by its attack) you must damage another character you control."
		},
		"victory": 2
	},
	{
		"set": "khazaddum",
		"id": 21,
		"quantity": 1,
		"type": "enemy",
		"title": "Orc Horn Blower",
		"icon": "seventh",
		"cost": 45,
		"strength": 2,
		"attack": 1,
		"defense": 1,
		"hp": 3,
		"traits": ["Orc", "Summoner"],
		"effect": {
			"normal": "Surge.",
			"when revealed": "Reveal 1 card from the encounter deck and add it to the staging area."
		}
	},
	{
		"set": "khazaddum",
		"id": 22,
		"quantity": 2,
		"type": "treachery",
		"title": "Hidden Threat",
		"icon": "seventh",
		"effect": {
			"when revealed": "Each player must raise his threat by 1 for each enemy in the staging area. Then, The last player discards an attachment he controls."
		}
	},
	{
		"set": "khazaddum",
		"id": 23,
		"quantity": 3,
		"type": "location",
		"title": "Upper Hall",
		"icon": "seventh",
		"strength": 3,
		"hp": 4,
		"traits": ["Underground"],
		"effect": {
			"normal": "Doomed 2"
		}
	},
	{
		"set": "khazaddum",
		"id": 24,
		"quantity": 1,
		"unique": true,
		"type": "objective",
		"title": "Book of Mazarbul",
		"icon": "seventh",
		"traits": ["Item", "Artifact"],
		"effect": {
			"normal": "Restricted.",
			"action": "Exhaust a hero to claim this objective. Then, attach Book of Mazarbul to that hero. (If detached, return Book of Mazarbul to the staging area.)\nAttached hero cannot attack and does not exhaust to commit to a quest."
		}
	},
	{
		"set": "khazaddum",
		"id": 25,
		"quantity": 1,
		"unique": true,
		"type": "enemy",
		"title": "The Nameless Fear",
		"icon": "flight",
		"cost": 50,
		"strength": -1,
		"attack": -1,
		"defense": -1,
		"hp": 27,
		"traits": ["Flame", "Shadow"],
		"effect": {
			"normal": "Immune to player card effects. The Nameless Fear cannot engage or be engaged.\nX is the number of victory points in the victory display."
		}
	},
	{
		"set": "khazaddum",
		"id": 26,
		"quantity": 3,
		"type": "treachery",
		"title": "New Devilry",
		"icon": "flight",
		"effect": {
			"when revealed": "If the players are not on stage 1, shuffle the current quest card into the quest deck, then reveal a new quest card. Otherwise, New Devilry gains surge.",
			"shadow": "If this attack is undefended, raise your threat by The Nameless Fear's Threat."
		}
	},
	{
		"set": "khazaddum",
		"id": 27,
		"quantity": 3,
		"type": "treachery",
		"title": "Shadow of Fear",
		"icon": "flight",
		"effect": {
			"when revealed": "The first player attaches Shadow of Fear to one of his heroes. (Counts as a Condition attachment with the text: \"Limit 1 per hero. Attached hero cannot exhaust or ready and its text box is treated as if it were blank. Action: Pay 3 resources from attached hero's pool to discard this card.\")"
		}
	},
	{
		"set": "khazaddum",
		"id": 28,
		"quantity": 4,
		"type": "treachery",
		"title": "A Foe Beyond",
		"icon": "flight",
		"effect": {
			"when revealed": "The last player deals damage equal to The Nameless Fear's ATK to a hero he controls. This effect cannot be canceled.",
			"shadow": "Deal damage equal to The Nameless Fear's ATK to the defending character."
		}
	},
	{
		"set": "khazaddum",
		"id": 29,
		"quantity": 1,
		"type": "objective",
		"title": "Abandoned Tools",
		"icon": "flight",
		"traits": ["Tools"],
		"effect": {
			"normal": "Guarded. Restricted.",
			"action": "Exhaust a her to claim this objective if it has no encounters attached. Then, attach Abandoned Tools to that hero. (If detached, return Abandoned Tools to the staging area.)"
		}
	},
	{
		"set": "khazaddum",
		"id": 30,
		"quantity": 1,
		"type": "enemy",
		"title": "Chieftain of the Pit",
		"icon": "plundering",
		"cost": 27,
		"strength": 2,
		"attack": 5,
		"defense": 2,
		"hp": 4,
		"traits": ["Goblin", "Orc"],
		"effect": {
			"when revealed": "Chieftain of the Pit gets +3 ATK until the end of the round.",
			"shadow": "Attacking enemy attacks again after this attack. Deal it another shadow card for the next attack."
		}
	},
	{
		"set": "khazaddum",
		"id": 31,
		"quantity": 5,
		"type": "enemy",
		"title": "Goblin Spearman",
		"icon": "plundering",
		"cost": 15,
		"strength": 2,
		"attack": 2,
		"defense": 2,
		"hp": 2,
		"traits": ["Goblin", "Orc"],
		"effect": {
			"normal": "Goblin Spearman gets +2 ATK if its attack is undefended.",
			"shadow": "Add Goblin Spearman to the staging area."
		}
	},
	{
		"set": "khazaddum",
		"id": 32,
		"quantity": 2,
		"type": "enemy",
		"title": "Goblin Archer",
		"icon": "plundering",
		"cost": 48,
		"strength": 2,
		"attack": 1,
		"defense": 3,
		"hp": 1,
		"traits": ["Goblin", "Orc"],
		"effect": {
			"normal": "Players cannot optionally engage Goblin Archer.\nCharacters with ranged are eligible to attack Goblin Archer while it is in the staging area.",
			"forced": "After an enemy is revealed from the encounter deck, the first player must deal 1 damage to 1 character he controls."
		}
	},
	{
		"set": "khazaddum",
		"id": 33,
		"quantity": 3,
		"type": "treachery",
		"title": "Undisturbed Bones",
		"icon": "plundering",
		"effect": {
			"when revealed": "Each player must deal X damage to 1 ally he controls. X is the number of allies he controls.",
			"shadow": "If the defending character is an ally, discard it from play."
		}
	},
	{
		"set": "khazaddum",
		"id": 34,
		"quantity": 2,
		"type": "location",
		"title": "Plundered Armoury",
		"icon": "plundering",
		"strength": 3,
		"hp": 2,
		"traits": ["Underground"],
		"effect": {
			"normal": "While Plundered Armoury is in the staging area, enemies get +1 ATK.",
			"response": "After Plundered Armoury leaves play as an explored location, each player may attach a Weapon or Armour attachment from his hand to 1 character he controls."
		}
	},
	{
		"set": "khazaddum",
		"id": 35,
		"quantity": 4,
		"type": "enemy",
		"title": "Goblin Follower",
		"icon": "twists",
		"cost": 33,
		"strength": 1,
		"attack": 3,
		"defense": 2,
		"hp": 4,
		"traits": ["Goblin", "Orc"],
		"effect": {
			"when revealed": "Goblin Follower engages the last player.",
			"shadow": "Attacking enemy gets +1 ATK. (+2 ATK instead if attacking the last player.)"
		}
	},
	{
		"set": "khazaddum",
		"id": 36,
		"quantity": 3,
		"type": "location",
		"title": "Branching Paths",
		"icon": "twists",
		"strength": 1,
		"hp": 3,
		"traits": ["Underground", "Dark"],
		"effect": {
			"normal": "While Branching Paths is in the staging area each Dark location gets +1 Threat.",
			"forced": "After Branching Paths leaves play as an explored location, look at the top 3 cards of the encounter deck. Players must choose 1 of those to reveal and add to the staging area, moving the other 2 to the bottom of the deck."
		}
	},
	{
		"set": "khazaddum",
		"id": 37,
		"quantity": 2,
		"type": "location",
		"title": "Lightless Passage",
		"icon": "twists",
		"strength": 4,
		"hp": 4,
		"traits": ["Underground", "Dark"],
		"effect": {
			"travel": "Players must exhaust a Cave Torch to travel here.",
			"shadow": "Cancel all combat damage dealt to attacking enemy."
		}
	},
	{
		"set": "khazaddum",
		"id": 38,
		"quantity": 3,
		"type": "location",
		"title": "Zigil Mineshaft",
		"icon": "twists",
		"strength": 5,
		"hp": 5,
		"traits": ["Underground", "Dark"],
		"effect": {
			"action": "Raise each player's threat by 1 to place 1 progress token on Zigil Mineshaft."
		}
	},
	{
		"set": "khazaddum",
		"id": 39,
		"quantity": 1,
		"type": "treachery",
		"title": "Many Roads",
		"icon": "twists",
		"effect": {
			"normal": "Surge.",
			"when revealed": "Shuffle all locations in the encounter discard pile back into the encounter deck."
		}
	},
	{
		"set": "khazaddum",
		"id": 40,
		"quantity": 3,
		"type": "treachery",
		"title": "Burning Low",
		"icon": "twists",
		"effect": {
			"when revealed": "Each enemy and location currently in the staging area gets +1 Threat until the end of the phase. (+3 Threat instead if it is a Dark location.) Players may exhaust a Cave Torch to cancel this effect.",
			"shadow": "Attacking enemy gets +2 ATK."
		}
	},
	{
		"set": "khazaddum",
		"id": 41,
		"quantity": 1,
		"type": "objective",
		"title": "Cave Torch",
		"icon": "twists",
		"traits": ["Light"],
		"effect": {
			"normal": "Attach to a hero. Restricted.",
			"action": "Exhaust Cave Torch to place up to 3 progress tokens on a Dark location.",
			"forced": "After Cave Torch exhausts, discard the top card of the encounter deck. If that card is an enemy, add it to the staging area."
		}
	},
	{
		"set": "khazaddum",
		"id": 42,
		"quantity": 2,
		"type": "enemy",
		"title": "Great Cave-troll",
		"icon": "moria",
		"cost": 38,
		"strength": 2,
		"attack": 7,
		"defense": 3,
		"hp": 10,
		"traits": ["Troll"],
		"effect": {
			"normal": "Immune to ranged damage.\nNo attachments can be played on Great Cave-troll."
		},
		"victory": 3
	},
	{
		"set": "khazaddum",
		"id": 43,
		"quantity": 1,
		"type": "enemy",
		"title": "Orc Drummer",
		"icon": "moria",
		"cost": 50,
		"strength": 1,
		"attack": 1,
		"defense": 3,
		"hp": 1,
		"traits": ["Orc", "Summoner"],
		"effect": {
			"normal": "While Orc Drummer is in the staging area, each enemy gets +X Threat. X is the number of players in the game."
		}
	},
	{
		"set": "khazaddum",
		"id": 44,
		"quantity": 3,
		"type": "enemy",
		"title": "Stray Goblin",
		"icon": "moria",
		"cost": 29,
		"strength": -1,
		"attack": -1,
		"defense": 2,
		"hp": 2,
		"traits": ["Goblin", "Orc"],
		"effect": {
			"normal": "X is the number of players in the game.",
			"shadow": "Attacking enemy gets +X ATK. X is the number of players in the game."
		}
	},
	{
		"set": "khazaddum",
		"id": 45,
		"quantity": 3,
		"type": "treachery",
		"title": "Chance Encounter",
		"icon": "moria",
		"effect": {
			"when revealed": "Put the top enemy in the encounter discard pile into play, engaged with the first player. If this effect put no enemies into play, Chance Encounter gains surge.",
			"shadow": "Attacking enemy gets +1 ATK. (+3 ATK instead if engaged with the first player.)"
		}
	},
	{
		"set": "khazaddum",
		"id": 46,
		"quantity": 2,
		"type": "treachery",
		"title": "Massing in the Deep",
		"icon": "moria",
		"effect": {
			"normal": "Doomed 1.",
			"when revealed": "Reveal X additional cards from the encounter deck and add them to the staging area. X is the number of players in the game.",
			"shadow": "Attacking enemy gets +X ATK. X is the number of players in the game."
		}
	},
	{
		"set": "khazaddum",
		"id": 47,
		"quantity": 3,
		"type": "location",
		"title": "The Mountains' Roots",
		"icon": "moria",
		"strength": -1,
		"hp": -1,
		"traits": ["Underground"],
		"effect": {
			"normal": "X is the number of players in the game.",
			"shadow": "Attacking enemy gets +X ATK. X is the number of players in the game."
		}
	},
	{
		"set": "khazaddum",
		"id": 48,
		"quantity": 3,
		"type": "treachery",
		"title": "Cave In",
		"icon": "hazards",
		"traits": ["Hazard"],
		"effect": {
			"when revealed": "Remove all progress tokens from the current quest card and active location. If Cave In removed no progress tokens, it gains surge."
		}
	},
	{
		"set": "khazaddum",
		"id": 49,
		"quantity": 2,
		"type": "treachery",
		"title": "Crumbling Ruin",
		"icon": "hazards",
		"traits": ["Hazard"],
		"effect": {
			"when revealed": "Each player must exhaust a character and discard the top card of his deck, if able. If the printed cost of the discarded card is equal to or higher than the remaining hit points of the exhausted character, discard the exhausted character."
		}
	},
	{
		"set": "khazaddum",
		"id": 50,
		"quantity": 2,
		"type": "treachery",
		"title": "Dark and Dreadful",
		"icon": "hazards",
		"effect": {
			"when revealed": "Deal 1 damage to each exhausted character. (2 damage instead if the active location is a Dark location.)",
			"shadow": "Deal 1 damage to the defending character. (Attacking enemy gets +2 ATK instead if this attack is undefended.)"
		}
	},
	{
		"set": "khazaddum",
		"id": 51,
		"quantity": 1,
		"type": "treachery",
		"title": "Sudden Pitfall",
		"icon": "hazards",
		"traits": ["Hazard"],
		"effect": {
			"when revealed": "The first player must discard 1 questing character he controls, if able. This effect cannot be canceled.",
			"shadow": "Discard the defending character from play."
		}
	},
	{
		"set": "khazaddum",
		"id": 52,
		"quantity": 1,
		"type": "location",
		"title": "Dreadful Gap",
		"icon": "hazards",
		"strength": 2,
		"hp": -1,
		"traits": ["Underground", "Hazard"],
		"effect": {
			"when revealed": "Immediately travel to Dreadful Gap. If another location is currently active, return it to the staging area.\nX is the number of characters in play."
		},
		"victory": 3
	},
	{
		"set": "khazaddum",
		"id": 53,
		"quantity": 3,
		"type": "location",
		"title": "Fouled Well",
		"icon": "hazards",
		"strength": 3,
		"hp": 3,
		"traits": ["Underground", "Dark", "Hazard"],
		"effect": {
			"when revealed": "Each player may choose and discard 1 card at random from his hand. If all players did not discard 1 card, Fouled Well gains surge."
		}
	},
	{
		"set": "khazaddum",
		"id": 54,
		"quantity": 4,
		"type": "enemy",
		"title": "Black Uruks",
		"icon": "misty",
		"cost": 32,
		"strength": 2,
		"attack": 3,
		"defense": 3,
		"hp": 2,
		"traits": ["Uruk", "Orc"],
		"effect": {
			"when revealed": "The first player must choose and discard an attachment from a questing character, if able.",
			"shadow": "If this attack is undefended, deal 2 additional shadow cards to attacking enemy."
		}
	},
	{
		"set": "khazaddum",
		"id": 55,
		"quantity": 3,
		"type": "enemy",
		"title": "Mountain Warg",
		"icon": "misty",
		"cost": 30,
		"strength": 2,
		"attack": 4,
		"defense": 2,
		"hp": 4,
		"traits": ["Creature"],
		"effect": {
			"normal": "If Mountain Warg is dealt a shadow card with no effect, return Mountain Warg to the staging area after it attacks.",
			"shadow": "Attacking enemy gets +1 ATK. (+2 ATK instead if a Mountain is the active location.)"
		}
	},
	{
		"set": "khazaddum",
		"id": 56,
		"quantity": 3,
		"type": "treachery",
		"title": "Bitter Wind",
		"icon": "misty",
		"effect": {
			"when revealed": "The first player must discard 3 resources from each hero he controls.",
			"shadow": "Defending player must discard 2 resources from each hero he controls."
		}
	},
	{
		"set": "khazaddum",
		"id": 57,
		"quantity": 1,
		"type": "location",
		"title": "Knees of the Mountain",
		"icon": "misty",
		"strength": 2,
		"hp": 3,
		"traits": ["Mountain"],
		"effect": {
			"normal": "While Knees of the Mountain is in the staging area, it gains: \"Forced: After an enemy engages a player, it gets +1 ATK until the end of the round.\""
		}
	},
	{
		"set": "khazaddum",
		"id": 58,
		"quantity": 2,
		"type": "location",
		"title": "Turbulent Waters",
		"icon": "misty",
		"strength": 3,
		"hp": 2,
		"traits": ["Mountain"],
		"effect": {
			"normal": "While Turbulent Waters is the active location, players cannot optionally engage enemies."
		}
	},
	{
		"set": "khazaddum",
		"id": 59,
		"quantity": 2,
		"type": "location",
		"title": "Warg Lair",
		"icon": "misty",
		"strength": 1,
		"hp": 3,
		"traits": ["Mountain"],
		"effect": {
			"when revealed": "Search the encounter deck and discard pile for 1 copy of Mountain Warg and add it to the staging area, if able. Shuffle the encounter deck.",
			"response": "After Warg Lair leaves play as an explored location, each player draws 1 card."
		}
	},
	{
		"set": "khazaddum",
		"id": 60,
		"quantity": 3,
		"type": "enemy",
		"title": "Goblin Scout",
		"icon": "goblin",
		"cost": 37,
		"strength": 3,
		"attack": 1,
		"defense": 0,
		"hp": 2,
		"traits": ["Goblin", "Orc", "Scout"],
		"effect": {
			"normal": "Each player with a threat of 25 or higher cannot optionally engage Goblin Scout."
		}
	},
	{
		"set": "khazaddum",
		"id": 61,
		"quantity": 5,
		"type": "enemy",
		"title": "Goblin Swordsman",
		"icon": "goblin",
		"cost": 20,
		"strength": 1,
		"attack": 3,
		"defense": 1,
		"hp": 2,
		"traits": ["Goblin", "Orc"],
		"effect": {
			"normal": "Goblin Swordsman gets +2 ATK if its attack is undefended.",
			"shadow": "Add Goblin Swordsman to the staging area."
		}
	},
	{
		"set": "khazaddum",
		"id": 62,
		"quantity": 3,
		"type": "treachery",
		"title": "Watchful Eyes",
		"icon": "goblin",
		"effect": {
			"when revealed": "The first player attaches Watchful Eyes to one of his heroes. (Counts as a Condition attachment with the text: \"Limit 1 per hero. Forced: If attached hero is exhausted at the end of the combat phase, reveal 1 card from the encounter deck and add it to the staging area.\")"
		}
	},
	{
		"set": "khazaddum",
		"id": 63,
		"quantity": 2,
		"type": "location",
		"title": "Goblin Tunnels",
		"icon": "goblin",
		"strength": 2,
		"hp": 7,
		"traits": ["Underground", "Dark"],
		"effect": {
			"normal": "While Goblin Tunnels is in the staing area, it gains \"Forced: After a Goblin is revealed from the encounter deck, remove a progress token from the current quest card.\"",
			"shadow": "Attacking enemy gets +1 ATK. (+3 ATK instead if attacking enemy is a Goblin.)"
		}
	},
	{
		"set": "khazaddum",
		"id": 64,
		"quantity": 1,
		"type": "quest",
		"title": "Entering the Mines",
		"icon": "pit",
		"hp": 7,
		"effect": {
			"A": {
				"normal": "You have been sent by the White Council to Moria, to deliver a message to Balin and his Dwarven colony. No one has heard from him in a while.",
				"setup": "Search the encounter deck for East-gate and Cave Torch. Put East-gate into play as the active location, and have the first player attach Cave Torch to a hero of his choice. Set First Hall and Bridge of Khazad-dum aside, out of play. Shuffle the encounter deck."
			},
			"B": {
				"normal": "The doors of the East-gate hang crooked on their henges. The darkness inside the doorway is still and impenetrable, shutting out the last beams of a sinking sun.",
				"when revealed": "Reveal 1 encounter card per player, and add it to the staging area.\nPlayers cannot advance to the next stage of the scenario unless Bridge of Khazad-dum is in their victory display."
			}
		}
	},
	{
		"set": "khazaddum",
		"id": 65,
		"quantity": 1,
		"type": "quest",
		"title": "Goblin Patrol",
		"icon": "pit",
		"hp": 11,
		"effect": {
			"A": {
				"normal": "The skeletons of Dwarves and Orcs lie undisturbed, but you have discovered no recent sign of the Dwarven colony. The sound of scampering feet travels to your ears, and you move in that direction to investigate. There is a patrol of Goblins, marching in a loose formation through the shadows."
			},
			"B": {
				"when revealed": "Each player must search the encounter deck and discard pile for 1 enemy of his choice, and add it to the staging area. One choice must be Patrol Leader, if able.",
				"forced": "After an enemy is revealed from the encounter deck, discard it instead of adding it to the staging area.\nIf there are no enemies in play, immediately advance to the next stage of the scenario. (Players can also advance by placing 11 progress tokens on Goblin Patrol.)"
			}
		}
	},
	{
		"set": "khazaddum",
		"id": 66,
		"quantity": 1,
		"type": "quest",
		"title": "A Way Up",
		"icon": "pit",
		"hp": 12,
		"effect": {
			"A": {
				"normal": "You have captured a member of the patrol, and press the wounded Goblin for information about the Dwarves. It gives a nasty laugh, and with a mouthful of blood spits out \"Balin can be found in the chamber of records!\" It can say no more."
			},
			"B": {
				"normal": "The Chamber of Records is on the Seventh Level of Moria. The way up is treacherous, and you are accompanied by a sense of unease and vague dread.\nHeroes do not collect resources during the resource phase.\nIf the players defeat this stage, they win the game."
			}
		}
	},
	{
		"set": "khazaddum",
		"id": 67,
		"quantity": 1,
		"type": "quest",
		"title": "Search for the Chamber",
		"icon": "seventh",
		"hp": 15,
		"effect": {
			"A": {
				"normal": "You are investigating the Seventh Level of Moria, searching for the Chamber of Records and any sign of Balin's colony. In the heavy twilight of a hall, a bulky tome is discovered in the grip of a Dwarf Skeleton. You carefully take possession of the book. Perhaps it will give you some answers.",
				"setup": "Search the encounter deck for Book of Mazarbul, and have the first player attach it to a hero of his choice. Shuffle the encounter deck."
			},
			"B": {
				"normal": "The Dwarven runes of the book appear to hold a detailed record of the fledgling colony. But there is some Elvish script at the end which seems out of place...",
				"when revealed": "Reveal 1 encounter card per player, and add it to the staging area."
			}
		}
	},
	{
		"set": "khazaddum",
		"id": 68,
		"quantity": 1,
		"type": "quest",
		"title": "The Fate of Balin",
		"icon": "seventh",
		"hp": 17,
		"effect": {
			"A": {
				"normal": "You have discovered the Chamber. Before you lies the resting place of Balin, last lord of Moria. The final portion of the book tells the grim tale- Balin was slain in the Dimrill Dale, and the Dwarves were then trapped in the mines. It seems as if there are no survivors. You stand silently by his tomb, but cannot tarry. Orc war cries and horns sound close. You leave the cumbersome book as a testament to the Dwarves' valor, and prepare to fight your way out, lest Balin's fate becomes your own..."
			},
			"B": {
				"when revealed": "Remove Book of Mazarbul from the game.",
				"forced": "At the end of the staging step, reveal the top X cards of the encounter deck, adding all enemies to the staging area. Discard the other revealed cards without resolving them. X is the number of players.\nIf the players defeat this stage, they win the game."
			}
		}
	},
	{
		"set": "khazaddum",
		"id": 69,
		"quantity": 1,
		"type": "quest",
		"title": "A Presence in the Dark",
		"icon": "flight",
		"hp": 0,
		"effect": {
			"A": {
				"normal": "You have discovered the fate of the Dwarven colony, and seek to leave Moria. But exiting may not be as simple as entering...",
				"setup": "Prepare the quest deck. Add The Nameless Fear to the staging area. Remove all copies of A Foe Beyond from the encounter deck. Then, shuffle 1 copy of A Foe Beyond per player back into the encounter deck."
			},
			"B": {
				"normal": "As you leave the Seventh Level, the air grows thick and drums begin to roll from the deeps. A man-shape shadow, yet greater, masses at the end of the hall, and begins to head straight for you.",
				"when revealed": "Reveal 1 encounter card per player, and add it to the staging area. Then, add A Presence in the Dark to your victory display."
			}
		},
		"victory": 2
	},
	{
		"set": "khazaddum",
		"id": 70,
		"quantity": 1,
		"type": "quest",
		"title": "Search for an Exit - Heading Down",
		"icon": "flight",
		"hp": 5,
		"effect": {
			"A": {
				"normal": "As the presence draws near, doubt and fear surround you like a vast shadow. You must find daylight, you must escape from the Black Pit...\nWhile Search for an Exit is the active quest card, only flip it to side 2B at the beginning of the staging step."
			},
			"B": {
				"normal": "It looks like you may have to head back up the other way.\nPlayers may bypass this quest card at the end of the combat phase.",
				"forced": "If Heading Up is in the player's victory display at the end of any quest phase, shuffle Heading Up back into the quest deck."
			}
		},
		"victory": 1
	},
	{
		"set": "khazaddum",
		"id": 71,
		"quantity": 1,
		"type": "quest",
		"title": "Search for an Exit - Heading Up",
		"icon": "flight",
		"hp": 7,
		"effect": {
			"A": {
				"normal": "As the presence draws near, doubt and fear surround you like a vast shadow. You must find daylight, you must escape from the Black Pit...\nWhile Search for an Exit is the active quest card, only flip it to side 2B at the beginning of the staging step."
			},
			"B": {
				"normal": "Perhaps if you climbed this pile of rocks, there would be a way out...\nPlayers may bypass this quest card at the end of the combat phase.",
				"forced": "If Heading Down is in the player's victory display at the end of any quest phase, shuffle Heading Down back into the quest deck."
			}
		},
		"victory": 1
	},
	{
		"set": "khazaddum",
		"id": 72,
		"quantity": 1,
		"type": "quest",
		"title": "Search for an Exit - A Wrong Turn",
		"icon": "flight",
		"hp": 1,
		"effect": {
			"A": {
				"normal": "As the presence draws near, doubt and fear surround you like a vast shadow. You must find daylight, you must escape from the Black Pit...\nWhile Search for an Exit is the active quest card, only flip it to side 2B at the beginning of the staging step."
			},
			"B": {
				"normal": "This is a dangerous part of the Mines\nPlayers may bypass this quest card at the end of the combat phase.",
				"when revealed": "Reveal 1 encounter card per player, and add it to the staging area."
			}
		},
		"victory": 2
	},
	{
		"set": "khazaddum",
		"id": 73,
		"quantity": 1,
		"type": "quest",
		"title": "Search for an Exit - Narrow Paths",
		"icon": "flight",
		"hp": 3,
		"effect": {
			"A": {
				"normal": "As the presence draws near, doubt and fear surround you like a vast shadow. You must find daylight, you must escape from the Black Pit...\nWhile Search for an Exit is the active quest card, only flip it to side 2B at the beginning of the staging step."
			},
			"B": {
				"normal": "Players may bypass this quest card at the end of the combat phase.",
				"when revealed": "Each player chooses 1 questing character he controls. Each questing character not chosen does not count its Willpower until the end of the turn.",
				"forced": "After placing the 1st progress token on Narrow Paths, search the encounter deck and discard pile for Abandoned Tools and add it to the staging area, if able."
			}
		},
		"victory": 1
	},
	{
		"set": "khazaddum",
		"id": 74,
		"quantity": 1,
		"type": "quest",
		"title": "Search for an Exit - Hasty Council",
		"icon": "flight",
		"hp": 0,
		"effect": {
			"A": {
				"normal": "As the presence draws near, doubt and fear surround you like a vast shadow. You must find daylight, you must escape from the Black Pit...\nWhile Search for an Exit is the active quest card, only flip it to side 2B at the beginning of the staging step."
			},
			"B": {
				"normal": "You pause momentarily to consider your options...",
				"when revealed": "Shuffle all copies of A Foe Beyond from the encounter discard pile back into the encounter deck. Reveal the top 2 cards of the quest deck. Choose 1 to become the active quest (flipped to side 2B) and put the other on the bottom of the quest deck. Then, add Hasty Council to your victory display."
			}
		},
		"victory": 2
	},
	{
		"set": "khazaddum",
		"id": 75,
		"quantity": 1,
		"type": "quest",
		"title": "Search for an Exit - Blocked by Shadow",
		"icon": "flight",
		"hp": 9,
		"effect": {
			"A": {
				"normal": "As the presence draws near, doubt and fear surround you like a vast shadow. You must find daylight, you must escape from the Black Pit...\nWhile Search for an Exit is the active quest card, only flip it to side 2B at the beginning of the staging step."
			},
			"B": {
				"normal": "Players may bypass this quest card at the end of the combat phase.\nIf the players defeat this stage, they escape and win the game.",
				"when revealed": "The first player chooses 1 of the following:\nEach player discards 1 card from the top of the encounter deck. If the card is a treachery card, the discarding player is eliminated from the game.\nReveals the next quest card, putting Blocked by Shadow on the bottom of the quest deck."
			}
		}
	},
	{
		"set": "khazaddum",
		"id": 76,
		"quantity": 1,
		"type": "quest",
		"title": "Search for an Exit - Escape from Darkness",
		"icon": "flight",
		"hp": 4,
		"effect": {
			"A": {
				"normal": "As the presence draws near, doubt and fear surround you like a vast shadow. You must find daylight, you must escape from the Black Pit...\nWhile Search for an Exit is the active quest card, only flip it to side 2B at the beginning of the staging step."
			},
			"B": {
				"normal": "There is a weakness in the walls. You can practically taste the freedom beyond.\nAbandoned Tools gains: \"Refresh Action: Exhaust attached hero to put a progress token on Escape from Darkness.\"\nPlayers may bypass this quest card at the end of the combat phase.\nProgress tokens cannot be placed on Escape from Darkness except by Abandoned Tools. If the players defeat this stage, they escape and win the game."
			}
		}
	}
]
