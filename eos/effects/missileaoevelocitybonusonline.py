# missileAOEVelocityBonusOnline
#
# Used by:
# Modules from group: Missile Guidance Enhancer (3 of 3)
type = "passive"


def handler(fit, module, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "aoeVelocity", module.getModifiedItemAttr("aoeVelocityBonus"),
                                    stackingPenalties=True)
