import unittest

import json
import glob

from tensorboard_into_matplotlib.main import tensorboard_to_json

class TestTensorboardIntoMatplotlib(unittest.TestCase):

    def test_open(self):

        input_file_name =  "tests/content/asymmetric_ff_asac_InvertedPendulum-v4/events.out.tfevents.1668517881.takumao-System-Product-Name.3781.0"# @param {typee:"string"}
        output_path =  "tests/outputs"# @param {typee:"string"}
        output_file_name = 'test.json' #@param {type:"string"}
        tensorboard_to_json(input_file_name, output_path, output_file_name)

    def test_open_multiple(self):

        input_file_names = "tests/content/asymmetric_ff_asac_InvertedPendulum-v4/events.*" #@param {type: "string"}
        output_path =  "tests/outputs"# @param {typee:"string"}
        output_file_name = 'multiple_test' #@param {type:"string"}

        files = glob.glob(input_file_names)
        for i in range(len(files)):
          output_json_file_name = output_file_name + str(i+1) +'.json'
          tensorboard_to_json(files[i], output_path, output_json_file_name)

    def test_confirm_key(self):
        json_name = "tests/outputs/multiple_test1.json"
        expected = {'reward/train': None, 
                    'reward/test': None, 
                    'loss/critic_1': None,
                    'loss/critic_2': None, 
                    'loss/entropy_loss': None, 
                    'entropy_temprature/alpha': None}

        with open(json_name) as f:
            jsn = json.load(f)

        self.assertEqual(jsn.keys(), expected.keys())

