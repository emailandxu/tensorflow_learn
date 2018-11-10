import tensorflow as tf

# define the input layer as 1-d tensor
a = tf.constant([5,3],name="input_a")

# define the second layer
# it will recieve all the items of the tensor, 
# sum them or product them
b = tf.reduce_prod(a,name="prod_b")
c = tf.reduce_sum(a,name="sum_c")

# define the output layer
d = tf.add(b,c,name="add_d")

with tf.Session() as sess:
    output = sess.run(d)
    print(output)

    # SummaryWriter is deprecated, use tf.summary.FileWriter
    writer = tf.summary.FileWriter('./my_graph', sess.graph)
