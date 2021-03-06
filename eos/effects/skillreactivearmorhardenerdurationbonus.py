# skillReactiveArmorHardenerDurationBonus
#
# Used by:
# Skill: Resistance Phasing
type = "passive"


def handler(fit, src, context):
    lvl = src.level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Resistance Shift Hardener", "duration",
                                  src.getModifiedItemAttr("durationBonus") * lvl)
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Resistance Phasing"), "duration",
                                  src.getModifiedItemAttr("durationBonus") * lvl)
