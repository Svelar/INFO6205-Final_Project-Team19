# !/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import numpy as np

TOTAL_W = 800  # area's width
TOTAL_H = 500  # area's height
DANGER_DIS = 35  # when distance closer than this, may be infected

# Infection Rate -COVID-19
#
COV_R0 = 5.7
COV_K = 0.01
COV_S = COV_R0 / 80  # 7.125%
COV_EV = 0.9  # mRNA vaccine effectiveness

# Diagnose Rate
Diagnose_Rate = 0.9
# Death Rate
DEATH_Rate = 0.05
# People amount settings
TOTAL_NUM = 500
INFECTED_NUM = 1
# random.randint(0, total_num)
HEALTHY_NUM = TOTAL_NUM - INFECTED_NUM
MASKED_RATE = 0.5  # rate of people wear masks

VIRUS_LATENCY = 7

# IR_WW = 0.9  # The infection rate of both without a mask
# IR_MM = 0.01  # both with a mask
# IR_WM = 0.5  # the infected without a mask，the healthy with
# IR_MW = 0.3  # the infected with a mask，the healthy without
#
# INFECTED_RATE = [[IR_WW * COV_S, IR_MW * COV_S], [IR_WM * COV_S, IR_MM * COV_S]]
# # the healthy with vaccine
# INFECTED_RATE_WITH_VACCINE = [[IR_WW * COV_S * (1 - COV_EV), IR_MW * COV_S * (1 - COV_EV)],
#                               [IR_WM * COV_S * (1 - COV_EV), IR_MM * COV_S * (1 - COV_EV)]]
#
# VACCINE_RATE = 0.4  # rate of people get vaccine



# Infection Rate -SARS
SARS_R0 = 3
SARS_S = SARS_R0/80 #3.75%
IR_WW = 0.9  # The infection rate of both without a mask
IR_MM = 0.01  # both with a mask
IR_WM = 0.5  # the infected without a mask，the healthy with
IR_MW = 0.3  # the infected with a mask，the healthy without
#
INFECTED_RATE = [[IR_WW*SARS_S, IR_MW*SARS_S], [IR_WM*SARS_S, IR_MM*SARS_S]]
# no vaccine
INFECTED_RATE_WITH_VACCINE = INFECTED_RATE
VACCINE_RATE = 0
