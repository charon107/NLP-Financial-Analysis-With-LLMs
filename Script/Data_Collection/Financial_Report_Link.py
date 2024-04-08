import requests
import pandas as pd

# 定义基础URL和Header
base_url = "https://www.nseindia.com/api/corp-info"
hdr = {
    'Cookie': '_ga=GA1.1.84271405.1703581009; _ga_QJZ4447QD3=GS1.1.1708937852.13.0.1708939543.0.0.0; defaultLang=en; AKA_A2=A; nseQuoteSymbols=[{"symbol":"AAKASH","identifier":null,"type":"equity"},{"symbol":"AAREYDRUGS","identifier":null,"type":"equity"},{"symbol":"AARTECH","identifier":null,"type":"equity"},{"symbol":"TATACONSUM","identifier":null,"type":"equity"},{"symbol":"SYRMA","identifier":null,"type":"equity"}]; nsit=n7pRal3uKpdSTXV86XZEk7oO; bm_mi=C98894B088BAF48C926E2AC2B769CC4B~YAAQf3ERAnFBYsiNAQAAt3Ym5Ra4qEskRHwhO4WJeFYuT0KauwQJUlneuIzS6THIQ+Tft0BcrFUPxmle7BBJvtEoPtw1CCySAy/WfWwOhgLYTrdqp6Wc7mXGGC+ghV4SAS8A6l8CJl/0D2RxVRrnZIP25JDj1k+b0qQqAVqMX4hv4kI+c4k5TAD8AoOtbmWF4ZJGtjJuYCgjAhxtWibe/OgydUFr+Bfc4Veub2N/KyRkn2rKR8UHTNgr7g2yJvGn5sgvzDelYbTkvz3GNpzjLGPD4dt609nfZSSbnA8epRunjn2hZHCc6/O5ILJ0BYy0yYcOX1NaAUDYGEbUk9LKBKQ=~1; ak_bmsc=3FFC75E46405911016BEF9AB593D05A5~000000000000000000000000000000~YAAQf3ERAvRCYsiNAQAAR30m5RZ6FthQdOmOs3k6RGetDImc5etaqfaedUUnjPod+Ybrctp0LDsOKs0Xq6vqG10juVjRr+YvMDfnUMgiMna0WXGYJ1YqrMfsdmezAcSc4Aq9+4cz9K29jEvQ2o1oTrnQHP7/hlYOB3SaDOCYrGgqyyem9Hq4zJzmTtNzM1mIUBKC6BwgAme+JEnbFDCa1p5KVFoLqsMUVhCCMpnKJxXBrdDOe/lmKgha2SN7eLSLhftRr5Yybj2Xwg6uxs4DXq+Qe9wIA9bNwGI/U8lM7WFsoawSW6/ediBobs/MUYYILb68KDJmqAoD8VhbZtnfkCDS/WQlVxxKLM2bn1RJa6t1TDyD1TJUpCYryJSmTLDBHmN9emKDzDtC7SDFjbx0tPAQngtPZAjpknlIEvyEXnhd5H2ghZN3xLApCs9Qk4tK6VEbQsykytX3stKrNdp5UOgEnP3Pb49RivFoW/J63nbRaBQxREqYu1U7CgOYpHwp7Q==; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcwODk0NjUzMywiZXhwIjoxNzA4OTUzNzMzfQ.i3WTsaFssUln56JZtHP3_UvZ1RJ464dda1zO5Sor9VM; _ga_87M7PJ3R97=GS1.1.1708946519.22.1.1708946533.0.0.0; bm_sv=06AE1FA144EF8646787C091434491043~YAAQf3ERAtpOYsiNAQAA+bQm5RZMphb6+VcNi9BblEHYJ3B57sxe6o2WqWiReISM/j/BuKH1FCvGyyCkT01X1XGbTxQt8NqsW6yeFcWQ5qeugU5B8ecAtdwM47B2+x/2ZuAQm16Cqf+O8bVcuFXRGUKeNh/IMELWhNKJcMivnv+OK8mN8MaoLFTjZru3ON7Ac5mT32iWeZoOsjsfcEZU9BY6LUGSEKJgi/mWomoAEyoMr6KUz0gdbraNu4jZxTMTGbZ9~1; RT="z=1&dm=nseindia.com&si=931de461-6c59-480c-a733-8d5b4b96651f&ss=lt2umtfk&sl=1&se=8c&tt=11h&bcn=%2F%2F684dd326.akstat.io%2F&nu=3edfkc86&cl=ej8&ld=cor"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# 从CSV文件读取所有公司的Symbol
csv_file_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\All_Companies_Financial_Data.csv'
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
output_excel_path = r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Download_Link.csv'
result_df.to_csv(output_excel_path, index=False, encoding='utf-8')  # 使用UTF-8编码保存CSV
print(f"爬取的数据已保存到：{output_excel_path}")
