import random
import data_base

'''
    造物说明：
        本文件制造的是对应的初始参数，未来可能会改变，且不是唯一对应的。
        取出设定并补充设定，对应的输出对象应保存在other里。
'''

'''
    根据生物参数给予他一个合适的数值。
    输入：
    包含人物的参数的list：return_list
    对应人物属于自定义还是随机生成的中文str：keys
    输出:
    对应人物dic信息的other
'''

def give_life_goodvalue(return_list,key):
    typ = {"高": lambda: "high_", "低": lambda: "low_"}[return_list[2]]()
    typ = {"平民": lambda: (typ + "M"), "神": lambda: ("god"), "精灵": lambda: (typ + "JL")}[return_list[0]]()
    if key == "自定义":
        job = input("请为你的角色描述一个职阶")
        if job == '':
            job = random.choice(data_base.types_of_job[typ])
        else:
            data_base.show_data(data_base.types_of_job[typ])
            realjob = input("请为你的角色选择一个真实职阶，注意只能从上述职阶中选择。")
            if realjob not in data_base.types_of_job[typ]:
                realjob = random.choice(data_base.types_of_job[typ])
    else:
        job = random.choice(data_base.types_of_job[typ])
    need_weight = {"平民": lambda: data_base.M_need_weight, "神": lambda: data_base.god_need_weight, "精灵": lambda: data_base.JL_need_weight}[return_list[0]]()
    need=random.choice(data_base.choice_weight(data_base.types_of_needs_basic,need_weight))
    out_look = dict()
    for items in data_base.all_out_look:
        out_look.update({items:data_base.out_look_get(items,return_list)})
    return{"职阶设定":job,"需求":need,"特点":out_look}
def give_weapen_goodvalue():
    print('not defined')
