import xml.etree.ElementTree as ET

import requests


def get_articles():
    r = requests.get("https://medium.com/feed/@niranjannb7777")
    tree = ET.fromstring(r.text)

    out = []
    for item in tree.iter("item"):
        title = item.find("title").text
        link = item.find("link").text
        date = item.find("pubDate").text

        out.append({
            "title": title,
            "link": link,
            "date": date,
        })
    return out
