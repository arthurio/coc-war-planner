V0.0
==
- Setup wagtail
- Create an account
- Create models:
    * Member
        fk(user)
        lvl
        username
        clan_id
    * Clan
        pin
        name
        location
        lvl
    * Troop
        name
        category=choice(tier 1, tier 2, tier 3, dark)
        preferred_target
        attack_type
        housing_space
        training_time
        barack_level_required
        range
        movement_speed
        attack_speed
        extra_data(json)
    * TroopLvl
        unique_together(fk(troop_id), lvl)
        training_cost
        research_time
        research_cost
        laboratory_level_required
        hitpoints
        damage_per_second
        damage_per_attack
        extra_data(json)
    * Spell
        name
        type=choice(regular, dark)
        radius
        number_of_pulses
        time_between_pulses
        housing_space
        time_to_brew
        target
        spell_factory_level_required
        extra_data(json))
    * SpellLvl
        unique_together(fk(spell_id), lvl)
        cost
        research_cost
        research_time
        laboratory_level_required
        extra_data(json)
    * Troops
        unique_together(user, troup)
        troop_lvl
    * Spells
        unique_together(user, spell)
        spell_lvl
    * Hero
        name
        attack_type
        movement_speed
        attack_speed
        range
        search_radius
    * HeroLvl
        unique_together(fk(hero_id), lvl)
        damage_per_second
        damage_per_hit
        hitpoints
        regeneration_time
        ability_level
        training_cost
        training_time
        town_hall_level_required
    * HeroAbility
        unique_together(fk(hero_id), lvl)
        damage_increase
        health_recovery
        ability_time
        summoned_unites
        extra_data(json)
    * Heros
        unique_together(user, hero)
        hero_lvl
    * TownHall
        user
        lvl
    * War
        clan
        enemy_clan
        number_of_players
        members(users)
        preparation_time_remaining
        time_remaining
    * Attack
        war
        member(user)
        enemy_rank
        enemy_town_hall_level
        stars
        durations
        iteration=choice(first, second)

- Admin interface to create Spells, Troops and Heros (or initial_data)

v0.1
==
- leave clan/remove user from clan
- Apis:
    * Choose clan (+add clan)
    * Set TownHall
    * Set Troops
    * Set Spells
    * Set Heros
    * Create war
    * Affect attacks to clan members

v0.2
==
- Do some UI work

v1.0
==
- Create all the models for the buildings
- Clan autocomplete
- Set troops on attacks

v1.1
==
- Suggest enemy clans members if exist when setting up attacks
