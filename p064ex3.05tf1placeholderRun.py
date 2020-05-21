#ptl petit livre

#ptl p32
import tensorflow as tf




with tf.name_scope("placeholders"):
  a = tf.compat.v1.placeholder(tf.float32, shape=(1,))
  b = tf.compat.v1.placeholder(tf.float32,shape=(1,))
  c= a + b
  
  with tf.Session() as sess:
    c_eval = sess.run(c, {a: [1.], b: [2.]})
    
