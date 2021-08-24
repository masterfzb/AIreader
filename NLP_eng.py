import random
import NLP_discribing

'''
================================================================codes=================================================

'''
'''
输入：
1.num：取的词语类型及对应数量的字典
2.take_key：从数据库取对应关键字的词语类型的字典串及对应stencil

输出：
输出描述性句子，由数个含list的list组成，可能需要解list的工具变成
'''

def nlp_eng_discribing_things(name,name_list,discribing_type):
    take_key = name_list[name]
    if discribing_type == '生物':
        result_many_list_of_discribes = NLP_discribing.give_life_discribe(take_key,name_list[name]['其他属性'])
    return result_many_list_of_discribes
'''
#0.stencil：一个格式为str，具体内容是输出的语句的语法格式，其中待填入的词语用{n30}来代替，其中的n3代表三字名词，0代表标号，第一个
num:一个字典，对应需要取的词语类型及对应数量
num_words：一个字典，对应随机取的各类词的全部种类对应的词汇。

'''
