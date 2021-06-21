from shelly.device import Device


class Plug(Device):
    def getPower(self):
        return self._get("/meter/0")
    
    def getRelay(self):
        return self._get('/relay/0')
