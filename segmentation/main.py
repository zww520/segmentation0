import Graph
import matplotlib.pyplot as plt
import numpy as np
import time
if __name__ == '__main__':
    st = time.time()
    graph = Graph.graph(0.8,500,2800,'test.jpg')
    graph.BuildGraph()
    graph.MergeComponent()
    ed = time.time()
    graph.ShowImgs()
    print("cost time",ed-st)



















