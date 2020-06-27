"""
# @Time    :  2020/6/27
# @Author  :  Jimou Chen
"""
import identity.deal_plate_image
from identity.tool_function import *

# 按照车牌结构，第一位是中文，第二位是英文，后面的是英文和数字混合
chinese_words = get_chinese_words_list()
eng_words = get_eng_words_list()
eng_num_words = get_eng_num_words_list()
all_words = get_all_words_list()

results = []


# 匹配识别每个字符
def template_words(word_image, word_type, start_index):
    # 自适应阈值处理
    ret, word_image = cv2.threshold(word_image, 0, 255, cv2.THRESH_OTSU)
    show_gray(word_image)
    print('正在识别中......')
    best_score = []  # 定义一个最高匹配度的列表
    for words in word_type:
        score = []
        for word in words:
            result = template_score(word, word_image)
            score.append(result)
        best_score.append(max(score))  # 匹配到效果最好的所在下标
    best_index = best_score.index(max(best_score))
    # if min(best_score) <= 0:
    #     return
    res = keywords[start_index + best_index]
    print('识别结果为：------', res)
    results.append(res)


# 先匹配第一个中文，读取一个车牌的中文字符
# c_img = cv2.imread('./every_word/1.png')
# c_img = gauss_img(c_img)
# template_words(c_img, chinese_words, 34)
# print(results)

# 得到字符的个数，有的车牌是7个，有的是8个
count_list = read_directory('./every_word')
count_words = len(count_list)

for i in range(1, count_words + 1):
    c_img = cv2.imread('./every_word/' + str(i) + '.png')
    c_img = gauss_img(c_img)
    # 为了提高匹配效率，把第一位的中文和第二位的英文单独拿出来匹配
    if i == 1:
        template_words(c_img, chinese_words, 34)
    elif i == 2:
        template_words(c_img, eng_words, 10)
    elif 3 <= i <= 8:
        template_words(c_img, eng_num_words, 0)
    else:
        break

print(results)
