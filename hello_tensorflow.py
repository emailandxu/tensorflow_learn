import tensorflow as tf

# define the input layer
a = tf.constant(5,name="input_a")
b = tf.constant(3,name="input_b")

# define the second layer
c = tf.multiply(a,b,name="mul_c")
d = tf.add(a,b,name="add_d")

# define the output layer
e = tf.add(c,d,name="add_e")

with tf.Session() as sess:
    output = sess.run(e)
    print(output)

    # you can pass any op into sess.run()
    print(sess.run(c))
    # SummaryWriter is deprecated, use tf.summary.FileWriter
    writer = tf.summary.FileWriter('./my_graph', sess.graph)
