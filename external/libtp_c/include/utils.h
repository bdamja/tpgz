#ifndef UTILS_H
#define UTILS_H

#include <cstdint>
#include "d/com/d_com_inf_game.h"

// Toggles save event flags
void setEventFlag(u16 flag);

// Toggles temp event flags
void setTempEventFlag(u16 flag);

// Toggles equipment items
void setItemFirstBit(u8 item);

// Toggle dungeon switches
void setDungeonSwitch(int pFlag, int i_roomNo);

// Set Savefile spawn info
void setReturnPlace(const char* stage, s8 room, u8 spawn);

void setNextStageName(const char* name);
void setNextStageLayer(s8 layer);
void setNextStageRoom(s8 room);
void setNextStagePoint(s16 point);

int popcount(uint32_t i);

#endif