import copy
import sys
import argparse
import struct
from enum import IntEnum, unique

@unique
class Platform(IntEnum):
    GCN = 0
    WII = 1


class Requirements(IntEnum):
    POS = 1
    CAM = 2

def main(args=None):
    parser = argparse.ArgumentParser(
        sys.argv[0], description="A tool to generate the metadata file for the any% BiTE save files.")
    parser.add_argument(
        "-p", "--platform", type=str.upper, choices=[e.name for e in Platform], default=Platform.GCN.name, help="The platform to generate for.")
    args = parser.parse_args()

    args.platform = Platform[args.platform]

    default_entry = {
        "requirements": 0,
        "pos": (0.0,0.0,0.0),
        "angle": 0,
        "cam": {"pos":(0,0,0), "target": (0,0,0)},
        "counter": 0,
    }

    # order matters
    file_names = [
        "ordon_gate_clip",
        "ordon_gate_clip",
        "goats",
        "hugo",
        "faron_twilight",
        "ems",
        "purple_mist",
        "forest_bit",
        "forest_escape",
        "lanayru_gate_clip",
        "pillar_clip",
        "lakebed_1",
        "deku_toad",
        "karg",
        "kb1",
        "eldin_twilight",
        "lanayru_twilight",
        "waterfall_sidehop",
        "iza",
        "spr_warp",
        "spr",
        "darkhammer",
        "lakebed_bk_skip",
        "onebomb",
        "mdh_tower",
        "mdh_bridge",
        "camp",
        "ag",
        "poe_1_skip",
        "death_sword_skip",
        "stallord",
        "stallord",
        "silver_rupee",
        "cits_early",
        "cits_1",
        "aeralfos_skip",
        "fan_tower",
        "argorok",
        "palace_1",
        "palace_2",
        "early_platform",
        "zant",
        "hc",
        "hc_tower",
        "beast_ganon",
        "horseback_ganon",
    ]

    if args.platform is Platform.WII:
        # order matters
        file_names = [
            "ordon_gate_clip",
            "ordon_gate_clip",
            "faron_gate_clip_1",
            "seam_clip",
            "oob_to_gorge",
            "faron_gate_clip_2",
            "goats",
            "sewers",
            "sewers_tower",
            "sewers_rooftops",
            "hugo",
            "faron_twilight",
            "ems",
            "purple_mist",
            "bite",
            "kb1",
            "rebite",
            "forest_temple",
            "eldin_twilight",
            "basement_bugs",
            "eld_inn",
            "bombhouse_skip",
            "eldin_steam_cycle",
            "epona_oob_to_flight_by_fowl",
            "quaforce_clip",
            "kargarok_fight",
            "kargarok_flight",
            "lanayru_twilight",
            "inner_zd_bug",
            "waterfall_sidehop",
            "ct_bug",
            "dock_bug",
            "boss_bug",
            "iza",
            "plumm_cs_skip",
            "plumm_oob",
            "enter_lakebed",
            "lakebed_1",
            "pot_push",
            "pot_push",
            "deku_toad",
            "lakebed_bk_skip",
            "morpheel",
            "louise_glitch",
            "rope_skip",
            "mdh_tower",
            "mdh_bridge",
            "post_mdh",
            "snowpeak_cave",
            "messenger_skip",
            "blind_snowboarding",
            "snowpeak_ruins",
            "snowpeak_ruins_mbbb",
            "spr_spinner_boost",
            "freezard_skip",
            "dark_hammer",
            "desert_fence_clip",
            "bulblin_camp",
            "ag",
            "poe_gate_skip",
            "pgs_ebmb",
            "early_boss_key",
            "triple_stalfos_skip",
            "death_sword",
            "epic_spinner",
            "stallord",
            "stallord",
            "mirror_chamber",
            "early_city",
            "cits",
            "arg_cs_skip",
            "cits_west_inside",
            "aeralfos_skip",
            "cits_2",
            "cits_bk_clip",
            "fanless",
            "fan_tower",
            "argorok",
            "pot1",
            "sol1_backtrack",
            "stupidroom",
            "smart_room",
            "sol2_backtrack",
            "pot2",
            "pot_bk",
            "earlypf",
            "zant",
            "zant_dangoro",
            "zant_final",
            "ct_mailman_skip",
            "hc",
            "kb4",
            "darknut",
            "hc_aeralfos",
            "towerclimb",
            "beast_ganon",
            "horseback",
        ]

    anyb_p = [{**copy.deepcopy(default_entry), "id": i, "filename": file_names[i]} for i in range(len(file_names))]

    file_dict = {}
    for i, e in enumerate(file_names):
        if not e in file_dict:
            file_dict[e] = [i]
        else:
            file_dict[e].append(i)

    def update_entry(filename, data, n = 1):
        count = sum(1 for entry in anyb_p if entry["filename"] == filename)
        if n <= count and n > 0:
            anyb_p[file_dict[filename][n - 1]] = {**anyb_p[file_dict[filename][n - 1]], **data}

    # ordon gate clip
    update_entry("ordon_gate_clip", n = 1, data = {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (827.450012, 216.490097, -4533.90625),
        'angle': 498,
        'cam': {'pos': (833.467468, 477.604675, -4241.97266), 'target': (827.497559, 329.622986, -4532.90723)},
        'counter': 10,
    })

    # back in time
    update_entry("ordon_gate_clip", n = 2, data = {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (466.622467, 319.770752, -11651.3867),
        'angle': 52540,
        'cam': {'pos': (735.525391, 524.418701, -11576.4746), 'target': (465.674622, 421.052704, -11651.0684)},
        'counter': 10,
    })

    # seam clip
    update_entry("seam_clip", data = {
        'requirements': Requirements.POS,
        'pos': (-45726.7188, -7515.41748, 97416.9766),
        'angle': 52884,
        'counter': 10,
    })

    # hugo
    update_entry("hugo", data = {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (701.797302, 85.5212784, -5299.6123),
        'angle': 63622,
        'cam': {'pos': (735.525391, 524.418701, -11576.4746), 'target': (465.674622, 421.052704, -11651.0684)},
    })

    # purple mist
    update_entry("purple_mist", data = {
        'requirements': Requirements.POS,
        'pos': (-23524.6152, 250.0, -16220.166),
        'angle': 40758,
        'counter': 30,
    })

    # king bulblin 1
    if args.platform is Platform.WII:
        update_entry("kb1", data = {
            'requirements': Requirements.POS,
            'pos': (-9717.6035, 337.0316, 97.9661),
            'angle': 16384,
            'counter': 30,
        })

    # boss bug
    if args.platform is Platform.WII:
        update_entry("boss_bug", data = {
            'requirements': Requirements.POS,
            'pos': (-87517.1562, -18789.2812, 38927.0820),
            'angle': 41851,
            'counter': 30,
        })

    # plumm oob
    if args.platform is Platform.WII:
        update_entry("plumm_oob", data = {
            'requirements': Requirements.POS,
            'pos': (-104271.3750, -18470.0, 52661.7812),
            'angle': 45103,
            'counter': 30,
        })

    # mdh tower
    if args.platform is Platform.WII:
        update_entry("mdh_tower", data = {
            'requirements': Requirements.POS | Requirements.CAM,
            'pos': (25362.3184, -3028.7673, 10060.8379),
            'angle': 29327,
            'counter': 30,
        })

    # freezard skip
    if args.platform is Platform.WII:
        update_entry("freezard_skip", data = {
            'requirements': Requirements.POS | Requirements.CAM,
            'pos': (-125.9265, 33.8123, -3688.0295),
            'angle': 32768,
            'counter': 30,
        })

    # dark hammer
    if args.platform is Platform.WII:
        update_entry("dark_hammer", data = {
            'requirements': Requirements.POS | Requirements.CAM,
            'pos': (0.7448, 0.0, 1330.9711),
            'angle': 32768,
            'counter': 20,
        })

    # forest escape
    update_entry("forest_escape", data = {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (-12433.6016, -235.969193, -17103.998),
        'angle': 29553,
        'cam': {'pos': (-12552.8252, -53.5801048, -16729.5313), 'target': (-12433.2979, -106.667023, -17104.9512)},
        'counter': 30,
    })

    # lanayru gate clip
    update_entry("lanayru_gate_clip", data = {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (-63026.2852, -9065.92578, 71680.3438),
        'angle': 44248,
        'cam': {'pos': (-62655.8125, -8900.91309, 71903.6328), 'target': (-63064.2148, -8969.97656, 71661.0781)},
        'counter': 15,
    })

    # eldin twilight
    update_entry("eldin_twilight", data = {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (455.088379, -150.0, 11516.7227),
        'angle': 6058,
        'cam': {'pos': (219.367218, -20.1253014, 11157.582), 'target': (482.515137, -39.9999771, 11558.5283)},
        'counter': 10,
    })

    # epona oob to lanayru
    update_entry("epona_oob_to_flight_by_fowl", data = {
        'requirements': Requirements.POS,
        'pos': (16501.3535, 3304.0415, 34706.0977),
        'angle': 61639,
        'counter': 10,
    })

    # iza
    update_entry("iza", data = {
        'requirements': Requirements.POS,
        'pos': (5979.97217, 150.0, -2748.34155),
        'angle': 10114,
    })

    # snowpeak messenger skip
    update_entry("messenger_skip", data = {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (-9294.87988, 980.0, -11712.3838),
        'angle': 346,
        'cam': {'pos': (-9309.65137, 1280.4469, -12130.7695), 'target': (-9294.2207, 1180.0, -11692.3945)},
        'counter': 10,
    })

    # spr
    update_entry("spr", data = {
        'requirements': Requirements.POS,
        'pos': (0.0, 150.0, 6000.0),
        'angle': 33768,
    })

    # morpheel
    update_entry('onebomb', data = {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (-1193.0, -23999.00, -770.0),
        'angle': 10754,
        'counter': 20,
    })

    # louise glitch
    update_entry("louise_glitch", {
        'requirements': Requirements.POS,
        'pos': (2861.78076, -1150, 4507.41846),
        'angle': 32750,
    })

    # rope skip
    # this spawns outside of telma's bar, because the save being in telma's bar will always set it to the wrong layer (4) for some reason
    update_entry("rope_skip", {
        'requirements': Requirements.POS,
        'pos': (3159.06836, -500, 5492.82129),
        'angle': 33276,
    })

    # poe gate skip
    update_entry('poe_gate_skip', data = {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (0, -19.55, -600),
        'angle': 32768
    })

    # poe gate skip ending blow moon boots
    update_entry('pgs_ebmb', data = {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (-749.9980, 50.0000, -3265.0000),
        'angle': 16384,
        'cam': {
            'pos': (-549.9980, 200.0000, -3265.0000), 
            'target': (-749.9980, 50.0000, -3265.0000)
        },
        'counter': 10,
    })

    # elh bomb boost
    update_entry('enter_lakebed', data = {
        'requirements': Requirements.POS,
        'pos': (-87645.3203, -21052.0078, 38436.0898),
        'angle': 45767,
        'counter': 10,
    })

    # pot push
    update_entry('pot_push', data = {
        'requirements': Requirements.POS,
        'pos': (7296.9878, -50.0000, -0.6072),
        'angle': 16374,
        'counter': 20,
    })

    # lakebed bk skip
    update_entry('lakebed_bk_skip', data = {
        'requirements': Requirements.POS,
        'pos': (63.3586, 1500.0000, 3139.0151),
        'angle': 32727,
        'counter': 10,
    })

    # light sword
    update_entry('pot2', data = {
        'requirements': Requirements.POS,
        'pos': (250.0000, -200.0000, 11000.0000),
        'angle': 0,
        'counter': 10,
    }) 

    # kb4
    update_entry('kb4', data = {
        'requirements': Requirements.POS,
        'pos': (-8593.0000, 52.0000, -4873.0000),
        'angle': 24354,
        'counter': 20,
    })

    # city 1
    update_entry("cits", {
        'requirements': Requirements.POS,
        'pos': (1309.60645, -240.0, 5533.43848),
        'angle': 16384,
        'counter': 10
    })

    # epic spinner
    update_entry("epic_spinner", {
        'requirements': Requirements.POS,
        'pos': (-4815.0, -1700.0, -2848.0),
        'angle': 49152,
        'counter': 10
    })           

    # triple stalfos skip
    update_entry("triple_stalfos_skip", {
        'requirements': Requirements.POS,
        'pos': (-4603.0, -1700.0, -2895.0),
        'angle': 16119,
        'counter': 10
    }) 

    # kargarok rider fight
    update_entry("kargarok_fight", data = {
        'requirements': Requirements.POS,
        'pos': (-107158.469, -23433.293, 46868.5273),
        'angle': 64976,
        'counter': 30
    })

    # sewers tower
    update_entry("sewers_tower", {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (25524, -3010, 8087),
        'angle': 32737,
        'cam': {
            'pos': (25771.3672, -2753.22388, 7785.64941),
            'target': (25535.5352, -2890, 8078.35254)
        },
        'counter': 30
    })

    # sewers rooftops
    update_entry("rooftops", {
        'requirements': Requirements.POS,
        'pos': (27441, 2930, 6796),
        'angle': 32465,
        'counter': 30
    })

    # eldin steam cycle
    update_entry("eldin_steam_cycle", {
        'requirements': Requirements.POS,
        'pos': (411.544403, 18.8815422, 9147.74805),
        'angle': 33423,
        'counter': 10
    })

    # inner zd bug
    update_entry("inner_zd_bug", {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (0, -8.27449322, -2750),
        'angle': 32768,
        'cam': {
            'pos': (-280.019684, 76.9521179, -2899.97949),
            'target': (8.7422813, 86.7255249, -2740)
        },
        'counter': 30
    })

    # ct bug
    update_entry("ct_bug", {
        'requirements': Requirements.POS,
        'pos': (2185.91479, -725, 6443.65088),
        'angle': 19198,
    })

    # plumm cs skip
    update_entry("plumm_cs_skip", {
        'requirements': Requirements.POS,
        'pos': (-101516.211, -18470, 53531.9336),
        'angle': 57707,
    })

    # blind snowboarding
    update_entry("blind_snowboarding", {
        'requirements': Requirements.POS,
        'pos': (-14476.7305, 1814.04504, -9606.24609),
        'angle': 36106,
    })

    # desert fence clip
    update_entry("desert_fence_clip", {
        'requirements': Requirements.POS,
        'pos': (3885.38916, -732.859985, 18491.7715),
        'angle': 40266,
    })

    # mirror chamber portal
    update_entry('mirror_chamber', {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (5336.63672, 4392.44238, -20123.7754),
        'angle': 54828,
        'cam': {
            'pos': (5772.17188, 4685.60254, -20415.6738),
            'target': (5344.75195, 4542.44629, -20157.0879)
        },
        'counter': 10
    })

    # pot right wing inside 2
    update_entry('smart_room', data = {
        'requirements': Requirements.POS | Requirements.CAM,
        'pos': (3999.17676, -725, 249.467438),
        'angle': 32768,
        'cam': {
            'pos': (4036.18408, -505, 378.042297),
            'target': (4026.32227, -565, 248.41687)
        },
        'counter': 30
    })

    # pot sol 1 backtrack
    update_entry("sol1_backtrack", {
        'requirements': Requirements.POS,
        'pos': (0, 0, 300),
        'angle': 41971,
    })

    # pot sol 2 backtrack
    update_entry("sol2_backtrack", {
        'requirements': Requirements.POS,
        'pos': (0, 0, 300),
        'angle': 41971,
    })

    # mailman skip outside of castle town
    update_entry("ct_mailman_skip", {
        'requirements': Requirements.POS,
        'pos': (-70000, -1400, 10662),
        'angle': 16384,
    })

    file = open("any.bin", "wb")

    for entry in anyb_p:
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

if __name__ == "__main__":
    main()