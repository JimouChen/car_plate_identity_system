"""
# @Time    :  2020/6/27
# @Author  :  Jimou Chen
"""
# import identity.deal_plate_image
from identity.tool_function import *
import numpy as np

# 定义要匹配的关键字，根据实际情况，去掉O和I
keywords = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
            'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '藏', '川', '鄂', '甘', '赣', '贵', '桂', '黑', '沪', '吉', '冀',
            '津', '晋', '京', '辽', '鲁', '蒙', '闽', '宁', '青', '琼', '陕',
            '苏', '皖', '湘', '新', '渝', '豫', '粤', '云', '浙']

# 匹配中文
chinese_words = []
for i in range(34, 64):
    c_word = read_directory('./refer_img/' + keywords[i])
    chinese_words.append(c_word)

# 先匹配第一个中文，读取一个车牌的中文字符
c_img = cv2.imread('./every_word/1.png')
c_img = gauss_img(c_img)

# 自适应阈值处理
ret, c_img = cv2.threshold(c_img, 0, 255, cv2.THRESH_OTSU)
show_gray(c_img)

# 先遍历匹配中文
best_score = []  # 定义一个最高匹配度的列表
for c_word in chinese_words:
    score = []
    for word in c_word:
        # fromfile()函数读回数据时需要用户指定元素类型，并对数组的形状进行适当的修改
        template_img = cv2.imdecode(np.fromfile(word, dtype=np.uint8), 1)
        # 对读进来的模板图片进行处理
        # template_img = cv2.cvtColor(template_img, cv2.COLOR_RGB2GRAY)
        template_img = gauss_img(template_img)
        ret, template_img = cv2.threshold(template_img, 0, 255, cv2.THRESH_OTSU)

        # 不能直接匹配，要使两张图片具有相同的尺寸
        height, width = template_img.shape
        image = c_img.copy()
        image = cv2.resize(image, (width, height))  # 把图片尺寸设成一样的
        # 调用模板匹配函数matchTemplate，用cv2.TM_CCOEFF的算法进行匹配，返回值越大，表示越相关
        result = cv2.matchTemplate(image, template_img, cv2.TM_CCOEFF)
        score.append(result[0][0])
    best_score.append(max(score))


print(best_score.index(max(best_score)))
print(keywords[34 + best_score.index(max(best_score))])
