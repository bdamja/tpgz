#ifndef M_DO_M_DO_AUDIO_H
#define M_DO_M_DO_AUDIO_H

#include "../dolphin/types.h"
#include "../Z2AudioLib/Z2AudioMgr.h"

class mDoAud_zelAudio_c {
public:
    Z2AudioMgr mAudioMgr;
};

extern "C" {
extern mDoAud_zelAudio_c g_mDoAud_zelAudio;
}

inline void mDoAud_seStart(u32 i_sfxID, const Vec* i_sePos, u32 param_2, s8 i_reverb) {
    Z2SeMgr__seStart(&Z2GetAudioMgr()->mSeMgr, i_sfxID, i_sePos, param_2, i_reverb, 1.0f, 1.0f, -1.0f, -1.0f, 0);
}

inline void mDoAud_seStop(u32 i_sfxID, u32 param_2) {
    Z2SeMgr__seStop(&Z2GetAudioMgr()->mSeMgr, i_sfxID, param_2);
}

#endif /* M_DO_M_DO_AUDIO_H */
