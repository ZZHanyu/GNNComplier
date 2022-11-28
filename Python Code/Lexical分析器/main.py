import LexcialAnalysis.lexans as LAD

def main():
    EX1 = LAD.lexanalysis()
    while(True):
        strs = input()
        if strs.strip() == "":
            break
        else:
            strs = EX1.comment_eliminate(str(strs))
            EX1.findTokens(str(strs))

    # OUTPUT
    EX1.output_id()
    EX1.output_inv()
    EX1.output_keyw()
    EX1.output_delim()
    EX1.output_ops()
    EX1.output_cons()

if __name__ == '__main__':
    main()
