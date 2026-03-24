#include <main.h>
#include "slashcheck.h"
#include "gz_flags.h"

namespace tpgz::modules {
void main() {
    GZFlg_addFlag(new GZFlag{GZFLG_SLASH, ACTIVE_FUNC(STNG_TOOLS_SLASH), GAME_LOOP,
                             SlashChecker::execute});
}
void exit() {
    auto* flg = GZFlg_removeFlag(GZFLG_SLASH);
    delete flg;
}

}  // namespace tpgz::modules