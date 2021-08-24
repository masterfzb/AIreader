
import pandas as pd
import os
import data_base

'''
    一个存取dict的小工具
    无限嵌套的dict会以excel的格式保存在文件夹里。
    注意：dict内不能有list格式，否则读取会失败。
    a = {'b':{'c':{}}}
'''

def savepathyes(savepath):
    if not os.path.exists(savepath):
        os.mkdir(savepath)


def save_a_dic(dic,savepath,dicname):#dict，D：/....,“life_list”
    savepathyes(savepath)#确保savepath存在
    k = []
    for key in dic:
        if type(dic[key]) == type({}):
            save_a_dic(dic[key],savepath + dicname+"/",key)
            num = [key, "dicttype"]
        else:
            num = [key, dic[key]]
        k.append(num)#[[key1:"dicttype"],[key2:"afdk;lasjfk;asdjfds;afjks;dak;f"]]
    data = pd.DataFrame(k)
    writer = pd.ExcelWriter(savepath + dicname + '.xlsx')  # 写入Excel文件
    data.to_excel(writer)
    writer.save()

def read_a_dic(savepath,dicname):
    thedict ={}
    file = savepath+'/'+ dicname + '.xlsx'
    data = pd.read_excel(file).to_dict()
    for keys in data[0]:
        thedict[data[0][keys]]=data[1][keys]
        if data[1][keys]=='dicttype':
            try:
                thedict[data[0][keys]] = read_a_dic(savepath+'/'+ dicname + '/',data[0][keys])
            except:
                thedict[data[0][keys]] = {}
    return thedict

'''
杀掉一个键值，并更新到系统里
world_update
输入：
save_path保存的路径str
dicname待更新的dict的名字str
dic待更新的dict
执行过程中会将dic更新到系统存储目录里

kill_a_key
输入：
save_path保存的路径str
dicname包含带删除键值key的dict的名字str
killname带删除的键值key的名字str
dic包含删除键值key的dict
输出：
删除键值对后的dic
执行过程中会将删除键值对后的dic更新到系统存储目录里

'''

def del_file(path_data):
    for i in os.listdir(path_data) :# os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + "\\" + i#当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data) == True:#os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file_data)
        else:
            del_file(file_data)

		
def world_update(savepath,dicname,dic):
    del_file(savepath+'/'+dicname)
    os.remove(savepath+'/'+dicname+'.xlsx')
    save_a_dic(dic,savepath,dicname)

def kill_a_key(savepath,dicname,killname,dic):
    if killname in dic.keys():
        del dic[killname]
    world_update(savepath,dicname,dic)
    return dic

