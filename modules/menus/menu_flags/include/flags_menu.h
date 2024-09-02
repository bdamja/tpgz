#pragma once
#include "menus/menu.h"

enum FlagsIndex {
    GENERAL_FLAGS_INDEX,
    DUNGEON_FLAGS_INDEX,
    PORTAL_FLAGS_INDEX,
    RUPEE_FLAGS_INDEX,
    FLAG_RECORDS_INDEX,
    FLAG_LOG_INDEX,

    FLAGS_COUNT
};

class FlagsMenu : public Menu {
public:
    FlagsMenu(Cursor&);
    virtual ~FlagsMenu();
    virtual void draw();

private:
    Line lines[FLAGS_COUNT];
};
