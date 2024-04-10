import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import json

# 读取 Excel 文件获取 URL 列以及公司名称和符号
# excel_path = r"D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\matched_companies.xlsx"
# df = pd.read_excel(excel_path)
# # 确保URL, Company Name, 和 Symbol列的名称与你的Excel文件中的实际列名称匹配
# urls = df['URL']
# company_names = df['Company Name']
# symbols = df['Symbol']
#
# # 初始化 HTTP 请求的头部
# hdr = {
#     'Cookie': 'visits=6; gdpr_userpolicy_eu=1; gdpr_region=eu; _w18g_gdpr_consent_data=personal_info_consent%3AY%23personalization_consent%3AY%23age_consent%3AY%23recommendation_adv_remarketting_consent%3AY%23adv_remarketting_consent%3AY%23marketting_communication_consent%3AY; A18ID=1700241178544.164364; _gcl_au=1.1.332455451.1700241179; _cb=CIlCKND2a_K4qgDui; WZRK_G=57a9e747c2e74a9280aefacb2587ba79; _w18g_consent=Y; __io=10b9e7344.12acd25a5_1703673960144; __io_r=mail.qq.com; __io_first_source=mail.qq.com; __io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22mail.qq.com%22%7D; _gid=GA1.2.801615192.1706521752; dtCookie=v_4_srv_6_sn_31E3A8B145A5A2765380BE57415F687B_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1; _io_ht_r=1; __io_unique_43938=29; isVistedCbPage=true; USR_DFP_TARGETING={"p_value":0,"dob":"","gender":"","income_data":"","occupation":"","industry":""}; nousersess=srxh27qqui66nsiq; _uzitok=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjc3JmIjoiZ2hhTUM5ZW9yYmdSdU5JbjczajJFUWc2QUFNanpxSzBTY1VEQXpLcTI2QzVCbWFNIiwiaWF0IjoxNzA2NTM0NzAwfQ.N0MA4oK_G484-N82HSR2MIKTtubhC_qAdp6OlY0v7yc; MC_PPID_LOGIC=0229d64202f3e21c2a3c893f014672ea; __io_lv=1706534706800; _abck=99C3D9D0B21D6519F2C3621F0E9C1BAD~0~YAAQlAUXAtwoU0eNAQAAfztmVQu+Bxol79VVzBaZRtOuVN2/EtDZ8qL0YLIuOai8Vyd9scF97sGkhTEh+QyRefO2xCVzGCvJCayYmgQkGq/Za9JNu+Ka7Aw8eLPMhyg+5jtW+AcbHRHILqdkqeHzFLQAL3yjxNb8wgfPOrUqoCQRKrBkzSwXfrCCbGz4R+4Kf84Bxn56mZhk1wXEug+LDGJya2RSXogcY/WVdsMlCovXbeDo73oQmNWIKSOk6zVvBngZdW0N+/M1wmcDFhOHoYy71NpE2iCZlc7yTrkLixqZfZ2fKzfnAmwbYHa78dWmKA2ATmTywTwKMFe5PRLPqNbetSpAv38qDXLzP0EtORneHX7euE80mVzql8TyIRD037vJLNlBx7H5I/RqTXA0zcaoCc7XeT8KbJn/TNSS~-1~-1~1706538367; ak_bmsc=36124D451347BE886D035E3B8CDD8AC4~000000000000000000000000000000~YAAQlAUXAvMoU0eNAQAA7jxmVRbfZ+nebzMPc/XdA78O/iXoPbp3NBT4n37LLV3rKo/+9WgM4hMxzxRD/N+CQUJA4s3KYZyroaXpA/ztGQfvIQo1nAB0eZOGh46PKwEQGqfT8wfeLrL5kbaSOWc5L0oPTupYIi9ERb0nzeCsE0NUdClFoI0quz2p9GEy/EBdYOhFx/zqB54SxYzoBelDprLhiodis0xbSxtDlr95nkzX6hftIwIla+xbIqighmpJYQS5A/sFwxyCD4IoISDYFyJ2nZ5O8/bwhccHLH78aHZwtuZKRuAdT4VxK7JdzmBKnslVAho8J3v3+O8m3RPHOynnC/84oQ68XgT2tW1cFcVf1eMJWOM+D9bm5K8qRHdWQ5NOCcCkPbhaKeErckYO5P4vuquLU+Vq/cSVGTGYgFOOtJrErBpB6K+VXIZ0+2eOZXx0jIfCM48iBTLUvqncCJXEhy3Bgv9yLKv9nfG2KtFOBNpXJMlaNNsiDfaEYDpx7ZzIBi/s; verify=%24%24%23%23%24%241; nnmc=Charon+Li; UIDHASH=d9025f4728fc800e6e6395a4c431df9a58beafc2e7099f2adc47c8d5cc42d3c3; token-normal=qiAfBsg1Cu5dRhiBfqdRHTID5g3HC2zR1ZzGowKN6WJcxE7wZaSXXBVCbjawY-FzSmEyjANFm7d_gJcmGCkgmw; DEF_VIEW=4; tvuid=VlZoa1EycDJSMEY1TWc9PQ%3D%3D; mcpro=0; gdpr_consent_cookie=UXdCjvGAy2; bm_sv=1D9CA9D19716327EDD436D6249E5FA8E~YAAQlAUXAgEsU0eNAQAAZV9mVRaHyaSziBa72Jh5DyiuVVCVp/CPtHiBqHEd3jIVheHz1nSRT61irBkWwcwt1I8PQgF74PI1yIo9NUfQcpz5WfLNaYjftPf3zJkMj6XXC1TNyvmPN4VBvXXPuuDUByr77qKQaFV8uFP7AiWrtFMki3/uq3c5eiTqIzo66WKAUabMqFOyugaPr/2CSQ+1vftkVMrSBsl4jrAIjYCv1LEQ7g62Na3eHh5ydNKbsfKKe2pMot2/~1; PHPSESSID=oeqlat69bun9aba62rtjef1p06; MC_WAP_INTERSTITIAL_NEW_LOGIC_20240129={"0":"https://www.moneycontrol.com/financials/a&mfebcon/consolidated-ratiosVI/F03#F03","1":"https://www.moneycontrol.com/financials/a&mfebcon/ratiosVI/F03#F03","2":"https://www.moneycontrol.com/financials/indianrailwayfinancecorporation/ratiosVI/IRF#IRF","3":"https://www.moneycontrol.com/india/stockpricequote/infrastructure-general/abinfrabuild/I07"}; _ga_4S48PBY299=GS1.1.1706534312.22.1.1706541378.0.0.0; _ga=GA1.1.270074858.1700241157; _gat=1; stocks=|A.B.Infrabuild_I12~6%7CN_JB02%7E9%7CN_F04%7E7%7CIndian.Railway_IRF%7E2%7CReliance_RI%7E2%7CN_SGBOC5960%7E1%7C3M.India_B3M%7E14%7CIWML_IIFLW54277%7E14%7CAdani.Energy_AT18%7E2%7CZydus.Wellness_CNA%7E6; _chartbeat2=.1700241187999.1706541379308.0011101011100001.BUEGETHSzyoQjpMF2llIODGa_1O.1; _cb_svref=external; WZRK_S_86Z-5ZR-RK6Z=%7B%22p%22%3A33%2C%22s%22%3A1706536123%2C%22t%22%3A1706541385%7D',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
# }
#
# # CSV 文件的路径和表头
# csv_filename = r"D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\matched1_companies.xlsx"
# headers = ['Company_Name', 'Revenue', 'Net Profit', 'EPS', 'BVPS', 'ROE', 'NIM', 'Debt to Equity']
#
# # 存储所有公司的财务数据
# all_financial_data = []
#
# # 遍历所有 URL
# for URL, company_name, symbol in zip(urls, company_names, symbols):
#     try:
#         resp = requests.get(URL, headers=hdr)
#         soup = BeautifulSoup(resp.text, 'html.parser')
#
#         # 获取公司名称（使用Excel中的公司名称）
#         Company_Name = company_name
#
#         # 查找并解析财务数据
#         data_div = soup.find('div', id='S-12-graph')
#         financial_data = {}
#         if data_div:
#             json_data = json.loads(data_div.text)
#             headings = ['Revenue', 'Net Profit', 'EPS', 'BVPS', 'ROE', 'NIM', 'Debt to Equity']
#             for heading in headings:
#                 for item in json_data:
#                     if item['heading'] == heading:
#                         for record in item['data']:
#                             if record['year'] == '2023':
#                                 financial_data[heading] = record['value']
#                                 break
#
#         # 添加公司财务数据到列表
#         all_financial_data.append([
#             Company_Name,
#             financial_data.get('Revenue', 'N/A'),
#             financial_data.get('Net Profit', 'N/A'),
#             financial_data.get('EPS', 'N/A'),
#             financial_data.get('BVPS', 'N/A'),
#             financial_data.get('ROE', 'N/A'),
#             financial_data.get('NIM', 'N/A'),
#             financial_data.get('Debt to Equity', 'N/A')
#         ])
#
#     except Exception as e:
#         print(f"Error processing {company_name} ({symbol}): {e}")
#
#
# # 写入CSV文件
# with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(headers)  # 写入表头
#     csvwriter.writerows(all_financial_data)  # 写入所有公司数据





# csv_filename = r"D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\All_Companies_Financial_Data.csv"
# df_csv = pd.read_csv(csv_filename)
#
# # 初始化一个列表来存储符合条件的公司名称
# companies_with_mostly_na_names = []
# # 检查每一行
# for index, row in df_csv.iterrows():
#     # 计算非数字（'N/A'）的数量
#     # print(row)
#     na_count = (row == -10000000).sum()
#     # 如果'N/A'的数量超过4，添加到列表中
#     if na_count == 7 :
#         companies_with_mostly_na_names.append(row['Company_Name'])
#
#
# df = pd.read_excel('D:\\Program Files (x86)\\Python\\PythonProject\\FYP\\Financial Report\\Data_List.xlsx')
#
# # 找到与companies_with_mostly_na_names匹配的公司名称
# matched_companies = df[df['Company Name'].isin(companies_with_mostly_na_names)]
#
# # 你可以选择打印这些公司，也可以保存到新的Excel文件
# # print(matched_companies)
#
# # 如果你想保存到一个新的Excel文件，并指定路径
# matched_companies.to_excel('D:\\Program Files (x86)\\Python\\PythonProject\\FYP\\Financial Report\\matched_companies.xlsx', index=False)


# all_companies = pd.read_csv('D:\\Program Files (x86)\\Python\\PythonProject\\FYP\\Financial Report\\All_Companies_Financial_Data.csv')
# matched_companies = pd.read_csv('D:\\Program Files (x86)\\Python\\PythonProject\\FYP\\Financial Report\\matched1_companies.csv')
#
# # 确保 Company_Name 作为索引
# all_companies.set_index('Company_Name', inplace=True)
# matched_companies.set_index('Company_Name', inplace=True)
#
# # 使用 matched_companies 更新 all_companies
# all_companies.update(matched_companies)
#
# # 重置索引，如果你想要 Company_Name 再次作为一个列
# all_companies.reset_index(inplace=True)
#
# # 保存更新后的数据到一个新的CSV文件
# all_companies.to_csv('D:\\Program Files (x86)\\Python\\PythonProject\\FYP\\Financial Report\\All_Companies_Financial_Data.csv', index=False)


# # 读取Excel和CSV文件
# data_list_df = pd.read_excel('D:\\Program Files (x86)\\Python\\PythonProject\\FYP\\Financial Report\\Data_List.xlsx')
# all_companies_df = pd.read_csv('D:\\Program Files (x86)\\Python\\PythonProject\\FYP\\Financial Report\\All_Companies_Financial_Data.csv')
#
# # 确保两个DataFrame中的公司名称列的名称匹配，为了简化操作，我们可以先重命名其中一个DataFrame的列
# data_list_df.rename(columns={'Company Name': 'Company_Name'}, inplace=True)
#
# # 创建一个映射，将公司名称映射到Symbol
# symbol_mapping = data_list_df.set_index('Company_Name')['Symbol'].to_dict()
#
# # 在all_companies_df中添加一个新列'Symbol'，使用map函数根据公司名称映射Symbol值
# all_companies_df['Symbol'] = all_companies_df['Company_Name'].map(symbol_mapping)
#
# # 保存更新后的DataFrame到CSV文件
# all_companies_df.to_csv('D:\\Program Files (x86)\\Python\\PythonProject\\FYP\\Financial Report\\Updated_All_Companies_Financial_Data_with_Symbol.csv', index=False)
