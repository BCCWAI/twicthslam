import cv2
import numpy as np

from skimage.measure import ransac
from skimage.transform import FundamentalMatrixTransform

class Extractor(object):
  def __init__(self):
    # 启动STAR检测器
    self.orb = cv2.ORB_create(100)
    # Brute-Force匹配器很简单，它取第一个集合里一个特征的描述子并用第二
    # 个集合里所有其他的特征和他通过一些距离计算进行匹配。最近的返回。
    self.bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    self.last = None

  def extract(self, img):
    # 用ORB找到关键点并且用ORB计算描述符
    #kp = self.orb.detect(img_chunk, None)

    # detection--发现
    feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)
  
    # extraction--提取
    kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in feats]
    kps, des = self.orb.compute(img, kps) # 计算特征向量(图像，关键点)
  
    # matching--特征匹配连线
    ret = []
    if self.last is not None:
      matches = self.bf.knnMatch(des, self.last['des'], k=2)
      for m, n in matches:
        if m.distance < 0.75*n.distance:
          kp1 = kps[m.queryIdx].pt
          kp2 = self.last['kps'][m.trainIdx].pt
          ret.append((kp1, kp2))

    # filter--过滤器
    if len(ret) > 0:
      ret = np.array(ret)
      print(ret.shape)

      model, inliers = ransac((ret[:, 0],ret[:, 1]), 
                               FundamentalMatrixTransform,
                               min_samples=8, 
                               residual_threshold=1, 
                               max_trials=100)
    
      ret = ret[inliers]
    
    # return
    self.last = {'kps':kps, 'des':des}
    return ret



