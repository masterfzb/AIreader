import random
import data_base
import randomvalues

'''
    造物说明：
        本文件只制造最基础且难以更改的参数。
        人物包含字典（姓氏，名字，阶层，其他参数）
        输入（种族，层阶）或（种族），输出一个人物
        或者随机获得一个人物
        请不要乱输入，否则会随机创造。
        创造结果不满意，只能改名不能改姓
'''

'''
制造一个随机的生物，涉及生物对应权重来约束生成对象的数量
输出一个包含对应人物参数的return_list
'''


def create_a_random_type():
    return_list = list()
    times = 0
    for items in data_base.all_list:
        return_list.append(random.choice(data_base.choice_weight(items, data_base.all_list_weight[times])))
        times += 1
    return return_list


'''
制造一个特定生物，这里不需要权重，大部分对应属性需要自己选择。
如果乱取名会自动随机选择。
输出一个包含对应人物参数的return_list
'''


def create_a_type_choice(types, list):
    print("目前支持的" + types + "有:")
    data_base.show_data(list)
    types_in = input("输入要创建的" + types + ":")
    if types_in not in list:
        types_in = random.choice(list)
    return types_in


def create_a_definite_type():
    print(
        '''
            这个功能用于创造一个特定的人物，请不要输入不存在的种族或等级。
            --------------------注意!------------------------
            加入输入了错误的种族或等级，系统将创建一个随机的种族或等级。
        '''
    )
    times = 0
    return_list = list()
    for items in data_base.all_list:
        return_list.append(create_a_type_choice(data_base.all_list_name[times], items))
        times = times + 1
    return return_list


'''
输入包括：
包含人物的参数的list：return_list
对应人物属于自定义还是随机生成的中文str：keys
包含全体对象信息的dict：life_list
输出包括：
一个合适的姓str
一个合适的名str
'''


def give_life_name(return_list, key, life_list):
    typ = {"高": lambda: "high_", "低": lambda: "low_"}[return_list[2]]()
    typ = {"平民": lambda: (typ + "M"), "神": lambda: ("god"), "精灵": lambda: (typ + "JL")}[return_list[0]]()
    # 生成姓
    if key == "自定义":
        data_base.show_data(str(data_base.first_name[typ]))
        first_name = input("请从上述姓氏中选择一个姓")
        if first_name not in data_base.first_name[typ]:
            first_name = random.choice(data_base.first_name[typ])
    else:
        first_name = random.choice(data_base.first_name[typ])
    # 生成名
    typ = {"高": lambda: "high_", "低": lambda: "low_"}[return_list[2]]()
    zukind = {"宗族": lambda: "zu", "散人": lambda: "san"}[return_list[3]]()
    sexkind = {"男": lambda: "man_" + zukind, "女": lambda: "woman", "不涉及": lambda: "woman"}[return_list[1]]()
    typ = {"平民": lambda: sexkind, "神": lambda: ("god"), "精灵": lambda: (typ + "JL")}[return_list[0]]()

    if key == "自定义":
        maybeuse = random.choice(data_base.second_name_1[typ]) + random.choice(data_base.second_name[typ])
        last_name = input("姓氏为" + first_name + "请输入一个名字,或者使用随机生成的" + first_name + maybeuse + "：")
        if last_name == '':
            last_name = maybeuse
    else:
        last_name = random.choice(data_base.second_name_1[typ]) + random.choice(data_base.second_name[typ])

    while first_name + last_name in life_list.keys():
        print('姓名重复，必须重新命名')
        last_name = random.choice(data_base.second_name_1[typ]) + random.choice(data_base.second_name[typ])
    return first_name, last_name


'''
create_a_life
输入包括：
包含人物的参数的list：return_list
对应人物属于自定义还是随机生成的中文str：keys
包含全体对象信息的dict：life_list
输出：
一个life_list保存格式的字典。
备注:
life_list的格式为
{名{reurn_list参数的对应内容，其他参数{}}
'''


def be_a_dict(first_name, last_name, return_list, other):
    man = {}
    man[first_name + last_name] = {}
    man[first_name + last_name].update({"姓": first_name})
    man[first_name + last_name].update({"名": last_name})
    times = 0
    for items in data_base.all_list_name:
        man[first_name + last_name].update({items: return_list[times]})
        times += 1
    man[first_name + last_name].update({"其他属性": other})
    return man


def create_a_life(return_list, key, life_list):
    first_name, last_name = give_life_name(return_list, key, life_list)
    # 生成其他参数
    other = randomvalues.give_life_goodvalue(return_list, key)
    # 保存
    if key == "自定义":
        maybeuse = input("请确认是否创建" + str(be_a_dict(first_name, last_name, return_list, other)) + ",拒绝请输入no:")
        if maybeuse == "no":
            return create_a_life(return_list, key, life_list)
        else:
            return be_a_dict(first_name, last_name, return_list, other)
    else:
        return be_a_dict(first_name, last_name, return_list, other)


def create_a_weapen():
    print('not defined')
