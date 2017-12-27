#《TensorFlow 实战 Google 深度学习框架》3.2.2 张量的使用
import tensorflow as tf

#使用张量记录中间结果
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], dtype=None, shape=None, name="b", verify_shape=False)
result = tf.add(a, b, name="add")

# 直接计算向量的和，这样可读性会比较差
result = tf.constant([1.0, 2.0], name="a") + tf.constant([2.0, 3.0], name="b")
print(result)