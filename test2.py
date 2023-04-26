import math

with open('fyx_chinamoney.csv', 'r') as f:
    code_list = f.readline().split(',') 
    batch_size = 80
    num_batches = len(code_list) // batch_size + (len(code_list) % batch_size > 0) # 计算批次数
for i in range(num_batches):
    batch_start = i * batch_size
    batch_end = (i + 1) * batch_size
    print(code_list[batch_start:batch_end]) 