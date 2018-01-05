import tensorflow as tf

weights = tf.constant([[1.0, -2.0], [-3.0, 4.0]])
with tf.Session() as sess:
	print(sess.run(tf.contrib.layers.l1_regularizer(0.5)(weights)))

	print(sess.run(tf.contrib.layers.l2_regularizer(0.5)(weights)))