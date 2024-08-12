#ifndef F_PC_MANAGER_H_
#define F_PC_MANAGER_H_

#include "f_pc_leaf.h"
#include "f_pc_executor.h"
#include "f_pc_node.h"

LIBTP_DEFINE_FUNC(fpcEx_Search__FPFPvPv_PvPv, fpcEx_Search_void______void____void_____void___, base_process_class*, fpcEx_Search, (fpcLyIt_JudgeFunc pFunc, void* pUserData))

typedef int (*FastCreateReqFunc)(void*);
typedef void (*fpcM_ManagementFunc)(void);
typedef int (*fpcM_DrawIteraterFunc)(void*, void*);

inline u32 fpcM_GetID(const void* pProc) {
    return pProc != NULL ? ((base_process_class*)pProc)->mBsPcId : 0xFFFFFFFF;
}
inline s16 fpcM_GetName(const void* pActor) {
    return ((base_process_class*)pActor)->mProcName;
}
inline u32 fpcM_GetParam(const void* pActor) {
    return ((base_process_class*)pActor)->mParameters;
}

inline void fpcM_SetParam(void* p_actor, u32 param) {
    ((base_process_class*)p_actor)->mParameters = param;
}

inline s16 fpcM_GetProfName(const void* pActor) {
    return ((base_process_class*)pActor)->mBsTypeId;
}

inline bool fpcM_IsFirstCreating(void* proc) {
    return ((base_process_class*)proc)->mInitState == 0;
}

inline void* fpcM_GetAppend(const void* proc) {
    return ((base_process_class*)proc)->mpUserData;
}

enum {
    fpcM_ERROR_PROCESS_ID_e = 0xFFFFFFFF
};

typedef int (*FastCreateReqFunc)(void*);
typedef void (*fpcM_ManagementFunc)(void);
typedef int (*fpcM_DrawIteraterFunc)(void*, void*);

inline process_profile_definition* fpcM_GetProfile(void* proc) {
    return (process_profile_definition*)((base_process_class*)proc)->mpProf;
}

inline BOOL fpcM_IsExecuting(unsigned int id) {
    return fpcEx_IsExist(id);
}

inline void* fpcM_LyJudge(process_node_class* i_node, fpcLyIt_JudgeFunc i_func, void* i_data) {
    return fpcLyIt_Judge(&i_node->mLayer, i_func, i_data);
}

void fpcM_Draw(void* pProc);
s32 fpcM_DrawIterater(fpcM_DrawIteraterFunc pFunc);
s32 fpcM_Execute(void* pProc);
s32 fpcM_Delete(void* pProc);
BOOL fpcM_IsCreating(unsigned int pID);
void fpcM_Management(fpcM_ManagementFunc pFunc1, fpcM_ManagementFunc pFunc2);
void fpcM_Init();
base_process_class* fpcM_FastCreate(s16 pProcTypeID, FastCreateReqFunc param_2, void* param_3,
                                    void* pData);
s32 fpcM_IsPause(void* pProc, u8 param_2);
void fpcM_PauseEnable(void* pProc, u8 param_2);
void fpcM_PauseDisable(void* pProc, u8 param_2);

#endif
