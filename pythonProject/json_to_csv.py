import numpy as np
import pandas as pd
from Serializer import Serializer
from parallel import ProcessMonitor
numbers = [
"0 - 6848",
"1 - 13616",
"2 - 24952",
"3 - 23140",
"4 - 7440",
'5 - 15276',
"6 - 26436",
"7 - 23352",
'8 - 23452',
'9 - 13604',
'10 - 11704',
'11 - 25496',
'12 - 13272',
'13 - 3916',
'14 - 6116',
'15 - 13972',
]

ser = Serializer()
pm = ProcessMonitor()
pm.df['label'] = np.zeros(len(pm.df))

for i in numbers:

    num, pidx = i.split(" - ")
    json = ser.deserialize(f"data\\test{num}.json")
    print(i, len(json))
    for data in json:
        _pid = str(data[1]['EventHeader']['ProcessId'])
        pid = _pid + f" - {num}"
        new_data = {'EventId': data[0], 'Task': data[1]['Task Name'],
                    'Base Process Exe': pid}
        pm.append(new_data['Base Process Exe'], new_data['Task'], new_data['EventId'])
        if pidx == _pid:
            pm.df.loc[pm.df.pid == pid, 'label'] = 1

pm.df.to_csv("data\\main.csv")

