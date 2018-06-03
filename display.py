#!/usr/bin/env python3

import sdl2
import sdl2.ext


class Display(object):
  def __init__(self, W, H):
    sdl2.ext.init()

    self.W, self.H = W, H
    self.window = sdl2.ext.Window("twitch SLAM", size=(W, H), position=(-500, -500))
    self.window.show()

  def paint(self, img):
    # junk
    events = sdl2.ext.get_events() # 获取当前在事件队列中的所有SDL事件
    for event in events:
      if event.type == sdl2.SDL_QUIT:
        exit(0)
    #print(dir(window))

    # draw--窗口是在运行时创建的SDL_Window对象
    surf = sdl2.ext.pixels3d(self.window.get_surface())
    #surf[:] = img.swapaxes(0,1)[:,:,0] # 就是将第1个维度和第2个维度交换
    surf[:,:,0:3] = img.swapaxes(0,1)  # 就是将第1个维度和第2个维度交换
    
    # blit--块传送
    self.window.refresh()
