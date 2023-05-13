import requests
from tqdm import tqdm
from os import path
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def dl(url: str):
    print("Please note that this downloader needs to close the system proxy!")
    # 用流stream的方式获取url的数据
    resp = requests.get(url, stream=True, verify=False, allow_redirects=True)
    # 拿到文件的长度，并把total初始化为0
    total = int(resp.headers.get('content-length', 0))
    # 从url中获取文件名
    filename = path.basename(url)
    # 初始化tqdm，传入总数，文件名等
    with open(filename, 'wb') as file, tqdm(
        ncols=100,
        desc=filename,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)
