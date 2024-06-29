import pandas as pd
import pm4py
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.objects.log.util import dataframe_utils
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.util import exec_utils

df = pd.read_csv('case_activities.csv')

df = df.rename(columns={
    'case_id': 'case:concept:name',
    'activity': 'concept:name',
    'timestamp': 'time:timestamp'
})

df = dataframe_utils.convert_timestamp_columns_in_df(df)
log = log_converter.apply(df)

heu_net = heuristics_miner.apply_heu(log)


parameters = {}
gviz = hn_visualizer.apply(heu_net, parameters=parameters)

png_file_path = "case_activities_process_graph.png"
hn_visualizer.save(gviz, png_file_path)

print(f"Graph saved as {png_file_path}")
