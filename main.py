import datetime

from jinja2 import Environment, FileSystemLoader

from utils.articles import get_articles
from utils.handles import get_handles

data = {'job': 'Software Developer/Backend Developer', 'place': 'Kerala, India', 'header': 'images/header.jpeg',
        'profile_url': 'https://github.com/niranjanneeru', 'handles': get_handles(), 'articles': get_articles(),
        'date': datetime.date.today().strftime("%d %B %Y")}

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("main.jinja")

content = template.render(data)

with open("README.md", mode="w", encoding="utf-8") as file:
    file.write(content)
