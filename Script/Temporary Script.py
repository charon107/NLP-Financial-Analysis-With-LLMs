# # import os
# # import pandas as pd
# #
# # # 指定CSV文件路径
# # csv_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\All_Companies_Financial_Data.csv'
# #
# # # 指定文件夹路径
# # folder_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Data\Report_PDF'
# #
# # # 读取CSV文件
# # df = pd.read_csv(csv_path)
# #
# # # 获取Symbol列的所有值，并转换为集合，以便快速查找
# # symbols_in_csv = set(df['Symbol'])
# #
# # # 获取文件夹中所有文件的名称（去掉.pdf后缀），同样转换为集合
# # files_in_folder = {file.replace('.pdf', '') for file in os.listdir(folder_path) if file.endswith('.pdf')}
# #
# # # 查找数据库中有但文件夹中没有的Symbol
# # missing_files = symbols_in_csv - files_in_folder
# # if missing_files:
# #     print("Symbols in the database but missing in the folder:")
# #     for symbol in missing_files:
# #         print(symbol)
# #
# # # 查找文件夹中有但数据库中没有的Symbol
# # extra_files = files_in_folder - symbols_in_csv
# # if extra_files:
# #     print("Files in the folder but missing in the database:")
# #     for symbol in extra_files:
# #         print(symbol)
# #
# # if not missing_files and not extra_files:
# #     print("All files match the database symbols.")
# # import os
# # import fitz  # PyMuPDF库
#
# # # 指定PDF文件夹路径和目标文本文件夹路径
# # pdf_folder_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Data\Report_PDF'
# # text_folder_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Data\Report_Txt'
# #
# # # 确保目标文本文件夹存在，如果不存在则创建
# # if not os.path.exists(text_folder_path):
# #     os.makedirs(text_folder_path)
# #
# # # 遍历PDF文件夹中的PDF文件
# # for filename in os.listdir(pdf_folder_path):
# #     if filename.endswith('.pdf'):
# #         pdf_file_path = os.path.join(pdf_folder_path, filename)
# #
# #         # 使用PyMuPDF库打开PDF文件
# #         pdf_document = fitz.open(pdf_file_path)
# #
# #         # 遍历PDF页面并提取文本内容
# #         text = ""
# #         for page_num in range(pdf_document.page_count):
# #             page = pdf_document[page_num]
# #             text += page.get_text()
# #
# #         # 构造目标文本文件的路径
# #         text_file_path = os.path.join(text_folder_path, os.path.splitext(filename)[0] + '.txt')
# #
# #         # 将提取的文本内容保存到Unicode文本文件中
# #         with open(text_file_path, "w", encoding="utf-8") as text_file:
# #             text_file.write(text)
# #
# # print("PDF文件已成功转换为Unicode文本文件并保存在指定文件夹中。")
#
#
# import requests
# from bs4 import BeautifulSoup
# import urllib.request
# import json
# import os
# import csv
# import pandas as pd
#
# import subprocess
# def run_script(script_name):
#     """运行指定的Python脚本"""
#     try:
#         # 指定编码为UTF-8，并忽略解码错误
#         completed_process = subprocess.run(['python', script_name], check=True, text=True, capture_output=True, encoding='utf-8', errors='ignore')
#         print(f"{script_name} 输出:\n{completed_process.stdout}")
#     except subprocess.CalledProcessError as e:
#         # 如果脚本执行失败，打印错误信息
#         print(f"运行 {script_name} 时出错: {e}")
#
# # 示例：运行脚本
#
# run_script(r'D:\Program Files (x86)\Python\PythonProject\FYP\Script\All_Company_Balance_Sheet.py')
# run_script(r'D:\Program Files (x86)\Python\PythonProject\FYP\Script\All_Company_Cash&Flow_Sheet.py')
# run_script(r'D:\Program Files (x86)\Python\PythonProject\FYP\Script\All_Company_Profit&Loss_Sheet.py')
# run_script(r'D:\Program Files (x86)\Python\PythonProject\FYP\Script\All_Company_Ratio_Sheet.py')
#
#
# import requests
# import json
# import pandas as pd
#
# # url = "https://www.nseindia.com/api/corp-info?symbol=RELIANCE&corpType=annualreport&market=cm"
# # hdr = {
# #     'Cookie': '_ga=GA1.1.84271405.1703581009; _ga_QJZ4447QD3=GS1.1.1708937852.13.0.1708939543.0.0.0; defaultLang=en; AKA_A2=A; nseQuoteSymbols=[{"symbol":"AAKASH","identifier":null,"type":"equity"},{"symbol":"AAREYDRUGS","identifier":null,"type":"equity"},{"symbol":"AARTECH","identifier":null,"type":"equity"},{"symbol":"TATACONSUM","identifier":null,"type":"equity"},{"symbol":"SYRMA","identifier":null,"type":"equity"}]; nsit=n7pRal3uKpdSTXV86XZEk7oO; bm_mi=C98894B088BAF48C926E2AC2B769CC4B~YAAQf3ERAnFBYsiNAQAAt3Ym5Ra4qEskRHwhO4WJeFYuT0KauwQJUlneuIzS6THIQ+Tft0BcrFUPxmle7BBJvtEoPtw1CCySAy/WfWwOhgLYTrdqp6Wc7mXGGC+ghV4SAS8A6l8CJl/0D2RxVRrnZIP25JDj1k+b0qQqAVqMX4hv4kI+c4k5TAD8AoOtbmWF4ZJGtjJuYCgjAhxtWibe/OgydUFr+Bfc4Veub2N/KyRkn2rKR8UHTNgr7g2yJvGn5sgvzDelYbTkvz3GNpzjLGPD4dt609nfZSSbnA8epRunjn2hZHCc6/O5ILJ0BYy0yYcOX1NaAUDYGEbUk9LKBKQ=~1; ak_bmsc=3FFC75E46405911016BEF9AB593D05A5~000000000000000000000000000000~YAAQf3ERAvRCYsiNAQAAR30m5RZ6FthQdOmOs3k6RGetDImc5etaqfaedUUnjPod+Ybrctp0LDsOKs0Xq6vqG10juVjRr+YvMDfnUMgiMna0WXGYJ1YqrMfsdmezAcSc4Aq9+4cz9K29jEvQ2o1oTrnQHP7/hlYOB3SaDOCYrGgqyyem9Hq4zJzmTtNzM1mIUBKC6BwgAme+JEnbFDCa1p5KVFoLqsMUVhCCMpnKJxXBrdDOe/lmKgha2SN7eLSLhftRr5Yybj2Xwg6uxs4DXq+Qe9wIA9bNwGI/U8lM7WFsoawSW6/ediBobs/MUYYILb68KDJmqAoD8VhbZtnfkCDS/WQlVxxKLM2bn1RJa6t1TDyD1TJUpCYryJSmTLDBHmN9emKDzDtC7SDFjbx0tPAQngtPZAjpknlIEvyEXnhd5H2ghZN3xLApCs9Qk4tK6VEbQsykytX3stKrNdp5UOgEnP3Pb49RivFoW/J63nbRaBQxREqYu1U7CgOYpHwp7Q==; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcwODk0NjUzMywiZXhwIjoxNzA4OTUzNzMzfQ.i3WTsaFssUln56JZtHP3_UvZ1RJ464dda1zO5Sor9VM; _ga_87M7PJ3R97=GS1.1.1708946519.22.1.1708946533.0.0.0; bm_sv=06AE1FA144EF8646787C091434491043~YAAQf3ERAtpOYsiNAQAA+bQm5RZMphb6+VcNi9BblEHYJ3B57sxe6o2WqWiReISM/j/BuKH1FCvGyyCkT01X1XGbTxQt8NqsW6yeFcWQ5qeugU5B8ecAtdwM47B2+x/2ZuAQm16Cqf+O8bVcuFXRGUKeNh/IMELWhNKJcMivnv+OK8mN8MaoLFTjZru3ON7Ac5mT32iWeZoOsjsfcEZU9BY6LUGSEKJgi/mWomoAEyoMr6KUz0gdbraNu4jZxTMTGbZ9~1; RT="z=1&dm=nseindia.com&si=931de461-6c59-480c-a733-8d5b4b96651f&ss=lt2umtfk&sl=1&se=8c&tt=11h&bcn=%2F%2F684dd326.akstat.io%2F&nu=3edfkc86&cl=ej8&ld=cor"',
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
# # }
# #
# # response = requests.get(url, headers=hdr)
# # data = json.loads(response.text)
# # # print(data)
# # report_urls = {
# #     'Report URL 2021_2022': 'Not available',
# #     'Report URL 2020_2021': 'Not available',
# #     'Report URL 2019_2020': 'Not available',
# #     'Report URL 2018_2019': 'Not available'
# # }
# #
# # if data:
# #     # 遍历data列表，提取每个年份的报告URL
# #     for report in data:
# #         if 'fileName' in report and 'year' in report:
# #             year = report['year']
# #             # 根据年份设置对应的报告URL
# #             if year == '2021-2022':
# #                 report_urls['Report URL 2021_2022'] = report['fileName']
# #             elif year == '2020-2021':
# #                 report_urls['Report URL 2020_2021'] = report['fileName']
# #             elif year == '2019-2020':
# #                 report_urls['Report URL 2019_2020'] = report['fileName']
# #             elif year == '2018-2019':
# #                 report_urls['Report URL 2018_2019'] = report['fileName']
# # result_df = pd.DataFrame(
# #     columns=['Report URL 2021_2022', 'Report URL 2020_2021', 'Report URL 2019_2020', 'Report URL 2018_2019'])
# # result_df = pd.concat([result_df, pd.DataFrame([new_row])], ignore_index=True)
# # output_excel_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Download_Link.csv'
# # result_df.to_csv(output_excel_path, index=False)
# #
# # print(f"结果已保存到：{output_excel_path}")
#
# # import os
# # import requests
# # import pandas as pd
# #
# # # 读取数据库
# # df = pd.read_csv("D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Download_Link.csv")
# #
# # # 定义保存文件的文件夹
# # directories = {
# #     "Report URL 2021-2022": r"D:\Program Files (x86)\Python\PythonProject\FYP\Data\2021_2022\Report_Zip",
# #     "Report URL 2020-2021": r"D:\Program Files (x86)\Python\PythonProject\FYP\Data\2020_2021\Report_Zip",
# #     "Report URL 2019-2020": r"D:\Program Files (x86)\Python\PythonProject\FYP\Data\2019_2020\Report_Zip",
# #     "Report URL 2018-2019": r"D:\Program Files (x86)\Python\PythonProject\FYP\Data\2018_2019\Report_Zip",
# # }
# #
# # for directory in directories.values():
# #     os.makedirs(directory, exist_ok=True)
# #
# # # 下载每个URL指向的文件
# # for index, row in df.iterrows():
# #     for column, directory in directories.items():
# #         file_url = row[column]
# #         if pd.notna(file_url):
# #             try:
# #                 response = requests.get(file_url)
# #                 response.raise_for_status()  # 确保请求成功
# #
# #                 # 提取文件名并构建保存路径
# #                 file_name = file_url.split('/')[-1]
# #                 save_path = os.path.join(directory, file_name)
# #
# #                 # 保存文件
# #                 with open(save_path, 'wb') as file:
# #                     file.write(response.content)
# #
# #                 print(f"文件 {file_name} 已保存到 {directory}")
# #             except requests.RequestException as e:
# #                 print(f"下载 {file_url} 时发生错误: {e}")
# #
# # print("所有文件下载完成。")






#
# # # 查找缺失数据的公司，保存其Symbol
# import pandas as pd
#
# # 读取CSV文件
# df = pd.read_csv('D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Test\Company_Profit&Loss_Sheet_19.csv')
#
# # 筛选出第4列（索引为3）值为NULL的行
# filtered_df = df[df.iloc[:, 4].isnull()]
#
# # 打印这些行的Symbol列
# print(filtered_df['Symbol'])
#
# # 将这些Symbol保存到一个新的CSV文件中
# filtered_df['Symbol'].to_csv(r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Test\filtered_symbols.csv', index=False)
# #
#
#
# import csv
# from bs4 import BeautifulSoup
# import requests
# import os
# import pandas as pd
# hdr = {
#     'Cookie': 'visits=6; gdpr_userpolicy_eu=1; gdpr_region=eu; _w18g_gdpr_consent_data=personal_info_consent%3AY%23personalization_consent%3AY%23age_consent%3AY%23recommendation_adv_remarketting_consent%3AY%23adv_remarketting_consent%3AY%23marketting_communication_consent%3AY; A18ID=1700241178544.164364; _gcl_au=1.1.332455451.1700241179; _cb=CIlCKND2a_K4qgDui; WZRK_G=57a9e747c2e74a9280aefacb2587ba79; _w18g_consent=Y; __io=10b9e7344.12acd25a5_1703673960144; __io_r=mail.qq.com; __io_first_source=mail.qq.com; __io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22mail.qq.com%22%7D; _gid=GA1.2.801615192.1706521752; dtCookie=v_4_srv_6_sn_31E3A8B145A5A2765380BE57415F687B_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1; _io_ht_r=1; __io_unique_43938=29; isVistedCbPage=true; USR_DFP_TARGETING={"p_value":0,"dob":"","gender":"","income_data":"","occupation":"","industry":""}; nousersess=srxh27qqui66nsiq; _uzitok=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjc3JmIjoiZ2hhTUM5ZW9yYmdSdU5JbjczajJFUWc2QUFNanpxSzBTY1VEQXpLcTI2QzVCbWFNIiwiaWF0IjoxNzA2NTM0NzAwfQ.N0MA4oK_G484-N82HSR2MIKTtubhC_qAdp6OlY0v7yc; MC_PPID_LOGIC=0229d64202f3e21c2a3c893f014672ea; __io_lv=1706534706800; _abck=99C3D9D0B21D6519F2C3621F0E9C1BAD~0~YAAQlAUXAtwoU0eNAQAAfztmVQu+Bxol79VVzBaZRtOuVN2/EtDZ8qL0YLIuOai8Vyd9scF97sGkhTEh+QyRefO2xCVzGCvJCayYmgQkGq/Za9JNu+Ka7Aw8eLPMhyg+5jtW+AcbHRHILqdkqeHzFLQAL3yjxNb8wgfPOrUqoCQRKrBkzSwXfrCCbGz4R+4Kf84Bxn56mZhk1wXEug+LDGJya2RSXogcY/WVdsMlCovXbeDo73oQmNWIKSOk6zVvBngZdW0N+/M1wmcDFhOHoYy71NpE2iCZlc7yTrkLixqZfZ2fKzfnAmwbYHa78dWmKA2ATmTywTwKMFe5PRLPqNbetSpAv38qDXLzP0EtORneHX7euE80mVzql8TyIRD037vJLNlBx7H5I/RqTXA0zcaoCc7XeT8KbJn/TNSS~-1~-1~1706538367; ak_bmsc=36124D451347BE886D035E3B8CDD8AC4~000000000000000000000000000000~YAAQlAUXAvMoU0eNAQAA7jxmVRbfZ+nebzMPc/XdA78O/iXoPbp3NBT4n37LLV3rKo/+9WgM4hMxzxRD/N+CQUJA4s3KYZyroaXpA/ztGQfvIQo1nAB0eZOGh46PKwEQGqfT8wfeLrL5kbaSOWc5L0oPTupYIi9ERb0nzeCsE0NUdClFoI0quz2p9GEy/EBdYOhFx/zqB54SxYzoBelDprLhiodis0xbSxtDlr95nkzX6hftIwIla+xbIqighmpJYQS5A/sFwxyCD4IoISDYFyJ2nZ5O8/bwhccHLH78aHZwtuZKRuAdT4VxK7JdzmBKnslVAho8J3v3+O8m3RPHOynnC/84oQ68XgT2tW1cFcVf1eMJWOM+D9bm5K8qRHdWQ5NOCcCkPbhaKeErckYO5P4vuquLU+Vq/cSVGTGYgFOOtJrErBpB6K+VXIZ0+2eOZXx0jIfCM48iBTLUvqncCJXEhy3Bgv9yLKv9nfG2KtFOBNpXJMlaNNsiDfaEYDpx7ZzIBi/s; verify=%24%24%23%23%24%241; nnmc=Charon+Li; UIDHASH=d9025f4728fc800e6e6395a4c431df9a58beafc2e7099f2adc47c8d5cc42d3c3; token-normal=qiAfBsg1Cu5dRhiBfqdRHTID5g3HC2zR1ZzGowKN6WJcxE7wZaSXXBVCbjawY-FzSmEyjANFm7d_gJcmGCkgmw; DEF_VIEW=4; tvuid=VlZoa1EycDJSMEY1TWc9PQ%3D%3D; mcpro=0; gdpr_consent_cookie=UXdCjvGAy2; bm_sv=1D9CA9D19716327EDD436D6249E5FA8E~YAAQlAUXAgEsU0eNAQAAZV9mVRaHyaSziBa72Jh5DyiuVVCVp/CPtHiBqHEd3jIVheHz1nSRT61irBkWwcwt1I8PQgF74PI1yIo9NUfQcpz5WfLNaYjftPf3zJkMj6XXC1TNyvmPN4VBvXXPuuDUByr77qKQaFV8uFP7AiWrtFMki3/uq3c5eiTqIzo66WKAUabMqFOyugaPr/2CSQ+1vftkVMrSBsl4jrAIjYCv1LEQ7g62Na3eHh5ydNKbsfKKe2pMot2/~1; PHPSESSID=oeqlat69bun9aba62rtjef1p06; MC_WAP_INTERSTITIAL_NEW_LOGIC_20240129={"0":"https://www.moneycontrol.com/financials/a&mfebcon/consolidated-ratiosVI/F03#F03","1":"https://www.moneycontrol.com/financials/a&mfebcon/ratiosVI/F03#F03","2":"https://www.moneycontrol.com/financials/indianrailwayfinancecorporation/ratiosVI/IRF#IRF","3":"https://www.moneycontrol.com/india/stockpricequote/infrastructure-general/abinfrabuild/I07"}; _ga_4S48PBY299=GS1.1.1706534312.22.1.1706541378.0.0.0; _ga=GA1.1.270074858.1700241157; _gat=1; stocks=|A.B.Infrabuild_I12~6%7CN_JB02%7E9%7CN_F04%7E7%7CIndian.Railway_IRF%7E2%7CReliance_RI%7E2%7CN_SGBOC5960%7E1%7C3M.India_B3M%7E14%7CIWML_IIFLW54277%7E14%7CAdani.Energy_AT18%7E2%7CZydus.Wellness_CNA%7E6; _chartbeat2=.1700241187999.1706541379308.0011101011100001.BUEGETHSzyoQjpMF2llIODGa_1O.1; _cb_svref=external; WZRK_S_86Z-5ZR-RK6Z=%7B%22p%22%3A33%2C%22s%22%3A1706536123%2C%22t%22%3A1706541385%7D',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
# }
#
#
# # 从CSV读取URL的函数
#
# def read_urls_from_csv(urls_csv_path,missing_symbols_csv_path):
#     # 读取包含所有URLs的CSV文件
#     df_urls = pd.read_csv(urls_csv_path)
#
#     # 读取包含缺失数据公司Symbols的CSV文件
#     df_missing_symbols = pd.read_csv(missing_symbols_csv_path)
#
#     # 获取缺失数据公司的Symbols列表
#     missing_symbols = df_missing_symbols['Symbol'].tolist()
#
#     # 在URLs的DataFrame中找到对应的URLs
#     urls = df_urls[df_urls['Symbol'].isin(missing_symbols)]['URL'].tolist()
#
#
#     return urls
#
# def construct_balance_sheet_url(base_url):
#     # 分割基础URL以获取公司名称和代码
#     parts = base_url.split('/')
#     company_name = parts[6]
#     code = parts[7]
#
#     # 构建balance sheet的URL
#     balance_sheet_url = f"https://www.moneycontrol.com/financials/{company_name}/consolidated-profit-lossVI/{code}#{code}"
#     return balance_sheet_url
#
# #
# # 修改脚本来处理每个URL
#
# def write_csv_for_year(data, csv_header):
#     csv_file_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Test\Missing_symbols_Data.csv'
#     # 检查文件是否存在，以决定是否写入表头
#     file_exists = os.path.exists(csv_file_path)
#     with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:  # 使用'a'模式以追加数据
#         writer = csv.writer(file)
#         if not file_exists:  # 如果文件不存在，写入表头
#             writer.writerow(csv_header)
#         writer.writerow(data)
#
# def process_urls(urls):
#     for url in urls:
#         try:
#
#           resp = requests.get(construct_balance_sheet_url(url), headers=hdr)
#           soup = BeautifulSoup(resp.text, 'html.parser')
#
#           resp2 = requests.get(url, headers=hdr)
#           soup2 = BeautifulSoup(resp2.text, 'html.parser')
#
#           span_tag = soup2.find('span', string="NSE:")
#         # 定位紧跟在 <span> 标签之后的 <p> 标签
#           p_tag = span_tag.find_next('p') if span_tag else None
#         # 提取文本
#           Symbol = p_tag.text.strip() if p_tag else 'Data not found'
#
#           company_name_element = soup2.select_one('div.div_desktop div.name_left.topsel_tab div#stockName.inid_name > h1')
#           Company_name = company_name_element.get_text(strip=True) if company_name_element else None
#
#           mctable = soup.find('table', class_='mctable1')
#         # 提取表格数据
#           table_data = []
#           table_data.insert(0, [f"Symbol", Symbol])
#           table_data.insert(1, [f"Company_name", Company_name])
#           if mctable:
#             # 遍历所有的行
#               for row in mctable.find_all('tr'):
#                 # 提取每一行的td元素
#                   cells = row.find_all('td')
#                   row_data = [cell.get_text(strip=True) for cell in cells]
#                   if row_data:
#                       table_data.append(row_data)
#
#           years = [23,22,21,20,19]
#         # Extract the general headers from the provided data structure (ignoring 'Symbol' and 'Company_name')
#           general_headers = [row[0] for row in table_data[4:]]
#
#         # The CSV header will include 'Particulars' followed by the general headers
#           csv_header = ['Symbol', 'Company Name'] + general_headers
#           print(f"公司代码: {Symbol }")
#           # print(f"提取的数据: {table_data}")
#
#           for year_index, year in enumerate(years):
#             # Extract data for this year
#               data_row = [table_data[0][1], table_data[1][1]]  # Symbol and Company Name
#               for row in table_data[4:]:
#                   data_row.append(row[year_index + 1] if len(row) > year_index + 2 else '')
#             # Write to CSV
#               write_csv_for_year(data_row, csv_header)
#
#         except Exception as e:
#             print(f"提取{url}数据失败: {e}")
#             continue
#
#
# # 主执行
# if __name__ == '__main__':
#     urls_csv_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Filtered_Companies_Financial_Data.csv'
#     missing_symbol_csv_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Test\filtered_symbols.csv'
#     urls = read_urls_from_csv(urls_csv_path=urls_csv_path,missing_symbols_csv_path=missing_symbol_csv_path)
#     process_urls(urls)
#

#
# # 将缺失值数据库按照19-23年进行分类，同一年份的数据库放在同一个表中
# import pandas as pd
#
# # 加载数据
# data = pd.read_csv(r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Test\Missing_symbols_Data.csv')
#
# # 跳过第一行表头后，按索引分组
# # 创建一个字典，键是余数（0到4），每个键对应的值是一个空列表
# groups = {i: [] for i in range(5)}
#
#
# for i in range(0, len(data)):
#     # 用索引除以5得到余数，确定分组
#     remainder = i % 5
#     # 余数是4的放在第一个组，以此类推，余数是0的放在第五个组
#     group_number = 4 if remainder == 0 else remainder - 1
#     # 添加行到对应的组
#     groups[group_number].append(data.iloc[i])
#
# # 将分组的数据转换为DataFrame，并保存为CSV文件
# for group_number, rows in groups.items():
#     # 创建DataFrame
#     group_df = pd.DataFrame(rows)
#     # 输出到CSV文件，文件名中包含组号
#     group_df.to_csv(f'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Test\grouped_rem_{group_number + 1}.csv', index=False)

# 填充缺失的数据
import pandas as pd

# 假设数据存储在CSV文件中，你需要根据实际情况修改路径
years = ['19', '20', '21', '22', '23']

for year in years:
    # 读取两个数据库
    db_path = f'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Test/{year}.csv'
    company_db_path = f'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Test\Company_Profit&Loss_Sheet_{year}.csv'

    try:
        db = pd.read_csv(db_path)
        company_db = pd.read_csv(company_db_path)
    except Exception as e:
        print(f"Error reading files for year {year}: {e}")
        continue

    # 以Symbol为键进行匹配，用db更新company_db中的数据
    # 确保两个数据库中的'Symbol'列都是唯一的
    # 如果不是唯一的，需要先处理重复项
    company_db.set_index('Symbol', inplace=True)
    db.set_index('Symbol', inplace=True)

    # 进行更新
    company_db.update(db)

    # 重置索引，如果你希望'Symbol'列回到DataFrame的列中
    company_db.reset_index(inplace=True)

    # 将更新后的数据保存回CSV文件
    try:
        company_db.to_csv(company_db_path, index=False)
    except Exception as e:
        print(f"Error writing file for year {year}: {e}")