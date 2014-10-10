import requests

class hydra():
    def __init__ (self, url, cachetime = 60):
        self.url = url
        self.cachetime = cachetime
        self.update_server_list()

    def get_list(self, force=False):
        if force is True or (time.time() - self.last_update) > self.cachetime:
            self.update_server_list()
        return self.server_list

    def update_server_list(self):
        try:
            self.server_list = requests.get(self.url).json()
            self.last_update = time.time()
        except:
            print "ERROR: update server_list"