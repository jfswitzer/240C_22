import pandas as pd
import os
import sys

#helper code for 240C
dirr = "/home/jen/CompArch/ChampSim/results_50M"
filenames = []
outfile = sys.argv[1]
directory = os.fsencode("/home/jen/CompArch/ChampSim/results_50M")
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".txt"):
         filenames.append(filename)

def extract_data(fn):
    datas = {}
    splits = fn.split(".champsimtrace.xz-")
    datas['run'] = splits[1][:-4]
    datas['id'] = splits[0]
    lines = []
    with open(dirr+"/"+fn,"r") as f:
        lines = f.readlines()
    for line in lines:
        indy = line.find('CPU 0 cumulative IPC: ')
        if indy != -1:
            cumu_ipc = float(line[indy+22:indy+27].strip())
            datas['cumulative_ipc']=cumu_ipc
        indy = line.find('CPU 0 Branch Prediction Accuracy: ')
        if indy != -1:
            bpa = float(line[indy+34:indy+39].strip())
            datas['branch_pred_accuracy']=bpa
        indy = line.find('MPKI: ')
        if indy != -1:
            mpki = float(line[indy+6:indy+11].strip())
            datas['mpki']=mpki
    return datas

agg = {'id':[],'cumulative_ipc':[],'branch_pred_accuracy':[],'mpki':[],'run':[]}
for fn in filenames:
    agg['id'].append(extract_data(fn).get('id'))
    agg['run'].append(extract_data(fn).get('run'))    
    agg['cumulative_ipc'].append(extract_data(fn).get('cumulative_ipc'))
    agg['branch_pred_accuracy'].append(extract_data(fn).get('branch_pred_accuracy'))
    agg['mpki'].append(extract_data(fn).get('mpki'))    
df = pd.DataFrame.from_dict(agg)
df.to_csv(outfile+'.csv')


