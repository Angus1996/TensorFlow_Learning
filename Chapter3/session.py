#《TensorFlow 实战 Google 深度学习框架》3.1.2 会话
import tensorflow as tf

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], dtype=None, shape=None, name="b", verify_shape=False)
result = tf.add(a, b, name="add")

# # 创建一个会话
# sess = tf.Session()
# # 使用这个创建好的会话来得到关心的运算的结果。比如可以调用 seee.run(result),
# # 来得到3.1节样例中张量result 的取值
# sess.run(result)
# # 关闭会话使得本次运行中使用到的资源可以被释放
# sess.close()

# 创建一个会话，并通过Python 中的上下文管理器来管理这个会话
with tf.Session() as sess:
	print(sess.run(result))
	#效果同上
	print(result.eval(session=sess))
# 不需要再调用 “Session.close()” 函数来关闭会话
# 当上下文退出时会话关闭和资源释放也自动完成了