import tensorflow as tf

tf.train.import_meta_graph('some string')


tf.train.Saver().restore(tf.Session(), 'some string')
