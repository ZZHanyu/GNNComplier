#   简易训练集

class train_dataset(object):
    def __init__(self):
        self.calcute_string = []
        self.calcute_string.append("x = (a + b/2)*3-1;")
        self.calcute_string.append("arr += 12 * (x - y*3);")
        self.calcute_string.append("ab = a+b/2*3;")
        self.calcute_string.append("exp = e*e*e*e*e*e;")
        self.calcute_string.append("sum = a + b + c + d + e + f + g +h ;")
        
        self.keyword_string = []
        self.keyword_string.append("if (a < b) { };")
        self.keyword_string.append("else { if ( a == b ) };")
        self.keyword_string.append("while ( x == y );")
        self.keyword_string.append("return 0;")
        self.keyword_string.append("int main ( ) { };")
        
        self.identifer_string = []
        self.identifer_string.append("int a = 0;")
        self.identifer_string.append("double x,y,z=0.0;")
        self.identifer_string.append("string str = [];")
        self.identifer_string.append("int arr [ 5 ] = [1,2,3,4,5,6,7,8,9,10];")
        self.identifer_string.append("float p = 3.1415926;")


    def get_train_data(self):
        temp_array = []
        temp_array.append(self.calcute_string)
        temp_array.append(self.keyword_string)
        temp_array.append(self.identifer_string)

        return temp_array


