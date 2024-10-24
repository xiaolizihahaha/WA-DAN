import os
import pandas as pd

def list_files_to_dataframe(folder_path):
    """
    将指定文件夹中的所有文件按名称顺序写入到 DataFrame 中。

    :param folder_path: 文件夹路径
    :return: 包含文件名的 DataFrame
    """
    # 获取文件夹中的所有文件名，并按名称排序
    files = sorted(os.listdir(folder_path))
    
    # 创建 DataFrame
    df = pd.DataFrame(files, columns=['dcm_name'])
    df.to_excel("1.xlsx",index=False)
    
    return df

# 示例用法
folder_path = "D:\\project\\BBN\\pngs-data-pro(V2)"
df = list_files_to_dataframe(folder_path)

