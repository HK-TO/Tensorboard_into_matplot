import os
import json

import tensorboard as tb
import matplotlib.pyplot as plt

from tensorboard.backend.event_processing.event_accumulator import EventAccumulator


#@title TensorBoardからJsonfileに変換する関数
def tensorboard_to_json(input_path, output_path, output_file_name):
    event_acc = EventAccumulator(input_path, size_guidance={'scalars': 0})
    event_acc.Reload() # ログファイルのサイズによっては非常に時間がかかる
    #すべてのscalarデータを取得しそのjsonファイルを取得する
    scalars = {}
    for tag in event_acc.Tags()['scalars']:
        events = event_acc.Scalars(tag)
        scalars[tag] = [event.value for event in events]

    os.makedirs(output_path, exist_ok=True)
    with open(os.path.join(output_path, output_file_name), 'w') as fout:
        json.dump(scalars, fout)

