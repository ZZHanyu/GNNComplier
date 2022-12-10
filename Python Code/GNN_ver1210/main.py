import LexcialAnalysis.lexans as LAD
import GNNMethod.gnn as gnn
import graph.gnn_graph as draw
import tensor.HeteroGraph as hg
import tensor.train as train

def main():
    EX1 = LAD.lexanalysis()
    EX2 = gnn.GNN()
    EX4 = []

    adj_list = []
    all_lines = []

    # 加载训练集
    train_dataset = train.train_dataset()
    strs = train_dataset.get_train_data()
    print(strs)
    for i in range(0,len(strs)):
        EX1.reset_data()
        EX2.reset_data()
        for j in range(0,len(strs[i])):
            strs[i][j] = EX1.comment_eliminate(str(strs[i][j]))
            EX1.findTokens(str(strs[i][j]))
            EX2.get_statement(strs[i][j])
        EX2.init_node(EX1)
        adj_list = EX2.init_adjacency()
        all_lines = EX2.get_all_line()
        EX4.append(hg.HeteroGraph(adj_list, all_lines))
        EX4[i].get_train()

    print("---Training Sucessed!---\n")

    print("*\bNow Please Enter your code below:\n")
    EX1 = LAD.lexanalysis()
    EX2 = gnn.GNN()
    while(True):
        strs = input()
        #   如果某一行输入为空，则终止程序（strip是除去\n 空格的strs）
        if strs.strip() == "":
            break
        else:
            strs = EX1.comment_eliminate(str(strs))
            #   Lex分析器
            EX1.findTokens(str(strs))
            #   判断是否为语句，是则存储
            EX2.get_statement(strs)

    # 将Lex分析的结果传入GNN构建器
    EX2.init_node(EX1)
    EX2.init_adjacency()

    for i in range(len(EX4)):
        EX4[i].run_function()
    #EX3 = draw.Graph(EX2)
    #EX3.drwa_graph(EX2)

if __name__ == '__main__':
    main()
