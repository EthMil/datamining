# def input_list():
#     file_name = raw_input("please input the name of the file: ")
#     fo = open(file_name)
#     fo_lines = fo.readline()
#     file_list = []
#     while fo_lines:
#         fo_lines = fo_lines.strip("\n")
#         split_lines = fo_lines.split(",")
#         fo_lines = fo.readline()
#         file_list.extend(split_lines)
#     for i in file_list:
#         print(i)
#     fo.close()

def frequent_items(file_name, support_threshold):
    frequent_item_list = []
    fo = open(file_name)
    fo_lines = fo.readline()
    #read in all lines of the text file input.
    while fo_lines:
        fo_lines = fo_lines.strip("\n")
        #for each line, separate each element
        split_lines = fo_lines.split(",")
        fo_lines = fo.readline()
        #for every element in the list created, check to see if the element has already been seen.
        for i in split_lines:
            flag = 0
            if frequent_item_list:
                for j in frequent_item_list:
                    #if the element has been seen before, add one to the count for that element and update the flag.
                    if j[0] == i:
                        j[1] = j[1] + 1
                        flag = 1
                if flag == 0:
                    #if the element hasn't been seen before, add it to the list of elements counted.
                    frequent_item_list.extend([[i,1]])
            else:
                temp = [[i, 1]]
                frequent_item_list.extend(temp)
        frequent_item_list_return = [x for x in frequent_item_list if x[1] > support_threshold]
    fo.close()
    return frequent_item_list_return

def frequent_pair_finder(frequent_item_list):
    frequent_pair_list = []
    j = 0
    for i in frequent_item_list:
        k = j + 1
        while k < len(frequent_item_list):
            temp = [[i[0],frequent_item_list[k][0],0]]
            frequent_pair_list.extend(temp)
            k += 1
        j += 1
    # return frequent_pair_list
    fo = open("shrooms2.data")
    fo_lines = fo.readline()
    file_list = []
    # for i in frequent_pair_list:
        # print(i)
    while fo_lines:
        fo_lines = fo_lines.strip("\n")
        split_lines = fo_lines.split(",")
        fo_lines = fo.readline()
        # print(all(x in i for x in ['a', 'b']))
        # print(split_lines)
        for i in frequent_pair_list:
            # print(i)
            # print(split_lines)
            for j in split_lines:
                if i[0] == j:
                    for k in split_lines:
                        if i[1] == k:
                            i[2] += 1
    fo.close()
    frequent_pair_list_return = [x for x in frequent_pair_list if x[2] > support_threshold]

    return frequent_pair_list_return


file_name = raw_input("please input the name of the file: ")
support_threshold = input("please input the support threshold: ")
frequent_item_list = frequent_items(file_name, support_threshold)
# print(frequent_item_list)
frequent_pair = frequent_pair_finder(frequent_item_list)
for i in frequent_pair:
    print i[0]+', '+i[1]+', ',i[2],';'
    # ('17w, 18o, ', 27, ';')            