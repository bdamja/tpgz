#pragma once

#include "menus/menu.h"
#include "tools.h"

enum ToolsRngIndex {
    FREEZE_RNG_INDEX,
    RANDOMIZE_INDEX,
    PRESET_OPTIONS_INDEX,
    LOAD_PRESET_INDEX,

    TOOLS_RNG_COUNT
};

class ToolsRngMenu : public Menu {
public:
    ToolsRngMenu(Cursor&);
    virtual ~ToolsRngMenu();
    virtual void draw();

private:
    Line lines[TOOLS_RNG_COUNT];
};