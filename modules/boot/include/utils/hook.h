#pragma once

#define HOOK_AMNT 18
enum HookIndex {
    HK_LIB_INIT_INDEX = 0,
    HK_LIB_GAME_LOOP_INDEX = 1,
    HK_LIB_DRAW_INDEX = 2,
    HK_LIB_READ_CONTROLLER_INDEX = 3,
    HK_SUPER_CLAWSHOT_INDEX = 4,
    HK_DISABLE_GRAV_INDEX = 5,
    HK_UNRESTRICTED_ITEMS_INDEX = 6,
    HK_TRANSFORM_ANYWHERE_INDEX = 7,
    HK_INVINCIBLE_ENEMIES_INDEX = 8,
    HK_ONEVENTBIT_INDEX = 9,
    HK_OFFEVENTBIT_INDEX = 10,
    HK_ONSWITCH_INDEX = 11,
    HK_PUTSAVE_INDEX = 12,
    HK_MYEXCEPTIONCALLBACK_INDEX = 13
};

volatile int* r0 = reinterpret_cast<volatile int*>(0x80451168); // gc ntsc-u
volatile int* r1 = reinterpret_cast<volatile int*>(0x8045116C);
volatile int* r2 = reinterpret_cast<volatile int*>(0x80451170);

namespace Hook {
void applyHooks();
}  // namespace Hook