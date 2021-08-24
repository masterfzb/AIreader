'''
    一些用于生成代码的小工具，对程序没影响。
'''
import pyttsx3
import use_to_wave

import numpy as np
import sounddevice as sd


text='你知道我在说什么吗'
text1='我怎么知道'
voice=pyttsx3.init()
voice.say(text)

result = voice.getProperty('voice')
voice.runAndWait()
voice.save_to_file(text, 'try.MP3')
voice.save_to_file(text1, 'try.MP3')
#use_to_wave.use_to_save(text)
use_to_wave.use_to_save(text1)



for a in ['M_','JL_','god_']:
    for b in ['man_','woman_']:
        for c in['low','mid','high','very_high']:
            #'god_woman_very_high':"",
            print('\'' + str(a + b + c) + '\':' + '{\'\':\"\".split(\'/\')},')
            #'M_man_low':"".split('/'),
            #print('\''+str(a+b+c)+'\':'+'\"\"'+".split(\'/\'),")
            #'god_woman_very_high':complete_the_discribe('god_woman_very_high'),
            #print('\''+str(a+b+c)+'\':'+'complete_the_discribe(\''+str(a+b+c)+'\'),')
