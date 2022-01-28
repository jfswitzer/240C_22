#plotting
import matplotlib.pyplot as plt
import sys
import pandas as pd
import numpy as np

fig = plt.gcf()
fig.set_size_inches(9,4)

df1 = pd.read_csv('pips_lats.csv')
df2 = pd.read_csv('tap_lats.csv')

df2['n'] = df2['id'].map(lambda x: int(x[-3:]))
df1['n'] = df1['id'].map(lambda x: int(x[-3:]))
df1 = df1.sort_values(by=['n'])
df2 = df2.sort_values(by=['n'])

plt.bar([x+0.5 for x in df1['n']],df1['cumulative_ipc'],label='PIPS',width=0.5,zorder=3)
plt.bar(df2['n'],df2['cumulative_ipc'],label='TAP',width=0.5,zorder=3)
plt.legend()
plt.ylabel('Cumulative IPC',fontsize=12)
plt.xlabel('Benchmark ID',fontsize=12)
plt.grid(axis='y',zorder=0)
plt.tight_layout()
plt.savefig('latencies.eps',format='eps')
plt.show()
