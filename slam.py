#!/usr/bin/env python3
import time
import cv2
from display import Display
#import pygame
#import numpy

W = 1920//2
H = 1080//2

disp = Display(W, H)

def process_frame(img):
  # cv2 + SDL2: 显示绘制纹理多边形
  img = cv2.resize(img,(W, H))
  disp.paint(img)


  '''
  # 显示结果帧 -- 取名图片窗口名为image，显示图片是img
  #cv2.imshow('image', img)

  # 按任意键播放视频 -- 单帧播放视频
  #cv2.waitKey(0)
  #print("====================")
  # (1080, 1920, 3)
  #print(img.shape)
  #print(img)
  '''
 

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


