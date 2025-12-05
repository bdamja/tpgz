#include "settings.h"
#include <cstdio>
#include <algorithm>

ListMember g_font_opt[] = {"consola",   "calamity-bold",  "lib-sans",      "lib-sans-bold",
                           "lib-serif", "lib-serif-bold", "press-start-2p"};

bool g_swap_equips_flag;

tpgz::containers::deque<GZSettingEntry*> g_settings;

KEEP_FUNC void GZStng_add(GZSettingID id, void* data, size_t size) {
    auto it = g_settings.begin();
    for (; it != g_settings.end(); ++it) {
        if ((*it)->id == id) {
            break;
        }
    }
    if (it == g_settings.end()) {
        GZSettingEntry* entry = new GZSettingEntry{id, size, data};
        g_settings.push_back(entry);
    } else {
        GZSettingEntry* entry = *it;
        void* old_data = entry->data;
        delete[] (uint8_t*)old_data;
        entry->data = data;
        entry->size = size;
    }
}

KEEP_FUNC void GZStng_remove(GZSettingID id) {
    auto it = g_settings.begin();
    for (; it != g_settings.end(); ++it) {
        if ((*it)->id == id) {
            break;
        }
    }
    if (it != g_settings.end()) {
        auto* entry = *it;
        void* data = entry->data;
        delete[] (uint8_t*)data;
        g_settings.erase(it);
        delete entry;
    }
}

KEEP_FUNC GZSettingEntry* GZStng_get(GZSettingID id) {
    auto it = g_settings.begin();
    for (; it != g_settings.end(); ++it) {
        if ((*it)->id == id) {
            break;
        }
    }
    GZSettingEntry* entry = nullptr;
    if (it != g_settings.end()) {
        entry = *it;
    }
    return entry;
}

KEEP_FUNC tpgz::containers::deque<GZSettingID>* GZStng_getList() {
    auto list = new tpgz::containers::deque<GZSettingID>;
    list->resize(g_settings.size());
    std::transform(g_settings.begin(), g_settings.end(), list->begin(),
                   [](GZSettingEntry* entry) { return entry->id; });
    return list;
}

void GZ_initFont() {
    uint32_t fontType = GZStng_getData(STNG_FONT, 0);
    if (fontType >= 0 && fontType < FONT_OPTIONS_COUNT) {
        char buf[40] = {0};
        snprintf(buf, sizeof(buf), "tpgz/fonts/%s.fnt", g_font_opt[fontType].member);
        Font::loadFont(buf);
    }
}

cXyz g_pot_position_1 = {9579.6f, 0.0f, -76.9f}; // default positions
cXyz g_pot_position_2 = {9491.1f, 0.0f, -30.3f};
cXyz g_pot_position_3 = {9396.6f, -1.0f, 18.9f};
cXyz g_pot_position_4 = {9297.3f, -1.0f, 30.7f};

int s_pot_count = 0;

#if defined(WII_NTSCU_10) || defined(WII_PAL)
#define BLUE_POT_ID 762
#else
#define BLUE_POT_ID 764
#endif

KEEP_FUNC PotResult find_pots_in_radius(const cXyz& center, float radius, int maxCount) {
    PotResult result;
    float r2 = radius*radius;

    node_class* node = g_fopAcTg_Queue.mpHead;
    for (int i = 0; i < g_fopAcTg_Queue.mSize; i++) {
        if (!node) break;

        create_tag_class* tag = (create_tag_class*)node;
        fopAc_ac_c* actor = (fopAc_ac_c*)tag->mpTagData;

        if (actor->mBase.mProcName == BLUE_POT_ID) {
            float dx = actor->current.pos.x - center.x;
            float dz = actor->current.pos.z - center.z;
            float dist2 = dx*dx + dz*dz;

            if (dist2 <= r2) {
                result.pots[result.count++] = actor;
                if (result.count == maxCount)
                    break;
            }
        }

        node = node->mpNextNode;
    }

    return result;
}

KEEP_FUNC void store_pot_positions(const PotResult& found) {
    if (found.count != 4) return;

    g_pot_position_1 = found.pots[0]->current.pos;
    g_pot_position_2 = found.pots[1]->current.pos;
    g_pot_position_3 = found.pots[2]->current.pos;
    g_pot_position_4 = found.pots[3]->current.pos;
}
