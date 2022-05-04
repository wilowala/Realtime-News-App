from flask import render_template
from . import main
from ..request import get_news, get_sources, get_local_news


@main.route("/")
def index():
    sources = get_sources()
    news = get_news()
    local = get_local_news()
    return render_template("index.html", sources = sources, news = news, local = local)

@main.route("/news")
def news():
    news = get_news()
    local = get_local_news()
    return render_template("news.html", news = news, local = local)
