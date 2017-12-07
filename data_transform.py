"""
    对训练集进行格式处理，每一句用空行隔开，每一行包含：字 B/I
"""
def word_BI(sourceFileName,targetFileName):
    f = open(sourceFileName, 'r', encoding='utf-8')
    f_BI = open(targetFileName, 'a', encoding='utf-8')
    lines = [line.rstrip() for line in f.readlines()]
    line_word = [line.split() for line in lines]
    print(len(line_word))
    word_num = 0 #统计数据中所有的词数
    character_num = 0  #统计数据中所有的字数
    for words in line_word:
        word_num += len(words)
        for word in words:
            character_num += len(word)
            if (len(word) == 1):
                f_BI.write(word + ' ' + 'B\n')
            else:
                for i in range(len(word)):
                    if (i == 0):
                        f_BI.write(word[i] + ' ' + 'B' + '\n')
                    else:
                        f_BI.write(word[i] + ' ' + 'I' + '\n')
        if (words != line_word[-1]):
            f_BI.write('\n')
    f_BI.close()
    f.close()

if __name__ == "__main__":
    print("utils main")
    word_BI("./data/CTB5/train.ctb50.seg", "./data/CTB5/train.ctb50.BI.seg")
    word_BI("./data/CTB5/dev.ctb50.seg", "./data/CTB5/dev.ctb50.BI.seg")
    word_BI("./data/CTB5/test.ctb50.seg", "./data/CTB5/test.ctb50.BI.seg")