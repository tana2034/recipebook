import re

class Validator():
    alnumReg = re.compile(r'^[a-zA-Z0-9]+$')
    urlReg = re.compile(r'http(s)?://([\w-]+\.)+[\w-]+(/[-\w ./?%&=]*)?')


    def isAlNum(self, value):
        return self.alnumReg.match(value)


    def isUrl(self, value):
        return self.urlReg.match(value)
        
