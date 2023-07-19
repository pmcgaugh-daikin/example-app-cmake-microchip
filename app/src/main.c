/*
 * Copyright (c) 2023 Daikin Comfort Technologies North America, Inc.
 * Copyright (c) 2021 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 * 
 * This file has been modified by Daikin Comfort Technologies North America, Inc.
 *  - remove sensor references and add counter logging
 * 
 */

#include <zephyr/kernel.h>
#include <zephyr/drivers/gpio.h>
#include <app_version.h>

#include <zephyr/logging/log.h>
LOG_MODULE_REGISTER(main, CONFIG_APP_LOG_LEVEL);

int main(void)
{
    printk("Zephyr Example Application %s\n", APP_VERSION_STRING);

    static const struct gpio_dt_spec led0 = GPIO_DT_SPEC_GET(DT_ALIAS(led0), gpios);
    gpio_pin_configure_dt(&led0, GPIO_OUTPUT);


	while (1) {
        if (!gpio_is_ready_dt(&led0))
        {
            return 0;
        }

        static int cnt = 0;
        cnt++;
        LOG_INF("Current iteration: %d", cnt);
        
        gpio_pin_toggle(led0.port, led0.pin);

		k_sleep(K_MSEC(1000));
	}

	return 0;
}

