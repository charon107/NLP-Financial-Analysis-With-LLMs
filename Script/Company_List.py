import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

base_url = 'https://www.moneycontrol.com/india/stockpricequote'
alphabets_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z', 'others']

headers = {
    'authority': 'www.moneycontrol.com',
    'method': 'GET',
    'path': '/india/stockpricequote/A',
    'Cookie': 'gdpr_userpolicy_eu=1; gdpr_region=eu; _w18g_gdpr_consent_data=personal_info_consent%3AY%23personalization_consent%3AY%23age_consent%3AY%23recommendation_adv_remarketting_consent%3AY%23adv_remarketting_consent%3AY%23marketting_communication_consent%3AY; A18ID=1700241178544.164364; _gcl_au=1.1.332455451.1700241179; _cb=CIlCKND2a_K4qgDui; WZRK_G=57a9e747c2e74a9280aefacb2587ba79; _w18g_consent=Y; __io=10b9e7344.12acd25a5_1703673960144; __io_r=mail.qq.com; __io_first_source=mail.qq.com; __io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22mail.qq.com%22%7D; MC_PPID_LOGIC=454d3594c7d1374dbdb3652359de4bb9; UIDHASH=82fd5872c225c63e6d5bb8ec49361c7917167e71bdc43d0e3d169714f7a9036d; gdpr_consent_cookie=AxZXu8GRxn; tvuid=UVhoYVdIVTRSMUo0Ymc9PQ%3D%3D; stocks=|3M.India_B3M~14%7CIWML_IIFLW54277%7E14%7CAdani.Energy_AT18%7E2%7CZydus.Wellness_CNA%7E6%7CAdani.Enterpris_AE01%7E2%7CAU.Small.Finance_ASF03%7E3%7CAstral.Poly.Tec_APT02%7E1%7CAbbott.India_KP%7E6%7CABB.India_ABB%7E3%7CAAVAS.Financiers_AF32%7E1; _ga_4S48PBY299=GS1.1.1706064481.19.1.1706072831.0.0.0; _ga=GA1.2.270074858.1700241157; _gid=GA1.2.801615192.1706521752; dtCookie=v_4_srv_6_sn_31E3A8B145A5A2765380BE57415F687B_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1; _io_ht_r=1; __io_session_id=53e7424dc.09af67059_1706522286346; __io_unique_43938=29; isVistedCbPage=true; __io_visit_43938=1; bm_sz=5E7879FE1E20742587DA3E0E2312671F~YAAQigUXAr+O01GNAQAAgNrjVBZV8X+eXbI42VVtCxsTI8IR+xAC9txXSs29sWa3jFBab6KhMGMD8W+S+0PdZkALJA2Ngn071BPtHwsurmMfkxQMlHBolwaAMpZMuCB92usoXGfxVSk8CpIyJzvmzjmpolYgYwqZstknCoSovMLsFX1dJB4ttQCOCUjIT6wyMJRoHfVyAaJXH5EzviZ9omyLoy7vsRIpSzkRKFhpPvOkijSN7AOMB6pKdJAmxtHTIlD3OX7vge5QPcPwTbdXtGQ4Fh/N0ju+5YK6XRwNwj1uqxWttEURzJBWnbcs5Cqvmw+jzhVzkxDOcn5hFCO4Zs9zOA==~3159107~4536631; ak_bmsc=DA1FC317F5DC3B969269D352425558D5~000000000000000000000000000000~YAAQigUXAhGP01GNAQAAv97jVBYvMw/RdzulL6gDyAkqmhkfCpi1suCEJd/4KyqZTFcI4rZmMdaQLlY/65qodByaHAdeQD63ud31JjrrsnvkdusdQjUNk3cv+sAlDkDdO24Bg4d3L0oLbZ1+ElezJ0HhDbGrKLzu5PmV1F21Ow4YaverpzIoZPLDjDNmq37wLx/Abi3mbrYTE+KD167sfIjvG26ZuTfy38V8yaFdk2hiwArjYIMP+28Jlp8wZoZJadujgFkWzQ2i16S31GKhAC1hlwvj2vDd3kMY/i+scdF9rphf0rIf+4Hn/3nCCaFaUeNv8mRavlZxELoeOkmKG1yN5ulWiegV1HDNm9DNzejGxaplL+EP0W0pTn4I8ex7sRPWJTfZUJkWvaxTTkZsT4HSiUOd8DKA7C6yyiqCfmprfrEQxblZSHXx6lBk7LdcDfEaz0dCvYy8X2Tg+mteXi81TTzDDMn1Ltho6MVWS1HB8vZGQlnT483k0rF9NaqTdRu9Sy3S; PHPSESSID=43d0dcejh4m6rdffgmpecgoht0; verify=0%24%24%23%23%24%241; nnmc=2502571794%40qq.com; token-normal=nyCg7yspBH9XG-TsatQTrD-PNYuzsb3FxoD2_z24i7NoJMxHL5uPP7wtIpibi3oKjnaMEuRv5vGT-UjvoSsyDA; DEF_VIEW=4; mcpro=0; _abck=99C3D9D0B21D6519F2C3621F0E9C1BAD~0~YAAQigUXAjiQ01GNAQAAA/PjVAsLmgKBacFt2iItosKdQ9pi8dZcUZvgOCZZGE1mupCXAu3MdXIm+lmuhDT7Y9eTz7ohmdeBQifqP+1tgpdRwhNtdkyZEVnT5vhHmJAZKaaP4U66gP30jlg+rJBdeQhS7gMkYVTJAS1iXeD1NxS28iuFK+tKxe1M/Nf9aeKXVCy+pS4MnESbyYM4gxiEhN/OLtZhr9Hzu62C+UTFvD86h6XsPbV1DJ24sRPZ5JUi81zPajAQ9x90uk36AFxfmWII/hUsnoSNmmGItvIjKQareh41XVZ9xYF32/f7AjWXbR2L5T267ImTr+yQutYVzhI9UylgzDjj/zMwt+OgwL/KfE7/nqka4ihnH3PBrylKHYm2Z/nQ4qJlyq7s1O2VzngDUtCcHSKX+bGs+tu7~-1~-1~1706529794; bm_sv=614EC8BE1EBDED9B18BF99A3292ACDA2~YAAQigUXAjmQ01GNAQAAA/PjVBYYGYyMDNzaRMTLSyy9Ms/PfYXMuKUjg6kCpNuVGhtDwxYwjdxXWK/NgkxmFlh/5wwAjwXMoCfqfHxDRl3uHs1Qk6HlpOne7Mp4PocaMhasHkuPWtxzh6hStmMIRlReYDS/KCBZn4K/Kl2OvrYkK/zSWFhTxoJnwlmZBSb4ZD3t4sc3SsPM3u7UVB9HLwqZpcx2/+FJH2Cr4ERv8TX36kMQOdw4QJ+FUDRvm5vrt3MENCb7~1; USR_DFP_TARGETING={"p_value":0,"dob":"","gender":"","income_data":"","occupation":"","industry":""}; __io_d=3_883510103; _gat=1; __io_nav_state43938=%7B%22current%22%3A%22%2Findia%2Fstockpricequote%2FA%22%2C%22currentDomain%22%3A%22www.moneycontrol.com%22%2C%22previous%22%3A%22%2Findia%2Fstockpricequote%2FA%22%2C%22previousDomain%22%3A%22www.moneycontrol.com%22%7D; __io_lv=1706526577998; _chartbeat2=.1700241187999.1706526578108.0011101011100001.DZg99OknMurBBd2ABCivavOmmm3l.1; _cb_svref=external; WZRK_S_86Z-5ZR-RK6Z=%7B%22p%22%3A26%2C%22s%22%3A1706521753%2C%22t%22%3A1706526578%7D',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': "document",
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

companies = []

for alp in alphabets_order:
    url = base_url.replace('/A', f'/{alp}')
    headers['path'] = url
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 找到所有公司名和链接
    for link in soup.find_all('a', class_='bl_12'):
        company_name = link.text.strip()
        company_url = link.get('href')
        companies.append([company_name, company_url])

# 将公司数据保存到 CSV 文件
csv_file = 'D:/Program Files (x86)/Python/PythonProject/FYP/Data/Company_List.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'URL'])  # 写入表头
    writer.writerows(companies)  # 写入数据

print("数据已保存到", csv_file)
