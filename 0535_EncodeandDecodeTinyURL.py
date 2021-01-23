import random
class Codec:

    def __init__(self):
        self.alpha = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.UrlMap = {}
        self.key = self.getRandId()
        
    def getRandId(self):
        identifier = ""
        for _ in range(6):
            i = random.randint(0, len(self.alpha)-1) # randint is boundary inclusive 
            identifier += self.alpha[i]
        return identifier
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        Random fixed length (6 digits) encoding
        """ 
        while self.key in self.UrlMap:
            self.key = self.getRandId()
        self.UrlMap[self.key] = longUrl
        return "https://tinyurl.com/" + self.key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.UrlMap[shortUrl.split("/")[-1]]      
