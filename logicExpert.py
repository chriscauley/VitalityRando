from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable, Items
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places.
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    GravitySuit, Varia, Wave, SpeedBooster, Spazer, Ice, Grapple,
    Plasma, Screw, Charge, SpaceJump, Energy, Reserve, Burst
) = items_unpackable

energy200 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 1
))

energy300 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 2
))
energy400 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 3
))
energy500 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 4
))
energy600 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 5
))
energy700 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 6
))
energy800 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 7
))
energy900 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 8
))
energy1000 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 9
))
energy1200 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy)  >= 11
))
energy1500 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy)  >= 14
))


hellrun1 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy200 in loadout)
))
hellrun2 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy300 in loadout)
))
hellrun3 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy400 in loadout)
))
hellrun4 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy500 in loadout)
))
hellrun5 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))
hellrun6 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy700 in loadout)
))
hellrun8 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy900 in loadout)
))
hellrun9 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1000 in loadout)
))
hellrun11 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1200 in loadout)
))
hellrun14 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1500 in loadout)
))

missile10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 2 >= 10
))
missile15 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 2 >= 15
))
super10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) >= 10
))
powerBomb2 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 2
))
powerBomb3 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 3
))
powerBomb4 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 4
))
powerBomb8 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 8
))
powerBomb15 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 15
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (PowerBomb in loadout)
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canBreakBlocks = LogicShortcut(lambda loadout: (
    #with bombs or screw attack, maybe without morph
    (canUseBombs in loadout) or
    (Screw in loadout)
))
bog = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) or
    (
        (Morph in loadout) and
        (Super in loadout) and
        (Charge in loadout)
        )
))
andavald = LogicShortcut(lambda loadout: (
    (canUsePB in loadout) and
    (
        (powerBomb3 in loadout) or
        (canIBJ in loadout) or
        (Springball in loadout)
        )
))
tacLacora = LogicShortcut(lambda loadout: (
    (bog in loadout) and
    (SpeedBooster in loadout) and
    (
        (HiJump in loadout) or
        (SpaceJump in loadout) or
        (canIBJ in loadout) or
        (Springball in loadout) or
        (powerBomb8 in loadout)
        ) #all to get into the first big room
))
phantoon = LogicShortcut(lambda loadout: (
    (tacLacora in loadout) and
    (
        (Missile in loadout) or
        (Super in loadout) or
        (Wave in loadout) or
        (
            (Charge in loadout) and
            (Grapple in loadout)
            )
        )
))
rightBog = LogicShortcut(lambda loadout: (
    (bog in loadout) and
    (
        (Charge in loadout) or
        (canUsePB in loadout)
        )
))
akhlys = LogicShortcut(lambda loadout: (
    (rightBog in loadout) and
    (Super in loadout)
))
GTarea = LogicShortcut(lambda loadout: (
    (akhlys in loadout) and
    (
        (
            (Wave in loadout) and
            (canUseBombs in loadout)
            ) or
        (
            (SpeedBooster in loadout) and
            (Charge in loadout) and
            (Varia in loadout)
            )
        ) #Is GT heated?
    #Does it need the volcano blown or Ridley dead?
))
gravityArea = LogicShortcut(lambda loadout: (
    (akhlys in loadout) and
    (
        (HiJump in loadout) or
        (GravitySuit in loadout)
        ) and
    (
        (energy800 in loadout) or
        (
            (energy400 in loadout) and
            (Varia in loadout)
            )
        ) #defeating BT/acid dive
))
area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}


location_logic: LocationLogicType = {
    "Morph Ball": lambda loadout: (
        True
    ),
    "Bombs": lambda loadout: (
        (canIBJ in loadout)
        #Other ways to defeat the Oums
    ),
    "Pendulu Top Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Landing Site Power Bomb": lambda loadout: (
        (canUsePB in loadout)
    ),
    "Parlor Kago Missile": lambda loadout: (
        (canUsePB in loadout) and
        (
            (Springball in loadout) or
            (powerBomb2 in loadout) or
            (canIBJ in loadout)
            )
    ),
    "Parlor Wall Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Pendulu Right Main Missile": lambda loadout: (
        (canUseBombs in loadout) and
        (
            (canIBJ in loadout) or
            (powerBomb4 in loadout) or
            (Springball in loadout)
            )
    ),
    "Pantry Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Pendulu Sand Mountain Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Pendulu Ship Super": lambda loadout: (
        (Morph in loadout) and
        (Super in loadout)
    ),
    "Pendulu Left Energy Tank": lambda loadout: (
        (Morph in loadout)
    ),
    "Pendulu Sand Cavern Missile": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Pendulu Sand Cavern Energy Tank": lambda loadout: (
        (canIBJ in loadout) or
        (powerBomb2 in loadout) or
        (
            (Morph in loadout) and
            (Springball in loadout)
            )
    ),
    "Pendulu Speed Locked Super": lambda loadout: (
        (Morph in loadout) and
        (SpeedBooster in loadout)
    ),
    "Draygon Lower Missile": lambda loadout: (
        (canUsePB in loadout) and
        (
            (canIBJ in loadout) or
            (Springball in loadout) or
            (powerBomb2 in loadout)
            )
        #TEST 
    ),
    "Draygon Top Missile": lambda loadout: (
        (canUsePB in loadout)
    ),
    "Draygon Super": lambda loadout: (
        (SpeedBooster in loadout) and
        (canUseBombs in loadout) and
        (
            (canIBJ in loadout) or
            (Springball in loadout) or
            (powerBomb3 in loadout)
            )
    ),
    "Tchornobog Treetop Missile": lambda loadout: (
        (bog in loadout) and
        (
            (canIBJ in loadout) or
            (powerBomb3 in loadout) or
            (
                (Springball in loadout) and
                (powerBomb2 in loadout)
                )
            )
    ),
    "Tchornobog Big Tree Missile": lambda loadout: (
        (bog in loadout)
    ),
    "Tchornobog Big Tree Energy": lambda loadout: (
        (bog in loadout)
    ),
    "Tchornobog Roots Super": lambda loadout: (
        (bog in loadout) and
        (SpeedBooster in loadout)
    ),
    "Tchornobog Roots Power Bomb": lambda loadout: (
        (bog in loadout) and
        (canUsePB in loadout)
    ),
    "Andavald Entry Missile": lambda loadout: (
        (canUsePB in loadout)
    ),
    "Andavald Morph Maze Missile": lambda loadout: (
        (andavald in loadout)
    ),
    "Screw Attack": lambda loadout: (
        (andavald in loadout) and
        (
            (Wave in loadout) or
            (Missile in loadout) or
            (Super in loadout)
            ) and
        (
            (GravitySuit in loadout) or
            (SpaceJump in loadout) or
            (HiJump in loadout) or
            (Springball in loadout)
            )
    ),
    "Screw Power Bomb": lambda loadout: (
        (andavald in loadout)
    ),
    "Above Plasma Missile": lambda loadout: (
        (andavald in loadout) and
        (Super in loadout)
    ),
    "Plasma Cavern Super": lambda loadout: (
        (andavald in loadout) and
        (SpeedBooster in loadout)
    ),
    "Plasma Snail Super": lambda loadout: (
        (andavald in loadout)
    ),
    "BT Super": lambda loadout: (
        (andavald in loadout)
    ),
    "Dead Pool Energy": lambda loadout: (
        (andavald in loadout) and
        (SpeedBooster in loadout)
    ),
    "Plasma Speed Missile": lambda loadout: (
        (andavald in loadout) and
        (SpeedBooster in loadout) and
        (
            (Grapple in loadout) or
            (GravitySuit in loadout) or
            (
                (Springball in loadout) and
                (HiJump in loadout)
                )
            )
    ),
    "Plasma Beam": lambda loadout: (
        (andavald in loadout) and
        (Plasma in loadout) and
        (
            (Grapple in loadout) or
            (GravitySuit in loadout) or
            (
                (Springball in loadout) and
                (HiJump in loadout)
                )
            )
    ),
    "Spo Spo Energy": lambda loadout: (
        (bog in loadout) and
        (Super in loadout)
    ),
    "Springball Energy Tank": lambda loadout: (
        (tacLacora in loadout) and
        (Wave in loadout)
    ),
    "Springball": lambda loadout: (
        (tacLacora in loadout) and
        (
            (canIBJ in loadout) or
            (Springball in loadout)
            )
    ),
    "Wave Missile": lambda loadout: (
        (tacLacora in loadout) and
        (Wave in loadout)
    ),
    "Wave Beam": lambda loadout: (
        (tacLacora in loadout) and
        (phantoon in loadout)
    ),
    "Phantoon Super": lambda loadout: (
        (phantoon in loadout) and
        (Grapple in loadout)
    ),
    "Grapple Power Bomb": lambda loadout: (
        (phantoon in loadout) and
        (canBreakBlocks in loadout)
    ),
    "Grapple Beam": lambda loadout: (
        (phantoon in loadout)
    ),
    "Grapple Missile": lambda loadout: (
        (phantoon in loadout)
    ),
    "Tac Lacora Central Missile": lambda loadout: (
        (tacLacora in loadout)
    ),
    "Tchornobog Roots Energy": lambda loadout: (
        (bog in loadout)
    ),
    "Charge Missile": lambda loadout: (
        (bog in loadout) and
        (SpeedBooster in loadout)
    ),
    "Charge Beam": lambda loadout: (
        (bog in loadout) and
        (
            (Charge in loadout) or
            (Super in loadout)
            )
    ),
    "HiJump Super": lambda loadout: (
        (rightBog in loadout) and
        (
            (HiJump in loadout) or
            (SpaceJump in loadout) or
            (canIBJ in loadout) or
            (
                (GravitySuit in loadout) and
                (SpeedBooster in loadout)
                )
            )
    ),
    "HiJump Missile": lambda loadout: (
        (canUsePB in loadout)
    ),
    "HiJump Power Bomb": lambda loadout: (
        (canUsePB in loadout)
    ),
    "Speed Booster": lambda loadout: (
        (canUsePB in loadout) and
        (
            (Missile in loadout) or
            (Charge in loadout)
            ) #defeating Dray
    ),
    "Draygon Lab Energy Tank": lambda loadout: (
        (canUsePB in loadout) and
        (SpeedBooster in loadout) and
        (
            (Missile in loadout) or
            (Charge in loadout)
            ) #defeating Dray
    ),
    "Pendulu Sand Pit Missile": lambda loadout: (
        (Morph in loadout) and
        (Super in loadout)
    ),
    "Spazer Missile": lambda loadout: (
        (Morph in loadout) and
        (Super in loadout)
    ),
    "Spazer": lambda loadout: (
        (Morph in loadout) and
        (Super in loadout) and
        (Charge in loadout)
    ),
    "Spazer Super": lambda loadout: (
        (Morph in loadout) and
        (Super in loadout) and
        (Charge in loadout)
    ),
    "Below Ridley Missile": lambda loadout: (
        (akhlys in loadout) and
        (Varia in loadout) and
        (
            (GravitySuit in loadout) or
            (energy600 in loadout)
            )
    ),
    "Space Jump Sky Missile": lambda loadout: (
        (akhlys in loadout) and
        (
            (Plasma in loadout) or
            (SpeedBooster in loadout) or
            (Charge in loadout) or
            (Spazer in loadout)
            ) and
        (
            (Varia in loadout) and
            (energy400 in loadout)
            )
    ),
    "Space Jump Lava Missile": lambda loadout: (
        (akhlys in loadout) and
        (Varia in loadout) and
        (
            (Plasma in loadout) or
            (SpeedBooster in loadout) or
            (Charge in loadout) or
            (Spazer in loadout)
            ) and
        (
            (Varia in loadout) and
            (energy400 in loadout)
            )
        
    ),
    "Space Jump Super": lambda loadout: (
        (akhlys in loadout) and
        (
            (Plasma in loadout) or
            (SpeedBooster in loadout) or
            (Charge in loadout) or
            (Spazer in loadout)
            ) and
        (
            (Varia in loadout) and
            (energy400 in loadout)
            )
    ),
    "Space Jump": lambda loadout: (
        (akhlys in loadout) and
        (
            (Plasma in loadout) or
            (SpeedBooster in loadout) or
            (Charge in loadout) or
            (Spazer in loadout)
            ) and
        (
            (Varia in loadout) and
            (energy400 in loadout)
            )
    ),
    "Below Ridley Power Bomb": lambda loadout: (
        (akhlys in loadout) and
        (
            (Ice in loadout) or
            (SpaceJump in loadout) or
            (HiJump in loadout) or
            (Springball in loadout) or
            (canIBJ in loadout) or
            (SpeedBooster in loadout)
            )
    ),
    "Akhlys First Fortress Super": lambda loadout: (
        (akhlys in loadout) and #implies Supers
        (canUseBombs in loadout) and
        (
            (powerBomb2 in loadout) or
            (canIBJ in loadout) or
            (Springball in loadout)
            )
    ),
    "Varia Area Power Bomb": lambda loadout: (
        (akhlys in loadout) and
        (canUsePB in loadout)
    ),
    "Varia Suit": lambda loadout: (
        (akhlys in loadout) and
        (canUsePB in loadout)
    ),
    "Varia Area Super": lambda loadout: (
        (akhlys in loadout) and
        (
            (Varia in loadout) or
            (energy600 in loadout) or
            (
                (GravitySuit in loadout) and
                (energy400 in loadout)
                )
            )
    ),
    "Ice Lower Super": lambda loadout: (
        (akhlys in loadout) and
        (
            (canIBJ in loadout) or
            (powerBomb2 in loadout) or
            (Springball in loadout)
            )
    ),
    "Ice Left Missile": lambda loadout: (
        (akhlys in loadout) and
        (canBreakBlocks in loadout) and
        (
            (HiJump in loadout) or
            (SpaceJump in loadout) or
            (canIBJ in loadout) or
            (Springball in loadout) or
            (Ice in loadout)
            )
    ),
    "Ice Right Missile": lambda loadout: (
        (akhlys in loadout) and
        (
            (canUseBombs in loadout) or
            (Springball in loadout)
            ) and
        (
            (HiJump in loadout) or
            (SpaceJump in loadout) or
            (canIBJ in loadout) or
            (Springball in loadout) or
            (Ice in loadout)
            )
    ),
    "Ice Beam": lambda loadout: (
        (akhlys in loadout)
    ),
    "Gold Torizo Bottom Missile": lambda loadout: (
        (GTarea in loadout) and
        (canUsePB in loadout)
    ),
    "Gold Torizo Top Missile": lambda loadout: (
        (GTarea in loadout) and
        (SpeedBooster in loadout)
    ),
    "Gold Torizo Energy": lambda loadout: (
        (GTarea in loadout) and
        (Charge in loadout)
    ),
    "Akhlys Boulder Super": lambda loadout: (
        (akhlys in loadout) and
        (Varia in loadout) and #hellrun for now
        (
            (GravitySuit in loadout) or
            (SpaceJump in loadout) or
            (Grapple in loadout) or
            (energy400 in loadout)
            )
    ),
    "Akhlys Boulder Power Bomb": lambda loadout: (
        (akhlys in loadout) and
        (Varia in loadout) and #hellrun for now
        (canUsePB in loadout) and
        (
            (GravitySuit in loadout) or
            (energy400 in loadout)
            )
    ),
    "Akhlys First Fortress Energy": lambda loadout: (
        (akhlys in loadout) and
        (canUsePB in loadout)
    ),
    "Dachora Super": lambda loadout: (
        (bog in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout)
    ),
    "Akhlys Speed Pirates Energy": lambda loadout: (
        (akhlys in loadout) and
        (SpeedBooster in loadout)
    ),
    "Gravity Super": lambda loadout: (
        (gravityArea in loadout)
        
    ),
    "Gravity Suit": lambda loadout: (
        (gravityArea in loadout)
    ),
    "Shaktool Power Bomb": lambda loadout: (
        (gravityArea in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "Shaktool Energy Tank": lambda loadout: (
        (gravityArea in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "Gravity Elevator Super": lambda loadout: (
        (gravityArea in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "HiJump": lambda loadout: (
        (rightBog in loadout) and
        (canUsePB in loadout)
    ),
    "Tchornobog Roots Missile": lambda loadout: (
        (bog in loadout)
    ),
    "Kraid Super": lambda loadout: (
        (bog in loadout) and
        (Charge in loadout)
    ),
    "Volcano Super": lambda loadout: (
        (akhlys in loadout) and
        (GravitySuit in loadout) and
        (Varia in loadout) and
        (SpeedBooster in loadout) and
        (Charge in loadout) and
        (energy700 in loadout) and
        (HiJump in loadout) and
        (
            (canUseBombs in loadout) or
            (SpaceJump in loadout)
            )
        #grav jump with extra energy to do the bottom jump??
    ),
    "Alpha Power Bomb": lambda loadout: (
        (canUsePB in loadout) and
        (Missile in loadout) and
        (Super in loadout) and
        (energy800 in loadout) and
        (Ice in loadout) and
        (Wave in loadout) and
        (Spazer in loadout) and
        (Plasma in loadout) and
        (Varia in loadout) and
        (GravitySuit in loadout) and
        (Springball in loadout) and
        (Screw in loadout) and
        (HiJump in loadout) and
        (SpaceJump in loadout) and
        (SpeedBooster in loadout)
        #this item should not be required, as it might be inaccessible
    ),

}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True
