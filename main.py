"""
Let's Begin the action :P
"""

from dirs import create_experiment_dirs, create_out_dirs
from params import FLAGS, read_arguments
from models import *
import tensorflow as tf


def main(_):
    # Reset the graph
    tf.reset_default_graph()

    # TODO Complete the params.py
    # Read the arguments of the program and validate it
    read_arguments()

    # TODO Complete the config.py
    # Get the Config of the program and init the dirs

    FLAGS.summary_dir, FLAGS.checkpoint_dir = create_experiment_dirs(FLAGS.exp_dir)

    # Create the Session of the graph
    # TODO Check for the gpu existed or not using tensorflow api check
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=1)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

    # Create environment
    # TODO Create environment

    # Create the model and init it
    # TODO Models
    model_class = globals()[FLAGS.model]

    # TODO Create the agent

    # TODO switch according to the mode
    if FLAGS.mode == None:
        try:
            pass
        except KeyboardInterrupt:
            pass
    else:
        raise Exception("Please select a proper mode for our wasted agent")

    sess.close()


if __name__ == '__main__':
    tf.app.run()
