import tensorflow as tf
#tf.InteractiveSession()
tf.compat.v1.InteractiveSession()

a = tf.constant(3)

b = tf.constant(4)
c = a + b
c.eval()
