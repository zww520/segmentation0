import numpy as np
import random as rand
import matplotlib.pyplot as plt
class component:
    def __init__(self,num_node):
        self.num_node = num_node
        self.parent = [i for i in range(num_node)]
        self.weight = [0 for i in range(num_node)]
        self.size = [1 for i in range(num_node)]
    def find(self,root):
        if root==self.parent[root]:
            return root
        else:
            self.parent[root]=self.find(self.parent[root])
            return self.parent[root]
    def get_size(self,u):
        return self.size[u]
    def get_dif(self,u,v,k):
        return min(self.weight[u]+k/self.size[u],self.weight[v]+k/self.size[v])

    def merge(self,u,v,w):
        self.parent[v]=u
        self.size[u]+=self.size[v]
        self.weight[u]=w
        self.weight[v]=w
    def image(self,shape):
        # img = np.zeros(shape)
        img = np.ones(shape)
        cnt = 0
        color_map = {}
        c = lambda: [rand.random() , rand.random() , rand.random()]
        for i in range(self.num_node):
            root = self.find(i)
            if root not in color_map.keys():
                color_map[root] = c()
                cnt+=1
            img[i//shape[1],i%shape[1]] = color_map[root]

        return img
    def show_images(self,src_img):
        shape = src_img.shape
        m = {}
        cnt = 0
        for i in range(self.num_node):
            root = self.find(i)
            if root not in m.keys():
                m[root]= set()
                cnt+=1
            m[root].add((i//shape[1],i%shape[1]))
        img = src_img
        cnt+=1
        row = int(round(cnt/5+0.5))
        plt.subplot(row,5, 1)
        plt.imshow(img)
        index = 1
        for key, value in m.items():
            index += 1
            sub_img = np.ones(img.shape, dtype=int) * 255
            for item in value:
                sub_img[item[0], item[1]] = img[item[0], item[1]]
            plt.subplot(row,5, index)
            plt.imshow(sub_img)
        plt.show()