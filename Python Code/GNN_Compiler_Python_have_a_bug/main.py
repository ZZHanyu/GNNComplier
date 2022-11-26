import LexcialAnalysis.lexans as LAD

def main():
    EX1 = LAD.lexanalysis()
    strs = input("Enter a string:")
    EX1.findTokens(strs)

if __name__ == '__main__':
    main()
