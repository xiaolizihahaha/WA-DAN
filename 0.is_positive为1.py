import pandas as pd

# 假设df是你的DataFrame
df0 = pd.read_excel("D:\\data\\new_train.xlsx")  # 示例：从CSV文件加载数据
names0 =  df0[(df0['tumor_nature'] == 1) & (df0['is_positive'] == 1)]['dcm_name'].tolist()
names = [name[:-4] + '-00-000000.dcm' for name in names0]
print(len(names))
df = pd.read_excel("D:\\data\\total0.xlsx")  # 示例：从CSV文件加载数据


# 创建布尔掩码，标识dcm_name在names列表中的行
mask = df['dcm_name'].isin(names)

# 计算满足条件的行数
matching_rows_count = mask.sum()

print(f"满足条件的行数: {matching_rows_count}")

# 筛选出dcm_name在names列表中的行，并将is_positive列设置为1
df.loc[df['dcm_name'].isin(names), 'positive'] = 1

df.to_excel('D:\\data\\modified_df.xlsx', index=False)



# import os
# name = "D:\\data\\test4-18"
# files = os.listdir(name)
# count = 0
# for f in files:
#     if f.endswith("-01-000000.png"):
#         count += 1
#         file_path = os.path.join(name, f)  # 关键修复：拼接完整路径
#         os.remove(file_path)
# print(count)