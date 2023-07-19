#-------------------------------------------------------------------------------
# Microchip Zephyr Example Application
#
# Copyright (c) 2023 Daikin Comfort Technologies North America, Inc.
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.13.1)

# To add new overlay or config files use the following commands
# set(OVERLAY_CONFIG "<YOUR FILE HERE>;${OVERLAY_CONFIG}" CACHE INTERNAL "" FORCE)
# set(DTC_OVERLAY_FILE "<YOUR FILE HERE>;${DTC_OVERLAY_FILE}" CACHE INTERNAL "" FORCE)

include("../scripts/zephyr_cmake_utils.cmake")

if("${CMAKE_BUILD_TYPE}" STREQUAL "Debug")
    message(AUTHOR_WARNING "WARNING: Debug build selected, debug.conf file is included")
    append_zephyr_config(confs_overlays/debug.conf)
endif()

if("${CONFIG_APP_MCUBOOT_BUILD}" STREQUAL "y")
    message(STATUS "Application MCUBOOT is enabled.")
    append_zephyr_config(confs_overlays/mcuboot.conf)
    append_zephyr_overlay(confs_overlays/atsame54_xpro_mcuboot_partitions.overlay)
    append_zephyr_overlay(confs_overlays/mcuboot.overlay)
endif()

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(app LANGUAGES C)

target_sources(app PRIVATE src/main.c)

get_cmake_property(_variableNames VARIABLES)
list(SORT _variableNames)

foreach(_variableName ${_variableNames})
    #message(STATUS "${_variableName}=${${_variableName}}")
endforeach()

set(VSCODE_SETTINGS_PATH "${CMAKE_CURRENT_SOURCE_DIR}/.vscode/cmake_cache.json")

if(EXISTS "${VSCODE_SETTINGS_PATH}")
    file(READ "${VSCODE_SETTINGS_PATH}" VSCODE_SETTINGS_JSON)
else()
    set(VSCODE_SETTINGS_JSON "{}")
endif()
    # foreach(_variableName ${_variableNames})
    # string(JSON VSCODE_SETTINGS_JSON_NEW SET ${VSCODE_SETTINGS_JSON} "${_variableName}" "\"${${_variableName}}\"")
    # string(JSON VSCODE_SETTINGS_JSON_NEW SET ${VSCODE_SETTINGS_JSON_NEW} "${_variableName}" "\"${${_variableName}}\"")

    # message(STATUS " ${_variableName}=${${_variableName}} ")
    # endforeach()
string(JSON VSCODE_SETTINGS_JSON_NEW SET ${VSCODE_SETTINGS_JSON} "BOARD_DIR" "\"${BOARD_DIR}\"")
string(JSON VSCODE_SETTINGS_JSON_NEW SET ${VSCODE_SETTINGS_JSON} "CONFIG_SOC_PART_NUMBER" "\"${CONFIG_SOC_PART_NUMBER}\"")
string(JSON VSCODE_SETTINGS_JSON_NEW SET ${VSCODE_SETTINGS_JSON} "SOC_SERIES" "\"${SOC_SERIES}\"")
string(JSON VSCODE_SETTINGS_JSON_NEW SET ${VSCODE_SETTINGS_JSON} "SOC_FAMILY" "\"${SOC_FAMILY}\"")
string(JSON VSCODE_SETTINGS_JSON_NEW SET ${VSCODE_SETTINGS_JSON} "ZEPHYR_SDK_INSTALL_DIR" "\"${ZEPHYR_SDK_INSTALL_DIR}\"")

# string(JSON VSCODE_SETTINGS_JSON_NEW SET ${VSCODE_SETTINGS_JSON_NEW} " your_var2" "whatever_value ")

# and so on ...
if(NOT "${VSCODE_SETTINGS_JSON_NEW}" STREQUAL "${VSCODE_SETTINGS_JSON} ")
    file(WRITE "${VSCODE_SETTINGS_PATH}" "${VSCODE_SETTINGS_JSON_NEW}")
endif()