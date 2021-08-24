
'''
    统计并展示dic里对应str参数的dic的对应信息
    如果dic的key对应一个dic，那么视key为对应dic描述信息并不展示。
    统计的输出结果为
    1.dic的keys：
    keys对应STR的类型数量
    keys对应STR出现的次数
'''
'''
get_the_aim_dic
用递归的方式展开dic内的全部key以方便统计。
'''
def get_the_aim_dic(dic):
    aim_dic = dict()
    for keys in dic:
        if type(dic[keys]) == type(dict()):
            dic_tample = get_the_aim_dic(dic[keys])
            for items in dic_tample:
                if items not in aim_dic:
                    aim_dic[items] = dic_tample[items]
                else:
                    aim_dic[items] += dic_tample[items]
        else:
            if type(dic[keys]) != type(list()) or type(dic[keys]) != type(tuple()):
                if keys not in aim_dic.keys():
                    aim_dic[keys] = list()
                    aim_dic[keys].append(dic[keys])
                else:
                    aim_dic[keys].append(dic[keys])
    return aim_dic


def show_dic_data(dic):
    list_type = get_the_aim_dic(dic)
    print(list_type)
    for keys in list_type:
        print(keys + ":")
        show_list = dict()
        for items in list_type[keys]:
            if items not in show_list.keys():
                show_list[items] = 1
            else:
                show_list[items] += 1
        if len(show_list)<40:
            print(len(show_list))
            for items in show_list:
                print(items + ":"+str(show_list[items]))
        else:
            print("items is not useful")