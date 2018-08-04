import tensorflow as tf

# setup for ctc_beam_search_decoder
placeholder = tf.placeholder(tf.float32, shape=(100, 256, 10))
# TODO: pytest gives error "module has no attribute "SparseTensor"
# sparseTensor = tf.SparseTensor(indices=[[0, 0], [1, 2]],
#                                values=[1, 2],
#                                dense_shape=[3, 4])

tf.nn.ctc_beam_search_decoder(
    placeholder,
    [256],
    beam_width=10,
    top_paths=10,
    merge_repeated=True)

# TODO: determine how to initialize a RNNCell object for this test
# tf.nn.bidirectional_dynamic_rnn()

# NOTE: commented out due to SparseTensor initialization issue above
# tf.nn.ctc_loss(
#     sparseTensor,
#     placeholder,
#     10,
#     preprocess_collapse_repeated=True,
#     ctc_merge_repeated=True,
#     ignore_longer_outputs_than_inputs=True,
#     time_major=True)

tf.nn.log_softmax(placeholder, axis=0, name='log_softmax_name', dim=0)
