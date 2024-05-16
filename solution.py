import pandas as pd
import numpy as np
import scipy.stats as stats


chat_id = 422633669 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    diff = x_success / x_cnt - y_success / y_cnt
    std_dev = (x_success / x_cnt * (1 - x_success / x_cnt) / x_cnt + y_success / y_cnt * (1 - y_success / y_cnt) / y_cnt)**0.5
    z_score = diff / std_dev
    p_value = stats.norm.cdf(z_score)
    
    return p_value < 0.05
