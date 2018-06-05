
# liuchuandeMacBook-Pro-4% source .bash_profile

1、tmux: 
   发现tmux大家介绍的不错，所以想尝试一下，但发现无论ctrl+a，还是ctrl+b都不好使，经过一番努力后才发现应该是ctrl+b松开后再按其他键。例如ctrl+b ？，应该先同时按ctrl+b 松开后，shift+/（即输入？）。

2、在linux的终端怎么退出python命令行：使用 quit(), exit(), 或者Ctrl-D退出命令行。

3、复制文字：鼠标选择文字，摁住command+c，粘贴用command+v

4、chmod +x slam.py
指令名称 : chmod 
使用权限 : 所有使用者 
使用方式 : chmod [-cfvR] [--help] [--version] mode file... 
说明 : Linux/Unix 的档案调用权限分为三级 : 档案拥有者、群组、其他。利用 chmod 可以藉以控制档案如何被他人所调用。 
参数 : 
mode : 权限设定字串，格式如下 : [ugoa...][[+-=][rwxX]...][,...]，其中 
u 表示该档案的拥有者，g 表示与该档案的拥有者属于同一个群体(group)者，o 表示其他以外的人，a 表示这三者皆是。 
+ 表示增加权限、- 表示取消权限、= 表示唯一设定权限。 
r 表示可读取，w 表示可写入，x 表示可执行，X 表示只有当该档案是个子目录或者该档案已经被设定过为可执行。 
-c : 若该档案权限确实已经更改，才显示其更改动作 
-f : 若该档案权限无法被更改也不要显示错误讯息 
-v : 显示权限变更的详细资料 
-R : 对目前目录下的所有档案与子目录进行相同的权限变更(即以递回的方式逐个变更) 
--help : 显示辅助说明 
--version : 显示版本 

5、安装opencv：用conda install opencv / pip install opencv-python
   使用opencv：liuchuandeMacBook-Pro-4% source .bash_profile 然后选择视频按任意键=视频流动
   # opencv-python
   export PYTHONPATH=$PYTHONPATH:/Users/bccw/anaconda3/lib
   # open -e .bash_profilei

6、安装pygame: brew install sdl sdl_image sdl_mixer sdl_ttf portmidi mercurial

7、vlc打开视频：alias vlc='/Applications/VLC.app/Contents/MacOS/VLC'

8、Git错误提示之：fatal: Not a git repository (or any of the parent directories): .git
  (1)git init
  (2)git add .
  (3)git status
  (4)git commit -m "works to display video"
  (5)git push
  echo "# twicthslam" >> README.md
  git init
  git add README.md
  git commit -m "first commit"
  git remote add origin https://github.com/BCCWAI/twicthslam.git
  git push -u origin master


9、在vi中按u可以撤销一次操作
      按ESC键进入vi模式（按鼠标右键进入vi模式）
      u：撤销上一步的操作
      Ctrl+r：恢复上一步被撤销的操作



