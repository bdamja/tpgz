#include "menus/menu_tools_rng/include/tools_rng_menu.h"
#include "menus/utils/menu_mgr.h"

KEEP_FUNC ToolsRngMenu::ToolsRngMenu(Cursor& cursor)
    : Menu(cursor),
      lines{{"freeze rng values", FREEZE_RNG_INDEX, "Freeze the 3 current RNG1 values", true,
             ACTIVE_FUNC(STNG_TOOLS_FREEZE_RNG)},
            {"randomize values", RANDOMIZE_INDEX, "Advance one iteration of the Wichmann-Hill algorithm", true,
             ACTIVE_FUNC(STNG_TOOLS_ADVANCE_RNG)}} {
}

ToolsRngMenu::~ToolsRngMenu() {}

GZSettingID l_mapping[] = {STNG_TOOLS_FREEZE_RNG, STNG_TOOLS_ADVANCE_RNG};

void ToolsRngMenu::draw() {
    if (GZ_getButtonTrig(BACK_BUTTON)) {
        g_menuMgr->pop();
        return;
    }

    if (GZ_getButtonTrig(SELECTION_BUTTON)) {
        GZSettingEntry* stng = nullptr;

        stng = GZStng_get(l_mapping[cursor.y]);

        if (!stng) {
            stng = new GZSettingEntry{l_mapping[cursor.y], sizeof(bool), new bool};
            g_settings.push_back(stng);
        }

        if (stng)
            *(bool*)stng->data = !*(bool*)stng->data;
    }

    cursor.move(0, MENU_LINE_NUM);
    GZ_drawMenuLines(lines, cursor.y, MENU_LINE_NUM);
}
