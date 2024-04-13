import csv
from bs4 import BeautifulSoup
import requests
import os

hdr = {
    'Cookie': 'visits=1; gdpr_userpolicy_eu=1; gdpr_region=eu; _w18g_gdpr_consent_data=personal_info_consent%3AY%23personalization_consent%3AY%23age_consent%3AY%23recommendation_adv_remarketting_consent%3AY%23adv_remarketting_consent%3AY%23marketting_communication_consent%3AY; A18ID=1700241178544.164364; _cb=CIlCKND2a_K4qgDui; WZRK_G=57a9e747c2e74a9280aefacb2587ba79; __io=10b9e7344.12acd25a5_1703673960144; __io_r=mail.qq.com; __io_first_source=mail.qq.com; __io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22mail.qq.com%22%7D; MC_PPID_LOGIC=0229d64202f3e21c2a3c893f014672ea; _gcl_au=1.1.1752714702.1708336554; __utma=129839248.907922309.1708339106.1708339106.1708339106.1; __utmz=129839248.1708339106.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); FCCDCF=%5Bnull%2Cnull%2Cnull%2C%5B%22CP6OgQAP6OgQAEsACBENAnEgAAAAAEPgABBoAAAOhQD2F2K2kKFkPCmQWYAQBCijaEAhQAAAAkCBIAAgAUgQAgFIIAgAIFAAAAAAAAAQEgCQAAQABAAAIACgAAAAAAIAAAAAAAQQAAAAAIAAAAAAAAEAAAAAAAQAAAAIAABEhCAAQQAEAAAAAAAQAAAAAAAAAAABAAA%22%2C%222~~dv.2072.70.89.93.108.122.149.196.2253.2299.259.2357.311.313.323.2373.338.358.2415.415.449.2506.2526.486.494.495.2568.2571.2575.540.574.2624.609.2677.864.981.1029.1048.1051.1095.1097.1126.1201.1205.1211.1276.1301.1344.1365.1415.1423.1449.1451.1516.1570.1577.1598.1651.1716.1735.1753.1765.1870.1878.1889.1958%22%2C%22C91689C5-A821-4ABC-9EE5-BA5855256A0A%22%5D%5D; __io_unique_43938=6; __io_lv=1709712672289; bm_mi=C596D8E360D50A0D3F5C8FA196C206C2~YAAQl8YcuE9nuLyOAQAAtKNJyRcD8WxNencdgsGFdvH7SJsxzPaK0NP2OGtschkK0mPqqliAoTaAOeyngz98EkcWuEkaZoMoczIoRyJSWppEaTnVhd9WLr4jDrJwVE4lDaVMsPaUmNRDlSL9iySkUobSf79D1Z89A9VeIIjZ+eQ0nKkyHqHW+d26B+ZpZziZDxEa1YhtRhbFg27ULi0PVj/K00E3TvhFV5DAwmhm8k5fXzu1QKGlt8avOn3P1tb5AtY5V4rSkvKEhiD8YHkL03QhZumiPfvzgWt3YFfEBPPJWPDh2SGxFBsyu6kZ5mMsrRyfcpVQo3M5+K9GLBZbPQREjSCT6g1vozL4~1; _is_in=0; bm_sz=259E870EB6A769882BFBE016BF9F637F~YAAQRcYcuMRDVq6OAQAAvaVJyRdvlUUdK3zf0oJTUKXxKMyRnISrwcNEEgxWGHI68LBNUB9lN18+mSgZ8TprUTsZ9ZysI1IMpF7ue5GRXm8qfe6Ynm49GneRPxHQo115Uj5rnzyTUdRBZ9IiwJHDKr1pLGEM48F2wKQwc1CF56D9BM9cJCORB+SjaV6zxWLYcr1HTnGei/Lt+96aOKhBzYB+SazJc9+28mRFw017R0+21bYF2HH2K4O763NUVwSC7wdDPuH17hM/ScSP96xn95za7gVuTM21it+dpdmlIh/cgXfBDvDrwb7Adn5MnsoYV+QASNtvgt5oFl3N1nRKNRXpGcxXLZUgOFxJzKoWck0MjCUn1CuCMPvkipY8~3158326~4273463; _gid=GA1.2.872396207.1712774031; ak_bmsc=954D573D322466842E312B5572340F52~000000000000000000000000000000~YAAQl8YcuJ9nuLyOAQAAEKdJyRexthyd1zUijLIokMDJuSRTmUygZP3eohitEhvjFqec0N5XP0WRglNwaqiCa5QXdfm/XOM0OL8Hu5U0zRguHFMmn2UqxD16t4+XpkV9BrLBEWpdemIqJu22Qb6MtQNhoPbd891t2CCszUlrGIDIzxgJZ0GeJfT9uzZlujI/9xNH1CcFuSwvvqz5+Zwm/AEG3nUvDlgJCl7zrko+UAIic2Uk1O/bH8t3S2ZxY3IjxWZYvvdgaSIey8EN+CUvp1fGuQ6HHPm0lLRH8vLqMuUrWRK7E0iFnU/VGG7g95NyAEac3Zfx+GAFXrmwxvg7StsTvvSQxwbihZlWeLn1JsmcAs5wmJqEFjl6wJHdxCLmPEkydwI1ssfkPGGJRSWeBLk4jvYc3+Ei7W5lbEqBt/7djejoK+P3ED/Q8SjOZg6Nr7S/9hLuMXUeeAr3M84496sPtGheGHNdvcGlxqxC1BH0D6zh1IkxME+JpqEFeolSpo2+hdOgGg6wp+60; PHPSESSID=2cjih93nmqubsf1r4k9mq8rge1; verify=0%24%24%23%23%24%241; nnmc=2502571794%40qq.com; UIDHASH=82fd5872c225c63e6d5bb8ec49361c7917167e71bdc43d0e3d169714f7a9036d; token-normal=nyCg7yspBH9XG-TsatQTrD-PNYuzsb3FxoD2_z24i7MPyf0JllHG1JF1qu3cQm8pqOD__FBoC6zSo65HQLwzhw; DEF_VIEW=4; gdpr_consent_cookie=AxZXu8GRxn; _w18g_consent=Y; tvuid=UVhoYVdIVTRSMUo0Ymc9PQ%3D%3D; mcpro=0; _abck=99C3D9D0B21D6519F2C3621F0E9C1BAD~0~YAAQRcYcuCVGVq6OAQAA+MNJyQs0HdMYnZDrge41fFRIZlU2zUzZ+4E50Ajdmt6Cl07PiawBBVPVhFbou3tQ+GzNQpL/adX59BjyizHNO0zWTF4T7vKbeJbdRPXTOYDso6i26wyD212RaF5WhFPwyv2Wsj22OxH367noF4QUj/uHJUe0gvOWMVvdMvlA7dCW+09Ij/KWx6oSFjy3HVKIL/CCUBuuHB6cB4dhtJxTBMcA6L4MK6D0SHlwQ8itu7L1o0XqYP2/NOI9+uQ7rS52T6hjTP4fzGD2E8QbzXAwSkM2AOuVtUyK9SD6tnXIars9lETcYXfWmn6rDCuVHf4gzGtDJn98//QS55VvkBqnEI6vnY1SVLWGvMTqEO6ImT17GqD33MRXrN64Ml0MoUnfZpEGwlRZ+wzcOkWp/vDd~-1~-1~1712777631; _cb_svref=https%3A%2F%2Fwww.moneycontrol.com%2Fpromo%2Fmc_interstitial_dfp.php%3Fsize%3D1280x540; dtCookie=v_4_srv_7_sn_2BB7CD9F5E0DD5AE279E3BE918E3D711_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_0; USR_DFP_TARGETING={"p_value":0,"dob":"","gender":"","income_data":"","occupation":"","industry":""}; nousersess=qse4dqkwtqoot2xt; isVistedCbPage=true; _t_tests=eyJuYTZRbDZiT0l2dEN3Ijp7ImNob3NlblZhcmlhbnQiOiJBIiwic3BlY2lmaWNMb2NhdGlvbiI6WyJEM0pHbUciLCJzaFplVyJdfSwiNklMd0YxZVNseTZqcSI6eyJjaG9zZW5WYXJpYW50IjoiQSIsInNwZWNpZmljTG9jYXRpb24iOlsiRF80UjU1Il19LCJsaWZ0X2V4cCI6Im0ifQ==; stocks=|Jio.Financial_JFS~1%7CVedanta_SG%7E2%7C3M.India_B3M%7E6%7CN_NII03%7E1%7CSoma.Textile_STI03%7E1%7CXpro.India_XI%7E1%7CYes.Bank_YB%7E1%7CN_KC18%7E1%7COrissa.Minerals_OMD%7E1; _chartbeat2=.1700241187999.1712774766253.0000000000000001.BhDIGs-8pXX833LXC2TJ5yUEDt6.5; bm_sv=E18E230D5857918870197C8A577FDEC2~YAAQ4aMQAiSW14iOAQAAMeFUyRfkKOQR1u3rCjXqf/tN5X49UkvjZtEqScGEX5wxaEDbUYKuQuAu/O5KapBr8V5HnndF6qnHWWF3ErZtCOBlGgRDlvePbt7hpFu8sJ2Nni+H2l0yc/RvXchKHyYPAr3Xb4/MxYSt3UDtDMfkgerQ5hXxPqZElbT7pr9OewZUAq/mFrNWvrs8Ir0yGdoR5tm3FoV7o0+Ec8d6+ooPy9lRFX6/TU7MNMzM7E249msed6Xw4JHwzw==~1; _ga=GA1.2.270074858.1700241157; WZRK_S_86Z-5ZR-RK6Z=%7B%22p%22%3A13%2C%22s%22%3A1712774032%2C%22t%22%3A1712774773%7D; _ga_4S48PBY299=GS1.1.1712774195.103.1.1712774864.0.0.0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}




# 从CSV读取URL的函数

def read_urls_from_csv(csv_file_path):
    urls = []
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            urls.append(row['URL'])  # 假设'URL'是URLs列的列标题
    return urls


def construct_ratio_sheet_url(base_url):
    # 分割基础URL以获取公司名称和代码
    parts = base_url.split('/')
    company_name = parts[6]
    code = parts[7]

    # 构建balance sheet的URL
    ratio_sheet_url = f"https://www.moneycontrol.com/financials/{company_name}/ratiosVI/{code}#{code}"
    return  ratio_sheet_url


# 修改脚本来处理每个URL

def write_csv_for_year(year, data, csv_header):
    csv_file_path = f'D:\Program Files (x86)\Python\PythonProject\FYP\Presentation\Financial_Parameters_Colloction\Ratio_Sheet\Company_Ratio_Sheet_{year}.csv'
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

          resp = requests.get(construct_ratio_sheet_url(url), headers=hdr)
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
        r'D:\Program Files (x86)\Python\PythonProject\FYP\Presentation\Pre_Company_List.csv')
    process_urls(urls)
