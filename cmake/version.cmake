if(NOT DEFINED TPGZ_VERSION)
    set(TPGZ_VERSION "unknown")
    find_package(Git QUIET)
    if(GIT_FOUND)
        execute_process(
            COMMAND ${GIT_EXECUTABLE} rev-parse --short HEAD
            WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
            OUTPUT_VARIABLE TPGZ_GIT_HASH
            OUTPUT_STRIP_TRAILING_WHITESPACE
            ERROR_QUIET
            RESULT_VARIABLE TPGZ_GIT_RESULT)
        if(TPGZ_GIT_RESULT EQUAL 0 AND TPGZ_GIT_HASH)
            set(TPGZ_VERSION ${TPGZ_GIT_HASH})
            execute_process(
                COMMAND ${GIT_EXECUTABLE} status --porcelain
                WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
                OUTPUT_VARIABLE TPGZ_GIT_DIRTY
                OUTPUT_STRIP_TRAILING_WHITESPACE
                ERROR_QUIET)
            if(TPGZ_GIT_DIRTY)
                set(TPGZ_VERSION "${TPGZ_VERSION}-dirty")
            endif()
        endif()
    endif()
endif()
message(STATUS "TPGZ_VERSION: ${TPGZ_VERSION}")
