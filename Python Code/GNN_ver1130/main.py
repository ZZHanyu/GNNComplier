import LexcialAnalysis.lexans as LAD
import GNNMethod.gnn as gnn

def main():
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

    # OUTPUT
    '''
    EX1.output_id()
    EX1.output_inv()
    EX1.output_keyw()
    EX1.output_delim()
    EX1.output_ops()
    EX1.output_cons()
    '''

    #   将Lex分析的结果传入GNN构建器
    EX2.init_node(EX1)
    EX2.init_adjacency()
    EX2.output_list()


if __name__ == '__main__':
    main()
