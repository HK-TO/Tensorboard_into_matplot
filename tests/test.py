import unittest
from tensorboard_into_matplotlib.main import tensorboard_to_json

class TestTensorboardIntoMatplotlib(unittest.TestCase):

    def test_open(self):

        input_path =  "tests/files/asymmetric_ff_asac_InvertedPendulum-v4"# @param {typee:"string"}
        output_path =  "tests/outputs"# @param {typee:"string"}
        output_file_name = 'test.json' #@param {type:"string"}
        tensorboard_to_json(input_path, output_path, output_file_name)
