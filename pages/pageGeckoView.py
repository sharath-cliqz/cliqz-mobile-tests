from utils import AllUtils
from common.exceptionList import GeckoFailure

class GeckoView(AllUtils):

    def __init__(self, settings):
        self.settings = settings

    def getADBlockAllGoodElem(self):
        try:
            return self.getGeckoElement("adBlockElems", "allGood", absNoScr=True)
        except:
            return None

    def getADBlockNoBlockingElem(self):
        try:
            return self.getGeckoElement("adBlockElems", "noBlocking", absNoScr=True)
        except:
            return None

    def isADBlocked(self):
        try:
            if "display:" in self.getADBlockAllGoodElem().getAttribute('style'):
                return True
            elif "display:" in self.getADBlockNoBlockingElem().getAttribute('style'):
                return False
        except Exception as e:
            self.log(e)
            raise GeckoFailure("Cant Find the required Element or Attribute.")