import os;
import sys;
import csv;
import jieba;

# jieba.set_dictionary('/home/diego/.local/lib/python3.8/site-packages/pinyin_jyutping_sentence/dict.txt.big')

os.system("rm output.txt")
myfile='in.txt'
os.system("sed -E 's/^ +//;s/ +$//;s/^M$//' " + sys.argv[1] + " > " + myfile)
with open('output.txt', 'a', newline='') as OutputFile:
    with open(myfile, newline='') as csvfile:
        lines = csvfile.readlines()
        for line in lines:
            line = line.strip()
            if line != '':
                phraseZH = ''
                linea = ''
                seg_list = jieba.cut(line, cut_all=False)
                baiduZH='https://fanyi.baidu.com/#zh/en/' + line
                mdbgZH='https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb=' + line
                baiduZH = ' <a href="' + baiduZH + '">Baidu</a>'
                mdbgZH = ' <a href="' + mdbgZH + '">MBDG</a>'

                for word in seg_list:
                    flag = False
                    for chars in word:
                        if '\u4E00' <= chars <=  '\u9FFF':
                            flag = True
                            break
                    if flag:
                        linea = '<a href="https://www.yellowbridge.com/chinese/dictionary.php?word=' + word + '" style="text-decoration:none;color:black">' + word + '</a>'
                        phraseZH = phraseZH + linea
                    else:
                        phraseZH = phraseZH + word
                OutputFile.write(phraseZH + baiduZH + mdbgZH + "\n")
            else:
                OutputFile.write("\n")
    csvfile.close()
OutputFile.close()
