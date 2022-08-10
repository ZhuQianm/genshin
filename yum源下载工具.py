import urllib.request
from bs4 import BeautifulSoup
import ssl
context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context
html_doc = "https://10.1.85.253/NS/V10/V10SP1.1/os/adv/lic/base/x86_64/Packages/"
req = urllib.request.Request(html_doc)
webpage = urllib.request.urlopen(req, context=context)
html = webpage.read()
soup = BeautifulSoup(html, 'html.parser')
yum_rpm = []
for k in soup.find_all('a'):
    if "rpm" in k.string:
        yum_rpm.append(k.string)
    else:
        continue
print("list download is ok")
i = 0
for line in yum_rpm:
    i+=1
    url = html_doc + line
    print(url, line)
    urllib.request.urlretrieve(html_doc + line, line)
print("下载完成，共{}个包".format(i))
