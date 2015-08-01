from django.contrib import admin
from coc_war_planner.core.models import Troop
from coc_war_planner.core.models import TroopLevel
from coc_war_planner.core.models import Spell
from coc_war_planner.core.models import SpellLevel
from coc_war_planner.core.models import Hero
from coc_war_planner.core.models import HeroAbility
from coc_war_planner.core.models import HeroLevel

admin.site.register(Troop)
admin.site.register(TroopLevel)
admin.site.register(Spell)
admin.site.register(SpellLevel)
admin.site.register(Hero)
admin.site.register(HeroAbility)
admin.site.register(HeroLevel)
