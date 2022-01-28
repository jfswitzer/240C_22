import matplotlib.pyplot as plt
import sys
import pandas as pd

# fig = plt.gcf()
# fig.set_size_inches(4.5,4)

# p='nd'
# df = pd.read_csv('taps_baseline.csv')
# df1 = pd.read_csv('tap_nd.csv')
# df1['n'] = df1['id'].map(lambda x: int(x[-3:]))
# df['n'] = df['id'].map(lambda x: int(x[-3:]))
# per_tag = {'4':[],'8':[],'9':[],'10':[],'12':[]}
# for r in df1.iterrows():
#     row = r[1]
#     baseline = df[df['n']==row['n']].to_numpy()[0][2]
#     per_tag[str(row[p])] = per_tag[str(row[p])]+[row['cumulative_ipc']/baseline]

# per_tag['9']=4*[pd.read_csv('tap_sm.csv')['ratio'].mean()] #for the baseline
# print(per_tag)
# x = []
# y = []
# for k,v in per_tag.items():
#     x.append(k)
#     y.append(sum(v)/4)

# ax = plt.gca()
# intervals = [1.05,1.1,1.15,1.2,1.25,1.3]
# plt.grid(axis='y',zorder=0)
# ax.set_yticks(intervals)

# plt.ylim(1,1.3)
# plt.bar(x,y,zorder=3,color='green')
# plt.ylabel("Speedup",fontsize=12)
# plt.xlabel("Number of descendents",fontsize=12)
# plt.tight_layout()
# plt.savefig('tap_nd.eps',format='eps')
# plt.show()

fig = plt.gcf()
fig.set_size_inches(4.5,4)

p='hist'
df = pd.read_csv('taps_baseline.csv')
df1 = pd.read_csv('tap_hist.csv')
df1['n'] = df1['id'].map(lambda x: int(x[-3:]))
df['n'] = df['id'].map(lambda x: int(x[-3:]))
per_tag = {'8':[],'12':[],'14':[],'16':[]}
for r in df1.iterrows():
    row = r[1]
    baseline = df[df['n']==row['n']].to_numpy()[0][2]
    per_tag[str(row[p])] = per_tag[str(row[p])]+[row['cumulative_ipc']/baseline]

x = []
y = []
for k,v in per_tag.items():
    x.append(k)
    y.append(sum(v)/4)

ax = plt.gca()
intervals = [1.22,1.23,1.24,1.25,1.26,1.27]
plt.grid(axis='y',zorder=0)
ax.set_yticks(intervals)
y[2]=pd.read_csv('tap_sm.csv')['ratio'].mean() #for the baseline
plt.ylim(1.22,1.27)
plt.bar(x,y,zorder=3,color='purple')
plt.ylabel("Speedup",fontsize=12)
plt.xlabel("History Size",fontsize=12)
plt.tight_layout()
plt.savefig('tap_hist.eps',format='eps')
plt.show()
