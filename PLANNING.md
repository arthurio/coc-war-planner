First usable Minimum Viable Product
===================================
:white_check_mark: V0.0
-----------------------
- [X] Setup wagtail
- [X] Create an account
- [X] Create models:
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

- [X] Admin interface to create Spells, Troops and Heros (or initial_data)
- [X] Setup Authentication system

v0.1
----
- [X] Add login/logout
- [ ] Create the profile page
    * [X] Update basic info (level, name)
    * [X] Change clan
    * [ ] Add missing clan
- [ ] Apis:
    * [X] List/Update/Add clan
    * [X] Member: Join/Leave clan
    * [ ] Set TownHall
    * [X] Set Troops
    * [ ] List Troop level
    * [ ] List Troop
    * [ ] Set Spells
    * [ ] Set Heros
    * [ ] Create war
    * [ ] Affect attacks to clan members
- [ ] Create the dashboard page
    * [X] Show Clan
    * [X] Show Troops
    * [ ] Show Heros
    * [ ] Show Spells

v0.2
----
- [ ] Troops UX
    * [ ] Add troop
    * [ ] Update troop level
- [ ] Heros UX
    * [ ] Add hero
    * [ ] Update hero level
- [ ] Spells UX
    * [ ] Add spell
    * [ ] Update spell level
- [ ] Clan UX
    * [ ] Leave clan
    * [ ] Remove user from clan (only chief)

v0.3
----
- [ ] Create the default template
- [ ] Add a navigation


Improve UX - UI
===============
v1.0
----
- [ ] Clan autocomplete
- [ ] Make country a list (choice)

v1.1
----
- [ ] Suggest enemy clans members if exist when setting up attacks
- [ ] Limit troop/spells/heros and their level based on the townhall
  level

v1.2
----
- [ ] Force email validation when registering

v1.3
----
- [ ] Customize Browsable API style
- [ ] Add a loader on the dashboard page for the different components

v1.4
----
- [ ] Use scss or stylus
- [ ] Customize loader http://fgnass.github.io/spin.js/

Improve Perfomances
===================
v2.0
----
- [ ] Create indexes on the mysql DB for search/ordering fields

Write tests
===========
v3.0
----
- [ ] Write Api tests:
    * [ ] Create troops (success)
    * [ ] Create existing troops
    * [ ] Create troops for someone else
    * [ ] Create troops wrong type of level
    * [ ] Update troops (success)
    * [ ] Update troops (wrong type of level)
    * [ ] Update troops of someone else
    * [ ] Update troops not existing
    * [ ] Get troops (success)
    * [ ] Get troops of someone else (success)
    * [ ] Get troops not existing
    * [ ] Non clan member update the chief of the clan
    * [ ] Leave clan -> transfer ownership
    * [ ] Create clan -> set current as chief + become member of clan
    * [ ] Create clan -> forbidden if already part of a clan
    * [ ] Update member (new clan or leave clan) -> update clans the member was a chief of

Add extra functionalities
=========================
v4.0
----
- [ ] Create all the models for the buildings
- [ ] Remove user from clan
