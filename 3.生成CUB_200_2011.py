import pandas as pd
df = pd.read_excel('D:\\data\\total.xlsx')
names = df['dcm_name'].values.tolist()
tumor_nature = df['tumor_nature'].values.tolist()


# 1、images文件夹
import os
import shutil
import pandas as pd

def copy_images_based_on_dataframe(df, source_folder, target_folder):
    # 遍历 DataFrame 中的每一行
    for index, row in df.iterrows():
        file_name = row['dcm_name'][:-4] + ".png"  # 获取文件名
        target_subfolder = row['tumor_nature']  # 获取目标子文件夹名称

        if row['tumor_nature'] == 0:
            target_subfolder = "000.no_tumor"
        else:
            target_subfolder = "001.tumor"

        # 构建源文件和目标文件夹路径
        source_file_path = os.path.join(source_folder, file_name)
        target_subfolder_path = os.path.join(target_folder, target_subfolder)

        # 创建目标子文件夹（如果不存在）
        os.makedirs(target_subfolder_path, exist_ok=True)

        # 复制文件到目标子文件夹
        shutil.copy2(source_file_path, target_subfolder_path)
        print(f"已复制: {file_name} 到 {target_subfolder_path}")


source_folder = 'D:\\data\\pngs-all(V3)'  # 替换为源文件夹路径
target_folder = 'D:\\project\\WS-DAN\\datasets\\CUB_200_2011(V3)\\images'  # 替换为目标文件夹路径

copy_images_based_on_dataframe(df, source_folder, target_folder)



# 2、classes.txt
# 不用改

# # 3、image_class_labels.txt
# def generate_file_lines1(n):
#     lines = []
#     for i in range(1, n+1):
#         # 动态生成每一行的内容

#         if tumor_nature[i-1] == 1:
#             c = '2'
#         else:
#             c = '1'
#         line = f"{i} {c}"
#         lines.append(line)
#     return lines

# # 指定需要生成多少行
# num_lines = len(names)  # 假设你要生成100行

# # 获取生成的内容
# file_lines = generate_file_lines1(num_lines)

# # 将内容写入 txt 文件
# with open("./datasets/CUB_200_2011(V2)/image_class_labels.txt", "w") as file:
#     for line in file_lines:
#         file.write(line + "\n")

# print(f"{num_lines}行内容已成功写入文件")


# # 4、images.txt
# def generate_file_lines2(n):
#     lines = []
#     for i in range(1, n+1):
#         # 动态生成每一行的内容

#         if tumor_nature[i-1] == 1:
#             c = '001.tumor/' + names[i-1][:-4] + '.png'
#         else:
#             c = '000.no_tumor/' + names[i-1][:-4] + '.png'
#         line = f"{i} {c}"
#         lines.append(line)
#     return lines

# # 指定需要生成多少行
# num_lines = len(names)  # 假设你要生成100行

# # 获取生成的内容
# file_lines = generate_file_lines2(num_lines)

# # 将内容写入 txt 文件
# with open("./datasets/CUB_200_2011(V2)/images.txt", "w") as file:
#     for line in file_lines:
#         file.write(line + "\n")

# print(f"{num_lines}行内容已成功写入文件")




# # 5、train_test_split.txt(1代表训练集，0代表测试集)
# def generate_file_lines(n):
#     lines = []
#     for i in range(1, n+1):
#         # 动态生成每一行的内容

#         if i <= 3798:  # train
#             c = '0'
#             # if names[i-1].endswith("-00-000000.dcm") or names[i-1].endswith("-L.dcm") or names[i-1].endswith("-R.dcm"):
#             #     c = '0'
#         elif i <= 4815:  # val
#             c = '0'
#         elif i <= 5881:  # test 1017 + 49
#             c = '0'
#         elif i <= 6468:  # test 587
#             c = '0'
#         else:            # test 5585
#             c = '0'
#         line = f"{i} {c}"
#         lines.append(line)
#     return lines

# # 指定需要生成多少行
# num_lines = len(names)  # 假设你要生成100行

# # 获取生成的内容
# file_lines = generate_file_lines(num_lines)

# # 将内容写入 txt 文件
# with open("./datasets/CUB_200_2011(V2)/train_test_split(all).txt", "w") as file:
#     for line in file_lines:
#         file.write(line + "\n")

# print(f"{num_lines}行内容已成功写入文件")


# # # 6、masks.txt
# def generate_file_lines6(n):
#     lines = []
#     for i in range(1, n+1):
#         # 动态生成每一行的内容

#         if  names[i-1].endswith("-L.dcm") or names[i-1].endswith("-R.dcm") or names[i-1].endswith("-D.dcm"):
#             c = 'masks/' + names[i-1][:-4] + '.png'
#         else:
#             c = 'masks/' + names[i-1][:-14] + '.png'
#         line = f"{i} {c}"
#         lines.append(line)
#     return lines

# # 指定需要生成多少行
# num_lines = len(names)  # 假设你要生成100行

# # 获取生成的内容
# file_lines = generate_file_lines6(num_lines)

# # 将内容写入 txt 文件
# with open("./datasets/CUB_200_2011(V2)/masks.txt", "w") as file:
#     for line in file_lines:
#         file.write(line + "\n")

# print(f"{num_lines}行内容已成功写入文件")


