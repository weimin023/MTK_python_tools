import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

STEP_ = 1

file = './form1.csv'
df = pd.read_csv(file)
df['ACLR'] = df['ACLR'].str.replace('[','')
df['ACLR'] = df['ACLR'].str.replace(']','')

df = df['ACLR'].str.split(expand=True)

AXIS = np.arange(101,112,1)

tmp_stack = []
for i in range(len(df)):
    tmp = df.iloc[i].to_numpy()
    tmp = tmp.astype(np.int)
    tmp = np.asarray(tmp[0::STEP_])
    
    if i==0:
        tmp_stack = tmp
    else:
        tmp_stack = np.vstack((tmp_stack,tmp))
    
        
print (tmp_stack)

plt.plot(AXIS[0::STEP_],tmp_stack.T,'--o')
plt.title('ACLR-Delay curve')
plt.xlabel('delay')
plt.ylabel('ACLR')
plt.legend(['Step=2'])
plt.grid()
plt.savefig('./ACLR_Delay.png', dpi=300)

plt.show()