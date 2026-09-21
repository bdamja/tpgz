#!/usr/bin/python3

"""
Generates the metadata file for the 100% save files.
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
        sys.argv[0], description="A tool to generate the metadata file for the 100% save files.")
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
        "goats",
        "ordon_gate_clip",
        "goats_2",
        "faron_twilight",
        "ems",
        "Purple Mist",
        "forest_1",
        "Forest Temple 2(ebf)",
        "Deku Like(ebf)",
        "Diababa (ebf)",
        "Eldin Vessel", # start of twilight
        "BHS",
        "lanayru_gate_clip",
        "pillar_clip",
        "lakebed_1",
        "deku_toad",
        "karg",
        "lanayru_twilight",
        "corotd",
        "early_ele",
        "gm",
        "kitty_climb",
        "dangoro",
        "fyrus",
        "waterfall_sidehop",
        "boss_bug",
        "kb2",
        "kb2",
        "escort_lja",
        "eldin_collection",
        "lakebed_bk_skip",
        "morpheel",
        "mdh_tower",
        "mdh_bridge",
        "post_mdh",
        "star_1",
        "kb1",
        "iza_1_skip",
        "lh_cave",
        "Desert Collection",
        "camp",
        "ag",
        "speedrat",
        "poe_1_skip",
        "death_sword_skip",
        "stallord",
        "post_ag",
        "spr",
        "darkhammer",
        "spr_2",
        "freezard_2",
        "spr_bk",
        "blizzeta",
        "nf_bomb_boost",
        "grove_skip",
        "grove_boost",
        "tot",
        "tot_early_poe",
        "tot_statue_throws",
        "tot_early_hp",
        "tot_darknut",
        "dot_skip",
        "post_tot",
        "snowboarding",
        "hotspring",
        "orange_backslice",
        "gorge_arc",
        "Flight By fowl",
        "silver_rupee",
        "dmt_poe",
        "ice_puzzle",
        "iza_2",
        "hv_archery",
        "cits_1",
        "city_gate_clip",
        "aeralfos_skip",
        "City 2",
        "cits_poe_cycle",
        "fan_tower",
        "argorok",
        "argorok", # phase 2
        "star_2",
        "palace_1",
        "palace_2",
        "early_platform",
        "zant",
        "coo",
        "coo_10",
        "CoO poe 1 (floor 17)",
        "coo_20",
        "coo_30",
        "CoO poe 2 (floor 33)",
        "coo_40",
        "cats",
        "hc",
        "hc_darknut",
        "Friendless",
        "hc_tower",
        "beast_ganon",
        "horseback_ganon",
    ]

    hundo_p = [{**copy.deepcopy(default_entry), "id": i, "filename": name}
             for i, name in enumerate(file_names)]

    file_dict = {e: i for i, e in enumerate(file_names)}

    def update_entry(filename, data):
        if filename in file_names:
            hundo_p[file_dict[filename]] = {**hundo_p[file_dict[filename]], **data}

    update_entry("ordon_gate_clip", {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (827.497559, 329.622986, -4532.90723),
        'angle': 498,
        'cam': {
            'pos': (833.467468, 477.604675, -4241.97266),
            'target': (827.497559, 329.622986, -4532.90723)
        },
        'counter': 10
    })

    update_entry("Purple Mist", {
        'requirements': Requirements.POS,
        'pos': (-23524.6152, 250.0, -16220.166),
        'angle': 40758,
        'counter': 30
    })

    update_entry("lanayru_gate_clip", {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (-63026.2852, -9065.92578, 71680.3438),
        'angle': 44248,
        'cam': {
            'pos': (-62655.8125, -8900.91309, 71903.6328),
            'target': (-63064.2148, -8969.97656, 71661.0781)
        },
        'counter': 15
    })

    update_entry("early_ele", {
        'requirements': Requirements.POS,
        'pos': (1197.00, -355.55, -5468.84),
        'angle': 45137,
    })

    update_entry("boss_bug", {
        'requirements': Requirements.POS,
        'pos': (-89100.00, -18811.2363, 39410.00),
        'angle': 21504,
    })

    update_entry("kb2", {
        'requirements': Requirements.POS | Requirements.CAM,
        'angle': 14957,
        'cam': {
            'pos': (-92795.1328, -5302.87988, 22505.3359),
            'target': (-92098.1797, -5398.54883, 22599.9102)
        },
        'counter': 30
    })

    update_entry("corotd", {
        'requirements': Requirements.POS,
        'pos': (-13715.0712, 0.00, -14238.0654),
        'angle': 27714,
    })

    update_entry("lakebed_bk_skip", {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (71.9835968, 1500.00, 2839.01587),
        'angle': 32767,
        'cam': {
            'pos': (71.9835968, 1719.93542, 2969.04565),
            'target': (71.9835968, 1660.0, 2839.01587)
        },
        'counter': 30
    })

    update_entry("mdh_tower", {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (25254.6875, -3031.50854, 10222.1445),
        'angle': 32025,
        'cam': {
            'pos': (10193.6064, 25254.7852, -2874.2627),
            'target': (25256.7285, -2919.95215, 2839.01587)
        },
        'counter': 15
    })

    update_entry("poe_1_skip", {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (-2046.97168, 0.0, -587.304871),
        'angle': 49030,
        'cam': {
            'pos': (-1779.00293, 213.707397, -584.686768),
            'target': (-2047.97168, 130.16568, -587.317139)
        },
        'counter': 10
    })

    update_entry("spr_bk_lja", {
        'requirements': Requirements.POS,
        'pos': (-2171.19, 973.96, -2384.89),
        'angle': 32887,
    })

    update_entry("grove_skip", {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (-9966.6689, 2000.0, 4085.1082),
        'angle': 22306,
        'cam': {
            'pos': (-10415.2363, 2212.92139, 4370.72852),
            'target': (-9965.82617, 2176.59863, 4084.57056)
        },
        'counter': 30
    })

    update_entry("hv_archery", {
        'requirements': Requirements.POS,
        'pos': (3125.57, -62.16, -9360.22),
        'angle': 64520,
    })

    update_entry("cits_1", {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (1309.60645, -240.0, 5533.43848),
        'angle': 16384,
        'cam': {
            'pos': (1027.53259, -108.096123, 5605.23047),
            'target': (1313.54285, -234.203003, 5545.16846)
        },
        'counter': 10
    })

    update_entry("cats", {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (5238.59, 0.00, -3575.74),
        'angle': 17282,
        'cam': {
            'pos': (4893.25391, 160.117676, -3524.51245),
            'target': (5309.32373, 160.1, -3581.83423)
        },
        'counter': 30
    })

    update_entry('city_gate_clip', data = {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (16516.6094, 0, -12722.480),
        'angle': 16384
    })

    # update_entry('kitty_climb', data = {
    #     'requirements': Requirements.POS,
    #     'pos': (-3849.0, -188.0, 3117.0),
    #     'angle': 28409 
    # })

    update_entry('Speed rat (turn wall)', data = {
        'requirements': Requirements.POS,
        'pos': (4159, 0, -2905),
        'angle': 0
    })

    update_entry('Friendless', data = {
        'requirements': Requirements.POS,
        'pos': (-2232, 2600, 5857),
        'angle': 48805 
    })

    update_entry('Friendless', data = {
        'requirements': Requirements.POS,
        'pos': (-2232, 2600, 5857),
        'angle': 48805 
    })

    update_entry('Deku Like(ebf)', data = {
        'requirements': Requirements.POS,
        'pos': (-7151, 4080, 6159),
        'angle': 16384 
    })

    update_entry('dmt_poe', data = {
        'requirements': Requirements.POS,
        'pos': (-1221.2317, -1969.3409, 17314.1797),
        'angle': 34005 
    })

    update_entry('freezard_2', data = {
        'requirements': Requirements.POS,
        'pos': (1734.7701, 950.0000, 74.5665),
        'angle': 49419 
    })

    update_entry('snowboarding', data = {
        'requirements': Requirements.POS,
        'pos': (-11424.1289, 900.0000, -9670.6328),
        'angle': 49152 
    })

    update_entry('speedrat', data = {
        'requirements': Requirements.POS,
        'pos': (4150, 0, -2877),
        'angle': 0 
    })

    file = open("hundo.bin", "wb")

    for entry in hundo_p:
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
