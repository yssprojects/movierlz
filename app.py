from flask import Flask ,render_template, request, redirect
import requests
from bs4 import BeautifulSoup
import json
app = Flask(__name__)
#a = input("enter Your Url \n")
#print("<------Getting Information---------->")
@appi.route()
def home:

    url = "https://4movierulz.lv/"
    res = requests.get(url).content
    soup = BeautifulSoup(res,'html.parser')
    image = soup.find_all("img",class_="attachment-full size-full wp-post-image")
    images = []
    names = []
    index = 1
    for links in image:
        names.append(links['alt'])
        images.append(links['src'])
    data = {'movie':names,'image':images}
    d = json.dumps(data)
    return d

if __name__ == "__main__":
     app.run(host="0.0.0.0",port= 5000)