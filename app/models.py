class Source:
    """Source Class to create the source object"""
    all_sources = []
    def __init__(self, name, description, url ):
        self.name = name
        self.description = description
        self.url = url

    def save_sources(self):
        Source.all_sources.append(self)


class News:
    """News Class to create the news object"""
    all_news = []

    def __init__(self, urlToImage, title, description, name, publishedAt, url  ):
        self.urlToImage =  urlToImage
        self.title= title
        self.description = description
        self.name = name
        self.publishedAt = publishedAt
        self.url  =url 
    
    def save_news(self):
        News.all_news.append(self)