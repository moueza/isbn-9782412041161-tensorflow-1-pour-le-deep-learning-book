#ptl petit livre

#ptl p32
import tensorflow as tf
#ptl p58
import numpy as np


#pl p42
sess= tf.compat.v1.Session()

with sess.as_default():
  a= tf.constant(3)
  b= tf.constant(4)
  c= a + b
  c.eval()
  #c.eval(session=sess)
