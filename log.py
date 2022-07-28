from datatime import datatime as dt
from time import time



def result_racional_logger(data):
    time = dt.now().strftime("%H:%M")
    with open('log.csv', 'a') as file:
        file.write('{}; result_racional; {}'.format(time, data))

def result_compl_logger(data):
    time = dt.now().strftime("%H:%M")
    with open('log.csv', 'a') as file:
        file.write('{}; result_compl; {}'.format(time, data))
