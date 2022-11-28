

import json


import tensorboard as tb
import matplotlib.pyplot as plt

from tensorboard.backend.event_processing.event_accumulator import EventAccumulator


#@title TensorBoardからJsonfileに変換する関数
def TensorboardtoJson(path, output_json_name):
  event_acc = EventAccumulator(path, size_guidance={'scalars': 0})
  event_acc.Reload() # ログファイルのサイズによっては非常に時間がかかる
  #すべてのscalarデータを取得しそのjsonファイルを取得する
  scalars = {}
  for tag in event_acc.Tags()['scalars']:
      events = event_acc.Scalars(tag)
      scalars[tag] = [event.value for event in events]
  with open(output_json_name, 'w') as fout:
      json.dump(scalars, fout)

path =  "../files/asymmetric_ff_asac_InvertedPendulum-v4"# @param {typee:"string"}
output_json_file_name = '../outputs/test.json' #@param {type:"string"}
TensorboardtoJson(path, output_json_file_name)


#@title 複数のTensorBoardからそれぞれのJsonfileに変換する関数
# import glob
# def TensorboardtoJson(path, output_json_name):
#   event_acc = EventAccumulator(path, size_guidance={'scalars': 0})
#   event_acc.Reload() # ログファイルのサイズによっては非常に時間がかかる
#   #すべてのscalarデータを取得しそのjsonファイルを取得する
#   scalars = {}
#   for tag in event_acc.Tags()['scalars']:
#       events = event_acc.Scalars(tag)
#       scalars[tag] = [event.value for event in events]
#   with open(output_json_name, 'w') as fout:
#       json.dump(scalars, fout)


# input_file_names = "/content/events.*" #@param {type: "string"}
# output_file_name = "/content/arc_CVI_float2_ANNep" #@param {type: "string"}
# files = glob.glob(input_file_names)
# for i in range(len(files)):
#   output_json_file_name = output_file_name + str(i+1) +'.json'
#   TensorboardtoJson(files[i], output_json_file_name)