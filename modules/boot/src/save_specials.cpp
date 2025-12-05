#include "save_specials.h"
#include "gz_flags.h"
#include "libtp_c/include/utils.h"
#include "libtp_c/include/d/com/d_com_inf_game.h"
#include "libtp_c/include/f_op/f_op_actor_mng.h"
#include "libtp_c/include/f_op/f_op_actor_iter.h"
#include "libtp_c/include/rel/d/a/b/d_a_b_ds.h"
#include "libtp_c/include/rel/d/a/obj/d_a_obj_lv4sand.h"
#include "libtp_c/include/d/d_procname.h"
#include "rels/include/defines.h"
#include "settings.h"

typedef bool (*predicate_t)(fopAc_ac_c&);

fopAc_ac_c* find_actor(predicate_t const& predicate) {
    if (predicate == nullptr) {
        return nullptr;
    }
    node_class* node = g_fopAcTg_Queue.mpHead;
    fopAc_ac_c* actorData = NULL;
    for (int i = 0; i < g_fopAcTg_Queue.mSize; i++) {
        if (node != NULL) {
            create_tag_class* tag = (create_tag_class*)node;
            fopAc_ac_c* tmpData = (fopAc_ac_c*)tag->mpTagData;
            if (predicate(*tmpData)) {
                actorData = tmpData;
                break;
            }
            node = node->mpNextNode;
        }
    }
    return actorData;
}

#if defined(WII_NTSCU_10) || defined(WII_PAL)
#define ROCK_ID 763
#else
#define ROCK_ID 765
#endif

KEEP_FUNC void SaveMngSpecial_OrdonRock() {
    gSaveManager.setSaveAngle(32768);
    gSaveManager.setSavePosition(400.0f, 307.5f, -11270.2f);
    gSaveManager.setLinkInfo();

    cXyz position(400.0f, 307.8f, -11365.f);

    fopAc_ac_c* actorData = find_actor([](fopAc_ac_c& act) {
        return act.mBase.mProcName == ROCK_ID && act.mBase.mParameters == 0x00FF6511;
    });

    if (actorData != NULL) {
        actorData->current.pos = position;
        actorData->shape_angle.y = 5880;
    }
}

KEEP_FUNC void SaveMngSpecial_BossFlags() {
    gSaveManager.injectDefault_during();
    bossFlags = 0xFF;
}

KEEP_FUNC void SaveMngSpecial_Goats1() {
    gSaveManager.injectDefault_during();
    setNextStageLayer(5);
}

KEEP_FUNC void SaveMngSpecial_Hugo() {
    gSaveManager.injectDefault_during();
    dComIfGs_onSwitch(47, 0);   // midna trigger off
    dComIfGs_offSwitch(63, 0);  // hugo alive
}

#if defined(WII_NTSCU_10) || defined(WII_PAL)
#define HUGO_ACTOR_ID 466
#else
#define HUGO_ACTOR_ID 468
#endif

KEEP_FUNC void SaveMngSpecial_SpawnHugo() {
    gSaveManager.setSaveAngle(40166);
    gSaveManager.setSavePosition(2.9385, 396.9580, -18150.087);
    gSaveManager.setLinkInfo();

    cXyz position(-289.9785, 401.5400, -18533.078);

    // Find hugo in the actor list
    fopAc_ac_c* actorData =
        find_actor([](auto& act) { return act.mBase.mProcName == HUGO_ACTOR_ID; });

    if (actorData != NULL) {
        actorData->current.pos = position;
        actorData->shape_angle.y = 5880;
    }
}

KEEP_FUNC void SaveMngSpecial_PurpleMist() {
    gSaveManager.injectDefault_during();
    dComIfGs_setTransformStatus(STATUS_HUMAN);
}

KEEP_FUNC void SaveMngSpecial_KargOoB() {
    gSaveManager.mPracticeFileOpts.inject_options_before_load = nullptr;
    gSaveManager.injectDefault_during();
    g_dComIfG_gameInfo.info.mRestart.mLastMode = 0xA;  // spawn on kargorok
    dComIfGs_setTransformStatus(STATUS_HUMAN);
}

KEEP_FUNC void SaveMngSpecial_WaterfallSidehop() {
    gSaveManager.injectDefault_during();
    g_dComIfG_gameInfo.info.mRestart.mLastSpeedF = 10.0f;  // link spawns swimming forward
}

KEEP_FUNC void SaveMngSpecial_KB2Skip() {
    gSaveManager.injectDefault_during();
    setNextStageLayer(3);
}

KEEP_FUNC void SaveMngSpecial_Escort() {
    gSaveManager.injectDefault_during();
    setNextStageRoom(0xD);
    setNextStagePoint(98);
    setNextStageLayer(2);
}

KEEP_FUNC void SaveMngSpecial_EscortKeys() {
    dComIfGs_setKeyNum(2);  // give 2 keys for field gates
}

KEEP_FUNC void SaveMngSpecial_Dangoro() {
    g_dComIfG_gameInfo.info.mZone[0].mBit.mSwitch[0] |= 0x200000;  // turn off intro cs, start fight
}

KEEP_FUNC void SaveMngSpecial_Norgor() {
    g_meter2_info.mRentalBombBag = 0;  // Rental Bomb Bag Idx set to bag 0
    dComIfGs_setItem(SLOT_15, NORMAL_BOMB);
    dComIfGs_setBombNum(0, 30);
    dComIfGs_setSelectItemIndex(SELECT_ITEM_Y, SLOT_15);
}

KEEP_FUNC void SaveMngSpecial_LakebedBKSkip() {
    gSaveManager.injectDefault_during();
    dComIfGs_onSwitch(2, 0);    // bridge turned
    dComIfGs_onSwitch(122, 0);  // dungeon intro cs off
}

KEEP_FUNC void SaveMngSpecial_Darkhammer() {
    dComIfGs_onEventBit(0x0B02);
    dComIfGs_onEventBit(0x0B04);  // iza bomb bag stolen
}

KEEP_FUNC void SaveMngSpecial_Morpheel() {
    dComIfGp_getPlayer()->mEquipItem = HOOKSHOT;                        // clawshot
    dComIfGp_getPlayer()->onNoResetFlg0(daPy_py_c::EQUIP_HEAVY_BOOTS);  // ib
    gSaveManager.setSaveAngle(10754);
    gSaveManager.setSavePosition(-1193.0f, -23999.0f, -770.0f);
    gSaveManager.setLinkInfo();
}

KEEP_FUNC void SaveMngSpecial_Iza1Skip() {
    gSaveManager.injectDefault_during();
    g_dComIfG_gameInfo.info.mRestart.mLastMode = 0xA;  // spawn on kargorok
    setNextStageName("F_SP112");                       // set stage to river
    setNextStageRoom(1);
    setNextStagePoint(0);
    setNextStageLayer(4);
}

KEEP_FUNC void SaveMngSpecial_AnyPlummOoB() {
    gSaveManager.injectDefault_during();
    g_dComIfG_gameInfo.info.mRestart.mLastMode = 0xA;  // spawn on kargorok
    setNextStageName("F_SP112");                       // set stage to river
    setNextStageRoom(1);
    setNextStagePoint(0);
    setNextStageLayer(4);
    bossFlags = 0xFF;
}

KEEP_FUNC void SaveMngSpecial_Stallord() {
    gSaveManager.injectDefault_during();
    g_dComIfG_gameInfo.info.mZone[0].mBit.mSwitch[0] |= 0x300000;  // turn off intro cs, start fight
    setNextStagePoint(1);                                          // spawn at in front of stally
}

KEEP_FUNC void SaveMngSpecial_Stallord2() {
    gSaveManager.mPracticeFileOpts.inject_options_after_counter = 20;

    daB_DS_c* stallord = (daB_DS_c*)fopAcM_SearchByName(PROC_B_DS);
    // create the phase 2 version of stallord
    fopAcM_create(PROC_B_DS, fopAcM_GetParam(stallord) | 2, &stallord->current.pos,
                  fopAcM_GetRoomNo(stallord), nullptr, nullptr, -1);
    fopAcM_delete(stallord);  // delete phase 1 stallord

    daObjLv4Wall_c* rwall = (daObjLv4Wall_c*)fopAcM_SearchByName(PROC_Obj_Lv4RailWall);
    daObjSwSpinner_c* spinnersw = (daObjSwSpinner_c*)fopAcM_SearchByName(PROC_Obj_SwSpinner);

    spinnersw->mRotSpeedY = 3000;  // set arena spinner switch to max speed
    rwall->field_0x954 = 101;  // set spinner switch speed counter to threshold
    rwall->mHeight = 3370.0f;  // set arena height to max
}

KEEP_FUNC void SaveMngSpecial_Stallord2_init() {
    gSaveManager.repeat_during = true;
    gSaveManager.repeat_count = 120;

    gSaveManager.injectDefault_during();
    g_dComIfG_gameInfo.info.mZone[0].mBit.mSwitch[0] |= 0x300000;  // turn off intro cs, start fight
    setNextStagePoint(1);                                          // spawn at in front of stally
}

KEEP_FUNC void SaveMngSpecial_SPRBossKey() {
    gSaveManager.injectDefault_during();
    setNextStageRoom(0xB);  // boss key room
    setNextStagePoint(0);   // default spawn
}

KEEP_FUNC void SaveMngSpecial_ToTEarlyPoe() {
    gSaveManager.injectDefault_during();
    gSaveManager.setSaveAngle(49299);
    gSaveManager.setSavePosition(-2462.85f, 2750.0f, -7.10f);
    gSaveManager.setLinkInfo();
}

KEEP_FUNC void SaveMngSpecial_ToTEarlyHP() {
    gSaveManager.injectDefault_during();
    gSaveManager.setSaveAngle(0);
    gSaveManager.setSavePosition(-6626.f, 5250.0f, -5587.f);
    gSaveManager.setLinkInfo();
    dComIfGs_onSwitch(224, 4);  // gate moved to correct pos
}

KEEP_FUNC void SaveMngSpecial_HugoArchery() {
    gSaveManager.injectDefault_during();
    // g_dComIfG_gameInfo.temp_flags.flags[14] = 0xC0;  // start archery minigame
}

KEEP_FUNC void SaveMngSpecial_CityPoeCycle() {
    gSaveManager.injectDefault_during();
    gSaveManager.setSaveAngle(71);
    gSaveManager.setSavePosition(-14005.31f, 3000.0f, -15854.05f);
    gSaveManager.setLinkInfo();
}

KEEP_FUNC void SaveMngSpecial_FanTower() {
    gSaveManager.injectDefault_during();
    g_dComIfG_gameInfo.info.mDan.mSwitch[0] = 0;  // reset city switches
}

KEEP_FUNC void SaveMngSpecial_Argorok() {
    gSaveManager.injectDefault_during();
    g_dComIfG_gameInfo.info.mZone[0].mBit.mSwitch[0] |= 0x10000;
}

KEEP_FUNC void SaveMngSpecial_Palace1() {
    gSaveManager.injectDefault_during();
    g_dComIfG_gameInfo.info.mDan.mSwitch[0] = 0;  // reset palace switches
}

KEEP_FUNC void SaveMngSpecial_Palace2() {
    dComIfGp_getPlayer()->mEquipItem = 3;  // master sword
    gSaveManager.injectDefault_during();
    gSaveManager.setSaveAngle(32731);
    gSaveManager.setSavePosition(251.83f, -200.0f, 10993.50f);
    gSaveManager.setLinkInfo();
}

KEEP_FUNC void SaveMngSpecial_CaveOfOrdeals() {
    gSaveManager.injectDefault_during();
    g_dComIfG_gameInfo.info.mDan.mSwitch[0] = 0;
}

KEEP_FUNC void BeastGanonSpecial_setLayer() {
    gSaveManager.injectDefault_during();
    setNextStageLayer(1);
}

KEEP_FUNC void SaveMngSpecial_emptyLake() {
    gSaveManager.injectDefault_during();
    setNextStageLayer(4);
    bossFlags = 0xFF;
}

KEEP_FUNC void SaveMngSpecial_Lakebed1() {
    gSaveManager.injectDefault_during();
    dComIfGs_onSwitch(122, 1);  // dungeon intro cs on
}

KEEP_FUNC void SaveMngSpecial_NoSQAeralfos() {
    gSaveManager.injectDefault_during();
    dComIfGs_setLife(4);  // one heart
}

#if defined(WII_NTSCU_10) || defined(WII_PAL)
#define BUBBLE_ACTOR_ID 489
#else
#define BUBBLE_ACTOR_ID 491
#endif

KEEP_FUNC void SaveMngSpecial_SpawnPGS() {
    dComIfGs_setLife(2); // half heart
    gSaveManager.setSaveAngle(16384);
    gSaveManager.setSavePosition(-749.9980, 50.0, -3265.0000);
    gSaveManager.setLinkInfo();

    cXyz position1(-277.2082, 500.0000, -3598.5154);
    cXyz position2(-277.2082, 500.0000, -3698.5154);

    // Find bubble in the actor list
    fopAc_ac_c* actorData1 =
        find_actor([](auto& act) { return act.mBase.mProcName == BUBBLE_ACTOR_ID && act.current.pos.x == -1425; });

    fopAc_ac_c* actorData2 =
        find_actor([](auto& act) { return act.mBase.mProcName == BUBBLE_ACTOR_ID && act.current.pos.x == -1225; });
        
    if (actorData1 != NULL) {
        actorData1->current.pos = position1;
        actorData1->shape_angle.y = 0;
    }

    if (actorData2 != NULL) {
        actorData2->current.pos = position2;
        actorData2->shape_angle.y = 0;
    }
}

KEEP_FUNC void SaveMngSpecial_ZantFinal() {
    daAlink_c__swordEquip(dComIfGp_getPlayer(), 0); // sword out
    gSaveManager.setSaveAngle(0);
    gSaveManager.setSavePosition(0.0f, 0.0f, 0.0f);
    gSaveManager.setLinkInfo();

    class daB_ZANT_c {
    public:
        /* 0x0000 */ fopEn_enemy_c base;
        /* 0x05AC */ u8 field_0x5ac[0x6d4 - 0x5ac];
        /* 0x06D4 */ int mAction;
        /* 0x06D8 */ int field_0x6d8;
        /* 0x06DC */ int mMode;
        /* 0x06E0 */ u8 field_0x6e0[0x1b];
        /* 0x06FB */ u8 mFightPhase;
    };

    // Find zant in the actor list
    daB_ZANT_c* actorData = (daB_ZANT_c*)find_actor([](auto& act) { return act.mBase.mProcName == PROC_B_ZANT; });

    // Set his action, fight phase and mode to trigger the transition demo
    if (actorData != nullptr) {
        // Set Zant's state
        actorData->mAction = 23;      // ACT_ROOM_CHANGE
        actorData->mFightPhase = 5;   // PHASE_YO
        actorData->mMode = 0;         // MODE_START_DEMO
    }
}

KEEP_FUNC void SaveMngSpecial_ZantDangoro() {
    gSaveManager.injectDefault_during();
    daAlink_c__swordEquip(dComIfGp_getPlayer(), 0); // sword out
    gSaveManager.setSaveAngle(0);
    gSaveManager.setSavePosition(0.0f, -500.0f, 0.0f);
    gSaveManager.setLinkInfo();
}

KEEP_FUNC void SaveMngSpecial_Sword() {
    daAlink_c__swordEquip(dComIfGp_getPlayer(), 0); // sword out
}

#if defined(WII_NTSCU_10) || defined(WII_PAL)
#define EPONA_ACTOR_ID 236
#else
#define EPONA_ACTOR_ID 238
#endif

KEEP_FUNC void SaveMngSpecial_HorseSpawn() {
    g_dComIfG_gameInfo.info.mRestart.mLastMode = 1;
}

KEEP_FUNC void SaveMngSpecial_HorseSpawnRunning() {
    g_dComIfG_gameInfo.info.mRestart.mLastMode = 1;
    g_dComIfG_gameInfo.info.mRestart.mLastSpeedF = 42.0f;
}

KEEP_FUNC void SaveMngSpecial_MoveEpona(float x, float y, float z) {
    cXyz new_pos(x, y, z);

    // Find epona in the actor list
    fopAc_ac_c* actorData =
        find_actor([](auto& act) { return act.mBase.mProcName == EPONA_ACTOR_ID; });
        
    if (actorData != NULL) {
        actorData->current.pos = new_pos;
    }
}

KEEP_FUNC void SaveMngSpecial_OobToGorge() {
    SaveMngSpecial_MoveEpona(-47534.7, -8099.5, 91469.8);
}

KEEP_FUNC void SaveMngSpecial_FaronGate1() {
    SaveMngSpecial_MoveEpona(-14513.4, 26.7, -14480.5);
}

KEEP_FUNC void SaveMngSpecial_FaronGate2() {
    SaveMngSpecial_MoveEpona(-41000.0, -6960.0, 108800.0);
}

KEEP_FUNC void SaveMngSpecial_reBiTE() {
    setNextStageLayer(2);
}

#if defined(WII_NTSCU_10) || defined(WII_PAL)
#define BLUE_POT_ID 762
#else
#define BLUE_POT_ID 764
#endif

KEEP_FUNC void SaveMngSpecial_PotPush2() {
    dComIfGs_setSelectItemIndex(SELECT_ITEM_B, SLOT_0); // rang on B
    dComIfGs_setSelectItemIndex(SELECT_ITEM_RIGHT, SLOT_15); // bombs on D-Pad left, it's backwards

    gSaveManager.setSaveAngle(21579);
    gSaveManager.setSavePosition(9208.0947, 0.0, 79.1174); // Link next to 4th pot
    gSaveManager.setLinkInfo();

    cXyz position1 = g_pot_position_1;
    cXyz position2 = g_pot_position_2;
    cXyz position3 = g_pot_position_3;
    cXyz position4 = g_pot_position_4;

    int type = 10; // big blue pot
    u16 angleZ = ((u16)type << 1) & 0x1F; // extra params, like type of pot, is stored in the z angle on init
    csXyz angleTowardsEntrance(0, 54711, angleZ);
    csXyz angleAwayEntrance(0, 21487, angleZ);
    u32 params = 0x00003FFF;
    s8 roomNo = dComIfGp_getPlayer()->current.roomNo;

    fopAcM_create(BLUE_POT_ID, params, &position1, roomNo, &angleTowardsEntrance, nullptr, -1);
    fopAcM_create(BLUE_POT_ID, params, &position2, roomNo, &angleAwayEntrance, nullptr, -1);
    fopAcM_create(BLUE_POT_ID, params, &position3, roomNo, &angleAwayEntrance, nullptr, -1);
    fopAcM_create(BLUE_POT_ID, params, &position4, roomNo, &angleAwayEntrance, nullptr, -1);
}
