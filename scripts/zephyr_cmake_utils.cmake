function(append_zephyr_config file)
    set(OVERLAY_CONFIG "${file};${OVERLAY_CONFIG}" CACHE INTERNAL "" FORCE)
endfunction()

function(append_zephyr_overlay file)
    set(DTC_OVERLAY_FILE "${file};${DTC_OVERLAY_FILE}" CACHE INTERNAL "" FORCE)
endfunction()