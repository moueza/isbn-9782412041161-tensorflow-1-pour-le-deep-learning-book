#ptl petit livre

#ptl p32
import tensorflow as tf
#ptl p58
import numpy as np



#pl p64
N=5
with tf.name_scope("placeholders"):
  x= tf.compat.v1.placeholder(tf.float32, (N, 1))
  y= tf.compat.v1.placeholder(tf.float32, (N, ))
