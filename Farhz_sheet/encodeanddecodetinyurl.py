class Codec:
    def __init__(self):
        self.sh = 'http://tinyurl.com/'
        self.sp = ''


    def encode(self, longUrl: str) -> str:
        self.sp = longUrl

        return self.sh+"826"


        """Encodes a URL to a shortened URL.
        """
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.sp
 #try below for better       
class Codec:
    def __init__(self):
        
        self.store = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        v = hash(longUrl)
        self.store['http://tinyurl.com/' + str(v)] = longUrl
        return 'http://tinyurl.com/' + str(v)
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
       
        return self.store[shortUrl]
        
