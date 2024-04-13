import requests
import pandas as pd

# 定义基础URL和Header
base_url = "https://www.nseindia.com/api/corp-info"
hdr = {
    'Cookie': '_ga=GA1.1.84271405.1703581009; _ga_QJZ4447QD3=GS1.1.1710425872.25.0.1710425872.0.0.0; nsit=IX6nJO-xgPzp5y89bVcrHsp4; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcxMzAyMDAwMiwiZXhwIjoxNzEzMDI3MjAyfQ.QcnFU584x-YF6L87vJE8hoJoaNSHvuprRqU7Cvz1Rpo; AKA_A2=A; _abck=72A80F72E739CBF18842835D1A57A88A~0~YAAQf3ERAlJX59COAQAALePy1wvDt0xjZROxJTfvo1HtH18YpE5vaHPq/zoJbaHDnS1q5mrAB7IVGSnMIBVKGtp3mkW85EwyiVY/S6DMHlposj/ZH2PuI68Ni/3rw6iCx1yLf8J7WYAcoi4Ao5r80fJf+MoWhaaM7GK6mkknYorTEa1yeL+lMDDVHIiQCcYdgvMHQDn+ghwuYvePmRqk3ZIp/ZLDbmAKFETEVCc63x9oqgJUb5IW9vaYIMJtNt56h6ZHQGQca+KXLEMiswwUGUB7i10NyhgrInwxkA/jvD4vFXKAZmSdmMjx6kkZqqlWv+33rIxbyuwxFDxSa8fXz+jGoKiOKmDDnBNDY+1RRqKjJp/39ypxYRoaPbfeuvcjx4FXAvgzZcVHMM3tAoRE9ABq1eHJXui7C+k=~-1~-1~-1; bm_sz=4DF89B7D23A1476A912EF630BA6C5BC7~YAAQf3ERAlVX59COAQAALePy1xcesFhNEmldd7b3a/wBiv/Nrfv7Rok2deO7v8IpS7WdxQvcMvv+In/7hNiFcsDtmY+5xKmXIfOLBxjSs1USjOMZMJKnq/5Y0Ch2i0Epf4TsA7dd+w7GGbwIvAemSALQU6+7QCunyS121+DfjLyJQi9R6a1M9ATD7CEX7mw3axwIS6H9mCAPoan5lzKhm4CdgJlz8yXZ/meZ/3AzLa+C0TyUT7kDitQxIf+QhJzCMfJ44LwYqGmJpRnyH8xjCJPQGaPpRrwE/ZUUZPr+HuHMfrBBrqeeBQXfzyqYkKjjBank6rowWPXQWL7BHgvTLYh4w/c15pvnLqujERLqcYBeFFbNb7SnxgECrTVGgdiRha0nqqECpRFVxnerOw==~3621941~3225414; defaultLang=en; _ga_87M7PJ3R97=GS1.1.1713020002.39.1.1713020002.0.0.0; ak_bmsc=80D3F7606C43C2007D41F85DB2ECD41D~000000000000000000000000000000~YAAQf3ERAhpY59COAQAA+Ofy1xfdTLpuYQtl85gs0STEP8P7iweckFs8QRMleQ4eyO0F5f4/D81Z7lUS+vMrt4/zWgUVP9grIMEQ4+y5ANSje+sOwKon/ddSib6DbYz7zTDRA3devj0f7CF7UUL1y04UtOGXEKAJ+6vMe8OjHeB0IMDAGkeaydXor0dg0st0XJg4i75uWv9bRQrXLBCaOWyF8TEEJWUj5so0MOq2zgQz3HgaRIhuwF2VAbQSICGgE8XHOfOb99nGU54c+qsPy8J76PjqgGE8UFFQlQP9No5mvH10jPbrz+UZKgiUYpjWtaOZx335Ah51zPnZMTC4V76MDgJBf8cy9FF+6d7AMJeTMW68sg2e4QKp5CgyfyRKwODWScaoTUpfeuCbaLROysQM14BueVog9DakOllnrUnX49gGBeyWvZLC/Pd89OpUOganyLoCdHNzfvZoSsk=; bm_sv=D2DF7FE01ED952C3FCD1580EB12D84CE~YAAQf3ERAsll59COAQAAYjrz1xeaTcqaRd1M/uOfui3iqK93zZ0YWyQIdLQlrzXoSOo6MToNPV6nWMdhKeLm/1Km+gOkqwoCNejp8+yGQ5YxCEzDiemgtp26gLVGz6Dg85W7a7ksttIfOROwIuMztAJY/kPvHXtJmT0JKvvKt03Dg8gywSRy1lKmyDp2jRVSBMBKJJLmIHaEYubzGysE1i5tCp4rLxmBYk0XjCq/Wzn1gF8N35SR0A1Jag/LgYsQhNM=~1; RT="z=1&dm=nseindia.com&si=3f59786b-2f81-492c-b1ae-567f96fadca1&ss=luy7vnp3&sl=1&se=8c&tt=2o7&bcn=%2F%2F684dd32d.akstat.io%2F&ld=3g9&ul=mqr"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

# 从CSV文件读取所有公司的Symbol
csv_file_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Presentation\Pre_Company_List.csv'
df_symbols = pd.read_csv(csv_file_path, encoding='utf-8')  # 确保使用UTF-8编码读取CSV

# 创建一个空的DataFrame来存储结果
result_df = pd.DataFrame()

for index, row in df_symbols.iterrows():
    symbol = row['Symbol']
    company_name = row['Company_Name']
    params = {
        'symbol': symbol,
        'corpType': 'annualreport',
        'market': 'cm'
    }

    try:
        # 发送GET请求
        response = requests.get(base_url, headers=hdr, params=params)
        response.raise_for_status()
        data = response.json()

        # 设置响应内容的编码为UTF-8
        response.encoding = 'utf-8'
        data = response.json()

        # 初始化一个字典来存储当前公司的所有年报URL
        report_urls = {}

        # 检查数据是否为列表类型
        if isinstance(data, list):
            # 遍历列表中的每个报告
            for report in data:
                from_year = report.get('fromYr')
                to_year = report.get('toYr')
                file_name = report.get('fileName')
                # 只提取2018-2019及之后的数据
                if from_year and int(from_year) >= 2018:
                    report_urls[f'Report URL {from_year}-{to_year}'] = file_name

            # 将公司名称、Symbol和年报URL添加到新行
            new_row = pd.DataFrame([{'Company Name': company_name, 'Symbol': symbol, **report_urls}])
            # 使用concat而不是append来添加新行
            result_df = pd.concat([result_df, new_row], ignore_index=True)

            # 打印完成提取的公司信息
            extracted_years = list(report_urls.keys())
            print(f"{company_name} 已完成提取，提取出的年份为：{', '.join(extracted_years)}")


    except requests.HTTPError as http_err:
       print(f"HTTP error occurred for {symbol}: {http_err}")
    except Exception as err:
       print(f"Other error occurred for {symbol}: {err}")

# 保存结果DataFrame到CSV文件
output_excel_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Presentation\Download_Link.csv'
result_df.to_csv(output_excel_path, index=False, encoding='utf-8')  # 使用UTF-8编码保存CSV
print(f"爬取的数据已保存到：{output_excel_path}")
