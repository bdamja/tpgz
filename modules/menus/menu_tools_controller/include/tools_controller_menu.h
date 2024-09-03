#pragma once

#include "menus/menu.h"
#include "tools.h"

enum ToolsControllerIndex {
    INPUT_VIEWER_INDEX,
    TURBO_MODE_INDEX,

    TOOLS_CONTROLLER_COUNT
};

class ToolsControllerMenu : public Menu {
public:
    ToolsControllerMenu(Cursor&);
    virtual ~ToolsControllerMenu();
    virtual void draw();

private:
    Line lines[TOOLS_CONTROLLER_COUNT];
};