#include "menus/menu_tools_rng/include/tools_rng_menu.h"
#include "menus/utils/menu_mgr.h"
#include "utils/hook.h"

KEEP_FUNC ToolsRngMenu::ToolsRngMenu(Cursor& cursor)
    : Menu(cursor),
      lines{{"freeze rng values", FREEZE_RNG_INDEX, "Freeze the 3 current RNG1 values", true,
             ACTIVE_FUNC(STNG_TOOLS_FREEZE_RNG)},
            {"randomize values", RANDOMIZE_INDEX, "Advance one iteration of the Wichmann-Hill algorithm"},
            {"presets: <ex>", PRESET_OPTIONS_INDEX, "Scroll through various known RNG values to apply"},
            {"load preset", LOAD_PRESET_INDEX, "Apply the RNG preset onto the current RNG values"},
            } {
}

ToolsRngMenu::~ToolsRngMenu() {}

GZSettingID l_mapping[] = {STNG_TOOLS_FREEZE_RNG};

void ToolsRngMenu::draw() {
    if (GZ_getButtonTrig(BACK_BUTTON)) {
        g_menuMgr->pop();
        return;
    }

    if (GZ_getButtonTrig(SELECTION_BUTTON)) {
        switch (cursor.y) {
            case RANDOMIZE_INDEX:
                *game_r0 = (*game_r0 * 171) % 30269;
                *game_r1 = (*game_r1 * 172) % 30307;
                *game_r2 = (*game_r2 * 170) % 30323;
                break;
            case LOAD_PRESET_INDEX:
                *game_r0 = 100;
                *game_r1 = 200;
                *game_r2 = 300;
                break;
            case FREEZE_RNG_INDEX:
                GZSettingEntry* stng = nullptr;

                stng = GZStng_get(l_mapping[cursor.y]);

                if (!stng) {
                    stng = new GZSettingEntry{l_mapping[cursor.y], sizeof(bool), new bool};
                    g_settings.push_back(stng);
                }

                if (stng)
                    *(bool*)stng->data = !*(bool*)stng->data;
                break;
        }
    }

    cursor.move(0, MENU_LINE_NUM);
    GZ_drawMenuLines(lines, cursor.y, MENU_LINE_NUM);
    GZ_drawRngLines(lines, cursor.y, MENU_LINE_NUM);
}
