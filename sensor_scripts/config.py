"""
Copyright (c) 2015, Stephanie Moyerman
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies,
either expressed or implied, of the FreeBSD Project.
"""

# Class for accel/mag/temp configuration and registers
class XM:
    ADDRESS = 0x1D
    WHO_AM_I = 0x0F    # r
    WHO_AM_I_OK = 0x49  #r
    OUT_TEMP_L_XM = 0x05 # r
    OUT_TEMP_H_XM = 0x06 # r
    STATUS_REG_M = 0x07 # r
    OUT_X_L_M = 0x08 # r
    OUT_X_H_M = 0x09 # r
    OUT_Y_L_M = 0x0A # r
    OUT_Y_H_M = 0x0B # r
    OUT_Z_L_M = 0x0C # r
    OUT_Z_H_M = 0x0D # r
    INT_CTRL_REG_M = 0x12 # rw
    INT_SRC_REG_M = 0x13 # r
    INT_THS_L_M = 0x14 # rw
    INT_THS_H_M = 0x15 # rw
    OFFSET_X_L_M = 0x16 # rw
    OFFSET_X_H_M = 0x17 # rw
    OFFSET_Y_L_M = 0x18 # rw
    OFFSET_Y_H_M = 0x19 # rw
    OFFSET_Z_L_M = 0x1A # rw
    OFFSET_Z_H_M = 0x1B # rw
    REFERENCE_X = 0x1C # rw
    REFERENCE_Y = 0x1D # rw
    REFERENCE_Z = 0x1E # rw
    CTRL_REG0_XM = 0x1F # rw
    CTRL_REG1_XM = 0x20 # rw
    CTRL_REG2_XM = 0x21 # rw
    CTRL_REG3_XM = 0x22 # rw
    CTRL_REG4_XM = 0x23 # rw
    CTRL_REG5_XM = 0x24 # rw
    CTRL_REG6_XM = 0x25 # rw
    CTRL_REG7_XM = 0x26 # rw
    STATUS_REG_A = 0x27 # r
    OUT_X_L_A = 0x28 # r
    OUT_X_H_A = 0x29 # r
    OUT_Y_L_A = 0x2A # r
    OUT_Y_H_A = 0x2B # r
    OUT_Z_L_A = 0x2C # r
    OUT_Z_H_A = 0x2D # r
    FIFO_CTRL_REG = 0x2E # rw
    FIFO_SRC_REG = 0x2F # r
    INT_GEN_1_REG = 0x30 # rw
    INT_GEN_1_SRC = 0x31 # r
    INT_GEN_1_THS = 0x32 # rw
    INT_GEN_1_DURATION = 0x33 # rw
    INT_GEN_2_REG = 0x34 # rw
    INT_GEN_2_SRC = 0x35 # r
    INT_GEN_2_THS = 0x36 # rw
    INT_GEN_2_DURATION =  0x37 # rw
    CLICK_CFG = 0x38 # rw
    CLICK_SRC = 0x39 # r
    CLICK_THS = 0x3A # rw
    TIME_LIMIT = 0x3B # rw
    TIME_LATENCY = 0x3C # rw
    TIME_WINDOW = 0x3D # rw
    ACT_THS = 0x3E # rw
    ACT_DUR = 0x3F # rw
    RANGE_M = {'2GAUSS': (0b00 << 5), '4GAUSS': (0b01 << 5), '8GAUSS': (0b10 << 5), '12GAUSS': (0b11 << 5)}
    RANGE_A = {'2G':(0b000 << 3),'4G':(0b001 << 3),'6G':(0b010 << 3),'8G':(0b011 << 3),'16G':(0b100 << 3)}
    CAL_M = {'2GAUSS': (2.0/32768.0), '4GAUSS': (4.0/32768.0), '8GAUSS': (8.0/32768.0), '12GAUSS': (12.0/32768.0)}
    CAL_A = {'2G': (2.0/32768.0),'4G': (4.0/32768.0),'6G':(6.0/32768.0),'8G':(8.0/32768.0),'16G':(16.0/32768.0)}
    CAL_TEMP = 1.0/8.0


# Class for gyro configuration and registers
class GYRO:
    ADDRESS = 0x6b
    WHO_AM_I = 0x0F # r
    WHO_AM_I_OK = 0xD4 #r
    CTRL_REG1_G = 0x20 # rw
    CTRL_REG2_G = 0x21 # rw
    CTRL_REG3_G = 0x22 # rw
    CTRL_REG4_G = 0x23 # rw
    CTRL_REG5_G = 0x24 # rw
    REFERENCE_G = 0x25 # rw
    STATUS_REG_G = 0x27 # r
    OUT_X_L_G = 0x28 # r
    OUT_X_H_G = 0x29 # r
    OUT_Y_L_G = 0x2A # r
    OUT_Y_H_G = 0x2B # r
    OUT_Z_L_G = 0x2C # r
    OUT_Z_H_G = 0x2D # r
    FIFO_CTRL_REG_G = 0x2E # rw
    FIFO_SRC_REG_G = 0x2F # r
    INT1_CFG_G = 0x30 # rw
    INT1_SRC_G = 0x31 # r
    INT1_TSH_XH_G = 0x32 # rw
    INT1_TSH_XL_G = 0x33 # rw
    INT1_TSH_YH_G = 0x34 # rw
    INT1_TSH_YL_G = 0x35 # rw
    INT1_TSH_ZH_G = 0x36 # rw
    INT1_TSH_ZL_G = 0x37 # rw
    INT1_DURATION_G = 0x38 # rw
    RANGE_G = {'245DPS': (0b00 << 4), '500DPS': (0b01 << 4), '2000DPS': (0b10 << 4)}
    CAL_G = {'245DPS': (245.0/32768.0), '500DPS': (500.0/32768.0), '2000DPS': (2000.0/32768.0)}

