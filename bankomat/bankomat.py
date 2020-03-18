def parce_string(param):
    res_dict = {}
    for x in param.split(','):
        res_dict[int(x.split(':')[0])] = int(x.split(':')[1])

    return res_dict


def banknot_taker(m, dict_banknot):
    tmp = int(m)
    tmp_dict = {}
    sort_arr = sorted(dict_banknot.items(), reverse=True)
    for x in sort_arr:
        count = 0
        index = int(x[0])
        while (dict_banknot[index] > 0 and tmp - index >= 0):
            tmp -= index
            dict_banknot[index] -= 1
            count += 1
        if (count > 0):
            tmp_dict[index] = count

    if (tmp > 0):
        print("can`t get cash")
        return -1;
    else:
        print("money:", tmp_dict)
        return tmp_dict


data = input("Enter [banknot:count] arrray: ")
number = input("Suma: ")

input_dict = parce_string(data)
banknot_taker(number, input_dict)
