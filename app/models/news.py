
class Source:
    '''
    News Source class to define Source Objects

    '''      
    def __init__(self, id, name, description, url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        
class Article:
    '''
    News Article class to define Article Objects

    '''

    def __init__(self, id, title, description, url, urlToImage, publishedAt, content):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content