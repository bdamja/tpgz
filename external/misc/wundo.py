#!/usr/bin/python3
"""
Generates the metadata file for the Wii 100% save files.
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
file_names = [
    "goats1",
    "ordongateclip",
    "goats2",
    "swordandshield",
    "farontwilight",
    "ems",
    "purplemist",
    "forestbit",
    "faronescape",
    "lanayrugateclip",
    "earlylakebedmidnadive",
    "jakeskip",
    "lakebeddisplacementclips",
    "dekutoad",
    # karg fight
    "kargflight",
    "foresttemple2",
    "diababa",
    # hfs postman skip
    "eldintwilight",
    # basement bugs
    # elde inn
    "bombhouseskip",
    # eldin steam cycle
    "posteldintwilight",
    "corotd",
    "earlyelevator",
    "goronmines",
    "keyshardskip",
    "dangoro",
    "fyrus",
    "zdbug",
    "waterfallsidehop",
    "ctbug",
    "dockbug",
    "plumm",
    "iza1skipsetup",
    "kb2skip",
    "wagonescort",
    "kb1skip",
    "premdhcleanup",
    "lakebedbkskip",
    "morpheel",
    "star1",
    "louiseglitch",
    "ropeskip",
    "mdhtower",
    # mdh bridge
    # post mdh
    "kb1",
    "gorgecleanup",
    "iza1skip",
    "lakehyliacave",
    "desert",
    "bulblincamp",
    "arbitersgrounds",
    "poe1skip",
    "poe4",
    "poe3",
    "agearlybk",
    "stalfosskip",
    "deathsword",
    "stallord",
    "stallord2",
    "postag",
    "outsidezdcleanup",
    "snowpeak",
    "graveyard",
    "snowpeakruins",
    "darkhammer",
    "sprsuperjump",
    "ladderfreezardcancel",
    "sprbkroom",
    "blizzeta",
    "faronjsmb",
    "grove2skip",
    "wreckagejsmb",
    "templeoftime",
    "totearlypoe",
    "totstatuethrows",
    "totearlyhp",
    "totbkroom",
    "totthirdstaircase",
    "totdarknut",
    "dotskip",
    "armagohma",
    "posttot",
    "yetarace",
    "renadosletter",
    "hotspringminigame",
    "southcastletown",
    "hyrulefieldcleanup",
    "flightbyfowl",
    "hugoarchery",
    "bellsilverrupee",
    "earlycity",
    "city1",
    "eastwing",
    "aeralfosskip",
    "city2",
    "annoyingroom",
    "peahatlja",
    "citybkclip",
    "fantower",
    "argorok",
    "argorok2",
    "caveofordeals",
    "coofloor10",
    "coofloor20",
    "coofloor30",
    "coofloor40",
    "postcoo",
    "boepostmanskip",
    "cats",
    "hfncleanup",
    "icecave",
    "northfieldgrotto",
    "iza2",
    "palaceeastwin",
    "phantomzant1",
    "postphantomzant1",
    "palacewestwing1",
    "palacewestwing2",
    "phantomzant2",
    "postphantomzant2",
    "doublesolroom",
    "potbkroom",
    "earlyplatform",
    "zant",
    "zantdangoro",
    "zantfinal",
    "star2",
    "hyrulecastle",
    "kb4",
    "darknutskip",
    "aeralfos",
    "finaltower",
    "beastganon",
    "horsebackganon"
]

wundo_p = [{**copy.deepcopy(default_entry), "id": i, "filename": name}
            for i, name in enumerate(file_names)]

file_dict = {}
for i, e in enumerate(file_names):
    if not e in file_dict:
        file_dict[e] = [i]
    else:
        file_dict[e].append(i)

def update_entry(filename, data, n = 1):
    count = sum(1 for entry in wundo_p if entry["filename"] == filename)
    if n <= count and n > 0:
        wundo_p[file_dict[filename][n - 1]] = {**wundo_p[file_dict[filename][n - 1]], **data}

# wii faron escape
update_entry("faronescape", data = {
    'requirements': Requirements.POS,
    'pos': (-13149.1650, 1.9844, -13106.8066),
    'angle': 16779,
    'counter': 10,
})

# lanayru gate clip
update_entry("lanayrugateclip", data = {
    'requirements': Requirements.POS,
    'pos': (-61951.3516, -9147.2793, 72637.9219),
    'angle': 41765,
    'counter': 10,
})

# coro text displacement
update_entry("corotd", data = {
    'requirements': Requirements.POS,
    'pos': (-13715.0713, 0, -14238.0654),
    'angle': 27714,
    'counter': 10,
})

# inner zd bug
update_entry("zdbug", {
    'requirements': Requirements.POS,
    'pos': (0, -8.27449322, -2750),
    'angle': 32768,
    'counter': 30
})

# castle town bug
update_entry("ctbug", data = {
    'requirements': Requirements.POS,
    'pos': (1003.9477, -200.0000, 6493.8564),
    'angle': 17793,
    'counter': 10,
})

# kb1 trigger skip in escort
update_entry("kb1skip", data = {
    'requirements': Requirements.POS,
    'pos': (4437.2925, -5765.1309, 52674.6719),
    'angle': 19735,
    'counter': 10,
})

# louise glitch
update_entry("louiseglitch", data = {
    'requirements': Requirements.POS,
    'pos': (2938.2393, -1150.0000, 4472.1841),
    'angle': 40960,
    'counter': 10,
})

update_entry("poe1skip", data = {
    'requirements': Requirements.POS,
    'pos': (-2146.1931, 0.0000, -609.7213),
    'angle': 49244,
    'counter': 10,
})

update_entry("poe4", data = {
    'requirements': Requirements.POS,
    'pos': (-6690.0000, 1050, 3993.3274),
    'angle': 16376,
    'counter': 10,
})

update_entry("poe3", data = {
    'requirements': Requirements.POS,
    'pos': (5574.4053, 1050, 560),
    'angle': 65530,
    'counter': 10,
})

update_entry("stalfosskip", data = {
    'requirements': Requirements.POS,
    'pos': (-4984, -1700, -2919.1047),
    'angle': 16384,
    'counter': 10,
})

update_entry("ladderfreezardcancel", data = {
    'requirements': Requirements.POS,
    'pos': (-2645.6860, 0, -4315.6831),
    'angle': 33554,
    'counter': 10,
})

update_entry("grove2skip", data = {
    'requirements': Requirements.POS,
    'pos': (-9957.9814, 2000, 3963.5327),
    'angle': 17515,
    'counter': 10,
})

# early tot broken stairs
update_entry("wreckagejsmb", data = {
    'requirements': Requirements.POS,
    'pos': (-297.3111, 1000, 5052.4692),
    'angle': 5942,
    'counter': 10,
})

update_entry("totearlyhp", data = {
    'requirements': Requirements.POS,
    'pos': (-6604.4204, 5050, -6780.6040),
    'angle': 0,
    'counter': 10,
})

update_entry("totbkroom", data = {
    'requirements': Requirements.POS,
    'pos': (2715, 7400, -7),
    'angle': 16384,
    'counter': 10,
})

update_entry("totthirdstaircase", data = {
    'requirements': Requirements.POS,
    'pos': (62.8, 6950, 3410),
    'angle': 0,
    'counter': 10,
})

update_entry("yetarace", data = {
    'requirements': Requirements.POS,
    'pos': (-71867.4766, -54450, 56622.8203),
    'angle': 45232,
    'counter': 10,
})

update_entry("earlycity", data = { 
    'requirements': Requirements.POS,
    'pos': (-4.2379, -770, -2968.9827),
    'angle': 57035,
    'counter': 10,
})

# big baba ascent cits
update_entry("annoyingroom", data = {
    'requirements': Requirements.POS,
    'pos': (-14000, 0, -15965.9912),
    'angle': 32768,
    'counter': 10,
})

# cits peahat poe cycle with hp
update_entry("peahatlja", data = {
    'requirements': Requirements.POS,
    'pos': (-14009.4453, 3000.4910, -16134.0078),
    'angle': 0,
    'counter': 10,
})

update_entry("citybkclip", data = {
    'requirements': Requirements.POS,
    'pos': (-7.2611, 3000, -11317.8408),
    'angle': 32698,
    'counter': 10,
})

update_entry("boepostmanskip", data = {
    'requirements': Requirements.POS,
    'pos': (34800, -299, -26735),
    'angle': 32768,
    'counter': 10,
})

update_entry("palacewestwing2", data = {
    'requirements': Requirements.POS,
    'pos': (3999.17676, -725, 249.467438),
    'angle': 32768,
    'counter': 10,
})

update_entry("kb4", data = {
    'requirements': Requirements.POS,
    'pos': (-8296.9180, 62, -5183.4233),
    'angle': 23289,
    'counter': 10,
})

file = open("wundo.bin", "wb")

for entry in wundo_p:
    print(entry)
    file.write(entry["requirements"].to_bytes(1, "big", signed=False))
    file.write(int(0).to_bytes(1, "big", signed=False)) # padding
    file.write(entry["angle"].to_bytes(2, "big", signed=False))
    file.write(struct.pack('>fff', *entry["pos"]))
    file.write(struct.pack('>fff', *entry["cam"]["pos"]))
    file.write(struct.pack('>fff', *entry["cam"]["target"]))
    file.write(entry["counter"].to_bytes(4, "big", signed=False))
    file.write(struct.pack(">32s", entry["filename"].encode("ascii")))
    file.write(int(0).to_bytes(4, "big", signed=False)) # padding