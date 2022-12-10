import matplotlib.pyplot as plt
import numpy as np
import random
import GNNMethod.gnn as gnn
import os

class Graph(object):
    def __init__(self,Adj):
        self.array = np.array(Adj.output_list())
        self.info = Adj.list_info()
        self.token = Adj.get_token()
        self.node_point = []
        self.line_point = []

    def drwa_graph(self,Adj):
        print(self.token)
        print(self.array)
        fig = plt.figure()
        plt.xlim(xmin=-1, xmax=27)  # x轴的范围[0,2]
        plt.ylim(ymin=-1, ymax=11)  # y轴的范围[0,2]
        plt.xlabel('X')
        plt.ylabel('Y')
        for j in range(0,self.info[1]):
            X = 0
            Y = j+2
            plt.scatter(X, Y, color="black", label=Adj.get_line(j))
            self.line_point.append([X,Y])
        print(self.line_point)

        for i in range(0,len(self.array)):
            X = random.randint(1,20)
            Y = random.randint(1,10)
            if (self.array[i][0] == 0):  # Identifiers
                plt.scatter(X, Y, color="red", label=self.token[0][self.array[i][1]])
                for j in range(0,self.info[1]):
                    if(self.array[i][2] == j):
                        plt.plot([X, self.line_point[j][0]], [Y,self.line_point[j][1]])
                        print(self.line_point[j])
            if (self.array[i][0] == 1):  # constants
                plt.scatter(X, Y, color="green", label=self.token[1][self.array[i][1]])
                for j in range(0,self.info[1]):
                    if(self.array[i][2] == j):
                        plt.plot([X, self.line_point[j][0]], [Y,self.line_point[j][1]])
            if (self.array[i][0] == 2):  # operators
                plt.scatter(X, Y, color="blue", label=self.token[2][self.array[i][1]])
                for j in range(0,self.info[1]):
                    if(self.array[i][2] == j):
                        plt.plot([X, self.line_point[j][0]], [Y,self.line_point[j][1]])
            if (self.array[i][0] == 3):  # delimiters
                plt.scatter(X, Y, color="magenta", label=self.token[3][self.array[i][1]])
                for j in range(0,self.info[1]):
                    if(self.array[i][2] == j):
                        plt.plot([X, self.line_point[j][0]], [Y,self.line_point[j][1]])
            if (self.array[i][0] == 4):  # keyword
                plt.scatter(X, Y, color="yellow", label=self.token[5][self.array[i][1]])
                for j in range(0,self.info[1]):
                    if(self.array[i][2] == j):
                        plt.plot([X, self.line_point[j][0]], [Y,self.line_point[j][1]])
            self.node_point.append([X,Y])

        plt.legend(loc='best',frameon=False)
        plt.savefig('./test2.jpg',dpi=400)
        plt.show()


