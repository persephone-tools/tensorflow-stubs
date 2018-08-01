import tensorflow as tf

# setup for ctc_beam_search_decoder
placeholder = tf.placeholder(tf.float32, shape=(100, 256, 10))

tf.nn.ctc_beam_search_decoder(
    placeholder, [256], beam_width=10, top_paths=10, merge_repeated=True)
