import csv
from bs4 import BeautifulSoup
import requests
import os
hdr = {
    'Cookie': 'visits=6; gdpr_userpolicy_eu=1; gdpr_region=eu; _w18g_gdpr_consent_data=personal_info_consent%3AY%23personalization_consent%3AY%23age_consent%3AY%23recommendation_adv_remarketting_consent%3AY%23adv_remarketting_consent%3AY%23marketting_communication_consent%3AY; A18ID=1700241178544.164364; _gcl_au=1.1.332455451.1700241179; _cb=CIlCKND2a_K4qgDui; WZRK_G=57a9e747c2e74a9280aefacb2587ba79; _w18g_consent=Y; __io=10b9e7344.12acd25a5_1703673960144; __io_r=mail.qq.com; __io_first_source=mail.qq.com; __io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22mail.qq.com%22%7D; _gid=GA1.2.801615192.1706521752; dtCookie=v_4_srv_6_sn_31E3A8B145A5A2765380BE57415F687B_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1; _io_ht_r=1; __io_unique_43938=29; isVistedCbPage=true; USR_DFP_TARGETING={"p_value":0,"dob":"","gender":"","income_data":"","occupation":"","industry":""}; nousersess=srxh27qqui66nsiq; _uzitok=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjc3JmIjoiZ2hhTUM5ZW9yYmdSdU5JbjczajJFUWc2QUFNanpxSzBTY1VEQXpLcTI2QzVCbWFNIiwiaWF0IjoxNzA2NTM0NzAwfQ.N0MA4oK_G484-N82HSR2MIKTtubhC_qAdp6OlY0v7yc; MC_PPID_LOGIC=0229d64202f3e21c2a3c893f014672ea; __io_lv=1706534706800; _abck=99C3D9D0B21D6519F2C3621F0E9C1BAD~0~YAAQlAUXAtwoU0eNAQAAfztmVQu+Bxol79VVzBaZRtOuVN2/EtDZ8qL0YLIuOai8Vyd9scF97sGkhTEh+QyRefO2xCVzGCvJCayYmgQkGq/Za9JNu+Ka7Aw8eLPMhyg+5jtW+AcbHRHILqdkqeHzFLQAL3yjxNb8wgfPOrUqoCQRKrBkzSwXfrCCbGz4R+4Kf84Bxn56mZhk1wXEug+LDGJya2RSXogcY/WVdsMlCovXbeDo73oQmNWIKSOk6zVvBngZdW0N+/M1wmcDFhOHoYy71NpE2iCZlc7yTrkLixqZfZ2fKzfnAmwbYHa78dWmKA2ATmTywTwKMFe5PRLPqNbetSpAv38qDXLzP0EtORneHX7euE80mVzql8TyIRD037vJLNlBx7H5I/RqTXA0zcaoCc7XeT8KbJn/TNSS~-1~-1~1706538367; ak_bmsc=36124D451347BE886D035E3B8CDD8AC4~000000000000000000000000000000~YAAQlAUXAvMoU0eNAQAA7jxmVRbfZ+nebzMPc/XdA78O/iXoPbp3NBT4n37LLV3rKo/+9WgM4hMxzxRD/N+CQUJA4s3KYZyroaXpA/ztGQfvIQo1nAB0eZOGh46PKwEQGqfT8wfeLrL5kbaSOWc5L0oPTupYIi9ERb0nzeCsE0NUdClFoI0quz2p9GEy/EBdYOhFx/zqB54SxYzoBelDprLhiodis0xbSxtDlr95nkzX6hftIwIla+xbIqighmpJYQS5A/sFwxyCD4IoISDYFyJ2nZ5O8/bwhccHLH78aHZwtuZKRuAdT4VxK7JdzmBKnslVAho8J3v3+O8m3RPHOynnC/84oQ68XgT2tW1cFcVf1eMJWOM+D9bm5K8qRHdWQ5NOCcCkPbhaKeErckYO5P4vuquLU+Vq/cSVGTGYgFOOtJrErBpB6K+VXIZ0+2eOZXx0jIfCM48iBTLUvqncCJXEhy3Bgv9yLKv9nfG2KtFOBNpXJMlaNNsiDfaEYDpx7ZzIBi/s; verify=%24%24%23%23%24%241; nnmc=Charon+Li; UIDHASH=d9025f4728fc800e6e6395a4c431df9a58beafc2e7099f2adc47c8d5cc42d3c3; token-normal=qiAfBsg1Cu5dRhiBfqdRHTID5g3HC2zR1ZzGowKN6WJcxE7wZaSXXBVCbjawY-FzSmEyjANFm7d_gJcmGCkgmw; DEF_VIEW=4; tvuid=VlZoa1EycDJSMEY1TWc9PQ%3D%3D; mcpro=0; gdpr_consent_cookie=UXdCjvGAy2; bm_sv=1D9CA9D19716327EDD436D6249E5FA8E~YAAQlAUXAgEsU0eNAQAAZV9mVRaHyaSziBa72Jh5DyiuVVCVp/CPtHiBqHEd3jIVheHz1nSRT61irBkWwcwt1I8PQgF74PI1yIo9NUfQcpz5WfLNaYjftPf3zJkMj6XXC1TNyvmPN4VBvXXPuuDUByr77qKQaFV8uFP7AiWrtFMki3/uq3c5eiTqIzo66WKAUabMqFOyugaPr/2CSQ+1vftkVMrSBsl4jrAIjYCv1LEQ7g62Na3eHh5ydNKbsfKKe2pMot2/~1; PHPSESSID=oeqlat69bun9aba62rtjef1p06; MC_WAP_INTERSTITIAL_NEW_LOGIC_20240129={"0":"https://www.moneycontrol.com/financials/a&mfebcon/consolidated-ratiosVI/F03#F03","1":"https://www.moneycontrol.com/financials/a&mfebcon/ratiosVI/F03#F03","2":"https://www.moneycontrol.com/financials/indianrailwayfinancecorporation/ratiosVI/IRF#IRF","3":"https://www.moneycontrol.com/india/stockpricequote/infrastructure-general/abinfrabuild/I07"}; _ga_4S48PBY299=GS1.1.1706534312.22.1.1706541378.0.0.0; _ga=GA1.1.270074858.1700241157; _gat=1; stocks=|A.B.Infrabuild_I12~6%7CN_JB02%7E9%7CN_F04%7E7%7CIndian.Railway_IRF%7E2%7CReliance_RI%7E2%7CN_SGBOC5960%7E1%7C3M.India_B3M%7E14%7CIWML_IIFLW54277%7E14%7CAdani.Energy_AT18%7E2%7CZydus.Wellness_CNA%7E6; _chartbeat2=.1700241187999.1706541379308.0011101011100001.BUEGETHSzyoQjpMF2llIODGa_1O.1; _cb_svref=external; WZRK_S_86Z-5ZR-RK6Z=%7B%22p%22%3A33%2C%22s%22%3A1706536123%2C%22t%22%3A1706541385%7D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}


# 从CSV读取URL的函数

def read_urls_from_csv(csv_file_path):
    urls = []
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            urls.append(row['URL'])  # 假设'URL'是URLs列的列标题
    return urls


def construct_balance_sheet_url(base_url):
    # 分割基础URL以获取公司名称和代码
    parts = base_url.split('/')
    company_name = parts[6]
    code = parts[7]

    # 构建balance sheet的URL
    balance_sheet_url = f"https://www.moneycontrol.com/financials/{company_name}/cash-flowVI/{code}#{code}"
    return balance_sheet_url


# 修改脚本来处理每个URL

def write_csv_for_year(year, data, csv_header):
    csv_file_path = f'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Cash&Flow_Sheet\Company_Cash&Flow_Sheet_{year}.csv'
    # 检查文件是否存在，以决定是否写入表头
    file_exists = os.path.exists(csv_file_path)
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:  # 使用'a'模式以追加数据
        writer = csv.writer(file)
        if not file_exists:  # 如果文件不存在，写入表头
            writer.writerow(csv_header)
        writer.writerow(data)

def process_urls(urls):
    for url in urls:
        try:

          resp = requests.get(construct_balance_sheet_url(url), headers=hdr)
          soup = BeautifulSoup(resp.text, 'html.parser')

          resp2 = requests.get(url, headers=hdr)
          soup2 = BeautifulSoup(resp2.text, 'html.parser')

          span_tag = soup2.find('span', string="NSE:")
        # 定位紧跟在 <span> 标签之后的 <p> 标签
          p_tag = span_tag.find_next('p') if span_tag else None
        # 提取文本
          Symbol = p_tag.text.strip() if p_tag else 'Data not found'

          company_name_element = soup2.select_one('div.div_desktop div.name_left.topsel_tab div#stockName.inid_name > h1')
          Company_name = company_name_element.get_text(strip=True) if company_name_element else None

          mctable = soup.find('table', class_='mctable1')
        # 提取表格数据
          table_data = []
          table_data.insert(0, [f"Symbol", Symbol])
          table_data.insert(1, [f"Company_name", Company_name])
          if mctable:
            # 遍历所有的行
              for row in mctable.find_all('tr'):
                # 提取每一行的td元素
                  cells = row.find_all('td')
                  row_data = [cell.get_text(strip=True) for cell in cells]
                  if row_data:
                      table_data.append(row_data)

          years = [23,22,21,20,19]
        # Extract the general headers from the provided data structure (ignoring 'Symbol' and 'Company_name')
          general_headers = [row[0] for row in table_data[4:]]

        # The CSV header will include 'Particulars' followed by the general headers
          csv_header = ['Symbol', 'Company Name'] + general_headers
          print(f"公司名称: {Company_name}")
          # print(f"提取的数据: {table_data}")

          for year_index, year in enumerate(years):
            # Extract data for this year
              data_row = [table_data[0][1], table_data[1][1]]  # Symbol and Company Name
              for row in table_data[4:]:
                  data_row.append(row[year_index + 1] if len(row) > year_index + 2 else '')
            # Write to CSV
              write_csv_for_year(year, data_row, csv_header)

        except Exception as e:
            print(f"提取{url}数据失败: {e}")
            continue


# 主执行
if __name__ == '__main__':
    urls = read_urls_from_csv(
        r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\Filtered_Companies_Financial_Data.csv')
    process_urls(urls)
