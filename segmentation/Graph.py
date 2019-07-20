import numpy as np
import skimage.io,skimage.filters
import Component
import math
class graph:
    def __init__(self,sigma,k,min_size,src_img,dec_img=""):
        self.sigma = sigma
        self.k =k
        self.min_size = min_size
        self.src_img = src_img
        self.dec_img = dec_img
        self.edge = []
        self.img = skimage.io.imread(self.src_img)
    def BuildGraph(self):
        smooth_img = skimage.filters.gaussian(self.img,sigma=self.sigma,multichannel=True)
        img_width = smooth_img.shape[1]
        img_height = smooth_img.shape[0]
        self.component = Component.component(img_width*img_height)
        step = [[0,1],[1,-1],[1,0],[1,1]]
        for x in range(img_height):
            for y in range(img_width):
                u = x*img_width+y
                for item in step:
                    tx = x+item[0]
                    ty = y+item[1]
                    if(tx<img_height and (ty<img_width and ty>=0)):
                        v = tx*img_width+ty
                        weight = math.sqrt((smooth_img[x,y][0]-smooth_img[tx,ty][0])**2
                                           +(smooth_img[x,y][1]-smooth_img[tx,ty][1])**2
                                           +(smooth_img[x,y][2]-smooth_img[tx,ty][2])**2)
                        self.edge.append([u,v,weight*255.0])
                        # self.edge.append([v,u,weight*225.0])
        self.edge = sorted(self.edge,key=lambda arg:arg[2])
    def MergeComponent(self):
        for item in self.edge:
            u = item[0]
            v = item[1]
            w = item[2]
            fu = self.component.find(u)
            fv = self.component.find(v)
            if fv!=fu:
                dif = self.component.get_dif(fu,fv,self.k)
                if dif>w:
                    self.component.merge(fu,fv,w)
        for item in self.edge:
            u = item[0]
            v = item[1]
            fu = self.component.find(u)
            fv = self.component.find(v)
            if fv!=fu:
                if self.component.get_size(fu) < self.min_size:
                    self.component.merge(fu,fv,w)
                elif self.component.get_size(fv) < self.min_size:
                    self.component.merge(fv,fu,w)

    def GetImg(self):
        return self.component.image(self.img.shape)
    def ShowImgs(self):
        self.component.show_images(self.img)

