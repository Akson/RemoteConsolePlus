'''Created by Dmytro Konobrytskyi, 2012(C)'''
from time import time
import os

class ImagesStorage(object):
    imagesNumber = 0
    tmpDirPath = None
    
    @staticmethod
    def AddFigure(fig):
        if ImagesStorage.tmpDirPath == None:
            ImagesStorage.tmpDirPath = "Tmp/Session_"+str(int(time()))+"/Img"
            os.makedirs(ImagesStorage.tmpDirPath)

        imgName = "\\img%s.png"%ImagesStorage.imagesNumber
        ImagesStorage.imagesNumber += 1
        fullImgPath = ImagesStorage.tmpDirPath + imgName
        fig.savefig(fullImgPath,format='png')
        return fullImgPath
