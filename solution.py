import pandas as pd
import numpy as np
import scipy.stats as stats


chat_id = 422633669 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    x_rate = x_success / x_cnt
    y_rate = y_success / y_cnt
    
    x_se = np.sqrt(x_rate * (1 - x_rate) / x_cnt)
    y_se = np.sqrt(y_rate * (1 - y_rate) / y_cnt)
    
    z = (x_rate - y_rate) / np.sqrt(x_se**2 + y_se**2)
    
    critical_value = 2.576
    
    return z > critical_value
