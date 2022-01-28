f = open('10pm.csv','r')
newlines = [l for l in f.readlines() if ('pips_tag' in l)]
fn = open('pips_tag2.csv','w+')
fn.writelines(newlines)
fn.close()
f.close()
