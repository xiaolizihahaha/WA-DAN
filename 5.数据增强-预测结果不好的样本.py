import pandas as pd

# # 计算预测正确的次数，存到times列，运行一次即可
# df = pd.read_excel('D:/data/predictions_filtered.xlsx')

# def calculate_times(row):

#     values = row[['裁剪后无mask’', '裁剪后有mask’', '裁剪前无mask’', '裁剪前有mask’', '裁剪前有mask1’', '裁剪前有mask1 互换’']].values
#     if row['tumor_nature'] == 1:
#         return sum(values == 1)
#     else:
#         return sum(values == 0)

# df['times’'] = df.apply(calculate_times, axis=1)
# df.to_excel('D:/data/predictions_filtered1.xlsx', index=False)




# # # 将预测结果不好的样本单独提出来，形成excel，运行一次即可
# df = pd.read_excel('D:/data/predictions_filtered.xlsx')
# filtered_df = df[df['age'].notna() & (df['times'] > 3)]
# filtered_df.to_excel('D:/data/predictions_filtered1.xlsx', index=False)



# # # 为这些预测结果不好的样本做数据增强，保存到temp中，运行一次即可
# import pandas as pd
# from PIL import Image
# import os
# from PIL import ImageEnhance

# # 4、对比度1.5
# def adjust_contrast(input_path, output_path, factor=1.5):
#     img = Image.open(input_path)
#     enhancer = ImageEnhance.Contrast(img)
#     contrast_img = enhancer.enhance(factor)
#     contrast_img.save(output_path)

# df = pd.read_excel("D:/data/predictions_filtered.xlsx")
# dcm_names = df['dcm_name'].values.tolist()

# for i in range(len(dcm_names)):
#     input_path = "D:\\data\\pngs-all(V1)\\" + dcm_names[i][:-4] + ".png" 


#     # # 对比度1.5
#     output_path = "D:\\data\\pngs_temp(V1)\\" + dcm_names[i][:-4] + ".png" 
#     adjust_contrast(input_path, output_path)
#     print(f"图片已保存为: {output_path}")


# copy图像
import os
import shutil
names = ['C20003_0000779-Anonymized-202007061434-D-R.dcm', 
'C16004A_0000641-Anonymized-202107310751-D-R.dcm', 
'C16002A_0000056-Anonymized-202106230938-D-R.dcm', 
'C20004D_0000077-Anonymized-202007231444-D-R.dcm', 
'C20004_0000554-Anonymized-202005260952-D-R.dcm', 
'C20004A_0000435-Anonymized-202006111857-D-R.dcm', 
'C19002B_0000135-Anonymized-202106101012-D-L.dcm', 
'C16002A_0000009-Anonymized-202106220752-D-L.dcm', 
'C20004_0000042-Anonymized-202005151505-D-L.dcm', 
'C20004B_0000459-Anonymized-202007040945-D-R.dcm', 
'C19004A_0001348-Anonymized-202104301636-D-L.dcm', 
'C20004_0000530-Anonymized-202005251602-D-L.dcm', 
'C16002_0000200-Anonymized-202105220956-D-R.dcm', 
'C16004A_0000518-Anonymized-202107280932-D-L.dcm', 
'C19004A_0000824-Anonymized-202104130810-D-L.dcm', 
'C20004B_0000394-Anonymized-202007021638-D-R.dcm', 
'C19002B_0000361-Anonymized-202106211451-D-R.dcm', 
'C20003B_0000079-Anonymized-202008101510-D-R.dcm', 
'C20003_0000811-Anonymized-202007071414-D-R.dcm', 
'C20004E_0000100-Anonymized-202008031703-D-R.dcm']

# 文件夹路径
folder_A = 'D:\\data\\pngs-all(V3)'
folder_B = 'D:\\data\\pngs_temp(V3)'
folder_C = 'D:\\data\\temp'


# 确保目标文件夹C存在
if not os.path.exists(folder_C):
    os.makedirs(folder_C)

# 遍历文件名称列表
for file_name in names:
    # 在文件夹A中查找文件
    file_name = file_name[:-4] + '.png'
    file_A_path = os.path.join(folder_A, file_name)
    if os.path.exists(file_A_path):
        # 复制到文件夹C并重命名
        shutil.copy(file_A_path, os.path.join(folder_C, file_name[:-4] + 'A' + '.png'))

    # 在文件夹B中查找文件
    file_B_path = os.path.join(folder_B, file_name)
    if os.path.exists(file_B_path):
        # 复制到文件夹C并重命名
        shutil.copy(file_B_path, os.path.join(folder_C, file_name[:-4] + 'B' + '.png'))

print("文件复制完成")



