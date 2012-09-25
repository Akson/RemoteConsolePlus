'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx
import cStringIO
import Image
import wx

class ImagesStorage(object):
    imagesNumber = 0
    
    @staticmethod
    def AddPNGImage(img):
        if ImagesStorage.imagesNumber == 0:
            wx.FileSystem.AddHandler(wx.MemoryFSHandler())
            ImagesStorage.imgRAM=wx.MemoryFSHandler()

        imgName = "img%s.png"%ImagesStorage.imagesNumber
        ImagesStorage.imgRAM.AddFile(imgName,img, wx.BITMAP_TYPE_PNG)

        ImagesStorage.imagesNumber += 1
        return "memory:" + imgName 

    @staticmethod
    def AddFigure(fig):
        #convert to python.Image object 
        imgdata=cStringIO.StringIO()
        fig.savefig(imgdata,format='png')
        imgdata.seek(0)
        im=Image.open(imgdata)
        
        #convert to wx.Image Object and then to wx.Bitmap
        wxim=wx.EmptyImage(im.size[0],im.size[1])
        wxim.SetData(im.convert("RGB").tostring())
        wximbmp=wx.BitmapFromImage(wxim)
        
        return ImagesStorage.AddPNGImage(wximbmp)