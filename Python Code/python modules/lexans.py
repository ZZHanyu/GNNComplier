
#
# Created by Zhao Hanyu on 2022/11/3.
#

class lexanalysis(object):

    # declare global variables
    def __init__(self):
        self.id = []
        self.cons = []
        self.ops = []
        self.delim = []
        self.inv = []
        self.keyw = []
        self.count_id = 0
        self.count_cons = 0
        self.count_ops = 0
        self.count_delim = 0
        self.count_inv = 0
        self.count_keyw = 0
        self.subs = []

    # Determine whether the input separator is valid according to the return value?
    # If it returns 1, it is proved to be + - * / such mathematical calculation symbols
    # If it returns 2, it is proved to be (), parentheses
    # If it returns 3, it proves to be a space (null character)

    def ValidDelimiter(self,ch):
        if (ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '' or ch == '='):
            return 1
        else:
            if (ch == '(' or ch == ')'):
                return 2

            else:
                if (ch == ' '):
                    return 3
        return 0

    # Determine whether the operator is valid, return 1 to prove it is valid, return 0 to prove it is invalid
    def ValidOperator(self,ch):
        if (ch == '=' or ch == '+' or ch == '-' or ch == '*' or ch == '/'):
            return 1
        return 0

    # Determine if the identifier is valid based on the return value
    def ValidIdentifier(self,str):
        #if (~((str[0] >= 'a' and str[0] <= 'z') or (str[0] >= 'A' and str[0] <= 'Z') or str[0] == '_')):
        #    return 0

        for i in range(0,len(str)):
            if (~((str[i] >= 'a' and str[i] <= 'z') or (str[i] >= 'A' and str[i] <= 'Z') or (str[i] >= '0' and str[i] <= '9') or str[i] == '_')):
                return 0
    
        return 1

    # Determine if the constant is valid based on the return value
    def ValidConstant(self,str):
        lens = len(str)

        if (lens == 0):
            return 0

        for i in range(0,lens):
            if ((str[i] != '0' and str[i] != '1' and str[i] != '2' and str[i] != '3' and str[i] != '4' and str[i] != '5' and str[i] != '6' and str[i] != '7' and str[i] != '8' and str[i] != '9' or str[i] == '-' and i > 0)):
                return 0

        return 1

    # Determine whether the keyword is valid according to the return value
    def ValidKeyword(self,str):
        if (str == "for" or str == "if" or str == "else if" or str == "else" or str == "while" or str == "do" or str == "return" or str == "int" or str == "float" or str == "bool" or str == "char" or str == "double"):
            return 1
        return 0

    # Judgment function: get input from the keyboard as a parameter, traverse from left to right
    def findTokens(self,str):
        #   Introduce two indexes, which are used as indexes for intercepting strings
        left = 0
        right = 0
        length = len(str)

        #The termination condition is that the left interval value (left) exceeds the right interval value (right) or the right interval value exceeds the overall length of the string (length).
        while (right <= length and left <= right):
            #NEXT: from top to bottom:
            #we judged the length and valid of the input token:
            if (self.ValidDelimiter(str[right]) == 0):
                right+=1
            if (self.ValidDelimiter(str[right]) != 0 and left == right):
                if (self.ValidOperator(str[right]) == 1):
                    self.ops[self.count_ops] = str[right]
                    self.count_ops += 1

                else:
                    if (self.ValidDelimiter(str[right]) != 3):
                        self.delim[self.count_delim] = str[right]
                        self.count_delim += 1

                    #   reset index
                    right += 1
                    left = right

            else:
                if (self.ValidDelimiter(str[right]) != 0 and left != right or (right == length and left != right)):
                    self.subs = str[left: right+1]

                if (self.ValidConstant(self.subs) == 1 and self.ValidDelimiter(str[right]) != 2):
                    self.cons[self.count_cons] = self.subs
                    self.count_cons += 1

                else:
                    if (self.ValidKeyword(self.subs) == 1 and self.ValidIdentifier(self.subs) == 1):
                        self.keyw[self.count_keyw] = self.subs
                        self.count_keyw += 1

                    else:
                        if (self.ValidKeyword(self.subs) == 0 and self.ValidIdentifier(self.subs) == 1):
                            self.id[self.count_id] = self.subs
                            self.count_id += 1


                        else:
                            if (self.ValidIdentifier(self.subs) == 0):

                                self.inv[self.count_inv] = self.subs
                                self.count_inv += 1

                        #   reset index
                        left = right



#output method:
    def output_id(self):
        len = 0
        print("=====Identifiers:=====\n")
        print("Total: %d \n",self.count_id)
        while (len <= self.count_id):
            print(self.id[len])
            len +=1

    def output_cons(self):
        len = 0
        print("=====Constants:=====\n")
        print("Total: %d \n",self.count_cons)
        while (len <= self.count_cons):
            print(self.cons[len])
            len += 1

    def output_ops(self):
        len = 0
        print("=====Operators:=====\n")
        print("Total: %d \n",self.count_ops)
        while (len <= self.count_ops):
            print(self.ops[len])
            len += 1


    def output_delim(self):
        len = 0
        print("=====Delimiters:=====\n")
        print("Total: %d \n",self.count_delim)
        while (len <= self.count_delim):
            print(self.delim[len])
            len += 1

    def output_inv(self):
        len = 0
        print("=====Keywords:=====\n")
        print("Total: %d \n",self.count_inv)
        while (len <= self.count_keyw):
            print(self.inv[len])
            len +=1

    def output_keyw(self):
        len = 0
        print("=====Invalid Identifiers:=====\n")
        print("Total: %d \n",self.count_keyw)
        while (len <= self.count_inv):
            print(self.keyw[len])
            len +=1

    def total_token(self):
        print("Total number of tokens: ", self.count_cons + self.count_delim + self.count_id + self.count_inv + self.count_ops + self.count_keyw)




