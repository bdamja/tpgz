#ifndef JAISOUND_H
#define JAISOUND_H

#include "../JGeometry.h"
#include "JAISoundHandles.h"
#include "JAISoundParams.h"
#include <cstddef>

class JAISoundID {
public:
    operator u32() const { return this->mId.mFullId; }

    JAISoundID(u32 pId) { mId.mFullId = pId; };

    JAISoundID(JAISoundID const& other) { mId = other.mId; };

    JAISoundID() {}

    bool isAnonymous() { return mId.mFullId == 0xffffffff; }
    void setAnonymous() { mId.mFullId = -1; }

    union {
        u32 mFullId;
        struct {
            u8 b0;
            u8 b1;
            u8 b2;
            u8 b3;
        } mBytes;
        struct {
            u16 mSoundType;
            u16 mShortId;
        } mAdvancedId;  // Debug doesn't have an inline for referencing the short ID so I assume
                        // it's similar to this
    } mId;
};

struct JASTrack {};

struct JAISoundStatus_ {
    void init() {
        field_0x0 = 0;
        field_0x1 = 0;
        *((u16*)(this) + 2) = 0;
        user_data = 0;
    }

    /* 0x0 */ u8 field_0x0;
    /* 0x1 */ u8 field_0x1;
    /* 0x2 */ u8 state[2];  // debug accesses like "state.flags.calcedOnce"
    /* 0x4 */ u32 user_data;
};  // Size: 0x6

struct JAISoundFader {
    void forceIn() {
        mIntensity = 1.0f;
        field_0x4.zero();
    }

    /* 0x00 */ f32 mIntensity;
    /* 0x04 */ JAISoundParamsTransition::TTransition field_0x4;
};  // Size: 0x10

class JAISoundHandle;
class JAIAudible;
class JAIAudience;
class JAISound {
public:
    u32 getUserData() const { return status_.user_data; }
    bool isHandleAttached() const { return handle_ != NULL; }

    /* 0x00 */ void* vtable;
    /* 0x04 */ JAISoundHandle* handle_;
    /* 0x08 */ JAIAudible* audible_;
    /* 0x0C */ JAIAudience* audience_;
    /* 0x10 */ s32 lifeTime;
    /* 0x14 */ s32 prepareCount;
    /* 0x18 */ JAISoundID soundID;
    /* 0x1C */ JAISoundStatus_ status_;
    /* 0x24 */ JAISoundFader fader;
    /* 0x34 */ s32 field_0x34;
    /* 0x38 */ s32 mCount;
    /* 0x3C */ JAISoundParams params;
};  // Size: 0x98

class JAISoundActivity {
public:
    void init() { field_0x0 = 0; }

    /* 0x0 */ u8 field_0x0;
};

#endif /* JAISOUND_H */
