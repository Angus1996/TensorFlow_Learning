#《TensorFlow 实战 Google 深度学习框架》3.1.2 计算图的使用
import tensorflow as tf

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], dtype=None, shape=None, name="b", verify_shape=False)
result = a + b

print(result)

print(a.graph is tf.get_default_graph())

g1 = tf.Graph()
with g1.as_default():
	v = tf.get_variable("v", initializer=tf.zeros_initializer()(shape=[1]))

g2 = tf.Graph()
with g2.as_default():
	v = tf.get_variable("v", initializer=tf.ones_initializer()(shape=[1]))

with tf.Session(graph=g1) as sess:
	tf.global_variables_initializer().run()
	with tf.variable_scope("", reuse=True):
		print(sess.run(tf.get_variable("v")))

with tf.Session(graph=g2) as sess:
	tf.global_variables_initializer().run()
	with tf.variable_scope("", reuse=True):
		print(sess.run(tf.get_variable("v")))