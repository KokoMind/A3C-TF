"""
These are the arguments that i want from you to specify.
All arguments are documented.
It will be verified by read_arguments function
"""

import tensorflow as tf

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('model', "", """ MODEL NAME """)
tf.app.flags.DEFINE_string('env', "", """ Environment name """)
tf.app.flags.DEFINE_string('mode', "", """ Mode of operation of the agent """)
tf.app.flags.DEFINE_integer('n_iterations', 100, """ n_iterations """)
tf.app.flags.DEFINE_float('learning_rate', 0.0001, """ initial lr """)
tf.app.flags.DEFINE_string('exp_dir', "", """ Experiment dir to store ckpt & summaries """)
tf.app.flags.DEFINE_string('out_dir', "", """ The output dir of the experiment """)
tf.app.flags.DEFINE_integer('save_every', 1, """ Save every n iterations """)
tf.app.flags.DEFINE_integer('save_max_to_keep', 2, """ Max to keep checkpoints in save""")


def read_arguments():
    print("\n\n")

    # TODO define the modes of the operation of the agent

    if FLAGS.model == "" or FLAGS.env == "" or FLAGS.mode == "" \
            or FLAGS.exp_dir == 0 or FLAGS.out_dir == 0.0:
        raise Exception("Please specify all necessary arguments and Be Sure that you have provided it all")

    print("\n Using this arguments -- check it -- \n")

    print("The name of the model is -- " + FLAGS.model + " -- ")
    print("The name of the env is -- " + FLAGS.env + " -- ")
    print("The name of the mode is -- " + FLAGS.mode + " -- \n")

    print("The number of iterations per epoch is -- " + str(FLAGS.n_iterations) + " -- ")
    print("The learning_rate is -- " + str(FLAGS.learning_rate) + " -- ")
    print("The exp_dir is -- " + str(FLAGS.exp_dir) + " -- ")
    print("The out_dir is -- " + str(FLAGS.out_dir) + " -- ")
    print("The save_every is -- " + str(FLAGS.save_every) + " -- ")
    print("The save_max_to_keep is -- " + str(FLAGS.save_max_to_keep) + " -- ")

    print("\n\n")
