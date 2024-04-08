import os
import zipfile
import re
import pandas as pd

# 文件解压缩
# 指定文件夹路径
# folder_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Report'  # 替换为包含压缩包的文件夹路径
# output_folder = r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Report'  # 解压缩后的目标文件夹路径
#
# # 遍历文件夹中的文件
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         file_path = os.path.join(root, file)
#
#         # 判断文件是否为ZIP文件
#         if zipfile.is_zipfile(file_path):
#             # 判断文件名是否包含"2022_2023"字符段
#             if "2022_2023" not in file:
#                 try:
#                     os.remove(file_path)  # 删除文件
#                     print(f"删除文件：{file_path}")
#                 except Exception as e:
#                     print(f"删除文件 {file_path} 时出现错误: {str(e)}")
#             else:
#                 # 解压缩包到指定文件夹
#                 with zipfile.ZipFile(file_path, 'r') as zip_ref:
#                     zip_ref.extractall(output_folder)
#                     print(f"解压缩文件：{file_path}")
#         else:
#             try:
#                 os.remove(file_path)  # 删除非ZIP文件
#                 print(f"删除非ZIP文件：{file_path}")
#             except Exception as e:
#                 print(f"删除非ZIP文件 {file_path} 时出现错误: {str(e)}")
#
# print("删除和解压缩完成")

# 文件改名，将ZIP改为PDF
# for filename in os.listdir(folder_path):
#     if filename.endswith('.zip'):
#         new_name = os.path.splitext(filename)[0] + '.pdf'  # 将扩展名从ZIP改为PDF
#         old_path = os.path.join(folder_path, filename)
#         new_path = os.path.join(folder_path, new_name)
#
#         # 重命名文件
#         os.rename(old_path, new_path)
#         print(f"重命名文件：{filename} -> {new_name}")
#
# print("重命名并改扩展名完成")


# 设置文件路径
data_file_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Data\MCAP31122023.xlsx'
link_file_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Download_Link.xlsx'
output_file_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\output.csv'
folder_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Report'

# 读取xlsx文件到DataFrame
data_df = pd.read_excel(data_file_path)
link_df = pd.read_excel(link_file_path)

# 创建一个空的DataFrame来存储结果

result_df = pd.DataFrame(columns=['Symbol', 'Company Name', 'Report URL'])

# 遍历文件夹中的PDF文件
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        symbol = os.path.splitext(filename)[0]  # 获取文件名（公司symbol）

        # 查找符合公司symbol的行
        company_row = data_df[data_df['Symbol'] == symbol]

        # 如果找到匹配的公司
        if not company_row.empty:
            company_name = company_row.iloc[0]['Company Name']

            # 查找符合公司名称的链接
            link_row = link_df[link_df['Company Name'] == company_name]

            # 如果找到匹配的链接
            if not link_row.empty:
                report_url = link_row.iloc[0]['Report URL']
                result_df = pd.concat([result_df, pd.DataFrame(
                    {'Symbol': symbol, 'Company Name': company_name, 'Report URL': report_url}, index=[0])],
                                      ignore_index=True)

# 将结果保存为CSV文件
result_df.to_csv(output_file_path, index=False)

print("任务完成，结果已保存到output.csv")
