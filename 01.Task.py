# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:* 
    
#     2+2 => 4; 
    
#     1+2*3 => 7; 
    
#     1-2*3 => -5;
    
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
        
#         *Пример:* 
        
#         1+2*3 => 7; 
        
#         (1+2)*3 => 9;


def calt_trad(list_of_math : list) -> list:
    result_2 = 0.00
    remove = -1
    while len(list_of_math) != 1:
        bool_minus = False

        if "*" in list_of_math or "/" in list_of_math:
            try:
                i = list_of_math.index("*")
            except:
                i = len(list_of_math)
            try:
                i_2 = list_of_math.index("/")
            except:
                i_2 = len(list_of_math)
            if i > i_2:
                i = i_2
                bool_minus = True
            if bool_minus:
                result_2 = float(list_of_math[i-1]) / float(list_of_math[i+1])
            else:
                result_2 = float(list_of_math[i-1]) * float(list_of_math[i+1])
            remove = i
        elif "+" in list_of_math or "-" in list_of_math:
            try:
                i = list_of_math.index("+")
            except:
                i = len(list_of_math)
            try:
                i_2 = list_of_math.index("-")
            except:
                i_2 = len(list_of_math)
            if i > i_2:
                i = i_2
                bool_minus = True
            if bool_minus:
                result_2 = float(list_of_math[i-1]) - float(list_of_math[i+1])
            else:
                result_2 = float(list_of_math[i-1]) + float(list_of_math[i+1])
            remove = i

        for i in range(0,3):
            del list_of_math[remove-1]

        list_of_math.insert(remove-1,result_2)
                # print(list_of_math)
    return list_of_math

def cal_with_stoto(list_of_math: list) -> list:
    
    while "(" in list_of_math:
        # print(list_of_math)     ( 1 * 9 ( 3*2) )
        new_list = []
        index_of_bracket_1 = 0
        index_of_bracket_2 = len(list_of_math)
        for i,item in enumerate(list_of_math):
            if item == "(":
                if "(" not in list_of_math[i+1:list_of_math.index(")")]:
                    index_of_bracket_1 = i
                    break
        index_of_bracket_2 = list_of_math.index(")")    
        # print(f"{index_of_bracket_1}-> {index_of_bracket_2}")    
        for i in list_of_math[index_of_bracket_1+1:index_of_bracket_2]:
            new_list.append(i)
        # print(new_list)
        for i in range(len(list_of_math[index_of_bracket_1:index_of_bracket_2+1])):
            del list_of_math[index_of_bracket_1]
        list_of_math.insert(index_of_bracket_1,calt_trad(new_list)[0])
    else:
        calt_trad(list_of_math)

# text_math = "12+3*2+7/2"
text_math = "".join(input(" Введите уравнение : ").split())

list_of_math = []

result = ""
for i in text_math:
    if not i.isdigit():
        list_of_math.append(result)
        result = ""
        list_of_math.append(i)
    if i.isdigit():
        result += i
list_of_math.append(result)

while "" in list_of_math:
    list_of_math.remove("")

print(list_of_math)

# print(list_of_math)

cal_with_stoto(list_of_math)
print(f"{text_math} = {eval(text_math)} *eval")
print(f"{text_math} = {list_of_math[0]} *counted")


( 2 + 3 * ( 6 - 8) )