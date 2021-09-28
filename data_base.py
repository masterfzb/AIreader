import random
import time
'''
数据库，未来数据库会向实体数据库迁移。
这些将作为初始化用数据。
并给出展示数据的一类解决方案
'''
'''
================================================================tools=================================================

'''
'''
对只有str的list用
'''
def geting_str(lists):
 lis = ''
 for items in lists:
  lis += items
 return lis
'''
将str转换为float
'''
def eval_str(lists):
 lis = list()
 for items in lists:
  lis.append(eval(items))
 return lis
'''
get_all_in_lists是一个获取无限嵌套的list的内容的工具
对一个无限嵌套的list，把内容弄成一个str并返回。

'''

def get_all_in_lists(lists):
 what_to_get = ''
 for items in lists:
  if type(items)==type(list()):
   what_to_get +=get_all_in_lists(items)
  else:
   what_to_get +=items
 return what_to_get
'''
   choice_weight（）是权重工具。
   list1为原始数据
   list2为数据权重
   list3会输出一个根据权重分配的list
'''
def choice_weight(list1,list2):
 times = 0
 list3 = list()
 for items in list1:
  #print(list2[times])
  if list2[times] >= 1:
   for i in range(0,list2[times]):
    list3.append(items)
  else:
   if (time.time()%10)/10 < list2[times]:
    list3.append(items)
  times += 1
 return list3
'''
show_list 和 show_dic 是简单的展示工具
展示对象分别是简单list和只包含dict格式的dict
'''
def show_data(lis):
 print(
  '''====================================================================\n'''+str(lis)+'\n====================================================================\n'
 )

def show_dic(dic):
 for items in dic:
  if type(dic[items])==type({}):
   print('==================================\n' + items + '\n==================================')
   show_dic(dic[items])
  else:
   print(items+':'+dic[items])
'''
为生物做设定
内容包含基础存在的参数和对应权重
未来会增加，每次增加都需要更改all_list前缀的list，使之包含对应内容
'''

'''
================================================================datas=================================================

'''
#种族设定

types_list = ["神", "精灵", "平民"]
types_list_weight = [0.125,0.25,2]
sex_list = ["男","女","不涉及"]
sex_list_sex= [1,2,0.005]
height_list = ["高", "低"]
height_list_weight = [0.5,2]
zu_list = ["宗族","散人"]
zu_list_weight =[0.25,2]
waimao_list =["平平无奇","丑陋不堪","姿色极佳","倾国倾城"]
waimao_list_weight = [2,0.5,1,0.5]

all_list = [tuple(types_list),tuple(sex_list),tuple(height_list),tuple(zu_list),tuple(waimao_list)]
all_list_weight = [tuple(types_list_weight),tuple(sex_list_sex),tuple(height_list_weight),tuple(zu_list_weight),tuple(waimao_list_weight)]
all_list_name = ("种族","性别","位阶","族群","外貌")
#all_list_values = ["types","sex","height","zu"]

'''
姓氏由种族和位阶决定
平民的名字另外还由性别决定
此外平民的宗族男性拥有特殊的第二字
'''

#取名设定
first_name = {"low_JL":("孑然/白马/青丘/夜宴/寒山/风月/崆峒/轩墨/虎/错/留观".split('/')),
 "high_JL":("饕餮/千年/劫/麒麟/龙/乘/忘川/修罗/貔貅/沧海".split('/')),
 "god":("神隐/时烬/墨染/须臾/帝/殇酒".split('/')),
"high_M":("猫/小诗/胧胧/皮皮/丘丘/杀神/楚楚".split('/')),
"low_M":("宫/鱼/方/陈/夏/黄/萧/上官/李/公输/叶/林/南方".split('/'))}

second_name_1 = {
	"man_san":("知/忘/溟/斩/留//超/空/读/修/酒///莫///虚/寒/笑/乱/秋/抄/丹/青".split('/')),
"man_zu":("天/地/玄/黄/宇/宙/洪/荒/河/清/日/海/晏".split('/')),
"woman":("初/海/湘/倩/冰//溟/空/虚/清/记/怜/海/".split('/')),
"low_JL":("非/空/秋/其/小/筑/城/时/凉///".split('/')),
 "high_JL":("窥/红/临/留/钟/流/晴//弥/区".split('/')),
 "god":("古/释//上/枯/旧/初//".split('/'))

}
second_name = {"man_zu":('才/德/行/渺/名/记/者/客/迷/烬/期/棋/奇'.split('/')),
"man_san":("书/名/定/克/千/终/青/必/天/生/棋".split('/')),
"woman":("倩/涵/韵/晗/菡/脉/冰/琳/林/霖/琦/期/幂/宓/姬/璃".split('/')),
"low_JL":("马/非/山/名/兽/橙/诗/时/印".split('/')),
 "high_JL":("天/名/江/仙/棋/觞/明/祭/耳".split('/')),
 "god":("名/天/隐/舞/斩/清/枯/冬/秋/封-".split('/')),
}

#参数设定
types_of_job = {"low_JL":("巡林者/守夜人/指路人/导学者/堕仙".split('/')),
 "high_JL":("神助/执法者/守剑者/守秘人/超位精灵/半神/高阶魔导/德鲁伊/鹰巡".split('/')),
 "god":("守时人/引路人/告密者/驱命者/殇神/秘宗/除尘/熄灯者/语冰人".split('/')),
"high_M":("修客/.\"女王.\"/豪绅/伪绅/强盗/前旧约骑士/新约骑士/祭司".split('/')),
"low_M":("耕客/行商/村医/祝客/电工/初心者/隐者/无名/隐名".split('/'))}

types_of_needs_basic = ("尚武","崇文","贪财","好色","滥情","惜命","从善")
JL_need_weight =[3,1,0.5,5,2,3,2]
M_need_weight =[0.5,0.5,1,3,0.5,1,0.7]
god_need_weight =[0.1,0.1,0.5,1,1,0.3,1]

all_out_look = ["发色","刘海","后发","脸型","身材","腿型","脚型","气质"]
out_look_dict_man ={
"发色":"玄墨/银白/金黄/冥紫/骚粉/粉红/天蓝/朱红/碧绿/苍白".split('/'),
"刘海":"M字刘海/中分/高额头/覆眼".split('/'),
"后发":"短双马尾/长双马尾/及腰长发/长至脚踝的长发/及颈部的短发/马尾/盘头发/羊角辫/盘子头发/姬式长发/姬式短发/笔直的后发".split('/'),
"脸型":"瓜子脸/鹅蛋脸".split('/'),
"身材":"瘦弱的身姿/匀称的身材/圆润的身材".split('/'),
"腿型":"笔直的腿/纤细的腿/匀称的腿/粗壮的大腿".split('/'),
"气质":"文弱书生/大将军/大侠/仙风道骨/无情客/隐者".split('/')
}
out_look_dict_man_weight ={
"发色":"4/2/1/0.5/0.1/0.3/1.5/1/0.4/1".split('/'),
"刘海":"4/2/1/0.5".split('/'),
"后发":"0.1/0.1/2/0.3/2/0.2/1/0.01/0.3/0.2/0.1/5".split('/'),
"脸型":"3/5".split('/'),
"身材":"2/3/4".split('/'),
"腿型":"3/4/5/6".split('/'),
"气质":"2/3/2/5/1/1".split('/')
}

out_look_good_dict_man ={
"发色":"乌黑浓密的/飘逸的/落落大方的/清新脱俗的/飘逸的/干净利落的/笔直干练的/精神焕发的/飘飘若仙的/飘飘若仙的".split('/'),
"刘海":"/".split('/'),
"后发":"/".split('/'),
"脸型":"可人的/俊俏的".split('/'),
"身材":"迷人的/令人激赏的/讨人喜欢的".split('/'),
"腿型":"腿玩年的/强壮的/紧实的/完美的".split('/'),
"气质":"帅气的/俊秀的".split('/')
}
out_look_good_dict_man_weight ={
"发色":"4/2/1/0.5/0.1/0.3/1.5/1/0.4/1".split('/'),
"刘海":"4/2".split('/'),
"后发":"0.1/0.1".split('/'),
"脸型":"3/5".split('/'),
"身材":"2/3/4".split('/'),
"腿型":"3/4/5/6".split('/'),
"气质":"2/3".split('/')
}

out_look_bad_dict_man ={
"发色":"头发稀疏的/乱蓬蓬的/脏乱的/不整洁的/过时的".split('/'),
"刘海":"/".split('/'),
"后发":"/".split('/'),
"脸型":"很突出的/令人不快的".split('/'),
"身材":"不好看的/平常的/略有些畸形的".split('/'),
"腿型":"普通的/平常的/略有些罗圈的/略不等长的".split('/'),
"气质":"猥琐至极/不能直视".split('/')
}
out_look_bad_dict_man_weight ={
"发色":"4/2/1/0.5/2".split('/'),
"刘海":"4/2".split('/'),
"后发":"0.1/0.1".split('/'),
"脸型":"3/5".split('/'),
"身材":"2/3/4".split('/'),
"腿型":"3/4/5/6".split('/'),
"气质":"2/3".split('/')
}

out_look_dict_woman ={
"发色":"玄墨/银白/金黄/冥紫/骚粉/粉红/天蓝/朱红/碧绿/苍白".split('/'),
"刘海":"M字刘海/中分/高额头/覆眼".split('/'),
"后发":"短双马尾/长双马尾/及腰长发/长至脚踝的长发/及颈部的短发/留着马尾/盘头的长发/扎着羊角辫/扎着盘子头/姬式长发/姬式短发/笔直的后发".split('/'),
"脸型":"瓜子脸/鹅蛋脸".split('/'),
"身材":"瘦弱的身体/匀称的身材/圆润的身体".split('/'),
"腿型":"笔直的腿/纤细的腿/匀称的腿/粗壮的腿".split('/'),
"气质":"小家碧玉/闺中少女/大家闺秀/仙子/风尘女子/美人儿".split('/')
}
out_look_dict_woman_weight ={
"发色":"8/5/3/2/5/3/2/4/1/4".split('/'),
"刘海":"4/2/1/0.5".split('/'),
"后发":"6/4/4/3/3/5/1/7/3/6/6/5".split('/'),
"脸型":"5/3".split('/'),
"身材":"6/5/4".split('/'),
"腿型":"5/4/5/1".split('/'),
"气质":"2/3/2/5/1/1".split('/')
}
out_look_good_dict_woman ={
"发色":"乌黑浓密的/飘逸的/大方的/清新脱俗的/飘逸的/干净利落的/笔直干练的/精神焕发的/飘飘若仙的/飘飘若仙的".split('/'),
"刘海":"/".split('/'),
"后发":"/".split('/'),
"脸型":"娇美的/惹人怜爱的".split('/'),
"身材":"迷人的/令人激赏的/讨人喜欢的".split('/'),
"腿型":"腿玩年的/强壮的/紧实的/完美的".split('/'),
"气质":"倾国倾城的/如沐春风的".split('/')
}
out_look_good_dict_woman_weight ={
"发色":"4/2/1/0.5/0.1/0.3/1.5/1/0.4/1".split('/'),
"刘海":"4/2".split('/'),
"后发":"0.1/0.1".split('/'),
"脸型":"3/5".split('/'),
"身材":"2/3/4".split('/'),
"腿型":"3/4/5/6".split('/'),
"气质":"2/3".split('/')
}

out_look_bad_dict_woman ={
"发色":"头发稀疏的/乱蓬蓬的/脏乱的/不整洁的/过时的".split('/'),
"刘海":"/".split('/'),
"后发":"/".split('/'),
"脸型":"很突出的/令人不快的".split('/'),
"身材":"不好看的/平常的/略有些畸形的".split('/'),
"腿型":"普通的/平常的/略有些罗圈的/略不等长的".split('/'),
"气质":"挺丑的/难看的".split('/')
}
out_look_bad_dict_woman_weight ={
"发色":"4/2/1/0.5/2".split('/'),
"刘海":"4/2".split('/'),
"后发":"0.1/0.1".split('/'),
"脸型":"3/5".split('/'),
"身材":"2/3/4".split('/'),
"腿型":"3/4/5/6".split('/'),
"气质":"2/3".split('/')
}

def out_look_get(item,return_list):
 #print(return_list)
 if return_list[1] == '男':
  if return_list[4] == '丑陋不堪' and return_list[0] !='神':
   to_return = geting_str(random.choices(out_look_bad_dict_man[item],eval_str(out_look_bad_dict_man_weight[item]),k=1))
  else:
   to_return = geting_str(random.choices(out_look_good_dict_man[item], eval_str(out_look_good_dict_man_weight[item]), k=1))
  to_return += geting_str(random.choices(out_look_dict_man[item],eval_str(out_look_dict_man_weight[item]),k=1))
 else:
  if return_list[4] == '丑陋不堪' and return_list[0] !='神':
   to_return = geting_str(random.choices(out_look_bad_dict_woman[item], eval_str(out_look_bad_dict_woman_weight[item]), k=1))
  else:
   to_return = geting_str(random.choices(out_look_good_dict_woman[item], eval_str(out_look_good_dict_woman_weight[item]), k=1))
  to_return += geting_str(random.choices(out_look_dict_woman[item], eval_str(out_look_dict_woman_weight[item]),k=1))
 return to_return