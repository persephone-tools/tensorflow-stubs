import tensorflow as tf

# setup for ctc_beam_search_decoder

# add a string where it should be a
tf.nn.ctc_beam_search_decoder(
    tf.placeholder(tf.float32, shape=(100, 256, 10)),
    'string',
    beam_width=10,
    top_paths=10,
    merge_repeated=True)  # E: incompatible type
