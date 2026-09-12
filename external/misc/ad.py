#!/usr/bin/python3
"""
Generates the metadata file for the all dungeons save files.
"""
import copy
from enum import IntEnum
import struct

class Requirements(IntEnum):
    POS = 1
    CAM = 2

default_entry = {
    "requirements": 0,
    "pos": (0.0, 0.0, 0.0),
    "angle": 0,
    "cam": {"pos": (0, 0, 0), "target": (0, 0, 0)},
    "counter": 0,
}

# order matters
# must be the .bin filenames
file_names = [
    "ordon_gate_clip", 
    "ordon_gate_clip", 
    "goats", 
    "hugo", 
    "faron_twilight", 
    "coro_bugs", 
    "mist_1",
    "ems", 
    "purple_mist", 
    "kb1",
    "kak_dc",
    "eldin_twilight", 
    "forest",
    "forest_2",
    "diababa", 
    "pillar_clip", 
    "lakebed1",
    "lakebed_main",
    "edt_double_lja",
    "edt_dc",
    "deku_toad",     
    "lanayru_twilight", 
    "mountain_umd", 
    "spr",
    "darkhammer",
    "spr_2",
    "lfc",
    "spr_bk_room",
    "blizzeta",
    "rusl_td",
    "early_elevator",
    "elevator_escape",
    "gm",
    "kitty_climb",
    "clawshot_switch",
    "dangoro", 
    "gm_2",
    "water_lja",
    "fyrus",
    "bk_skip", 
    "morpheel", 
    "mdh", 
    "camp",
    "ag", 
    "poe_gate_clip",
    "ag_early_bk",
    "stalfos_skip",
    "deathsword", 
    "ag_2",
    "stallord", 
    "faron_boost",
    "lost_woods_2",
    "sacred_grove",
    "tot",
    "first_staircase",
    "turning_platform",
    "statue_throws",
    "second_staircase",
    "tot_bk",
    "third_staircase",
    "tot_darknut",
    "dot_skip", 
    "silver_rupee", 
    "city1", 
    "city_gate_clip",
    "aeralfos", 
    "city2",
    "kai_clip",
    "fan_tower",
    "argorok", 
    "palace1", 
    "palace2", 
    "zant", 
    "hc", 
    "beast_ganon", 
    "horseback", 
]

ad_p = [{**copy.deepcopy(default_entry), "id": i, "filename": name}
            for i, name in enumerate(file_names)]

file_dict = {}
for i, e in enumerate(file_names):
    if not e in file_dict:
        file_dict[e] = [i]
    else:
        file_dict[e].append(i)

def update_entry(filename, data, n = 1):
    count = sum(1 for entry in ad_p if entry["filename"] == filename)
    if n <= count and n > 0:
        ad_p[file_dict[filename][n - 1]] = {**ad_p[file_dict[filename][n - 1]], **data}

# ordon gate clip
# for each of these, the angle is unsigned. putting a negative for the angle will crash when loading the saves and all saves after
# the camera stuff seems to be dysfunctional
update_entry("ordon_gate_clip", n = 1, data = {
    'requirements': Requirements.POS | Requirements.CAM,
    'pos': (827.450012, 216.490097, -4533.90625),
    'angle': 498,
    'cam': {
        'pos': (833.467468, 477.604675, -4241.97266),
        'target': (827.497559, 329.622986, -4532.90723)
    },
    'counter': 10
})

update_entry("ordon_gate_clip", n = 2, data = {
    'requirements': Requirements.POS | Requirements.CAM,
    'pos': (466.622467, 319.770752, -11651.3867),
    'angle': 52540,
    'cam': {
        'pos': (735.525391, 524.418701, -11576.4746),
        'target': (465.674622, 421.052704, -11651.0684)
    },
    'counter': 10
})

update_entry("hugo", {
    'requirements': Requirements.POS | Requirements.CAM,
    'pos': (701.797302, 85.5212784, -5299.6123),
    'angle': 63622,
    'cam': {
        'pos': (735.525391, 524.418701, -11576.4746),
        'target': (465.674622, 421.052704, -11651.0684)
    },
})

update_entry("purple_mist", {
    'requirements': Requirements.POS,
    'pos': (-23524.6152, 250.0, -16220.166),
    'angle': 40758,
    'counter': 30
})

update_entry("eldin_twilight", {
    'requirements': Requirements.POS | Requirements.CAM,
    'pos': (455.088379, -150.0, 11516.7227),
    'angle': 6058,
    'cam': {
        'pos': (219.367218, -20.1253014, 11157.582),
        'target': (482.515137, -39.9999771, 11558.5283)
    },
    'counter': 10
})

update_entry("rusl_td", {
    'requirements': Requirements.POS | Requirements.CAM,
    'pos': (-37785.152, 597.8449, -21831.369),
    'angle': 36422,
    'cam': {
        'pos': (-37785.152, 597.8449, -21831.369),
        'target': (-37785.152, 597.8449, -21831.369)
    },
    'counter': 10
})

update_entry("early_elevator", {
    'requirements': Requirements.POS | Requirements.CAM,
    'pos': (1130, -355.6, -5569),
    'angle': 43917,
    'cam': {
        'pos': (1130, -355.6, -5569),
        'target': (1130, -355.6, -5569)
    },
    'counter': 10
})

update_entry("bk_skip", {
    'requirements': Requirements.POS | Requirements.CAM,
    'pos': (71.9835968, 1500.00, 2839.01587),
    'angle': 32767,
    'cam': {
        'pos': (71.9835968, 1719.93542, 2969.04565),
        'target': (71.9835968, 1660.0, 2839.01587)
    },
    'counter': 30
})

update_entry("morpheel", {
    'requirements': Requirements.POS | Requirements.CAM,
    'pos': (-1193.0, -23999.00, -770.0),
    'angle': 10754
})

update_entry('poe_gate_clip', data = {
    'requirements': Requirements.POS | Requirements.CAM,
    'pos': (10.0035, -19.5500, -600.5942),
    'angle': 32768
})

update_entry('city_gate_clip', data = {
    'requirements': Requirements.POS | Requirements.CAM,
    'pos': (16516.6094, 0, -12722.480),
    'angle': 16384
})

update_entry('lakebed_main', data = {
    'requirements': Requirements.POS,
    'pos': (71.9836, 1500.00, 2839.01587),
    'angle': 32767
})

update_entry('edt_double_lja', data = {
    'requirements': Requirements.POS,
    'pos': (7298.4106, -50.0000, 4.0667),
    'angle': 16384
})

update_entry('lfc', data = {
    'requirements': Requirements.POS,
    'pos': (-2640.6411, 0.0000, -4806.1328),
    'angle': 36572
})

update_entry('spr_bk_room', data = {
    'requirements': Requirements.POS,
    'pos': (-3015.9932, 950.0000, -5443.8247),
    'angle': 48605
})

update_entry('early_elevator', data = {
    'requirements': Requirements.POS,
    'pos': (1119.9015, -355.6001, -5571.2036),
    'angle': 45717
})

update_entry('kitty_climb', data = {
    'requirements': Requirements.POS,
    'pos': (-1111.4636, -200.0000, 5438.0581),
    'angle': 49241
})

update_entry('stalfos_skip', data = {
    'requirements': Requirements.POS,
    'pos': (-731.9014, -2250.0000, -2682.4460),
    'angle': 16098
})

update_entry('tot_bk', data = {
    'requirements': Requirements.POS,
    'pos': (2996.9797, 7401.5000, -0.3486),
    'angle': 16374
})

update_entry('kai_clip', data = {
    'requirements': Requirements.POS,
    'pos': (1097.8264, 1312.7100, -11830.8057),
    'angle': 50124
})

update_entry('third_staircase', data = {
    'requirements': Requirements.POS,
    'pos': (76.6775818, 6950.0, 3465.99341),
    'angle': 64834
})

update_entry('turning_platform', data = {
    'requirements': Requirements.POS,
    'pos': (1620.3672, 4250.0000, -60.7700),
    'angle': 60379
})

file = open("ad.bin", "wb")

for entry in ad_p:
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
