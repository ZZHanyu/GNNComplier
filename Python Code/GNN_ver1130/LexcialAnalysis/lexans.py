
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
        self.subs = ""

    # Determine whether the input separator is valid according to the return value?
    # If it returns 1, it is proved to be + - * / such mathematical calculation symbols
    # If it returns 2, it is proved to be (), parentheses
    # If it returns 3, it proves to be a space (null character)

    def comment_eliminate(self,str):
        if not(str.find('\"') == -1):
            start = str.find('"')
            end = str.find('"',start+1)+1
            str1 = list(str)
            for i in range(start, end):
                str1[i] = ""
            str = ''.join(str1)
            return str
        else:
            if not(str.find('/*') == -1):
                start = str.find("/*")
                end = str.find("*/")+2
                str1 = list(str)
                for i in range(start, end):
                    str1[i] = ""
                str = ''.join(str1)
                return str
            else:
                if not(str.find("//") == -1):
                    start = str.find("//")
                    end = str.find('\n')
                    str1 = list(str)
                    for i in range(start, end):
                        str1[i] = ""
                    str = ''.join(str1)
                    return str
        return str


    def ValidDelimiter(self,ch):
        if ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == ',' or ch == '=' or ch == ';':
            return 1
        else:
            if ch == '(' or ch == ')':
                return 2

            else:
                if ch == ' ':
                    return 3
        return 0

    # Determine whether the operator is valid, return 1 to prove it is valid, return 0 to prove it is invalid
    def ValidOperator(self,ch):
        if ch == '=' or ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '<' or ch == '>':
            return 1
        return 0

    # Determine if the identifier is valid based on the return value
    def ValidIdentifier(self,str):
        if not((ord('a') <= ord(str[0]) <= ord('z')) or (ord('A') <= ord(str[0]) <= ord('Z')) or str[0] == '_'):
            return 0
        for i in range(1,len(str)):
            if not((ord('a') <= ord(str[i]) <= ord('z')) or (ord('A') <= ord(str[i]) <= ord('Z')) or (ord('0') <= str[i] <= ord('9')) or str[i] == '_'):
                return 0
        return 1

    # Determine if the constant is valid based on the return value
    def ValidConstant(self,str):
        lens = len(str)
        if lens == 0:
            return 0
        for i in range(0,lens):
            if not (str[i] == '0') and not(str[i] == '1') and not(str[i] == '2') and not(str[i] == '3') and not(str[i] == '4') and not(str[i] == '5') and not(str[i] == '6') and not(str[i] == '7') and not(str[i] == '8') and not(str[i] == '9') or str[i] == '-' and i > 0:
                return 0
        return 1

    # Determine whether the keyword is valid according to the return value
    def ValidKeyword(self,str):
        if str == "for" or str == "if" or str == "else" or str == "while" or str == "do" or str == "return" or str == "int" or str == "float" or str == "bool" or str == "char" or str == "double" or str == "main" or str == "printf":
            return 1
        else:
            return 0

    # Judgment function: get input from the keyboard as a parameter, traverse from left to right
    def findTokens(self,str):
        #   Introduce two indexes, which are used as indexes for intercepting strings
        left = 0
        right = 0
        length = len(str)

        #The termination condition is that the left interval value (left) exceeds the right interval value (right) or the right interval value exceeds the overall length of the string (length).
        while length-1 > right >= left:
            #NEXT: from top to bottom:
            #We judged the length and valid of the input token:
            if self.ValidDelimiter(str[right]) == 0:
                right+=1
            if not (self.ValidDelimiter(str[right]) == 0) and left == right:
                if self.ValidOperator(str[right]) == 1:
                    self.ops.append(str[right])
                    self.count_ops += 1
                else:
                    if not (self.ValidDelimiter(str[right]) == 3):
                        self.delim.append(str[right])
                        self.count_delim += 1
                #reset index
                right += 1
                left = right

            else:
                if not(self.ValidDelimiter(str[right]) == 0) and not (left == right) or (right == length and not(left == right)):
                    self.subs = str[left: right]
                    if self.ValidConstant(self.subs) == 1 and not (self.ValidDelimiter(str[right]) == 2):
                        self.cons.append(self.subs)
                        self.count_cons += 1
                    else:
                        if self.ValidKeyword(self.subs) == 1 and self.ValidIdentifier(self.subs) == 1:
                            self.keyw.append(self.subs)
                            self.count_keyw += 1
                        else:
                            if self.ValidKeyword(self.subs) == 0 and self.ValidIdentifier(self.subs) == 1:
                                self.id.append(self.subs)
                                self.count_id += 1
                            else:
                                if self.ValidIdentifier(self.subs) == 0:
                                    self.inv.append(self.subs)
                                    self.count_inv += 1
                    # Reset index
                    left = right

    #output method:
    def output_id(self):
        #print("=====Identifiers:=====\n")
        #print("Total:",self.count_id,"\n")
        #print(self.id)
        return self.id

    def output_cons(self):
        #print("=====Constants:=====\n")
        #print("Total:",self.count_cons,"\n")
        #print(self.cons)
        return self.cons

    def output_ops(self):
        #print("=====Operators:=====\n")
        #print("Total:",self.count_ops,"\n")
        #print(self.ops)
        return self.ops

    def output_delim(self):
        #print("=====Delimiters:=====\n")
        #print("Total:",self.count_delim,"\n")
        #print(self.delim)
        return self.delim

    def output_inv(self):
        #print("=====Invalid Identifers:=====\n")
        #print("Total:",self.count_inv,"\n")
        #print(self.inv)
        return self.inv

    def output_keyw(self):
        #print("=====KeyWords:=====\n")
        #print("Total:",self.count_keyw,"\n")
        #print(self.keyw)
        return self.keyw

    def total_token(self):
        print("Total number of tokens: ", self.count_cons + self.count_delim + self.count_id + self.count_inv + self.count_ops + self.count_keyw)




