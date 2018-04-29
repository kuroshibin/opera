#ServerInfo.py

class Info:

    def __init__(self, get):
        self.get = get

    def get_info(self):
        if self.get.lower() == 'uid':
            return '0x00000000'
        if self.get.lower() == 'heap':
            return '0x8000-0x1000000'
        if self.get.lower() == 'name':
            return 'simple Server'
        if self.get.lower() == 'about':
            return 'linux version'
        if self.get.lower() == 'ver':
            return '1.0.0b'
        if self.get.lower() == 'date':
            return '25-10-2016'
        if self.get.lower() == 'by':
            return 'www.eyecodec.com'
        if self.get.lower() == 'mail':
            return 'shaikatssj2@gmail.com'
        if self.get.lower() == 'remode':
            return 'Shaikatssj'