#include "stallord_l_slide_check.h"
#include <cstdio>
#include "controller.h"
#include "defines.h"
#include "fifo_queue.h"
#include "game_state.h"
#include "d/d_com_inf_game.h"

#define CLAWSHOT_SLOT 9
#define FULL_LEFT_STICK_X -72
#define CHECK_WINDOW 10
#define STICK_CHECK_FRAME 2
#define COLOR_EARLY 0x0000FF00
#define COLOR_GOOD 0x00CC0000
#define COLOR_NOT_LEFT 0x8300B300
#define COLOR_LATE 0x99000000

static bool sTimerStarted;
static bool sClawTakenOut;
static bool sLTooEarly;
static bool sGoalHit;
static bool sLOnFirstFrame;
static uint32_t sFrameCount;

static void reset() {
    sTimerStarted = false;
    sClawTakenOut = false;
    sLTooEarly = false;
    sGoalHit = false;
    sLOnFirstFrame = false;
    sFrameCount = 0;
}

KEEP_FUNC void StallordLSlideChecker::execute() {
    if (l_fopScnRq_IsUsingOfOverlap) {
        reset();
    }

    bool clawOnX = dComIfGs_getSelectItemIndex(SELECT_ITEM_X) == CLAWSHOT_SLOT;
    bool clawOnY = dComIfGs_getSelectItemIndex(SELECT_ITEM_Y) == CLAWSHOT_SLOT;
    bool xHeld = GZ_getButtonPressed(X);
    bool yHeld = GZ_getButtonPressed(Y);
    bool lHeld = GZ_getButtonPressed(L);
    bool clawHeld = (clawOnX && xHeld) || (clawOnY && yHeld);
    bool clawReleased = (clawOnX && !xHeld) || (clawOnY && !yHeld);
    char buf[32];

    if (clawHeld) {
        sClawTakenOut = true;
        if (!sLTooEarly && lHeld) {
            snprintf(buf, sizeof(buf), "L while %c still held", clawOnX ? 'X' : 'Y');
            FIFOQueue::push(buf, Queue, COLOR_EARLY);
            sClawTakenOut = false;
            sLTooEarly = true;
        }
    }

    if (!sTimerStarted && sClawTakenOut && clawReleased) {
        sClawTakenOut = false;
        sTimerStarted = !sLTooEarly;
        sLTooEarly = false;
    }

    if (!sTimerStarted) {
        return;
    }
    if (++sFrameCount >= CHECK_WINDOW) {
        reset();
        return;
    }
    if (!lHeld || sGoalHit) {
        return;
    }
    if (sFrameCount == 1) {
        sLOnFirstFrame = true;
        return;
    }
    sGoalHit = true;
    if (sFrameCount > STICK_CHECK_FRAME) {
        snprintf(buf, sizeof(buf), "L-slide %df late", sFrameCount - STICK_CHECK_FRAME);
        FIFOQueue::push(buf, Queue, COLOR_LATE);
        return;
    }
    int stickX = JUTGamePad::mPadStatus[0].stickX;
    int frame = sLOnFirstFrame ? 1 : 2;
    if (stickX == FULL_LEFT_STICK_X) {
        snprintf(buf, sizeof(buf), "%s frame L-slide", frame == 1 ? "1st" : "2nd");
        FIFOQueue::push(buf, Queue, COLOR_GOOD);
    } else {
        snprintf(buf, sizeof(buf), "not full left (%d, %df on L)", stickX, frame);
        FIFOQueue::push(buf, Queue, COLOR_NOT_LEFT);
    }
}
