import matplotlib.pyplot as plt
import sys
import pandas as pd

fig = plt.gcf()
fig.set_size_inches(4.5,4)

df = pd.read_csv('pips_baseline.csv')
df1 = pd.read_csv('pips_scouts.csv')
df1['n'] = df1['id'].map(lambda x: int(x[-3:]))
df['n'] = df['id'].map(lambda x: int(x[-3:]))
per_scouts = {'1':[],'2':[], '3': [], '4':[],'5': [], '8':[]}
for r in df1.iterrows():
    row = r[1]
    baseline = df[df['n']==row['n']].to_numpy()[0][2]
    print(per_scouts[str(row['scouts'])])
    per_scouts[str(row['scouts'])] = per_scouts[str(row['scouts'])]+[row['cumulative_ipc']/baseline]

per_scouts['4']=4*[pd.read_csv('pips_sm.csv')['ratio'].mean()] #for the baseline
print(per_scouts)
x = []
y = []
for k,v in per_scouts.items():
    x.append(k)
    y.append(sum(v)/4)
print(x)
print(y)
ax = plt.gca()
intervals = [1.18,1.2,1.22,1.24,1.26,1.28]
plt.grid(axis='y',zorder=0)
ax.set_yticks(intervals)
plt.ylim(1.18,1.28)
plt.bar(x,y,zorder=3)
plt.ylabel("Speedup",fontsize=12)
plt.xlabel("N Scouts",fontsize=12)
plt.tight_layout()
plt.savefig('pips_scouts.eps',format='eps')
plt.show()


# fig = plt.gcf()
# fig.set_size_inches(4.5,4)

# df = pd.read_csv('pips_baseline.csv')
# df1 = pd.read_csv('pips_tag2.csv')
# df1['n'] = df1['id'].map(lambda x: int(x[-3:]))
# df['n'] = df['id'].map(lambda x: int(x[-3:]))
# per_tag = {'2': [], '4': [], '8':[],'12':[],'16':[],'24':[]}

# per_tag['16']=4*[pd.read_csv('tap_sm.csv')['ratio'].mean()] #for the baseline
# for r in df1.iterrows():
#     row = r[1]
#     if str(row['tag'])=='13' or str(row['tag'])=='15':
#         continue    
#     baseline = df[df['n']==row['n']].to_numpy()[0][2]
#     per_tag[str(row['tag'])] = per_tag[str(row['tag'])]+[row['cumulative_ipc']/baseline]

# x = []
# y = []
# for k,v in per_tag.items():
#     x.append(k)
#     y.append(sum(v)/4)

# ax = plt.gca()
# intervals = [0.95,1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4]
# plt.grid(axis='y',zorder=0)
# ax.set_yticks(intervals)
# plt.ylim(0.9,1.35)
# plt.bar(x,y,zorder=3,color='darkblue')
# plt.ylabel("Speedup",fontsize=12)
# plt.xlabel("Tag Size",fontsize=12)
# plt.tight_layout()
# plt.savefig('pips_tags.eps',format='eps')
# plt.show()
