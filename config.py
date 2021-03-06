# !/usr/bin/env python
# -*- coding: utf-8 -*-

TOTAL_W = 800  # area's width
TOTAL_H = 500  # area's height
DANGER_DIS = 35  # when distance closer than this, may be infected


###
###
# Infection Rate -COVID-19
COV_R0 = 5.7
COV_K = 0.1
COV_S = COV_R0 / 80  # 7.125%
COV_S1 = COV_S * 0.8 / COV_K #super spreader (s*0.8)/k
COV_S2 = COV_S * 0.2 / (1 - COV_K) #normal spreader (s*0.2)/(1-k)
COV_EV = 0.9  # mRNA vaccine effectiveness
IR_WW = 0.9  # The infection rate of both without a mask
IR_MM = 0.01  # both with a mask
IR_WM = 0.5  # the infected without a mask，the healthy with
IR_MW = 0.3  # the infected with a mask，the healthy without
# rate of becoming super spreader
SUPER_RATE = COV_K
#normal spreader
INFECTED_RATE = [[IR_WW * COV_S2, IR_MW * COV_S2], [IR_WM * COV_S2, IR_MM * COV_S2]]
# the healthy with vaccine
INFECTED_RATE_WITH_VACCINE = [[IR_WW * COV_S2 * (1 - COV_EV), IR_MW * COV_S2 * (1 - COV_EV)],
                              [IR_WM * COV_S2 * (1 - COV_EV), IR_MM * COV_S2 * (1 - COV_EV)]]
VACCINE_RATE = 0.2  # rate of people get vaccine
# infected rate of super spreader
INFECTED_RATE_SUPER = [[IR_WW * COV_S1, IR_MW * COV_S1], [IR_WM * COV_S1, IR_MM * COV_S1]]
# the healthy with vaccine
INFECTED_RATE_WITH_VACCINE_SUPER = [[IR_WW * COV_S1 * (1 - COV_EV), IR_MW * COV_S1 * (1 - COV_EV)],
                              [IR_WM * COV_S1 * (1 - COV_EV), IR_MM * COV_S1 * (1 - COV_EV)]]
###
###
###



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


###
###
# Infection Rate -SARS
# SARS_R0 = 3
# SARS_K = 0.1
# SARS_S = SARS_R0/80 #3.75%
# SARS_S1 = SARS_S * 0.8 / SARS_K #super spreader (s*0.8)/k
# SARS_S2 = SARS_S * 0.2 / (1 - SARS_K) #normal spreader (s*0.2)/(1-k)
# SUPER_RATE = SARS_K
# IR_WW = 0.9  # The infection rate of both without a mask
# IR_MM = 0.01  # both with a mask
# IR_WM = 0.5  # the infected without a mask，the healthy with
# IR_MW = 0.3  # the infected with a mask，the healthy without
# INFECTED_RATE = [[IR_WW * SARS_S2, IR_MW * SARS_S2], [IR_WM * SARS_S2, IR_MM * SARS_S2]]
# no vaccine
# INFECTED_RATE_WITH_VACCINE = INFECTED_RATE
#
# INFECTED_RATE_SUPER = [[IR_WW * SARS_S1, IR_MW * SARS_S1], [IR_WM * SARS_S1, IR_MM * SARS_S1]]
# the healthy with vaccine
# INFECTED_RATE_WITH_VACCINE_SUPER = INFECTED_RATE_SUPER
# VACCINE_RATE = 0
###
###