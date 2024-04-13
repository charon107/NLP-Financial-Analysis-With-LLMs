import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm


base_url = 'https://www.moneycontrol.com/india/stockpricequote'
alphabets_order = ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
'U', 'V', 'W', 'X', 'Y', 'Z', 'others']



hdr = {
    'Cookie': 'gdpr_userpolicy_eu=1; gdpr_region=eu; _w18g_gdpr_consent_data=personal_info_consent%3AY%23personalization_consent%3AY%23age_consent%3AY%23recommendation_adv_remarketting_consent%3AY%23adv_remarketting_consent%3AY%23marketting_communication_consent%3AY; A18ID=1700241178544.164364; _cb=CIlCKND2a_K4qgDui; WZRK_G=57a9e747c2e74a9280aefacb2587ba79; __io=10b9e7344.12acd25a5_1703673960144; __io_r=mail.qq.com; __io_first_source=mail.qq.com; __io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22mail.qq.com%22%7D; MC_PPID_LOGIC=0229d64202f3e21c2a3c893f014672ea; _gcl_au=1.1.1752714702.1708336554; __utma=129839248.907922309.1708339106.1708339106.1708339106.1; __utmz=129839248.1708339106.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); FCCDCF=%5Bnull%2Cnull%2Cnull%2C%5B%22CP6OgQAP6OgQAEsACBENAnEgAAAAAEPgABBoAAAOhQD2F2K2kKFkPCmQWYAQBCijaEAhQAAAAkCBIAAgAUgQAgFIIAgAIFAAAAAAAAAQEgCQAAQABAAAIACgAAAAAAIAAAAAAAQQAAAAAIAAAAAAAAEAAAAAAAQAAAAIAABEhCAAQQAEAAAAAAAQAAAAAAAAAAABAAA%22%2C%222~~dv.2072.70.89.93.108.122.149.196.2253.2299.259.2357.311.313.323.2373.338.358.2415.415.449.2506.2526.486.494.495.2568.2571.2575.540.574.2624.609.2677.864.981.1029.1048.1051.1095.1097.1126.1201.1205.1211.1276.1301.1344.1365.1415.1423.1449.1451.1516.1570.1577.1598.1651.1716.1735.1753.1765.1870.1878.1889.1958%22%2C%22C91689C5-A821-4ABC-9EE5-BA5855256A0A%22%5D%5D; _is_in=0; verify=0%24%24%23%23%24%241; nnmc=2502571794%40qq.com; UIDHASH=82fd5872c225c63e6d5bb8ec49361c7917167e71bdc43d0e3d169714f7a9036d; token-normal=nyCg7yspBH9XG-TsatQTrD-PNYuzsb3FxoD2_z24i7MPyf0JllHG1JF1qu3cQm8pqOD__FBoC6zSo65HQLwzhw; DEF_VIEW=4; gdpr_consent_cookie=AxZXu8GRxn; _w18g_consent=Y; tvuid=UVhoYVdIVTRSMUo0Ymc9PQ%3D%3D; nousersess=qse4dqkwtqoot2xt; isVistedCbPage=true; _gid=GA1.2.889282728.1712933559; _abck=99C3D9D0B21D6519F2C3621F0E9C1BAD~0~YAAQlAUXAjzpJcmOAQAAoHHT1wveqQ7uk/QjOj/bea0e9E5dmZqCNdOMqHaiuQu/r9AZFFUUd16ArbQbEp6D8GFhCp3OLAq1vCQ/m50hmUxSwn3/IFud1zsi6a/mJNauWysjPrQTgwiu7wsqBtDA77RgLLbN2qJ3U+2ET9zL1N+GCnfDGCX/z3/E0ps60MDDfHNRuvDgH/fu4TTmmU9WD7DU85oD81hxSQD2pTKUv9cBWcbuUbCwOW1oYl6wbrid80RodFpUvTAMq5QnIY7qVP8ccyeKeZNmXSqwPAqyZ2bVsSjKTJkVrjFB7PX/0zpZUZhR7KY9X6Q2/jNLFM4kNciu295hU9fwm6iAkGalBDwcap26yqVXBOjMwngkxBjlPGHIQzwnLvjFWkreGo9qVejYBAjM/Zq1T3sS2w2w~-1~-1~1712777631; bm_sz=9B55AE92BE670869DB1FDF93DB0FA744~YAAQlAUXAj/pJcmOAQAAoHHT1xc+6Sk3htsRnS3ja3QqZov8Sb06n+0XRpdmt1hyg0Hyw4Dkmn1t3l5cQKVGXk4SecMyrr700PUuoSn0BYMRabH/emiLvpPT4iMbdBf3tBwytmAmuuBITSRcGVOMpUO6c+mgIAOy5IzmTZOejKxK9rnsOWFx8uaHnUZrLS4zbie2X6t483wNp2Oc+cerzwB4pKRfIF+IIOdwOwp3/8+JyQ0fJnV4zk7Bcb22VlnRhPbDIAgD4ffJHPrDOEVZ47WYAPn6VhP56y8x+GerlQK1bewwCP1bRz+eNXO2Lp1D9NxDVyJNlFdB8fss4nItdz8FNpZkbr5bDA3t4kEwCkHhKSfqdCECbCI6GR8=~4339504~4534849; bm_mi=B5218758A3028BEBF847080E0D1D5AC7~YAAQsgUXAo3+8quOAQAA33LT1xdwwLMY+CSWOwCiS5fOgnjQ9l4mjHGbsH7IC5mYYwt692YDJzFkdDyXeQZBD4M7de8rtHSfIJ0QnxPDZxQsS3U2fPDkYJSkmqSA6L5F/dhaqOSuFUPRu//WHhZf8TMr3T3DzHY5r5j29i0/MG2e+/rEF1Q38nIK096vBb6uprGRjaOXV8JSC56zUVXie4kAQ5vlsDpR/xObZ2ugxCbS4f8tc/6NyifuGAgnxFggsZqfEdd3eqOtSkxRgaJqcQ/36VouAORB7Q1w/H3Xg5BCVU5uDpwimxA4JnbY6clHN9MTF5CmsLWcEehjJp1HsDEnjdWpOa3p0gpV4leH2uCy33lccWE=~1; _sharedID=f8f2db9b-ada8-4607-a5e7-c758ea29c010; _sharedID_cst=zix7LPQsHA%3D%3D; __eoi=ID=99b902929c1b2050:T=1713017942:RT=1713017942:S=AA-Afjb1FEWHShumZ0POB9xbzepz; ak_bmsc=D4BEA5892A47FFAF34C179EC8A94DA74~000000000000000000000000000000~YAAQlAUXAvLpJcmOAQAA3ofT1xfi+ckwm1Bmb+E64w62VVhmY26ppc3wDebnsHW4zdVOHE3sGtmslx0pabZm7ZSu22zN1HtqM8DeQxDVnvYT/jWNnImS/M5cJdsF/3u7w50MqTppfQs5SGsdZYqITd9Q0R3hj9j4jbQqjJy5xuW1KNCJ7+6TI3PmRia1cgOHlv+0U/Of91teKe+CyJseYXequD3YmypUsq78Ct/fHCvdXJGao32U5NMgDaFcWin1Acp3i+bTcFM5KTumodDcYvE9AJfXe9GmXIa1cOr7FYvFwtl+xwfvNG5xRZkW/h/BDe9zbB9CeqMlXX80CXiXszjaAIBDWPcmnLSAWOWM8xaqLSG19DRrPlF7zMESbZzHGCKH8xYCCFDzlyUMPEXHyvyu0ATmHmAoSrf9Ut68n80MMJY1ZwltGwyt5VXEfyGtKHm3AQqzi7Bpl5ZveMIv5ZOkv6GferSElJikyOqmPDJptUDSpRZA9a1K17kh8g7re9Zfbc+4PKKqDw==; _t_tests=eyJUSHNKdzh6cnBrY2ttIjp7ImNob3NlblZhcmlhbnQiOiJBIiwic3BlY2lmaWNMb2NhdGlvbiI6WyI0dXNxaiIsIkNEVUZBOSJdfSwibmE2UWw2Yk9JdnRDdyI6eyJjaG9zZW5WYXJpYW50IjoiQSIsInNwZWNpZmljTG9jYXRpb24iOlsiQnZSX0JwIl19LCJsaWZ0X2V4cCI6Im0ifQ==; dtCookie=v_4_srv_3_sn_C9AC2C58F2802E1C890B5005FB220CD7_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_0; USR_DFP_TARGETING={"p_value":0,"dob":"","gender":"","income_data":"","occupation":"","industry":""}; _io_ht_r=1; __io_session_id=143f627c5.76624b7c1_1713023532045; __io_unique_43938=13; __io_visit_43938=1; PHPSESSID=g1jqphpj4tjcgsn4aac1h1h434; stocks=|Godrej.Consumer_GCP~1%7CCommercial.Eng_CEB%7E1%7CHindalco_H%7E1%7CDabur.India_DI%7E1%7CBLS.Internation_BLS%7E1%7CAjanta.Pharma_AP22%7E1%7CAditya.Birla.F_PFR%7E1%7CIWML_IIFLW54277%7E1%7CTCS_TCS%7E1%7CAgarwal.Ind_BBR%7E1%7CIdea.Cellular_IC8%7E2; _ga_4S48PBY299=GS1.1.1713023281.106.1.1713023650.0.0.0; _ga=GA1.2.270074858.1700241157; _gat=1; _chartbeat5=; __io_d=4_1767915979; __io_nav_state43938=%7B%22current%22%3A%22%2Findia%2Fstockpricequote%22%2C%22currentDomain%22%3A%22www.moneycontrol.com%22%2C%22previous%22%3A%22%2Findia%2Fstockpricequote%22%2C%22previousDomain%22%3A%22www.moneycontrol.com%22%7D; __io_lv=1713023955778; _chartbeat2=.1700241187999.1713023955932.0000000000001011.RIVkMDTgJ4yDCu_MlvulI2zmmHM.1; _cb_svref=external; WZRK_S_86Z-5ZR-RK6Z=%7B%22s%22%3A1713023940%2C%22t%22%3A1713023961%2C%22p%22%3A6%7D; bm_sv=C2CB5BFD6B86F8DB2E4657F45352ABA2~YAAQsgUXAkQ396uOAQAArmIv2Bf6hb7m5tRomvLAo8u+4UwToLQV699wViv06+z5GvfyCrCwv+13gpGlFCiecWHhgW6ULWEgi6wu4f5/a1/3dkBF1jaD8wLLbLdk4wGZK1WuxALSLbuX0l78FpafoOcFRK+zwAktSZcMgQFU5E6oRdHd5bBXro8iRC+4pEek9Wg/2ka40GG42UXE3ALITsJQYbNdvTivEe7DuHw1FE2H94dLQx6NMcGFvEHfSzRqC9EQFtF+gQ==~1; _chartbeat4=t=B0vzbSBvZm-oCihy4YjobbvCllQrQ&E=0&x=0&c=0.18&y=4888&w=181',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

companies = []

# 使用tqdm包装字母列表以显示进度
for alp in tqdm(alphabets_order, desc="Crawling companies"):
    url = base_url.replace('/A', f'/{alp}')
    hdr['path'] = url
    response = requests.get(url, headers=hdr)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 找到所有公司名和链接
    for link in soup.find_all('a', class_='bl_12'):
        company_name = link.text.strip()
        company_url = link.get('href')
        companies.append([company_name, company_url])

# 将公司数据保存到 CSV 文件
csv_file = 'D:\Program Files (x86)\Python\PythonProject\FYP\Presentation\All_Company_List.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'URL'])  # 写入表头
    writer.writerows(companies)  # 写入数据

print("数据已保存到", csv_file)