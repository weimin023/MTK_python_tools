import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



file = './result/diff_list.csv'
df = pd.read_csv(file)
#print (df)



STEP_ = 3
#-------------------------------------------
PA_  = 0
SUB_ = 7
CBW_ = 10
#-------------------------------------------
optimal_error = 3


condition1 = df['PA'] == PA_
condition2 = df['SubBand'] == SUB_
condition3 = df['CBW'] == 10

target = df[condition1&condition2&condition3]


target['Step2_all_points'] = target['Step2_all_points'].str.replace('[','')
target['Step2_all_points'] = target['Step2_all_points'].str.replace(']','')
target['Step2_all_points'] = target['Step2_all_points'].str.replace(',',' ')
ACLR = target['Step2_all_points'].str.split(expand=True)
ACLR = ACLR.to_numpy().astype(np.float)
ACLR = ACLR[0]

target['Step2_all_delays'] = target['Step2_all_delays'].str.replace('[','')
target['Step2_all_delays'] = target['Step2_all_delays'].str.replace(']','')
target['Step2_all_delays'] = target['Step2_all_delays'].str.replace(',',' ')
DELAY = target['Step2_all_delays'].str.split(expand=True)
DELAY = DELAY.to_numpy().astype(np.float)
DELAY = DELAY[0]

to_dataframe = []
for STEP_ in range(1,6):
    print (STEP_)
    
    ACLR_  = np.asarray(ACLR[0::STEP_])
    DELAY_ = np.asarray(DELAY[0::STEP_])
    
    opt_idx = np.where(ACLR_==np.amin(ACLR_))
    opt_idx = opt_idx[0][0].astype(np.int)
    all_idx  = np.arange(opt_idx-optimal_error,opt_idx+optimal_error+1,1)
    
    all_ACLR  = ACLR_[[all_idx]]
    all_delay = DELAY_[[all_idx]]
    
    if STEP_ == 1:
        to_dataframe = all_ACLR
    else:
        to_dataframe = np.vstack((to_dataframe,all_ACLR))
        
    plt.plot(DELAY_,ACLR_,'--o')    

col_name = ['Opt-3','Opt-2','Opt-1','Opt','Opt+1','Opt+2','Opt+3']
idx_name = ['Step=1', 'Step=2', 'Step=3', 'Step=4', 'Step=5']
df2 = pd.DataFrame(to_dataframe, columns = col_name, index = idx_name)
print (df2)
df2.to_excel('./delay_result.xlsx')

    
    
    
filename = 'PA%d, SUB%d, CBW%d ACLR-Delay curve' %(PA_,SUB_,CBW_)
plt.legend(idx_name)
plt.title(filename)
plt.xlabel('delay')
plt.ylabel('ACLR')
plt.grid()
plt.savefig('./'+filename+'.png', dpi=300)

plt.show()
    



