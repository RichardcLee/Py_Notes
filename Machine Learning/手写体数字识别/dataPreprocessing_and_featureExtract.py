'''
project: data preprocess
author: 李云浩
date: 2018.1.15
comment: 实现图像预处理以及图像特征值提取
'''
import cv2
import os
import numpy as np
from tools import timer


def detect_num_border_in_picture(img: np.ndarray):
    '''
    " find the minx miny maxx maxy in the picture"
    :param img: 图像矩阵
    :return: 边界元组 minx, miny, maxx, maxy
    '''
    minx, miny, maxx, maxy = 39, 39, 0, 0   # 数字区域的边界
    for i, a_line_pixel in enumerate(img):  # 遍历像素点寻找边界值
        for j, pixel in enumerate(a_line_pixel):
            if pixel == 0:  # 只对于每一个黑色像素点进行比较
                minx = i if i < minx else minx
                miny = j if j < miny else miny
                maxx = i if maxx < i else maxx
                maxy = j if maxy < j else maxy
    # print('ones: ', minx, miny, maxx, maxy)
    return minx, miny, maxx, maxy


def clip_compress_picture(border: tuple, img: np.ndarray, leave_space: int=0):
    '''
    "裁剪图片，取出数字区域，并压缩为8*8"
    :param border: 边界元组 minx, miny, maxx, maxy
    :param img: 图像矩阵
    :param leave_space: 留白值，避免裁剪过度，默认不留白
    :return: img 处理后的图像矩阵
    '''
    minx, miny, maxx, maxy = border
    # img = img[minx-leave_space:maxx+leave_space, miny-leave_space:maxy+leave_space]
    x_space, y_space = maxx - minx, maxy - miny  # 图像中数字区域的高和宽
    if x_space > y_space:  # 若宽>高，取面积为宽*宽(x_space*x_space)个像素的区域，但要防止图像向上方偏移
        diff = (x_space - y_space) // 2     # 纵向居中偏移量
        y_start = miny-leave_space-diff if miny-leave_space-diff >=0 else 0  # 纵向裁剪起点需偏移diff个像素或直接偏移到0
        y_end = miny+x_space+leave_space-diff  if miny-leave_space-diff >=0 else x_space  # 纵向裁剪终点需偏移diff个像素或直接偏移到x_space
        img = img[minx-leave_space:maxx+leave_space+1, y_start:y_end]   # 切出图像中的数字
    else:   # 若宽<=高，取面积为高*高(y_space*y_space)个像素的区域，但要防止图像向左偏移
        diff = (y_space - x_space) // 2     # 横向居中偏移量
        x_start = minx-leave_space-diff if minx-leave_space-diff >=0 else 0  # 横向裁剪起点需偏移diff个像素或直接偏移到0
        x_end = minx+y_space+leave_space-diff if minx-leave_space-diff >=0 else y_space  # 横向裁剪终点需偏移diff个像素或直接偏移到y_space
        img = img[x_start:x_end, miny-leave_space:maxy+leave_space+1]

    img = cv2.resize(img, (8, 8), cv2.INTER_CUBIC)  # ８＊８图像
    return img


def save_pic(img, path, old_file_name):
    '''
    为每张图片生成新的名字，并将分类的图片存放到相应目录 0-0, 1-1, ..., 9-9
    :param img: 待保存的图像
    :param path: 保存路径
    :param old_file_name: 原文件名
    :return:
    '''
    dir_name = path+'/'+old_file_name.split('_')[0]
    if not os.path.exists(dir_name):    # 首先应创建对应的数字目录
        os.mkdir(dir_name)

    cv2.imwrite(dir_name+'/'+old_file_name.split('_')[-1], img)


@timer('开始提取特征', '特征提取完毕，')
def extract_feature_vector(new_path, save_path):
    '''
    提取特征向量，并保存
    :param new_path:　预处理后的图像的路径
    :param save_path:　特征值的保存路径
    :return:
    '''
    num_list = os.listdir(new_path)   # 数字０－９
    result = np.array([i for i in range(65)])   # 特征矩阵

    for num in num_list:
        pic_list = os.listdir(new_path + '/' + num)
        for pic in pic_list:
            img = cv2.imread(new_path + '/' + num + '/' + pic, cv2.IMREAD_GRAYSCALE)
            img = np.append(img, int(num))  # (65,)
            result = np.vstack((result, img))

    np.savetxt(save_path, result[1:])    # 第一行要去掉
    print('save data successfully!')


def load_picture(pic_path):
    '''
    读取灰度图并二值化，完成图像预处理流程，裁剪并压缩图像，返回图像矩阵
    :param pic_path: 待加载图像的路径
    :return:
    '''
    img = cv2.imread(pic_path, cv2.IMREAD_GRAYSCALE)  # 读取灰度图
    *_, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)  # 二值化
    border = detect_num_border_in_picture(img)  # 计算图像中的数字区域的边界
    img = clip_compress_picture(border, img, 0)  # 裁剪、压缩图像
    return img


@ timer('开始图像预处理', '预处理完成，')
def main(old_path, new_path):
    '''
    主函数
    :param old_path: 原图片的路径
    :param new_path: 处理后图像保存的路径
    :return:
    '''
    pic_list = os.listdir(old_path)
    for pic in pic_list:
        print(pic)
        img = load_picture(old_path + '/' + pic)
        save_pic(img, new_path, pic)    # 保存图像


if __name__ == '__main__':
    old_path = './WeMNTS'  # 保存原始数据（图片）的路径
    new_path = './after clip and compress'  # 分类保存预处理后的图像的路径
    save_path = 'train_data.txt'
    main(old_path, new_path)  # 图像预处理
    extract_feature_vector(new_path, save_path)   # 提取特征向量



