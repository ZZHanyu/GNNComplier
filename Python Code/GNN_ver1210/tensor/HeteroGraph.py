import torch
import torch.utils.data as Data
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


class HeteroGraph(object):
    
    def __init__(self,adj_list,all_lines):
        self.adj_list = adj_list
        self.torch_list = torch.Tensor(adj_list)
        self.statements = all_lines
        self.mean = []
        self.eig = []

    # 调用GPU加速（如果可用）:
    def GPU_available(self):
        if torch.cuda.is_available():
            adjtorch_cuda = self.torch_list.cuda()
            print(adjtorch_cuda)
        else:
            print("GPU is not available in your computers! Now using CPU...\n")

    def get_train(self):
        self.GPU_available()
        arrays = self.get_eigenvalues()
        print("This is eig = ",arrays)
        total_value = self.add_eig_matrix(arrays)
        temp = 0
        for i in range(0,len(total_value)):
            temp = temp + total_value[i]
        temp = temp/len(total_value)
        mean_value = total_value
        for j in range(0,len(mean_value)):
            mean_value[j] = mean_value[j] - temp
        print("mean value = ",mean_value)

        for m in range(0,len(arrays)):
            arr_std = np.std(arrays[m], ddof=1)
            for n in range(0,len(arrays[m])):
                arrays[m][n] = (arrays[m][n] - mean_value[m])/arr_std
            self.eig = (arrays)

        self.mean = mean_value
        return arrays

    def run_function(self):
        self.GPU_available()
        arrays = self.get_eigenvalues()
        for i in range(0,len(arrays)):
            arrays[i] = self.Euclidean_Distance(arrays[i],self.mean)
        print("after Euclidean_Distance = ",arrays)
        self.add_eig_matrix(arrays)

        # 转换为Tensor类型，并使用sigmod激活函数
        tensor_array = []
        for j in range(0,len(arrays)):
            tensor_array.append(torch.Tensor(arrays[j]))
            tensor_array[j] = torch.sigmoid(tensor_array[j])

    def get_eigenvalues(self):
        h = []
        for i in range(0, len(self.statements)): # 以ith的句子为中心点，对这一个句子包含不同种类的Token赋以不同的权重
            temp = [] # 记录statment i 的节点信息
            for j in range(0,len(self.adj_list)): # 对所有Token组合进行扫描
                if (self.adj_list[j][2] == i):
                    temp.append(self.adj_list[j][0]) # 取statement中每个Token种类代号作为特征向量
            h.append(temp)
        return h

    # 计算test样本和trained样本特征值的欧氏距离:
    def Euclidean_Distance(self,array,mean_value):
        arr_std = np.std(array,ddof=1)
        for i in range(0,len(array)):
            array[i] = (array[i] - mean_value[i])/arr_std

        distance = []
        # 迭代判断这个statement的特征值和已经训练好的三个结果哪个更接近？
        # 首先要统一特征向量长度:
        for j in range(0,len(self.eig)):
            #distance[0]代表 与calcuate特征值的距离
            #distance[1] 与keywords距离
            #distance[2] 与identifier距离
            if(len(array) > len(self.eig[j])):
                temp = np.array(array[0:len(self.eig[j])])
                self.eig[j] = np.array(self.eig[j])
                print("temp = ",temp,"eig = ",self.eig[j])
                distance.append(np.sqrt(np.sum(np.square(temp - self.eig[j]))))
            else:
                if(len(array)<len(self.eig)):
                    temp = np.array(array)
                    self.eig[j] = np.array(self.eig)
                    distance.append(np.sqrt(np.sum(np.square(temp - self.eig[j]))))
                else:
                    temp = np.array(array)
                    self.eig[j] = np.array(self.eig[j])
                    distance.append(np.sqrt(np.sum(np.square(temp - self.eig[j]))))

        MAX = max(distance[0],distance[1],distance[2])
        if(distance.index(MAX) == 0):
            print("This is Calcute Statement!")
        else:
            if(distance.index(MAX) == 1):
                print("This is Keyword Stsatement!")
            else:
                print("This is identifier statment!")

    def add_eig_matrix(self,array):
        #冒泡法找到最长长度
        max_size = 0
        for i in range(0,len(array)):
            if (len(array[i]) > max_size):
                max_size = len(array[i])
            else:
                continue

        temp = [0 for m in range(0,max_size)]
        for j in range(0,len(array)):
            for m in range(0,len(array[j])):
                temp[m] = temp[m] + array[j][m]

        print("after addtion matrix is = ",temp)
        return temp


    def output_torch(self):
        print('torch_list is: ', self.torch_list)
