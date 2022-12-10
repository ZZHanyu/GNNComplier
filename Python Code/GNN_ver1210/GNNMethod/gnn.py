import LexcialAnalysis.lexans as LAD

class GNN(object):

    def __init__(self):
        #   每一个token是一个node
        self.node = []
        #   一个语句是一个centernode，默认情况一行一个语句，以;辨别
        self.center_node = []
        #   链接 node 和 centernode的
        self.adjacency_list = []

    def delete_repeat(self,str_list):
        lens = len(str_list)
        i = 0
        while(i<lens):
            j = i + 1
            while(j<lens):
                if(str_list[i] == str_list[j]):
                    del str_list[j]
                    lens -= 1
                    continue
                else:
                    j += 1
            i += 1
        return str(str_list)

    #   初始化center node:
    def get_statement(self,strs):
        if not (strs.find(";")==-1):
            self.center_node.append(strs)

    def init_adjacency(self):
        for i in range(0,len(self.node)):
            for j in range(0, len(self.node[i])):
                for k in range(0,len(self.center_node)):
                    if (self.center_node[k].count(self.node[i][j]) > 0):
                        #   i-分类 j-类中token的代号 k-statement代号
                        self.adjacency_list.append([i,j,k])
        return self.adjacency_list

    def init_node(self,LexData):
        #   加载Lex分析得到的，已分好类、并删除重复项的词素
        #   以index表示权重
        #   定义类权重较低，接近0
        self.node.append(self.delete_repeat(LexData.output_inv()))
        self.node.append(self.delete_repeat(LexData.output_id()))
        self.node.append(self.delete_repeat(LexData.output_keyw()))
        #   运算类权重较高，接近5
        #   在这里，delimeter可能在if else语句中广泛使用，赋较低权重（3）
        self.node.append(self.delete_repeat(LexData.output_delim()))
        self.node.append(self.delete_repeat(LexData.output_cons()))
        self.node.append(self.delete_repeat(LexData.output_ops()))

    def output_list(self):
        return self.adjacency_list

    def list_info(self):
        info = [len(self.node) , len(self.center_node)]
        return info

    def get_token(self):
        return self.node

    def get_line(self,i):
        return self.center_node[i]

    def get_all_line(self):
        return self.center_node

    def length_of_statment(self):
        return len(self.center_node)

    def reset_data(self):
        self.node = []
        self.center_node = []
        self.adjacency_list = []