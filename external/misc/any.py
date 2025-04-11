#!/usr/bin/python3

"""
Generates the metadata file for the any% save files.
"""

import sys
import argparse
import copy
from enum import IntEnum, unique
import struct


@unique
class Platform(IntEnum):
    GCN = 0
    WII = 1


class Requirements(IntEnum):
    POS = 1
    CAM = 2


def main(args=None):
    parser = argparse.ArgumentParser(
        sys.argv[0], description="A tool to generate the metadata file for the any% save files.")
    parser.add_argument(
        "-p", "--platform", type=str.upper, choices=[e.name for e in Platform], default=Platform.GCN.name, help="The platform to generate for.")
    args = parser.parse_args()

    args.platform = Platform[args.platform]

    default_entry = {
        "requirements": 0,
        "pos": (0.0, 0.0, 0.0),
        "angle": 0,
        "cam": {"pos": (0, 0, 0), "target": (0, 0, 0)},
        "counter": 0,
    }

    # order matters
    file_names = [
        "ordon_gate_clip",
        "ordon_gate_clip",
        "goats",
        "hugo",
        "ems",
        "purple_mist",
        "forest_bit",
        "forest_escape",
        "gorge_void",
        "rupee_roll",
        "lanayru_gate_clip",
        "karg",
        "eldin_twilight",
        "bomb_house_skip",
        "lanayru_twilight",
        "waterfall_sidehop",
        "boss_bug",
        "iza",
        "plumm_oob",
        "elh",
        "lakebed_1",
        "deku_toad",
        "lakebed_bk_skip",
        "onebomb",
        "mdh_tower",
        "mdh_bridge",
        "spr_warp",
        "spr",
        "darkhammer",
        "camp",
        "ag",
        "poe_1_skip",
        "death_sword_skip",
        "stallord",
        "stallord",
        "cits_early",
        "cits_1",
        "aeralfos_skip",
        "cits_2",
        "fan_tower",
        "argorok",
        "palace_1",
        "palace_2",
        "early_platform",
        "zant",
        "hc",
        "darknut",
        "hc_tower",
        "beast_ganon",
        "horseback_ganon",
        "ganondorf",
    ]

    if args.platform is Platform.WII:
        # order matters
        file_names = [
            "ordon_gate_clip",
            "ordon_gate_clip",
            "seam_clip",
            "goats",
            "hugo",
            "faron_twilight",
            "ems",
            "purple_mist",
            "kargarok_fight",
            "kargarok_flight",
            "kb1",
            "eldin_twilight",
            "bombhouse_skip",
            "epona_oob_to_flight_by_fowl",
            "lanayru_twilight",
            "waterfall_sidehop",
            "boss_bug",
            "iza",
            "plumm_oob",
            "enter_lakebed",
            "lakebed_1",
            "deku_toad",
            "morpheel",
            "mdh_tower",
            "mdh_bridge",
            "messenger_skip",
            "snowpeak_ruins_mbbb",
            "freezard_skip",
            "dark_hammer",
            "bulblin_camp",
            "ag",
            "poe_1_skip",
            "early_boss_key",
            "death_sword",
            "stallord",
            "stallord",
            "early_city",
            "cits",
            "arealfos",
            "cits_2",
            "fan_tower",
            "argorok",
            "pot1",
            "stupidroom",
            "pot2",
            "earlypf",
            "zant",
            "hc",
            "darknut",
            "towerclimb",
            "beast_ganon",
            "horseback",
        ]

    any_p = [{**copy.deepcopy(default_entry), "id": i, "filename": name}
             for i, name in enumerate(file_names)]

    file_dict = {e: i for i, e in enumerate(file_names)}

    def update_entry(filename, data):
        if filename in file_names:
            any_p[file_dict[filename]] = {**any_p[file_dict[filename]], **data}

    # ordon gate clip
    update_entry("ordon_gate_clip", {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (827.450012, 216.490097, -4533.90625),
        'angle': 498,
        'cam': {
            'pos': (833.467468, 477.604675, -4241.97266),
            'target': (827.497559, 329.622986, -4532.90723)
        },
        'counter': 10
    })

    if args.platform is Platform.GCN:
        any_p[1]["requirements"] = Requirements.POS | Requirements.CAM
        any_p[1]["pos"] = (466.622467, 319.770752, -11651.3867)
        any_p[1]["angle"] = 52540
        any_p[1]["cam"]["pos"] = (735.525391, 524.418701, -11576.4746)
        any_p[1]["cam"]["target"] = (465.674622, 421.052704, -11651.0684)
        any_p[1]["counter"] = 10

    # back in time
    update_entry("bit", {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (466.622467, 319.770752, -11651.3867),
        'angle': 52540,
        'cam': {
            'pos': (735.525391, 524.418701, -11576.4746),
            'target': (465.674622, 421.052704, -11651.0684)
        },
        'counter': 10
    })


     # hugo
    update_entry("hugo", {
         'requirements': Requirements.POS | Requirements.CAM,
         'pos': (701.797302, 85.5212784, -5299.6123),
         'angle': 63622,
         'cam': {'pos': (735.525391, 524.418701, -11576.4746), 'target': (465.674622, 421.052704, -11651.0684)},
     })
 
     # purple mist
    update_entry("purple_mist", {
         'requirements': Requirements.POS,
         'pos': (-23524.6152, 250.0, -16220.166),
         'angle': 40758,
         'counter': 30,
     })
 
     # king bulblin 1
    if args.platform is Platform.WII:
         update_entry("kb1", {
             'requirements': Requirements.POS,
             'pos': (-9717.6035, 337.0316, 97.9661),
             'angle': 16384,
             'counter': 30,
         })
 
     # boss bug
    if args.platform is Platform.WII:
         update_entry("boss_bug", {
             'requirements': Requirements.POS,
             'pos': (-87517.1562, -18789.2812, 38927.0820),
             'angle': 41851,
             'counter': 30,
         })
 
     # plumm oob
    if args.platform is Platform.WII:
         update_entry("plumm_oob", {
             'requirements': Requirements.POS,
             'pos': (-104271.3750, -18470.0, 52661.7812),
             'angle': 45103,
             'counter': 30,
         })
 
     # mdh tower
    if args.platform is Platform.WII:
         update_entry("mdh_tower", {
             'requirements': Requirements.POS | Requirements.CAM,
             'pos': (25362.3184, -3028.7673, 10060.8379),
             'angle': 29327,
             'counter': 30,
         })
 
     # mdh bridge
    if args.platform is Platform.WII:
         update_entry("mdh_bridge", {
             'requirements': Requirements.POS | Requirements.CAM,
             'pos': (13050.0, 9825.0, 36202.0),
             'angle': 32768,
             'counter': 30,
         })
 
     # freezard skip
    if args.platform is Platform.WII:
         update_entry("freezard_skip", {
             'requirements': Requirements.POS | Requirements.CAM,
             'pos': (-1125.0, 0.0, -1275.0),
             'angle': 32768,
             'counter': 30,
         })
 
     # dark hammer
    if args.platform is Platform.WII:
         update_entry("dark_hammer", {
             'requirements': Requirements.POS | Requirements.CAM,
             'pos': (0.7448, 0.0, 1330.9711),
             'angle': 32768,
             'counter': 20,
         })

 
     # eldin twilight
    update_entry("eldin_twilight", {
         'requirements': Requirements.POS | Requirements.CAM,
         'pos': (455.088379, -150.0, 11516.7227),
         'angle': 6058,
         'cam': {'pos': (219.367218, -20.1253014, 11157.582), 'target': (482.515137, -39.9999771, 11558.5283)},
         'counter': 10,
     })
 
     # waterfall sidehop
    if args.platform is Platform.WII:
         update_entry("waterfall_sidehop", {
             'requirements': Requirements.POS,
             'pos': (1169.5876, 12.6414, -1114.5820),
             'angle': 0,
             'counter': 10,
         })
 
     # iza
    update_entry("iza", {
         'requirements': Requirements.POS,
         'pos': (5979.97217, 150.0, -2748.34155),
         'angle': 10114,
     })
 
     # snowpeak messenger skip
    update_entry("messenger_skip", {
         'requirements': Requirements.POS | Requirements.CAM,
         'pos': (-9294.87988, 980.0, -11712.3838),
         'angle': 346,
         'cam': {'pos': (-9309.65137, 1280.4469, -12130.7695), 'target': (-9294.2207, 1180.0, -11692.3945)},
         'counter': 10,
     })
 
     # morpheel
    update_entry('morpheel', {
         'requirements': Requirements.POS | Requirements.CAM,
         'pos': (-1193.0, -23999.00, -770.0),
         'angle': 10754,
         'counter': 20,
     })
 
     # poe 1 skip
    update_entry('poe_1_skip', {
         'requirements': Requirements.POS | Requirements.CAM,
         'pos': (-2046.97168, 0.0, -587.304871),
         'angle': 49030,
         'cam': {'pos': (-1779.00293, 213.707397, -584.686768), 'target': (-2047.97168, 130.16568, -587.317139)},
         'counter': 10,
     })

    file = open("any.bin", "wb")

    for entry in any_p:
        print(entry)
        file.write(entry["requirements"].to_bytes(1, "big", signed=False))
        file.write(int(0).to_bytes(1, "big", signed=False))  # padding
        file.write(entry["angle"].to_bytes(2, "big", signed=False))
        file.write(struct.pack('>fff', *entry["pos"]))
        file.write(struct.pack('>fff', *entry["cam"]["pos"]))
        file.write(struct.pack('>fff', *entry["cam"]["target"]))
        file.write(entry["counter"].to_bytes(4, "big", signed=False))
        file.write(struct.pack(">32s", entry["filename"].encode("ascii")))
        file.write(int(0).to_bytes(4, "big", signed=False))  # padding


if __name__ == "__main__":
    main(sys.argv)
