import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly

sess = tf.Session()

node3 = tf.add(node1, node2)

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)

add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b:4.5}))
