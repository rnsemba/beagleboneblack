beagleboneblack-utils
=====================

Some utilities I've found useful while developing using the Beaglebone black.

bb-pins
=======
Parse the pins, pingroups and pinmux files to display a consolidated view.

If you specify any command-line options, then bb-pins will use the options to generate a template DTS file.

Default output
--------------

When run without any command-line arguments, displays the header information, the internal name, pin number, and the current mode and pull-up configuration.

    Header P8_25 Name: GPIO1_0 Number: 0 GPIO: 1 0x800/000 Mode: mmc1_dat0 (1) Direction: in PUD: pull-up (Allocated: group: pinmux_emmc2_pins)
    Header P8_24 Name: GPIO1_1 Number: 1 GPIO: 33 0x804/004 Mode: mmc1_dat1 (1) Direction: in PUD: pull-up (Allocated: group: pinmux_emmc2_pins)
    Header P8_05 Name: GPIO1_2 Number: 2 GPIO: 34 0x808/008 Mode: mmc1_dat2 (1) Direction: in PUD: pull-up (Allocated: group: pinmux_emmc2_pins)
    Header P8_06 Name: GPIO1_3 Number: 3 GPIO: 35 0x80c/00c Mode: mmc1_dat3 (1) Direction: in PUD: pull-up (Allocated: group: pinmux_emmc2_pins)
    Header P8_23 Name: GPIO1_4 Number: 4 GPIO: 36 0x810/010 Mode: mmc1_dat4 (1) Direction: in PUD: pull-up (Allocated: group: pinmux_emmc2_pins)
    Header P8_22 Name: GPIO1_5 Number: 5 GPIO: 37 0x814/014 Mode: mmc1_dat5 (1) Direction: in PUD: pull-up (Allocated: group: pinmux_emmc2_pins)
    Header P8_03 Name: GPIO1_6 Number: 6 GPIO: 38 0x818/018 Mode: mmc1_dat6 (1) Direction: in PUD: pull-up (Allocated: group: pinmux_emmc2_pins)
    Header P8_04 Name: GPIO1_7 Number: 7 GPIO: 39 0x81c/01c Mode: mmc1_dat7 (1) Direction: in PUD: pull-up (Allocated: group: pinmux_emmc2_pins)
    Header P8_19 Name: EHRPWM2A Number: 8 GPIO: 22 0x820/020 Mode: gpio0[22] (7) Direction: in PUD: pull-down 
    Header P8_13 Name: EHRPWM2B Number: 9 GPIO: 23 0x824/024 Mode: gpio0[23] (7) Direction: in PUD: pull-down 
    Header P8_14 Name: GPIO0_26 Number: 10 GPIO: 26 0x828/028 Mode: gpio0[26] (7) Direction: in PUD: pull-down 
    Header P8_17 Name: GPIO0_27 Number: 11 GPIO: 27 0x82c/02c Mode: gpio0[27] (7) Direction: in PUD: pull-down 
    Header P8_12 Name: GPIO1_12 Number: 12 GPIO: 44 0x830/030 Mode: gpio1[12] (7) Direction: in PUD: pull-down 
    Header P8_11 Name: GPIO1_13 Number: 13 GPIO: 45 0x834/034 Mode: gpio1[13] (7) Direction: in PUD: pull-down 
    Header P8_16 Name: GPIO1_14 Number: 14 GPIO: 46 0x838/038 Mode: gpio1[14] (7) Direction: in PUD: pull-down 
    Header P8_15 Name: GPIO1_15 Number: 15 GPIO: 47 0x83c/03c Mode: gpio1[15] (7) Direction: in PUD: pull-down 
    Header P9_15 Name: GPIO1_16 Number: 16 GPIO: 48 0x840/040 Mode: gpio1[16] (7) Direction: in PUD: pull-down 
    Header P9_23 Name: GPIO1_17 Number: 17 GPIO: 49 0x844/044 Mode: gpio1[17] (7) Direction: in PUD: pull-down 
    Header P9_14 Name: EHRPWM1A Number: 18 GPIO: 50 0x848/048 Mode: gpio1[18] (7) Direction: in PUD: pull-down 
    Header P9_16 Name: EHRPWM1B Number: 19 GPIO: 51 0x84c/04c Mode: gpio1[19] (7) Direction: in PUD: pull-down 
    Header P9_11 Name: UART4_RXD Number: 28 GPIO: 30 0x870/070 Mode: gpio0[30] (7) Direction: in PUD: pull-up (NB: GPIOs limit current to 4-6mA output and approx. 8mA on input)
    Header P9_13 Name: UART4_TXD Number: 29 GPIO: 31 0x874/074 Mode: gpio0[31] (7) Direction: in PUD: pull-up 
    Header P9_12 Name: GPIO1_28 Number: 30 GPIO: 60 0x878/078 Mode: gpio1[28] (7) Direction: in PUD: pull-up 
    Header P8_26 Name: GPIO1_29 Number: 31 GPIO: 61 0x87c/07c Mode: gpio1[29] (7) Direction: in PUD: pull-up 
    Header P8_21 Name: GPIO1_30 Number: 32 GPIO: 62 0x880/080 Mode: mmc1_clk (2) Direction: in PUD: pull-up (Allocated: group: pinmux_emmc2_pins)
    Header P8_20 Name: GPIO1_31 Number: 33 GPIO: 63 0x884/084 Mode: mmc1_cmd (2) Direction: in PUD: pull-up (Allocated: group: pinmux_emmc2_pins)
    Header P8_18 Name: GPIO2_1 Number: 35 GPIO: 65 0x88c/08c Mode: gpio2[1] (7) Direction: in PUD: pull-down 
    Header P8_07 Name: TIMER4 Number: 36 GPIO: 66 0x890/090 Mode: gpio2[2] (7) Direction: in PUD: pull-up 
    Header P8_08 Name: TIMER7 Number: 37 GPIO: 67 0x894/094 Mode: gpio2[3] (7) Direction: in PUD: pull-up 
    Header P8_10 Name: TIMER6 Number: 38 GPIO: 68 0x898/098 Mode: gpio2[4] (7) Direction: in PUD: pull-up 
    Header P8_09 Name: TIMER5 Number: 39 GPIO: 69 0x89c/09c Mode: gpio2[5] (7) Direction: in PUD: pull-up 
    Header P8_45 Name: GPIO2_6 Number: 40 GPIO: 70 0x8a0/0a0 Mode: gpio2[6] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_46 Name: GPIO2_7 Number: 41 GPIO: 71 0x8a4/0a4 Mode: gpio2[7] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_43 Name: GPIO2_8 Number: 42 GPIO: 72 0x8a8/0a8 Mode: gpio2[8] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_44 Name: GPIO2_9 Number: 43 GPIO: 73 0x8ac/0ac Mode: gpio2[9] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_41 Name: GPIO2_10 Number: 44 GPIO: 74 0x8b0/0b0 Mode: gpio2[10] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_42 Name: GPIO2_11 Number: 45 GPIO: 75 0x8b4/0b4 Mode: gpio2[11] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_39 Name: GPIO2_12 Number: 46 GPIO: 76 0x8b8/0b8 Mode: gpio2[12] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_40 Name: GPIO2_13 Number: 47 GPIO: 77 0x8bc/0bc Mode: gpio2[13] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_37 Name: UART5_TXD Number: 48 GPIO: 78 0x8c0/0c0 Mode: gpio2[14] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_38 Name: UART5_RXD Number: 49 GPIO: 79 0x8c4/0c4 Mode: gpio2[15] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_36 Name: UART3_CTSN Number: 50 GPIO: 80 0x8c8/0c8 Mode: gpio2[16] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_34 Name: UART3_RTSN Number: 51 GPIO: 81 0x8cc/0cc Mode: gpio2[17] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_35 Name: UART4_CTSN Number: 52 GPIO: 8 0x8d0/0d0 Mode: gpio0[8] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_33 Name: UART4_RTSN Number: 53 GPIO: 9 0x8d4/0d4 Mode: gpio0[9] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_31 Name: UART5_CTSN Number: 54 GPIO: 10 0x8d8/0d8 Mode: gpio0[10] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_32 Name: UART5_RTSN Number: 55 GPIO: 11 0x8dc/0dc Mode: gpio0[11] (7) Direction: in PUD: Pullup/down disabled 
    Header P8_27 Name: GPIO2_22 Number: 56 GPIO: 86 0x8e0/0e0 Mode: gpio2[22] (7) Direction: in PUD: pull-down 
    Header P8_29 Name: GPIO2_23 Number: 57 GPIO: 87 0x8e4/0e4 Mode: gpio2[23] (7) Direction: in PUD: pull-down 
    Header P8_28 Name: GPIO2_24 Number: 58 GPIO: 88 0x8e8/0e8 Mode: gpio2[24] (7) Direction: in PUD: pull-down 
    Header P8_30 Name: GPIO2_25 Number: 59 GPIO: 89 0x8ec/0ec Mode: gpio2[25] (7) Direction: in PUD: pull-down 
    Header P9_22 Name: UART2_RXD Number: 84 GPIO: 2 0x950/150 Mode: gpio0[2] (7) Direction: in PUD: pull-up 
    Header P9_21 Name: UART2_TXD Number: 85 GPIO: 3 0x954/154 Mode: gpio0[3] (7) Direction: in PUD: pull-up 
    Header P9_18 Name: I2C1_SDA Number: 86 GPIO: 4 0x958/158 Mode: I2C1_SDA (2) Direction: in PUD: pull-down 
    Header P9_17 Name: I2C1_SCL Number: 87 GPIO: 5 0x95c/15c Mode: I2C1_SCL (2) Direction: in PUD: pull-down 
    Header P9_42A Name: GPIO0_7 Number: 89 GPIO: 7 0x964/164 Mode: gpio0[7] (7) Direction: in PUD: pull-down (Both signals are connected to P21 of P11)
    Header P9_20 Name: I2C2_SDA Number: 94 GPIO: 12 0x978/178 Mode: I2C2_SDA (3) Direction: in PUD: pull-up (Allocated: group: pinmux_i2c2_pins)
    Header P9_19 Name: I2C2_SCL Number: 95 GPIO: 13 0x97c/17c Mode: I2C2_SCL (3) Direction: in PUD: pull-up (Allocated: group: pinmux_i2c2_pins)
    Header P9_26 Name: UART1_RXD Number: 96 GPIO: 14 0x980/180 Mode: gpio0[14] (7) Direction: in PUD: pull-up 
    Header P9_24 Name: UART1_TXD Number: 97 GPIO: 15 0x984/184 Mode: gpio0[15] (7) Direction: in PUD: pull-up 
    Header P9_31 Name: SPI1_SCLK Number: 100 GPIO: 110 0x990/190 Mode: gpio3[14] (7) Direction: in PUD: pull-down 
    Header P9_29 Name: SPI1_D0 Number: 101 GPIO: 111 0x994/194 Mode: gpio3[15] (7) Direction: in PUD: pull-down 
    Header P9_30 Name: SPI1_D1 Number: 102 GPIO: 112 0x998/198 Mode: gpio3[16] (7) Direction: in PUD: pull-down 
    Header P9_28 Name: SPI1_CS0 Number: 103 GPIO: 113 0x99c/19c Mode: gpio3[17] (7) Direction: in PUD: pull-down 
    Header P9_27 Name: GPIO3_19 Number: 105 GPIO: 115 0x9a4/1a4 Mode: gpio3[19] (7) Direction: in PUD: pull-down 
    Header P9_25 Name: GPIO3_21 Number: 107 GPIO: 117 0x9ac/1ac Mode: gpio3[21] (7) Direction: in PUD: pull-down 
    Header P9_41A Name: CLKOUT2 Number: 109 GPIO: 20 0x9b4/1b4 Mode: gpio0[20] (7) Direction: in PUD: pull-down (Both signals are connected to P21 of P11)
    
Generating a DTS
----------------
Specify the pin-mode, direction, and pullup/pull-down mode for each pin.

For example:

`./bb-pins.py 'gpio2[2],out' 'gpio2[3],out' 'gpio2[5],out' 'gpio2[4],out' 'gpio1[13],out' 'gpio1[12],out' 'gpio0[23],in,pullup' 'gpio0[26],in,pullup' 'gpio1[15],in,pullup'`

Will produce this DTS template for you:

    /dts-v1/;
    /plugin/;
    
    /{
      compatible = "ti,beaglebone", "ti,beaglebone-black";
      board-name = "CustomizeThis";
      part-number = "CustomizeThis";
      version = "00A0";
    
      exclusive-use =
        "P8.07" /* gpio2_2 */,
        "P8.08" /* gpio2_3 */,
        "P8.09" /* gpio2_5 */,
        "P8.10" /* gpio2_4 */,
        "P8.11" /* gpio1_13 */,
        "P8.12" /* gpio1_12 */,
        "P8.13" /* gpio0_23 */,
        "P8.14" /* gpio0_26 */,
        "P8.15" /* gpio1_15 */,
        "gpio2_2",
        "gpio2_3",
        "gpio2_5",
        "gpio2_4",
        "gpio1_13",
        "gpio1_12",
        "gpio0_23",
        "gpio0_26",
        "gpio1_15";
    
      fragment@0 {
        target = <&am33xx_pinmux>;
    
        __overlay__ {
          pinctrl_generated: RNS_Generated_Pins {
    	pinctrl-single,pins = <
              0x090 0x0f /* P8_07 36 GPIO 66 out Mode: 7 */
              0x094 0x0f /* P8_08 37 GPIO 67 out Mode: 7 */
              0x09c 0x0f /* P8_09 39 GPIO 69 out Mode: 7 */
              0x098 0x0f /* P8_10 38 GPIO 68 out Mode: 7 */
              0x034 0x0f /* P8_11 13 GPIO 45 out Mode: 7 */
              0x030 0x0f /* P8_12 12 GPIO 44 out Mode: 7 */
              0x024 0x37 /* P8_13 9 GPIO 23 in Mode: 7 */
              0x028 0x37 /* P8_14 10 GPIO 26 in Mode: 7 */
              0x03c 0x37 /* P8_15 15 GPIO 47 in Mode: 7 */
    	>;
          };
        };
      };
    
      fragment@1 {
        target = <&ocp>;
        __overlay__ {
          test_helper: helper {
    	compatible = "bone-pinmux-helper";
    	pinctrl-names = "default";
    	pinctrl-0 = <&pinctrl_generated>;
    	status = "okay";
          };
        };
      };
    };

Credit
------
Inspired by [this perl script](http://captainunlikely.com/blog/2013/09/26/managing-the-gpio-pins-on-a-beaglebone-black/)
