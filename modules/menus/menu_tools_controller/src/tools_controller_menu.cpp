#include "menus/menu_tools_controller/include/tools_controller_menu.h"
#include "menus/utils/menu_mgr.h"

KEEP_FUNC ToolsControllerMenu::ToolsControllerMenu(Cursor& cursor)
    : Menu(cursor),
      lines{{"input viewer", INPUT_VIEWER_INDEX, "show current inputs", true,
             ACTIVE_FUNC(STNG_TOOLS_INPUT_VIEWER)},
            {"turbo mode", TURBO_MODE_INDEX, "simulates turbo controller inputs", true,
             ACTIVE_FUNC(STNG_TOOLS_TURBO_MODE)}} {
}

ToolsControllerMenu::~ToolsControllerMenu() {}

GZSettingID l_mapping[] = {STNG_TOOLS_INPUT_VIEWER, STNG_TOOLS_TURBO_MODE};

void ToolsControllerMenu::draw() {
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
