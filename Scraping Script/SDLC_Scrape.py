import requests

testdate = '30/08/2024'
url = 'https://www.delhisldc.org/Loaddata.aspx?mode='+testdate

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-GB,en;q=0.9',
    'cache-control': 'max-age=0',
    'connection': 'keep-alive',
    'cookie': 'ASP.NET_SessionId=t3tofjp4jvmqabh0fyfvmdsi',
    'dnt': '1',
    'host': 'www.delhisldc.org',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}
splits = ['09:00', '12:00', '15:00', '21:00']
month = '08'
year = '2024'

fp = open('EnergyData.txt', '+a')
for day in range(1, 32):
    date = str(day).zfill(2)+'/'+month+'/'+year
    Xurl = 'https://www.delhisldc.org/Loaddata.aspx?mode='+date
    response = requests.get(Xurl, headers=headers)

    print('Writing:', date)
    fp.write('\n\n'+date)
    for i in splits:
        val = i+' '+response.text.split(i)[1][9:17]
        #val = response.text.split(i)[1][9:17]
        print('Writing:', val)
        fp.write('\n'+val)
fp.close()