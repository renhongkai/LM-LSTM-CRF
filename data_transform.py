"""
    对训练集进行格式处理，每一句用空行隔开，每一行包含：字 B/I
"""
def word_BI(sourceFileName,targetFileName):
    f = open(sourceFileName, 'r', encoding='utf-8')
    f_BI = open(targetFileName, 'a', encoding='utf-8')
    lines = [line.rstrip() for line in f.readlines()]
    line_word = [line.split() for line in lines]
    word_num = 0 #统计数据中所有的词数
    character_num = 0  #统计数据中所有的字数
    for words in line_word:
        word_num += len(words)
        for word in words:
            character_num += len(word)
            if (len(word) == 1):
                f_BI.write(word + ' ' + 'B' + '\n')
            else:
                for i in range(len(word)):
                    if (i == 0):
                        f_BI.write(word[i] + ' ' + 'B' + '\n')
                    else:
                        f_BI.write(word[i] + ' ' + 'I' + '\n')
        f_BI.write('\n')
    # print("句子数", len(lines))
    # print("词数", word_num)
    # print("字数",character_num)
    f_BI.close()
    f.close()
def generate_test_data(test_data_filename):
    f = open(test_data_filename, 'r', encoding='utf-8')
    lines = [line.rstrip() for line in f.readlines()]
    test_data = []
    test_data_item = []
    for line in lines:
        if line == '':
            if len(test_data_item) != 0 :
                test_data.append(test_data_item)
            test_data_item = []
        else:
            test_data_item.append(line[0])
    if len(test_data_item) != 0:
        test_data.append(test_data_item)  # 追加最后一个句子
    f.close()
    return test_data

"""
    统计句子数，词数
"""

if __name__ == "__main__":
    print("utils main")
    word_BI("./data/CTB5/train.ctb50.seg", "./data/CTB5/train.ctb50.BI.seg")
    word_BI("./data/CTB5/dev.ctb50.seg", "./data/CTB5/dev.ctb50.BI.seg")
    word_BI("./data/CTB5/test.ctb50.seg", "./data/CTB5/test.ctb50.BI.seg")
    # generate_test_data("./data/CTB5/dev.ctb50.BI.seg")