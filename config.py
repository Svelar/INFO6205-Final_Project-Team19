import random

# 有关参数的定义
import numpy as np

TOTAL_W = 500  # 模拟场地总宽度
TOTAL_H = 400  # 模拟场地总高度
DANGER_DIS = 50  # 传染距离

# 感染率
# W = without Mask 不带口罩
# M = Mask 带口罩
# IR Infection Rate 传染率
# 前面的是 患者是否戴口罩
# 后面的是 健康是否戴口罩
# 值表示的是健康人员的传染概率

IR_WW = 0.8  # 双方都不带口罩的传染率
IR_MM = 0.01  # 双方都戴口罩的传染率
IR_WM = 0.3  # 患病一方不戴口罩，健康者戴口罩
IR_MW = 0.15  # 患病一方戴口罩，健康者不戴口罩
INFECTED_RATE = [[0.8, 0.15], [0.3, 0.01]]
# 打了疫苗的
INFECTED_RATE_WITH_VACCINE = [[0.8, 0.15], [0.3, 0.01]]

# 成功确诊率
Diagnose_Rate = 0.9
# 死亡率
DEATH_Rate = 0.05

# 实验的人数参数设定
total_num = 100
infected_num = random.randint(0, total_num)  # 这里以随机数确定起始感染人数
healthy_num = total_num - infected_num
masked_rate = 0.5  # 戴口罩的比例
vaccine_rate = 0.5
