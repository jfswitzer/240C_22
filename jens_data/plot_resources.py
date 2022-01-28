import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv('tap_size1.csv')

df2 = pd.read_csv('tap_size2.csv')

df3 = pd.read_csv('tap_size3.csv')

df4 = pd.read_csv('tap_size4.csv')

df1['n'] = df1['id'].map(lambda x: int(x[-3:]))
df1 = df1.sort_values(by=['n'])
df2['n'] = df2['id'].map(lambda x: int(x[-3:]))
df2 = df2.sort_values(by=['n'])
df3['n'] = df3['id'].map(lambda x: int(x[-3:]))
df3 = df3.sort_values(by=['n'])
df4['n'] = df4['id'].map(lambda x: int(x[-3:]))
df4 = df4.sort_values(by=['n'])

baseline=pd.read_csv('tap_sm.csv')
baseline['n'] = baseline['id'].map(lambda x: int(x[-3:]))
baseline = baseline.sort_values(by=['n'])

plt.scatter(df4['id'],df4['cumulative_ipc'],label="Biggest")
plt.scatter(df3['id'],df3['cumulative_ipc'],label="Bigger")
plt.scatter(df1['id'],df1['cumulative_ipc'],label="Smaller")
plt.scatter(df2['id'],df2['cumulative_ipc'],label="Smallest")

plt.plot(df4['id'],df4['cumulative_ipc'])
plt.plot(df3['id'],df3['cumulative_ipc'])
plt.plot(df1['id'],df1['cumulative_ipc'])
plt.plot(df2['id'],df2['cumulative_ipc'])

plt.plot(baseline['id'],baseline['cumulative_ipc'],color='black',linewidth=2,label='Default')

plt.xlabel("Benchmark")
plt.ylabel("Cumulative IPC",fontsize=2)


plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('resources_tap.eps',format='eps')
plt.show()
plt.show()

df1 = pd.read_csv('pips_size1.csv')

df2 = pd.read_csv('pips_size2.csv')

df3 = pd.read_csv('pips_size3.csv')

df4 = pd.read_csv('pips_size4.csv')

df1['n'] = df1['id'].map(lambda x: int(x[-3:]))
df1 = df1.sort_values(by=['n'])
df2['n'] = df2['id'].map(lambda x: int(x[-3:]))
df2 = df2.sort_values(by=['n'])
df3['n'] = df3['id'].map(lambda x: int(x[-3:]))
df3 = df3.sort_values(by=['n'])
df4['n'] = df4['id'].map(lambda x: int(x[-3:]))
df4 = df4.sort_values(by=['n'])

baseline=pd.read_csv('pips_sm.csv')
baseline['n'] = baseline['id'].map(lambda x: int(x[-3:]))
baseline = baseline.sort_values(by=['n'])

plt.scatter(df4['id'],df4['cumulative_ipc'],label="Biggest")
plt.scatter(df3['id'],df3['cumulative_ipc'],label="Bigger")
plt.scatter(df1['id'],df1['cumulative_ipc'],label="Smaller")
plt.scatter(df2['id'],df2['cumulative_ipc'],label="Smallest")

plt.plot(df4['id'],df4['cumulative_ipc'])
plt.plot(df3['id'],df3['cumulative_ipc'])
plt.plot(df1['id'],df1['cumulative_ipc'])
plt.plot(df2['id'],df2['cumulative_ipc'])

plt.plot(baseline['id'],baseline['cumulative_ipc'],color='black',linewidth=2,label='Default')

plt.xlabel("Benchmark")
plt.ylabel("Cumulative IPC",fontsize=2)


plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('resources_pips.eps',format='eps')
plt.show()
plt.show()
