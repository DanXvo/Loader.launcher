import os
import sys
import requests

class download:
    def __init__(self, url, savefile, savedir, version="0.0.1"):
        self.url = url
        self.version = version
        self.savefile = savefile
        self.savedir = savedir
    
    def download(self):
        self.r = requests.get(self.url)
        with open(self.savedir + self.savefile, 'wb') as file:
            file.write(self.r.content)
    
    def autorun(self):
        self.autorun_filename = self.savedir + self.savefile
        os.system(self.autorun_filename)

if __name__ == "__main__":
    try:
        if sys.argv[1] == "--downlaod":
            filedownlaod = download(sys.argv[2], sys.argv[3], sys.argv[4])
        
        else:
            print("using flag --downlaod <url>, <save_filename>, <save_dir>")
    except:
        exit(1)