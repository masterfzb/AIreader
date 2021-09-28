from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.filedialog as filedlg
import os
import pyttsx3
from pydub import AudioSegment
import threading

txtfile = ""
window = Tk()
pathlabel = Label(window, text="...")

'''
MP3转换接口：
use_by_txt(使用一个txt所在的地址直接调用，然后生成txt对应的MP3文件)
use_by_identity是一个独立程序，如果你在当前窗口调用，调用前记得注释掉main
'''




def fileFunc():
    default_dir = "文件路径"
    global txtfile
    global pathlabel
    txtfile = filedlg.askopenfilename(title="选择文件", initialdir=(os.path.expanduser(default_dir)))
    (path, fname) = os.path.split(txtfile)
    pathlabel["text"] = fname

def converThreadFunc(content):
    outfile = "out.aiff"
    tts = pyttsx3.init()
    tts.save_to_file(content, outfile)
    tts.runAndWait()

def convertFunc():
    if len(txtfile) == 0:
        msgbox.showinfo("提示", "请先选择文本文件")
        return
    content = open(txtfile, "r",encoding='ansi').read()
    if len(content)==0:
        msgbox.showinfo("提示", "文本文件没有内容，转换终止，不输出语音文件")
        return
    t1 = threading.Thread(target=converThreadFunc, args=(content,))
    t1.start()
    t1.join()
    outfile = "out.aiff"
    AudioSegment.from_file(outfile).export("out.mp3", format="mp3")
    msgbox.showinfo("提示", "转换成功，程序目录下的out.mp3就是最终的语音文件：%s" % os.getcwd())
    os.system("open '%s'" % os.getcwd())

def use_by_identity():
    window.title("TTS-文本转换语音")
    window.geometry("320x320+100+100")
    filebtn = Button(window, text="选择文本文件", command=fileFunc)
    convertbtn = Button(window, text="转换成语音", command=convertFunc)
    filebtn.place(x=10, y=10)
    pathlabel.place(x=10, y=40)
    convertbtn.place(x=10, y=80)
    window.mainloop()

def use_by_txt(txtpath):
    if len(txtpath) == 0:
        msgbox.showinfo("提示", "请先选择文本文件")
        return
    content = open(txtpath, "r",encoding='ansi').read()
    if len(content)==0:
        msgbox.showinfo("提示", "文本文件没有内容，转换终止，不输出语音文件")
        return
    converThreadFunc(content)
    outfile = "out.aiff"
    AudioSegment.from_file(outfile).export("tlj.mp3", format="mp3")
    #msgbox.showinfo("提示", "转换成功，程序目录下的tlj.mp3就是最终的语音文件：%s" % os.getcwd())
#use_by_identity()
#if __name__=="__main__":
    #main()