import requests


class Device:
    def __init__(self, ip):
        self.ip = ip
    
    def _get(self, path):
        r = requests.get("http://{0}{1}".format(self.ip, path))
        return r.json()
    
    def getInfos(self):
        return self._get("/shelly")
    
    def getSettings(self):
        return self._get("/settings")
    
    def getHostname(self):
        return self.getSettings()['device']['hostname']
    
    def getStatus(self):
        return self._get("/status")

