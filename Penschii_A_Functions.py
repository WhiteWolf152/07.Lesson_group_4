import random

def input_number_examination(text_in_input = "Enter number :" , case_def = 0, min_num = 0,max_num=10,bool_is_not_decimal = True):
    """Testing if input is a number

    Args:
        text_in_input (str, optional): Text for input. Defaults to "Enter number :".  \n
        case_def (int, optional):   # 0 : "Is it a number",
                                    # 1 : "Enter integer number ",
                                    # 2 : "Enter number > 0",
                                    # 3 : "Enter number between X > number < Y"
                                    Defaults to 0.\n
        min_num (int, optional): If needed test >= . Defaults to 0.\n
        max_num (int, optional): If needed test <=. Defaults to 10.\n
        bool_is_not_decimal (bool, optional): For between min and max shood it be decimal or not  \n
                                            True - number should not be decimal  \n
                                            False - number could be decimal. Defaults to True.\n

    Returns:
        int,float: output could be int or float
    """

    bool_is_number = True

    while bool_is_number:

        bool_si_minus = False
        bool_is_decimal = False

        number = input(f"{text_in_input}")

        if number[0] == "-":
            bool_si_minus = True
            number = number.replace("-","")

        for i in number:
            if i == ".":
                bool_is_decimal = True
                break
        
        if bool_is_decimal:
                whole_part = ""
                digit_part = ""
                for i in number:
                    if i != ".":
                        whole_part += str(i)
                    else:
                        break
                if whole_part.isdigit():
                    for i in number[len(whole_part)+1:]:
                        digit_part += str(i)
                    if digit_part.isdigit():
                        number = whole_part + "." + digit_part
                    number = float(number)
                    bool_is_number = False
        else:
            if number.isdigit():
                number = int(number)
                bool_is_number = False

        if bool_is_number:
            print("Not a number , try again")
            continue

        if bool_si_minus:
            number *= -1
        
        bool_is_number = input_number_params(number,case_def, min_num,max_num,bool_is_not_decimal)

    return number

def input_number_params(number , case_def, min_num ,max_num,bool_is_not_decimal):
    """Chak variants of input input_number_examination

    Args:
        number (_type_): number to chek
        case_def (_type_):  # 0 : "Is it a number",
                            # 1 : "Enter integer number ",
                            # 2 : "Enter number > 0",
                            # 3 : "Enter number between X > number < Y",
        min_num (_type_): number >=
        max_num (_type_): number <=
        bool_is_not_decimal (_type_):   True - dont allow decimals
                                        False - allow decimals
    """

            # 0 : "Is it a number",
            # 1 : "Enter integer number ",
            # 2 : "Enter number > 0",
            # 3 : "Enter number between X > number < Y",

    float_bool = True

    if case_def < 0 or case_def > 4:
        print("Wrong argument for test. Need from 0 to 3")
        return True

    match case_def:
        case 0:
            try:
                float(number)
                return False
            except ValueError:
                return True
        case 1:
            for i in str(number):
                    if i == ".":
                        print("Not an integer")
                        float_bool = False
            if float_bool:
                    return False
            else:
                    return True
        case 2:
            if number >= 0:
                return False
            else:
                print("Not >= 0")
                return True
        case 3:
            if bool_is_not_decimal:
                for i in str(number):
                    if i == ".":
                        print("Not an integer")
                        float_bool = False
                if float_bool:
                    if min_num > max_num:
                        min_num,max_num = max_num,min_num
                    if number >= min_num and number <= max_num:
                        return False
                    else:
                        print(f"not >={min_num} or =<{max_num} ")
                        return True
                else:
                    print("Enter not decimal")
                    return True
            else:
                if min_num > max_num:
                    min_num,max_num = max_num,min_num
                if number >= min_num and number <= max_num:
                    return False
                else:
                    print(f"not >={min_num} or =<{max_num} ")
                    return True

def array_creation_random_int(array_length = 10,min_random = 0,max_random = 10) -> list:
    """Creat an array of numbers in range

    Args:
        array_length (int, optional): length of array . Defaults to 10.
        min_random (int, optional): min umber of random. Defaults to 0.
        max_random (int, optional): max number of random. Defaults to 10.

    Returns:
        list: list of int random numbers
    """
    if array_length <=0:
        print("Wrong array length choose , settin it to deffoult 10")
        array_length = 10
    if min_random > max_random:
        print("Min value for random is bigger then max, changing placec")
        min_random,max_random=max_random,min_random
    elif min_random == max_random:
        print("Min = Max values for random - it will be 1 number")

    list_of_numbers =[]
    for i in range(0,array_length):
        list_of_numbers.append(random.randint(min_random,max_random))
    return list_of_numbers

def array_creation_range(range_start=0,range_end=10,range_step=1) -> list:
    """Creat a list of numbers in range

    Args:
        range_start (int, optional): Start of range. Defaults to 0.
        range_end (int, optional): end of range (has +1 in formula ). Defaults to 10.
        range_step (int, optional): step of range. Defaults to 1.

    Returns:
        list: list of integer numbers in rage
    """
    if range_start >= range_end:
        print("Start of array is bigger then End, changing placec")
        range_start,range_end = range_end,range_start
    if range_step <= 0:
        print("Wrong step , changing to deffoult 1")
        range_step = 1
    
    list_of_numbers =[*range(range_start,range_end+1,range_step)]
    return list_of_numbers

def array_creation_random_float(array_length = 10,digit_choose = 1,round_digit = 4) -> list:
    if digit_choose <0 or digit_choose>9:
        print("Wrong digit choose , settin it to deffoult 1")
        digit_choose = 1
    if round_digit < 0:
        print("Wrong round choose , settin it to deffoult 4")
        digit_choose = 1
    if array_length <=0:
        print("Wrong array length choose , settin it to deffoult 10")
        array_length = 10

    digit_lib = \
        {
            0 : 1 ,
            1 : 10 ,
            2 : 10**2 ,
            3 : 10**3 ,
            4 : 10**4 ,
            5 : 10**5 ,
            6 : 10**6 ,
            7 : 10**7 ,
            8 : 10**8 ,
            9 : 10**9 
        }

    list_of_numbers =[]
    for i in range(0,array_length):
        if round_digit == 0:
            list_of_numbers.append(int(round(random.random()*digit_lib[digit_choose])))
        else:
            list_of_numbers.append(round(random.random()*digit_lib[digit_choose],round_digit))
    return list_of_numbers

def print_dictionary_in_lines(dictionary_array):
    for i in dictionary_array:
        print(f"{i} : {dictionary_array[i]}")

def fibonachi_plus(fib_range : int) -> list:
    """makes array of fibonacci numbers > 0

    Args:
        fib_range (int): range of fibonacci numbers

    Returns:
        list: > 0 fibonacci array
    """
    flibonachi_list = [0,1]
    if fib_range > 1:
        for i in range(2,fib_range+1):
            # формула рассчёта фибоначи, для этог первые 2 числа записанны
            flibonachi_list.append(flibonachi_list[i-1]+flibonachi_list[i-2])
    return flibonachi_list

def fibonachi_minus(fib_range : int) -> list: # наверное можно было обойтись без этого и просто каждый второй эллемент обычного фибоначи умнодить на -1, но подумал - вдруг когда то потребуется только минуосовй фибоначи
    """makes fibonacci numbers < 0

    Args:
        fib_range (int): range of fibonacci numbers

    Returns:
        list: < 0 fibonacci array
    """
    flibonachi_list = [0,1]
    if fib_range > 1:
        for i in range(2,fib_range+1):
            # формула рассчёта фибоначи, для этог первые 2 числа записанны
            flibonachi_list.append(flibonachi_list[i-2]-flibonachi_list[i-1])
    return flibonachi_list

def fibonachi_from_minus_to_plus(fib_range : int) -> list:
    """compels two fibonacci arrays ( < 0 and > 0 ) in one fibonacci array

    Args:
        fib_range (int): range of fibonacci 

    Returns:
        list: list of fibonacci numbers
    """
    fib_plus = fibonachi_plus(fib_range) # создаёт положителный фибоначи
    flibonachi_list = fibonachi_minus(fib_range) # создаёт отрицательный фибоначи
    sort_array(flibonachi_list) # разворачивает отрицательный фибоначи
    for i in range(1,fib_range+1): # к отрицательному добавляет положительный по каждому эллементу 
        flibonachi_list.append(fib_plus[i])
    return flibonachi_list
        
def sort_array(list_of_numbers : list):
    """Sorts array in back order

    Args:
        list_of_numbers (list): array to sort
    """
    # стандартный цикл разворота списка
    for i in range(0,int(len(list_of_numbers)/2)):
        list_of_numbers[i],list_of_numbers[-(1+i)] = list_of_numbers[-(1+i)],list_of_numbers[i]

def file_create(path : str,text : str):
    """Созадёт файл с текстом

    Args:
        path (str): Название/Путь_файла
        text (str): текст для записи
    """
    file = open(path , "w",encoding='utf-8')
    file.write(text)
    file.close()

