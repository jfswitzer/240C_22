#plotting
import matplotlib.pyplot as plt
import sys
import pandas as pd
import numpy as np

def plot_tap(baseline,dfs):
    fig = plt.gcf()
    fig.set_size_inches(9,4)
    df1 = baseline
    df1['n'] = df1['id'].map(lambda x: int(x[-3:])) #make smarter
    df1 = df1.sort_values(by=['n'])
    itt = 0
    for df in dfs:
        df['n'] = df['id'].map(lambda x: int(x[-3:])) #make smarter
        df = df.sort_values(by=['n'])
        speedup = []
        n = []
        for r in df.iterrows():
            row = r[1]
            baseline = df1[df1['n']==row['n']].to_numpy()[0][2]
            print(baseline)
            n.append(row['n'])
            speedup.append(row['cumulative_ipc']/baseline)
        label='Next line'
        color='red'
        if row['run']=='hashed_perceptron-tap-next_line-spp_dev-no-lru-1core':
            label='TAP'
            color='purple'
            print(sum(speedup)/len(speedup))            
        plt.xticks([x-1.5+itt for x in n],rotation = 45)            
        plt.bar([x+itt for x in n],speedup,label=label,color=color,width=0.5,zorder=3)
        itt = itt+0.5
    plt.ylim(0.9,1.5)
    plt.grid(axis='y',zorder=0)        
    plt.ylabel("Speedup",fontsize=11)
    plt.xlabel("Benchmark ID",fontsize=11)
    plt.legend()
    ax = plt.gca()
    ax.set_xticklabels(list(df['id'].to_numpy())[:-2]+["spec_gobmk_001","spec_gobmk_002"])
    plt.tight_layout()
    plt.savefig('tap_sweep.eps',format='eps')
    plt.show()

def plot_pips(df1,df):
    fig = plt.gcf()
    fig.set_size_inches(4.5,3)
    df1['n'] = df1['id'].map(lambda x: int(x[-3:]))
    df['n'] = df['id'].map(lambda x: int(x[-3:]))
    df.sort_values(by=['mpki'])
    speedup = []
    n = []
    bids = []
    i=0
    for r in df.iterrows():
        row = r[1]
        baseline = df1[df1['n']==row['n']].to_numpy()[0][2]
        speedup.append(row['cumulative_ipc']/baseline)
        n.append(i+40)
        bids.append(row['id'])
        i=i+1
    speedup.sort()
    print("pips average speedup:")
    print(np.median(speedup))
    print("pips average speedup:")    
    plt.plot(n,speedup,color='lime',label='PIPS')
    plt.ylabel("Speedup",fontsize=11)
    plt.xlabel("Benchmark by speedup",fontsize=11)    
    ax = plt.gca()

    intervals = [1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8]
    ax.set_yticks(intervals)
    
    plt.xticks(n,rotation=45)
    ax.set_xticklabels(bids)
    ax.grid(axis='y')
    plt.legend()
    plt.tight_layout()
    plt.savefig('pips_sweep.eps',format='eps')
    plt.show()



df = pd.read_csv('tap_sweep.csv')
df1 = df[df['run']=='hashed_perceptron-next_line-next_line-spp_dev-no-lru-1core']
df2 = df[df['run']=='hashed_perceptron-tap-next_line-spp_dev-no-lru-1core']
baseline = df[df['run']=='hashed_perceptron-no-next_line-spp_dev-no-lru-1core']
plot_tap(baseline,[df1,df2])

# df = pd.read_csv('pips_sweep.csv')
# df1 = df[df['run']=='gshare-no-no-no-no-lru-1core']
# df2 = df[df['run']=='gshare-pips-no-no-no-lru-1core']
# plot_pips(df1,df2)
