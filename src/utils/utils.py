import random
import time
import json

def sleep_random(time_config):
    min_time = time_config["min"]
    max_time = time_config["max"]
    time.sleep(random.uniform(min_time, max_time))
    
def read_random_lines(file_path, num_lines=10):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    random_lines = random.sample(lines, num_lines)
    return [line.strip() for line in random_lines]

def read_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)