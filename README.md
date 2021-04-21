# INFO6205-Final_Project
### Instruction

1. The simulation of the spread of COVID-19 based on turtle, the program logic is relatively simple and understandable.
2. Most IDE will automatically install dependencies and packages.
3. To execute this program, run 'main .py'.
4. All configured information is in 'config .py'. Include R0, K factors and rate of mask and vaccine...
5. If you want to watch simulation of SARS, modify parameters in 'config.py' by commenting COVID block and canceling comments on SARS block.![image-20210421113308951](https://tva1.sinaimg.cn/large/008i3skNly1gprsdtxgynj316u0u00zi.jpg)![image-20210421113347317](https://tva1.sinaimg.cn/large/008i3skNly1gprsegdi9tj31ix0u078w.jpg)
6. Nothing to do with 'person.py'.
7. Unit tests are in test directory. Just run it.
8. Object Oriented Design
   - Property：
     - `total_num`：The amount of people
     - `infected_num`：The amount of the infected
     - `status`：Healthy status
     -  `infected_day`：Day of ill. >4 days There is a certain probability of changing to diagnosed, >7 days, there is a certain probability of death.
     -  `mask` `vaccine`: Mask and vaccine
   - Method:
     - `__init__`：Define object
     - `move`：Person move randomly.
     - `infect`：Closer than social distance, there are different probabilities of infection.
     - `day`：If the person is sick, call this function and the number of sick days +1, when the sick days are greater than the shortest incubation period, a certain probability will be converted to a diagnosis, and after the shortest death period, a certain probability of death
9. Turtle title can display the current number of days, the number of infections, the number of deaths, and the total number of people