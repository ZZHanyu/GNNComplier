import LexcialAnalysis.lexans as LAD

class GNN(object):
    def delete_repeat(self,str_list):
        lens = len(str_list)
        i=0
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
        return str_list

    def __init__(self):
        #   每一个token是一个node
        self.node = []
        #   一个语句是一个centernode，默认情况一行一个语句，以;辨别
        self.center_node = []
        #   链接 node 和 centernode的
        self.adjacency_list = []

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

    def init_node(self,LexData):
        #   加载Lex分析得到的，已分好类、并删除重复项的词素
        self.node.append(self.delete_repeat(LexData.output_id()))
        self.node.append(self.delete_repeat(LexData.output_cons()))
        self.node.append(self.delete_repeat(LexData.output_ops()))
        self.node.append(self.delete_repeat(LexData.output_delim()))
        self.node.append(self.delete_repeat(LexData.output_inv()))
        self.node.append(self.delete_repeat(LexData.output_keyw()))

    def output_list(self):
        print("adj list is here: ",self.adjacency_list)