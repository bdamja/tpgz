#include "menus/menu_tools_rng/include/tools_rng_menu.h"
#include "menus/utils/menu_mgr.h"
#include "utils/hook.h"
#include "rels/include/defines.h"
#include "menus/utils/menu_mgr.h"

#define MAX_RNG_PRESETS 10

KEEP_VAR ToolsRngData* toolsRngData;

KEEP_FUNC ToolsRngMenu::ToolsRngMenu(Cursor& cursor)
    : Menu(cursor),
      lines{{"freeze rng values", FREEZE_RNG_INDEX, "Freeze the 3 current RNG1 values", true,
             ACTIVE_FUNC(STNG_TOOLS_FREEZE_RNG)},
            {"randomize values", RANDOMIZE_INDEX, "Advance one iteration of the Wichmann-Hill algorithm"},
            {"load preset", LOAD_PRESET_INDEX, "Apply the RNG preset onto the current RNG values"},
            {"rng presets:", PRESET_OPTIONS_INDEX, "Scroll through various known RNG values", false, nullptr}
            } {
}

ToolsRngMenu::~ToolsRngMenu() {}

void ToolsRngMenu::draw() {
    cursor.setMode(Cursor::MODE_LIST);

    if (GZ_getButtonTrig(BACK_BUTTON)) {
        g_menuMgr->pop();
        return;
    }

    GZSettingEntry* stng = nullptr;

    RngPresetMember rng_opt[MAX_RNG_PRESETS] = {
        {"zant head 1st platform", 18177, 23597, 13040},
        {"zant head 3rd platform", 4134, 7345, 3379},
        {"zant head back left", 4995, 3011, 718},
        {"zant head back mid", 171, 344, 510},
        {"zant head back right", 29241, 28861, 26054},
        {"horseback pattern A", 4661, 29274, 13264},
        {"horseback pattern B", 1, 2, 3},//
        {"horseback pattern C", 1, 2, 3},//
        {"kb1 left after 3rd hit", 21744, 25914, 15568},
        {"kb1 right after 3rd hit", 20952, 7801, 9111},
    };

    if (GZ_getButtonTrig(SELECTION_BUTTON)) {
        switch (cursor.y) {
            case RANDOMIZE_INDEX:
                *game_r0 = (*game_r0 * 171) % 30269;
                *game_r1 = (*game_r1 * 172) % 30307;
                *game_r2 = (*game_r2 * 170) % 30323;
                break;
            case LOAD_PRESET_INDEX:
                stng = GZStng_get(STNG_TOOLS_FREEZE_RNG);
                if (!stng) {
                    stng = new GZSettingEntry{STNG_TOOLS_FREEZE_RNG, sizeof(bool), new bool};
                    g_settings.push_back(stng);
                }
                if (stng)
                    *(bool*)stng->data = true;

                *game_r0 = rng_opt[toolsRngData->l_rng_preset_idx].r0;
                *game_r1 = rng_opt[toolsRngData->l_rng_preset_idx].r1;
                *game_r2 = rng_opt[toolsRngData->l_rng_preset_idx].r2;
                break;
            case FREEZE_RNG_INDEX:
                stng = GZStng_get(STNG_TOOLS_FREEZE_RNG);

                if (!stng) {
                    stng = new GZSettingEntry{STNG_TOOLS_FREEZE_RNG, sizeof(bool), new bool};
                    g_settings.push_back(stng);
                }

                if (stng)
                    *(bool*)stng->data = !*(bool*)stng->data;
                break;
        }
    }
    
    switch (cursor.y) {
        case PRESET_OPTIONS_INDEX:
            cursor.x = toolsRngData->l_rng_preset_idx;
            cursor.move(MAX_RNG_PRESETS, MENU_LINE_NUM);

            if (cursor.y == PRESET_OPTIONS_INDEX) {
                toolsRngData->l_rng_preset_idx = cursor.x;
            }
            break;
        default:
            cursor.move(0, MENU_LINE_NUM);
            break;
        }
    
    lines[PRESET_OPTIONS_INDEX].printf(" <%s>", rng_opt[toolsRngData->l_rng_preset_idx].member);

    GZ_drawMenuLines(lines, cursor.y, MENU_LINE_NUM);
    GZ_drawRngLines(lines, cursor.y, MENU_LINE_NUM);
}
