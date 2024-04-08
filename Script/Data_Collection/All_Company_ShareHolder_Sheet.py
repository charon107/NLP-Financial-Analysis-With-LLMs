import requests
from bs4 import BeautifulSoup
import csv
import json
import re
import os

def generate_new_url(base_url):
    new_url_prefix = "https://www.moneycontrol.com/mc/widget/stockshareholding/topholdingspopup?classic=true&sc_did="
    sc_did = base_url.split('/')[-1]
    return new_url_prefix + sc_did

def fetch_and_save_company_data(url):
    hdr = {
        'Cookie': 'visits=6; gdpr_userpolicy_eu=1; gdpr_region=eu; _w18g_gdpr_consent_data=personal_info_consent%3AY%23personalization_consent%3AY%23age_consent%3AY%23recommendation_adv_remarketting_consent%3AY%23adv_remarketting_consent%3AY%23marketting_communication_consent%3AY; A18ID=1700241178544.164364; _gcl_au=1.1.332455451.1700241179; _cb=CIlCKND2a_K4qgDui; WZRK_G=57a9e747c2e74a9280aefacb2587ba79; _w18g_consent=Y; __io=10b9e7344.12acd25a5_1703673960144; __io_r=mail.qq.com; __io_first_source=mail.qq.com; __io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22mail.qq.com%22%7D; _gid=GA1.2.801615192.1706521752; dtCookie=v_4_srv_6_sn_31E3A8B145A5A2765380BE57415F687B_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1; _io_ht_r=1; __io_unique_43938=29; isVistedCbPage=true; USR_DFP_TARGETING={"p_value":0,"dob":"","gender":"","income_data":"","occupation":"","industry":""}; nousersess=srxh27qqui66nsiq; _uzitok=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjc3JmIjoiZ2hhTUM5ZW9yYmdSdU5JbjczajJFUWc2QUFNanpxSzBTY1VEQXpLcTI2QzVCbWFNIiwiaWF0IjoxNzA2NTM0NzAwfQ.N0MA4oK_G484-N82HSR2MIKTtubhC_qAdp6OlY0v7yc; MC_PPID_LOGIC=0229d64202f3e21c2a3c893f014672ea; __io_lv=1706534706800; _abck=99C3D9D0B21D6519F2C3621F0E9C1BAD~0~YAAQlAUXAtwoU0eNAQAAfztmVQu+Bxol79VVzBaZRtOuVN2/EtDZ8qL0YLIuOai8Vyd9scF97sGkhTEh+QyRefO2xCVzGCvJCayYmgQkGq/Za9JNu+Ka7Aw8eLPMhyg+5jtW+AcbHRHILqdkqeHzFLQAL3yjxNb8wgfPOrUqoCQRKrBkzSwXfrCCbGz4R+4Kf84Bxn56mZhk1wXEug+LDGJya2RSXogcY/WVdsMlCovXbeDo73oQmNWIKSOk6zVvBngZdW0N+/M1wmcDFhOHoYy71NpE2iCZlc7yTrkLixqZfZ2fKzfnAmwbYHa78dWmKA2ATmTywTwKMFe5PRLPqNbetSpAv38qDXLzP0EtORneHX7euE80mVzql8TyIRD037vJLNlBx7H5I/RqTXA0zcaoCc7XeT8KbJn/TNSS~-1~-1~1706538367; ak_bmsc=36124D451347BE886D035E3B8CDD8AC4~000000000000000000000000000000~YAAQlAUXAvMoU0eNAQAA7jxmVRbfZ+nebzMPc/XdA78O/iXoPbp3NBT4n37LLV3rKo/+9WgM4hMxzxRD/N+CQUJA4s3KYZyroaXpA/ztGQfvIQo1nAB0eZOGh46PKwEQGqfT8wfeLrL5kbaSOWc5L0oPTupYIi9ERb0nzeCsE0NUdClFoI0quz2p9GEy/EBdYOhFx/zqB54SxYzoBelDprLhiodis0xbSxtDlr95nkzX6hftIwIla+xbIqighmpJYQS5A/sFwxyCD4IoISDYFyJ2nZ5O8/bwhccHLH78aHZwtuZKRuAdT4VxK7JdzmBKnslVAho8J3v3+O8m3RPHOynnC/84oQ68XgT2tW1cFcVf1eMJWOM+D9bm5K8qRHdWQ5NOCcCkPbhaKeErckYO5P4vuquLU+Vq/cSVGTGYgFOOtJrErBpB6K+VXIZ0+2eOZXx0jIfCM48iBTLUvqncCJXEhy3Bgv9yLKv9nfG2KtFOBNpXJMlaNNsiDfaEYDpx7ZzIBi/s; verify=%24%24%23%23%24%241; nnmc=Charon+Li; UIDHASH=d9025f4728fc800e6e6395a4c431df9a58beafc2e7099f2adc47c8d5cc42d3c3; token-normal=qiAfBsg1Cu5dRhiBfqdRHTID5g3HC2zR1ZzGowKN6WJcxE7wZaSXXBVCbjawY-FzSmEyjANFm7d_gJcmGCkgmw; DEF_VIEW=4; tvuid=VlZoa1EycDJSMEY1TWc9PQ%3D%3D; mcpro=0; gdpr_consent_cookie=UXdCjvGAy2; bm_sv=1D9CA9D19716327EDD436D6249E5FA8E~YAAQlAUXAgEsU0eNAQAAZV9mVRaHyaSziBa72Jh5DyiuVVCVp/CPtHiBqHEd3jIVheHz1nSRT61irBkWwcwt1I8PQgF74PI1yIo9NUfQcpz5WfLNaYjftPf3zJkMj6XXC1TNyvmPN4VBvXXPuuDUByr77qKQaFV8uFP7AiWrtFMki3/uq3c5eiTqIzo66WKAUabMqFOyugaPr/2CSQ+1vftkVMrSBsl4jrAIjYCv1LEQ7g62Na3eHh5ydNKbsfKKe2pMot2/~1; PHPSESSID=oeqlat69bun9aba62rtjef1p06; MC_WAP_INTERSTITIAL_NEW_LOGIC_20240129={"0":"https://www.moneycontrol.com/financials/a&mfebcon/consolidated-ratiosVI/F03#F03","1":"https://www.moneycontrol.com/financials/a&mfebcon/ratiosVI/F03#F03","2":"https://www.moneycontrol.com/financials/indianrailwayfinancecorporation/ratiosVI/IRF#IRF","3":"https://www.moneycontrol.com/india/stockpricequote/infrastructure-general/abinfrabuild/I07"}; _ga_4S48PBY299=GS1.1.1706534312.22.1.1706541378.0.0.0; _ga=GA1.1.270074858.1700241157; _gat=1; stocks=|A.B.Infrabuild_I12~6%7CN_JB02%7E9%7CN_F04%7E7%7CIndian.Railway_IRF%7E2%7CReliance_RI%7E2%7CN_SGBOC5960%7E1%7C3M.India_B3M%7E14%7CIWML_IIFLW54277%7E14%7CAdani.Energy_AT18%7E2%7CZydus.Wellness_CNA%7E6; _chartbeat2=.1700241187999.1706541379308.0011101011100001.BUEGETHSzyoQjpMF2llIODGa_1O.1; _cb_svref=external; WZRK_S_86Z-5ZR-RK6Z=%7B%22p%22%3A33%2C%22s%22%3A1706536123%2C%22t%22%3A1706541385%7D',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }
    resp = requests.get(generate_new_url(url), headers=hdr)
    soup = BeautifulSoup(resp.text, 'html.parser')
    script_tag = soup.find('script', string=re.compile('var tophold_jsn'))

    if script_tag:
        match = re.search(r'var tophold_jsn = (\'{.*?}\')|(\"{.*?}\");', script_tag.string, re.DOTALL)
        if match:
            json_str = match.group().split(' = ')[1].rstrip(';')
            json_str = json_str[1:-1]
            try:
                tophold_data = json.loads(json_str)
            except json.JSONDecodeError as e:
                print(f"JSON解析错误: {e}")
                return
        else:
            print("未找到名为'tophold_jsn'的JSON数据。")
            return
    else:
        print("未找到包含'tophold_jsn'的<script>标签。")
        return

    resp2 = requests.get(url, headers=hdr)
    soup2 = BeautifulSoup(resp2.text, 'html.parser')
    company_name_element = soup2.select_one('div.div_desktop div.name_left.topsel_tab div#stockName.inid_name > h1')
    company_name = company_name_element.get_text(strip=True) if company_name_element else None
    # 省略了从soup中提取公司名称的代码部
    # 定义输出文件名
    output_filename = os.path.join(r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report', f"{company_name}_ShareHoder_Sheet.csv")
    # 保存到CSV的代码部分（省略了为简化）

    # 定义时间段列表
    select_tag = soup.find('select', {'id': 'quarter_ending_date'})
    options = select_tag.find_all('option') if select_tag else []

    # 构建time_periods列表，使用列表推导式从每个<option>标签提取内容
    time_periods = [option.get('value') for option in options]

    # 打开一个CSV文件准备写入
    with open(r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\All_Companies_ShareHolder_Sheet.csv',
              'a', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([f'Company Name:  {company_name}'])

        # 遍历每个时间段
        for period in time_periods:
            # 写入时间段作为标题
            csvwriter.writerow([period])
            # 写入股东名称和持股百分比的列标题
            csvwriter.writerow(['Name', '% Holding'])

            # 提取当前时间段的所有股东持股信息
            holdings = []
            for category, data in tophold_data[period].items():
                for item in data:
                    name = item.get('name')
                    holdingPercentage = item.get('holdingPercentage')
                    if name and holdingPercentage:
                        holdings.append((name, holdingPercentage))

            # 根据持股百分比降序排列
            holdings.sort(key=lambda x: float(x[1]), reverse=True)

            # 写入股东持股信息到CSV
            for name, holdingPercentage in holdings:
                csvwriter.writerow([name, holdingPercentage])

            # 在每个时间段之间添加一个空行以分隔
            csvwriter.writerow([])

# 读取所有公司的财务数据CSV
with open(r'D:\Program Files (x86)\Python\PythonProject\FYP\Financial Report\All_Companies_Financial_Data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row['URL']
        fetch_and_save_company_data(url)
        print(f"处理完毕：{url}")
