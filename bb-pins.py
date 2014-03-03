#!/usr/bin/python

import re
import sys

PINS = '/sys/kernel/debug/pinctrl/44e10800.pinmux/pins'
PINGROUPS = '/sys/kernel/debug/pinctrl/44e10800.pinmux/pingroups'

# Adapted from http://captainunlikely.com/blog/2013/09/26/managing-the-gpio-pins-on-a-beaglebone-black/
PIN_DATA = '''P8_01,,,,DGND,,,,,,,,,,
P8_02,,,,DGND,,,,,,,,,,
P8_03,6,0x818/018,38,GPIO1_6,gpio1[6],,,,,,mmc1_dat6,gpmc_ad6,R9,
P8_04,7,0x81c/01c,39,GPIO1_7,gpio1[7],,,,,,mmc1_dat7,gpmc_ad7,T9,
P8_05,2,0x808/008,34,GPIO1_2,gpio1[2],,,,,,mmc1_dat2,gpmc_ad2,R8,
P8_06,3,0x80c/00c,35,GPIO1_3,gpio1[3],,,,,,mmc1_dat3,gpmc_ad3,T8,
P8_07,36,0x890/090,66,TIMER4,gpio2[2],,,,,timer4,,gpmc_advn_ale,R7,
P8_08,37,0x894/094,67,TIMER7,gpio2[3],,,,,timer7,,gpmc_oen_ren,T7,
P8_09,39,0x89c/09c,69,TIMER5,gpio2[5],,,,,timer5,,gpmc_be0n_cle,T6,
P8_10,38,0x898/098,68,TIMER6,gpio2[4],,,,,timer6,,gpmc_wen,U6,
P8_11,13,0x834/034,45,GPIO1_13,gpio1[13],,,eQEP2B_in,mmc2_dat1,mmc1_dat5,lcd_data18,gpmc_ad13,R12,
P8_12,12,0x830/030,44,GPIO1_12,gpio1[12],,,EQEP2A_IN,MMC2_DAT0,MMC1_DAT4,LCD_DATA19,GPMC_AD12,T12,
P8_13,9,0x824/024,23,EHRPWM2B,gpio0[23],,,ehrpwm2B,mmc2_dat5,mmc1_dat1,lcd_data22,gpmc_ad9,T10,
P8_14,10,0x828/028,26,GPIO0_26,gpio0[26],,,ehrpwm2_tripzone_in,mmc2_dat6,mmc1_dat2,lcd_data21,gpmc_ad10,T11,
P8_15,15,0x83c/03c,47,GPIO1_15,gpio1[15],,,eQEP2_strobe,mmc2_dat3,mmc1_dat7,lcd_data16,gpmc_ad15,U13,
P8_16,14,0x838/038,46,GPIO1_14,gpio1[14],,,eQEP2_index,mmc2_dat2,mmc1_dat6,lcd_data17,gpmc_ad14,V13,
P8_17,11,0x82c/02c,27,GPIO0_27,gpio0[27],,,ehrpwm0_synco,mmc2_dat7,mmc1_dat3,lcd_data20,gpmc_ad11,U12,
P8_18,35,0x88c/08c,65,GPIO2_1,gpio2[1],mcasp0_fsr,,,mmc2_clk,gpmc_wait1,lcd_memory_clk,gpmc_clk_mux0,V12,
P8_19,8,0x820/020,22,EHRPWM2A,gpio0[22],,,ehrpwm2A,mmc2_dat4,mmc1_dat0,lcd_data23,gpmc_ad8,U10,
P8_20,33,0x884/084,63,GPIO1_31,gpio1[31],,,,,mmc1_cmd,gpmc_be1n,gpmc_csn2,V9,
P8_21,32,0x880/080,62,GPIO1_30,gpio1[30],,,,,mmc1_clk,gpmc_clk,gpmc_csn1,U9,
P8_22,5,0x814/014,37,GPIO1_5,gpio1[5],,,,,,mmc1_dat5,gpmc_ad5,V8,
P8_23,4,0x810/010,36,GPIO1_4,gpio1[4],,,,,,mmc1_dat4,gpmc_ad4,U8,
P8_24,1,0x804/004,33,GPIO1_1,gpio1[1],,,,,,mmc1_dat1,gpmc_ad1,V7,
P8_25,0,0x800/000,1,GPIO1_0,gpio1[0],,,,,,mmc1_dat0,gpmc_ad0,U7,
P8_26,31,0x87c/07c,61,GPIO1_29,gpio1[29],,,,,,,gpmc_csn0,V6,
P8_27,56,0x8e0/0e0,86,GPIO2_22,gpio2[22],,,,,,gpmc_a8,lcd_vsync,U5,
P8_28,58,0x8e8/0e8,88,GPIO2_24,gpio2[24],,,,,,gpmc_a10,lcd_pclk,V5,
P8_29,57,0x8e4/0e4,87,GPIO2_23,gpio2[23],,,,,,gpmc_a9,lcd_hsync,R5,
P8_30,59,0x8ec/0ec,89,GPIO2_25,gpio2[25],,,,,,gpmc_a11,lcd_ac_bias_en,R6,
P8_31,54,0x8d8/0d8,10,UART5_CTSN,gpio0[10],uart5_ctsn,,uart5_rxd,mcasp0_axr1,eQEP1_index,gpmc_a18,lcd_data14,V4,
P8_32,55,0x8dc/0dc,11,UART5_RTSN,gpio0[11],uart5_rtsn,,mcasp0_axr3,mcasp0_ahclkx,eQEP1_strobe,gpmc_a19,lcd_data15,T5,
P8_33,53,0x8d4/0d4,9,UART4_RTSN,gpio0[9],uart4_rtsn,,mcasp0_axr3,mcasp0_fsr,eQEP1B_in,gpmc_a17,lcd_data13,V3,
P8_34,51,0x8cc/0cc,81,UART3_RTSN,gpio2[17],uart3_rtsn,,mcasp0_axr2,mcasp0_ahclkr,ehrpwm1B,gpmc_a15,lcd_data11,U4,
P8_35,52,0x8d0/0d0,8,UART4_CTSN,gpio0[8],uart4_ctsn,,mcasp0_axr2,mcasp0_aclkr,eQEP1A_in,gpmc_a16,lcd_data12,V2,
P8_36,50,0x8c8/0c8,80,UART3_CTSN,gpio2[16],uart3_ctsn,,,mcasp0_axr0,ehrpwm1A,gpmc_a14,lcd_data10,U3,
P8_37,48,0x8c0/0c0,78,UART5_TXD,gpio2[14],uart2_ctsn,,uart5_txd,mcasp0_aclkx,ehrpwm1_tripzone_in,gpmc_a12,lcd_data8,U1,
P8_38,49,0x8c4/0c4,79,UART5_RXD,gpio2[15],uart2_rtsn,,uart5_rxd,mcasp0_fsx,ehrpwm0_synco,gpmc_a13,lcd_data9,U2,
P8_39,46,0x8b8/0b8,76,GPIO2_12,gpio2[12],,,,eQEP2_index,,gpmc_a6,lcd_data6,T3,
P8_40,47,0x8bc/0bc,77,GPIO2_13,gpio2[13],,,pr1_edio_data_out7,eQEP2_strobe,,gpmc_a7,lcd_data7,T4,
P8_41,44,0x8b0/0b0,74,GPIO2_10,gpio2[10],,,,eQEP2A_in,,gpmc_a4,lcd_data4,T1,
P8_42,45,0x8b4/0b4,75,GPIO2_11,gpio2[11],,,,eQEP2B_in,,gpmc_a5,lcd_data5,T2,
P8_43,42,0x8a8/0a8,72,GPIO2_8,gpio2[8],,,,ehrpwm2_tripzone_in,,gpmc_a2,lcd_data2,R3,
P8_44,43,0x8ac/0ac,73,GPIO2_9,gpio2[9],,,,ehrpwm0_synco,,gpmc_a3,lcd_data3,R4,
P8_45,40,0x8a0/0a0,70,GPIO2_6,gpio2[6],,,,ehrpwm2A,,gpmc_a0,lcd_data0,R1,
P8_46,41,0x8a4/0a4,71,GPIO2_7,gpio2[7],,,,ehrpwm2B,,gpmc_a1,lcd_data1,R2,
P9_01,,,,GND,,,,,,,,,,Ground
P9_02,,,,GND,,,,,,,,,,Ground
P9_03,,,,DC_3.3V,,,,,,,,,,
P9_04,,,,DC_3.3V,,,,,,,,,,250mA Max Current
P9_05,,,,VDD_5V,,,,,,,,,,
P9_06,,,,VDD_5V,,,,,,,,,,1A Max Current (only if DC jack powered)
P9_07,,,,SYS_5V,,,,,,,,,,250mA Max Current
P9_08,,,,SYS_5V,,,,,,,,,,250mA Max Current
P9_09,,,,PWR_BUT,,,,,,,,,,Has a 5V Level (pulled up by TP65217C)
P9_10,,,,SYS_RESETn,,,,,,,,RESET_OUT,A10,
P9_11,28,0x870/070,30,UART4_RXD,gpio0[30],uart4_rxd_mux2,,mmc1_sdcd,rmii2_crs_dv,gpmc_csn4,mii2_crs,gpmc_wait0,T17,NB: GPIOs limit current to 4-6mA output and approx. 8mA on input
P9_12,30,0x878/078,60,GPIO1_28,gpio1[28],mcasp0_aclkr_mux3,,gpmc_dir,mmc2_dat3,gpmc_csn6,mii2_col,gpmc_be1n,U18,
P9_13,29,0x874/074,31,UART4_TXD,gpio0[31],uart4_txd_mux2,,mmc2_sdcd,rmii2_rxerr,gpmc_csn5,mii2_rxerr,gpmc_wpn,U17,
P9_14,18,0x848/048,50,EHRPWM1A,gpio1[18],ehrpwm1A_mux1,,gpmc_a18,mmc2_dat1,rgmii2_td3,mii2_txd3,gpmc_a2,U14,
P9_15,16,0x840/040,48,GPIO1_16,gpio1[16],ehrpwm1_tripzone_input,,gpmc_a16,mii2_txen,rmii2_tctl,gmii2_txen,gpmc_a0,R13,
P9_16,19,0x84c/04c,51,EHRPWM1B,gpio1[19],ehrpwm1B_mux1,,gpmc_a19,mmc2_dat2,rgmii2_td2,mii2_txd2,gpmc_a3,T14,
P9_17,87,0x95c/15c,5,I2C1_SCL,gpio0[5],,,,ehrpwm0_synci,I2C1_SCL,mmc2_sdwp,spi0_cs0,A16,
P9_18,86,0x958/158,4,I2C1_SDA,gpio0[4],,,,ehrpwm0_tripzone,I2C1_SDA,mmc1_sdwp,spi0_d1,B16,
P9_19,95,0x97c/17c,13,I2C2_SCL,gpio0[13],,,spi1_cs1,I2C2_SCL,dcan0_rx,timer5,uart1_rtsn,D17,
P9_20,94,0x978/178,12,I2C2_SDA,gpio0[12],,,spi1_cs0,I2C2_SDA,dcan0_tx,timer6,uart1_ctsn,D18,
P9_21,85,0x954/154,3,UART2_TXD,gpio0[3],EMU3_mux1,,,ehrpwm0B,I2C2_SCL,uart2_txd,spi0_d0,B17,
P9_22,84,0x950/150,2,UART2_RXD,gpio0[2],EMU2_mux1,,,ehrpwm0A,I2C2_SDA,uart2_rxd,spi0_sclk,A17,
P9_23,17,0x844/044,49,GPIO1_17,gpio1[17],ehrpwm0_synco,,gpmc_a17,mmc2_dat0,rgmii2_rxdv,gmii2_rxdv,gpmc_a1,V14,
P9_24,97,0x984/184,15,UART1_TXD,gpio0[15],,,,I2C1_SCL,dcan1_rx,mmc2_sdwp,uart1_txd,D15,
P9_25,107,0x9ac/1ac,117,GPIO3_21,gpio3[21],,,EMU4_mux2,mcasp1_axr1,mcasp0_axr3,eQEP0_strobe,mcasp0_ahclkx,A14,
P9_26,96,0x980/180,14,UART1_RXD,gpio0[14],,,,I2C1_SDA,dcan1_tx,mmc1_sdwp,uart1_rxd,D16,
P9_27,105,0x9a4/1a4,115,GPIO3_19,gpio3[19],,,EMU2_mux2,mcasp1_fsx,mcasp0_axr3,eQEP0B_in,mcasp0_fsr,C13,
P9_28,103,0x99c/19c,113,SPI1_CS0,gpio3[17],,,eCAP2_in_PWM2_out,spi1_cs0,mcasp0_axr2,ehrpwm0_synci,mcasp0_ahclkr,C12,
P9_29,101,0x994/194,111,SPI1_D0,gpio3[15],,,mmc1_sdcd_mux1,spi1_d0,,ehrpwm0B,mcasp0_fsx,B13,
P9_30,102,0x998/198,112,SPI1_D1,gpio3[16],,,mmc2_sdcd_mux1,spi1_d1,,ehrpwm0_tripzone,mcasp0_axr0,D12,
P9_31,100,0x990/190,110,SPI1_SCLK,gpio3[14],,,mmc0_sdcd_mux1,spi1_sclk,,ehrpwm0A,mcasp0_aclkx,A13,
P9_32,,,,VADC,,,,,,,,,,Voltage Reference for ADC (NB:1.8V)
P9_33,,,,AIN4,,,,,,,,,C8,NB: 1.8V tolerant
P9_34,,,,AGND,,,,,,,,,,Ground for ADC
P9_35,,,,AIN6,,,,,,,,,A8,NB: 1.8V tolerant
P9_36,,,,AIN5,,,,,,,,,B8,NB: 1.8V tolerant
P9_37,,,,AIN2,,,,,,,,,B7,NB: 1.8V tolerant
P9_38,,,,AIN3,,,,,,,,,A7,NB: 1.8V tolerant
P9_39,,,,AIN0,,,,,,,,,B6,NB: 1.8V tolerant
P9_40,,,,AIN1,,,,,,,,,C7,NB: 1.8V tolerant
P9_41A,109,0x9b4/1b4,20,CLKOUT2,gpio0[20],EMU3_mux0,,timer7_mux1,clkout2,tclkin,,xdma_event_intr1,D14,Both signals are connected to P21 of P11
P9_41B,,0x9a8/1a8,116,GPIO3_20,gpio3[20],,,emu3,Mcasp1_axr0,,eQEP0_index,mcasp0_axr1,D13,Both signals are connected to P21 of P11
P9_42A,89,0x964/164,7,GPIO0_7,gpio0[7],xdma_event_intr2,mmc0_sdwp,spi1_sclk,pr1_ecap0_ecap_capin_apwm_o,spi1_cs1,uart3_txd,eCAP0_in_PWM0_out,C18,Both signals are connected to P21 of P11
P9_42B,,0x9a0/1a0,114,GPIO3_18,gpio3[18],,,,Mcasp1_aclkx,Mcaspo_axr2,eQEP0A_in,Mcasp0_aclkr,B12,Both signals are connected to P21 of P11
P9_43,,,,GND,,,,,,,,,,See pg 50 of the SRM
P9_44,,,,GND,,,,,,,,,,Ground
P9_45,,,,GND,,,,,,,,,,Ground
P9_46,,,,GND,,,,,,,,,,Ground'''

DTS_TEMPLATE='''/dts-v1/;
/plugin/;

/{
  compatible = "ti,beaglebone", "ti,beaglebone-black";
  board-name = "CustomizeThis";
  part-number = "CustomizeThis";
  version = "00A0";

  exclusive-use =
%s;

  fragment@0 {
    target = <&am33xx_pinmux>;

    __overlay__ {
      pinctrl_generated: RNS_Generated_Pins {
	pinctrl-single,pins = <
%s
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
'''

class HeaderPins:
  def __init__(self):
    self.pins = []
    self.pin_map = {}

  def init(self):
    for pinline in PIN_DATA.split('\n'):
      splitpinlines = pinline.split(',')
      hp = HeaderPin(*splitpinlines)
      self.pins.append(hp)
      if hp.number:
        self.pin_map[int(hp.number)] = hp
    self.readModes()
    self.readPinGroups()

  def readPinGroups(self):
    fh = open(PINGROUPS)
    current_group = ''
    for line in fh:
      if line.startswith('group:'):
        current_group = line
      if current_group != '':
	 if line.startswith('pin '):
	   pin = int(re.match(r'^pin ([0-9]+)', line).group(1))
	   if pin in self.pin_map.keys():
	     self.pin_map[pin].comment = (self.pin_map[pin].comment + ' Allocated: ' + current_group.strip()).strip()

    fh.close()

  def readModes(self):
    fh = open(PINS)
    pins = fh.readlines()
    for pin_str in pins[1:]:
      p = pin_str.split(' ')
      (_, pin, ioaddr, mode, _, _) = p
      mode = int(mode, 16)
      if int(pin) in self.pin_map.keys():
	pin = int(pin)
	self.pin_map[pin].current_mode = mode & 7
	self.pin_map[pin].enable_pullupdown = (mode & 8) >> 3
	self.pin_map[pin].pullup_or_pulldown = (mode & 16) >> 4
	self.pin_map[pin].direction = (mode & 32) >> 5
    fh.close()

directions = ['out', 'in']
pullupdown = ['pull-down', 'pull-up']
yesno = ['yes', 'no']

class HeaderPin:
  def __init__(self, head_pin, number, ioaddr, gpio, name, m7, m6, m5, m4, m3, m2, m1, m0, pin, comment):
    self.head_pin = head_pin
    self.number = number
    self.ioaddr = ioaddr
    self.gpio = gpio
    self.name = name
    self.modes = [m0, m1, m2, m3, m4, m5, m6, m7]
    self.pin = pin
    self.comment = comment
    self.current_mode = 0
    self.direction = 0
    self.group = ''

  def __str__(self):
    if self.comment:
      comment_str = '(%s)' % self.comment
    else:
      comment_str = ''
    if self.enable_pullupdown:
      pullup = 'Pullup/down disabled'
    else:
      pullup = pullupdown[self.pullup_or_pulldown]
    return 'Header %s Name: %s Number: %s GPIO: %s %s Mode: %s (%d) Direction: %s PUD: %s %s' % (
        self.head_pin, self.name, self.number, self.gpio, self.ioaddr, 
        self.modes[self.current_mode], self.current_mode,
        directions[self.direction], pullup, comment_str)

def generate_dts(header_pins, pin_config):
  pin_specs = '    ';
  hardware = '    ';
  pin_modes = '          ';
  pin_count = 0
  for comp in pin_config:
    entries = comp.split(',')
    located = False
    for pins in header_pins.pins:
      if entries[0] in pins.modes:
	if pin_count != 0:
	  pin_specs += ',\n    '
	  hardware += ',\n    '
	  pin_modes += '\n          '
	pin_name = entries[0].replace('[', '_').replace(']', '')
	pin_specs += '"%s" /* %s */' % (
	    pins.head_pin.replace('_', '.'), pin_name)
	hardware += '"%s"' % pin_name
	pin_modes += '0x%s' % pins.ioaddr[pins.ioaddr.index('/') + 1:]
	mode = pins.modes.index(entries[0])
	if entries[1] == 'in':
	  mode |= 0x10
	if len(entries) > 2:
	  pass
	  if entries[2] == 'pullup':
	    mode |= 0x20
	else:
	  mode |= 0x08
	pin_modes += ' 0x%02x /* %s %s GPIO %s %s Mode: %d */' % (mode,
	    pins.head_pin, pins.number, pins.gpio, entries[1],
	    pins.modes.index(entries[0]))

	pin_count += 1
	located = True
    if not located:
      print 'Could not find pin with mode ' + entries[0]
      return
  print DTS_TEMPLATE % (pin_specs + ',\n' + hardware, pin_modes)

header_pins = HeaderPins()
header_pins.init()

if len(sys.argv) == 1:
  for pin in header_pins.pin_map.keys():
    print header_pins.pin_map[pin]
else:
  generate_dts(header_pins, sys.argv[1:])
