from urllib.request import Request, urlopen
from urllib.parse import urlencode
import os.path

##WIP Doesn't work

headers = {
    # 'Host': 'adventofcode.com',
    # 'User-Agent': r"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
    # 'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'DNT': '1',
    # 'Connection': 'keep-alive',
    'Cookie': 'session=53616c7465645f5f71caae02e35ec32a12b01b6bfdb97b6c5a80739f6e5ccbcf9c7f9a7206474ac445b2ac1a67dbde05',
    # 'Upgrade-Insecure-Requests': '1',
    # 'Cache-Control': 'max-age=0'
}

def get_input(day):
    fname = f'day{day}_input.txt'
    if os.path.exists(fname):
        with open(fname) as f:           
            return f.read()
    url = f'https://adventofcode.com/2018/day/{day}/input'
    req = Request(url, headers=headers, method='get')
    with urlopen(req) as response:
        if response.code == 200:
            inp = response.read()
            with open(fname, 'w') as f:
                f.write(inp)
            return inp

if __name__ == "__main__":
    get_input(4)