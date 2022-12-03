import unittest
from tensorboard_into_matplotlib.main import tensorboard_to_json

class TestTensorboardIntoMatplotlib(unittest.TestCase):

    def test_open(self):

        path =  "../files/asymmetric_ff_asac_InvertedPendulum-v4"# @param {typee:"string"}
        output_json_file_name = '../outputs/test.json' #@param {type:"string"}
        tensorboard_to_json(path, output_json_file_name)
