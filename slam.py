#!/usr/bin/env python3
import time
import cv2
from display import Display
from extractor import Extractor
import numpy as np

W = 1920//2
H = 1080//2

F = 270
disp = Display(W, H)
K = np.array([[F,0,W//2], [0,F,H//2], [0,0,1]])
print(K)
fe = Extractor(K)

def process_frame(img):
  # cv2 + SDL2: 显示绘制纹理多边形
  img = cv2.resize(img,(W, H))
  matches,pose = fe.extract(img)
  if pose is None:
    return

  print("%d matches" % (len(matches)))
  print(pose)

  def denormalize(pt):
    return int(round(pt[0] + img.shape[0]//2)), int(round(pt[1] + img.shape[1]//2))

  for pt1, pt2 in matches:
    # 匿名函数lambda关键字 参数x ： 返回值= int(round(x)) 
    # =>为了解决那些功能很简单的需求而设计的一句话函数
    #
    # map(func, seq1[, seq2,…]) 
    # 第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，
    # 返回的是一个集合。Python函数编程中的map()函数是将func作用于seq中
    # 的每一个元素，并将所有的调用的结果作为一个list返回
    u1, v1 = fe.denormalize(pt1)
    u2, v2 = fe.denormalize(pt2)

    # 要绘制一个圆，需要它的中心坐标和半径
    cv2.circle(img, (u1, v1), color=(0,255,0),radius=3)
    cv2.line(img, (u1, v1), (u2, v2), color=(255,0,0))

  disp.paint(img)


if __name__ == "__main__":
  # 创建一个VideoCapture对象并从输入文件中读取
  # 如果输入是相机，则传递0而不是视频文件名称
  cap = cv2.VideoCapture('test.mp4')
  # 读直到视频完成
  while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
      process_frame(frame)
    else:
      break


 

 
