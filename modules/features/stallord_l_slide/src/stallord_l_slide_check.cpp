#ifdef GCN_PLATFORM

#include "game_state.h"
#include "defines.h"
#include <cstdio>
#include "stallord_l_slide_check.h"
#include "controller.h"
#include "fifo_queue.h"
#include "d/d_com_inf_game.h"
#include "SSystem/SComponent/c_counter.h"
#include "f_op/f_op_scene_req.h"
#include "m_Do/m_Do_printf.h"

#define X_HELD_CHECK !GZ_getButtonHold(X)
#define X_DOWN_CHECK GZ_getButtonPressed(X)
#define Y_HELD_CHECK !GZ_getButtonHold(Y)
#define Y_DOWN_CHECK GZ_getButtonPressed(Y)
#define L_HELD_CHECK !GZ_getButtonHold(L)
#define L_DOWN_CHECK GZ_getButtonPressed(L)

#define PAD Pad

KEEP_FUNC void StallordLSlideChecker::execute() {
    static bool sTimerStarted = false;
    static bool sClawTakenOut = false;
    static bool sLTooEarly = false;
    static bool sGoalHit = false;
    static bool sFrame_1_L = false;
    static uint32_t sFrameCount = 0;

    // reset counters on load
    if (l_fopScnRq_IsUsingOfOverlap) {
        sFrameCount = 0;
        sGoalHit = false;
        sTimerStarted = false;
    }

    bool claw_on_x = dComIfGs_getSelectItemIndex(SELECT_ITEM_X) == 9; // claw on x
    bool claw_on_y = dComIfGs_getSelectItemIndex(SELECT_ITEM_Y) == 9; // claw on y
    char claw_button = claw_on_x ? 'X' : 'Y';
    char buf[32];

    if (!sClawTakenOut){
        if ((claw_on_x && X_DOWN_CHECK) || (claw_on_y && Y_DOWN_CHECK)) {
            sClawTakenOut = true;
        }
    }

    if (!sLTooEarly && sClawTakenOut && L_DOWN_CHECK && ((claw_on_x && X_DOWN_CHECK) || (claw_on_y && Y_DOWN_CHECK))) {
        snprintf(buf, sizeof(buf), "L while %c still held", claw_button);
        FIFOQueue::push(buf, Queue, 0x0000FF00);
        sClawTakenOut = false;
        sLTooEarly = true;
    }

    if (!sTimerStarted && sClawTakenOut){
        if ((claw_on_x && !X_DOWN_CHECK) || (claw_on_y && !Y_DOWN_CHECK)) {
            // player let go of claw button
            sClawTakenOut = false;
            sTimerStarted = true;        
        }
    }

    if (sTimerStarted) {
        sFrameCount++;

        if (sFrameCount < 10) {
            if (L_DOWN_CHECK && !sGoalHit) {
                int stickX = JUTGamePad::mPadStatus[0].stickX;
                bool directly_left = stickX == -72;
                
                if (sFrameCount == 1) {
                    sFrame_1_L = true;
                    // need to do this because L slide checks stick angle 2 frames after letting go of claw
                }
            
                if (sFrameCount == 2) {
                    sGoalHit = true;
                    if (sFrame_1_L) {
                        if (directly_left) {
                            FIFOQueue::push("1st frame L-slide", Queue, 0x00CC0000);
                        } else {
                            snprintf(buf, sizeof(buf), "not full left (%d, 1f on L)", stickX);
                            FIFOQueue::push(buf, Queue, 0x8300B300);
                        }
                    } else {
                        if (directly_left) {
                            FIFOQueue::push("2nd frame L-slide", Queue, 0x00CC0000);
                        } else {
                            snprintf(buf, sizeof(buf), "not full left (%d, 2f on L)", stickX);
                            FIFOQueue::push(buf, Queue, 0x8300B300);
                        }
                    }
                } else if (sFrameCount > 2) {
                    sGoalHit = true;
                    snprintf(buf, sizeof(buf), "L-slide %df late", sFrameCount - 2);
                    FIFOQueue::push(buf, Queue, 0x99000000);
                }
            }
        } else {
            sFrameCount = 0;
            sGoalHit = false;
            sTimerStarted = false;
            sClawTakenOut = false;
            sFrame_1_L = false; 
            sLTooEarly = false;
        }
    }
}

#endif