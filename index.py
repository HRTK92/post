import asyncio
import datetime
import time

import aiohttp
import requests
from colorama import Fore, Back, Style


def time_display():
    dt_now = datetime.datetime.now()
    return dt_now.strftime('[%H:%M:%S]')


def post(url):
    url = url.rstrip('\n')
    print(f'{Fore.GREEN}[{time_display()}] {Style.RESET_ALL}{Style.DIM}[sending...]{Style.RESET_ALL}   {Style.DIM}{url}{Style.RESET_ALL}')
    requests.post(url)
    print(f'{Fore.GREEN}[{time_display()}] {Style.RESET_ALL}{Fore.GREEN}[Done]{Style.RESET_ALL}   {Style.DIM}{url}{Style.RESET_ALL}')



with open("list.txt", "r") as file:
    file_list = file
    while True:
        for url in file_list:
            post(url)
        time.sleep(10)
