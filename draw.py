import os
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import json

# 文件夹路径
base_dir = '/workspace/VBench/evaluation_results'
# 类别名字列表
categories = [
    "subject_consistency", "background_consistency", "aesthetic_quality",
    "imaging_quality", "object_class", "multiple_objects", "color",
    "spatial_relationship", "scene", "temporal_style", "overall_consistency",
    "human_action", "temporal_flickering", "motion_smoothness", "dynamic_degree",
    "appearance_style"
]
# 正则表达式匹配ckpt文件夹
ckpt_pattern = re.compile(r'checkpoint-(\d+)')

# 初始化一个字典来存储每个类别的分数和时间点
data = {category: [] for category in categories}

# 遍历base_dir中的每个文件夹
for folder in os.listdir(base_dir):
    match = ckpt_pattern.match(folder)
    if match:
        # 提取时间点
        time_point = int(match.group(1))
        folder_path = os.path.join(base_dir, folder)
        
        # 遍历该文件夹中的每个txt文件
        for file_name in os.listdir(folder_path):
            if file_name.endswith('_eval_results.json'):
                file_path = os.path.join(folder_path, file_name)
                
                with open(file_path, 'r') as file:
                    result = json.load(file)
                    #import pdb; pdb.set_trace()
                    for key, value in result.items():
                        category = key
                        score = value[0]
                    
                        # 只处理在给定类别名单中的类别
                        if category in data:
                            data[category].append((time_point, score))
                            
# 为每个类别创建一个PDF文件并绘制图像
for category, values in data.items():
    if values:
        values.sort()  # 按时间点排序
        times, scores = zip(*values)
        
        plt.plot(times, scores, label=category)
        
plt.xlabel('timestep')
plt.ylabel('score')
plt.legend()

plt.savefig('result.pdf', format='pdf')
plt.close()
