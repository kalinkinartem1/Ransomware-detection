import pickle
import queue
import threading
import time
from collections import defaultdict

import numpy as np
import pandas as pd
import psutil
from sklearn.metrics import f1_score, accuracy_score, balanced_accuracy_score, classification_report

pd.options.display.max_seq_items = None
import dask.dataframe as dd


class MyConcurrentCollection:
    def __init__(self):
        self.collection = queue.Queue()

    def append(self, x):
        self.collection.put(x)

    def pop(self):
        return self.collection.get()

    def __len__(self):
        return self.collection.qsize()

    def __str__(self):
        return f"{len(self)}"

    def print_collection(self):
        return self.collection.queue

    def empty(self):
        return self.collection.empty()


class ProcessMonitor:
    def __init__(self):
        self.df = defaultdict(lambda: np.zeros(44))
        self.mask = {
            "OPERATIONEND": 0,
            24: 1,
            "CLOSE": 2,
            14: 3,
            "CREATE": 4,
            12: 5,
            "QUERYSECURITY": 6,
            32: 7,
            "FSCTL": 8,
            23: 9,
            "QUERYINFORMATION": 10,
            22: 11,
            "CLEANUP": 12,
            13: 13,
            "READ": 14,
            15: 15,
            "DIRNOTIFY": 16,
            25: 17,
            "CREATENEWFILE": 18,
            30: 19,
            "WRITE": 20,
            16: 21,
            "NAMECREATE": 22,
            10: 23,
            "SETINFORMATION": 24,
            17: 25,
            "RENAME": 26,
            19: 27,
            "RENAMEPATH": 28,
            27: 29,
            "NAMEDELETE": 30,
            11: 31,
            "SETDELETE": 32,
            18: 33,
            "DELETEPATH": 34,
            26: 35,
            "DIRENUM": 36,
            20: 37,
            "QUERYEA": 38,
            34: 39,
            "FLUSH": 40,
            21: 41,
            "SETSECURITY": 42,
            31: 43,
        }
        with open("data\\isolation_forest_model.pkl", 'rb') as file:
            self.model = pickle.load(file)

    def append(self, pid, task, event):
        self.df[pid][self.mask[task]] += 1
        self.df[pid][self.mask[event]] += 1

    def predict(self):
        return [[key, self.model.predict([self.df[key]])] for key in self.df]


class Consumer(threading.Thread):
    def __init__(self, collection: MyConcurrentCollection):
        threading.Thread.__init__(self)
        self.daemon = True
        self.collection = collection
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None

    def run(self):
        self.times = []

        ex = 0
        pm = ProcessMonitor()
        c = 0
        count = 0
        while True:
            if not self.collection.empty():
                data = self.collection.pop()
                c += 1
                pid = data[1]['EventHeader']['ProcessId']
                if pid > 0:
                    self.times.append(time.time())
                    try:
                        process = psutil.Process(pid)
                        if process.name() != "System":
                            pm.append(process.parents()[0].exe() if len(process.parents()) > 0 else process.exe(),
                                      data[1]['Task Name'],
                                      data[0])

                    except psutil.NoSuchProcess:
                        print(f"dropped {pid}")
                        pm.df[pid] = np.zeros(44)

                    self.times.append(time.time())

                if c == 1000:
                    count += c
                    c = 0
                    print(pm.predict(), count)

            else:
                time.sleep(0.1)
                ex += 1
                if ex > 100:
                    print(pm.predict())
                    return


