import pandas as pd
import category_encoders as ce
import pandas as pd
import sklearn
from imblearn.ensemble import BalancedRandomForestClassifier, EasyEnsembleClassifier, BalancedBaggingClassifier
from imblearn.under_sampling import RandomUnderSampler, EditedNearestNeighbours, RepeatedEditedNearestNeighbours, AllKNN
from sklearn.covariance import EllipticEnvelope
from sklearn.ensemble import VotingClassifier, AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier, \
    IsolationForest
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import roc_auc_score, average_precision_score, f1_score, precision_score, recall_score, \
    classification_report, accuracy_score, balanced_accuracy_score
from sklearn.metrics import confusion_matrix
from imblearn.over_sampling import SMOTE, ADASYN, SVMSMOTE, KMeansSMOTE, BorderlineSMOTE
from imblearn.combine import SMOTEENN, SMOTETomek
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
import numpy as np
import warnings
import sklearn.tree as st
import sklearn.linear_model as sl
import sklearn.discriminant_analysis as sd
import sklearn.kernel_ridge as sk
import sklearn.svm as svmx
import sklearn.gaussian_process as sg
import sklearn.naive_bayes as sn
import sklearn.ensemble as se
import sklearn.neural_network as snn
import seaborn as sns
import matplotlib.pyplot as plt
# import compositions.bagging as cb
# import compositions.voting_by_majority as cvm
import matplotlib.pyplot as plt
import sklearn.ensemble as se

pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore")

df = pd.read_csv("/Users/artemkalinkin/PycharmProjects/pythonProject/data/main.csv", index_col=0)
print(df)

columns = list(df.columns)
columns.remove("label")
columns.remove("pid")

y = df["label"]
X = df[columns]

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, train_size=0.3, random_state=42)


# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------


def fit(model, supervized=False):
    if supervized:
        model.fit(X_train, y_train)
    else:
        model.fit(X_train)

    yhat = model.predict(X_test)
    print(f'{model}')
    print(classification_report(y_test, yhat))



model = RandomForestClassifier()
fit(model, True)

model = DecisionTreeClassifier()
fit(model, True)




#-----------------------------------------------------

#-----------------------------------------------------

# ----------------------------------------------------


# x_train = x_train[y_train == 0]

y_test[y_test == 1] = -1
y_test[y_test == 0] = 1

print(len(y_train[y_train == 1]) / len(y_train[y_train == 0]))


model = IsolationForest(contamination=0.1)  # 0.11
model.fit(X_train)
yhat = model.predict(X_test)
score = f1_score(y_test, yhat, pos_label=-1)
accuracy = accuracy_score(y_test, yhat)
b_accuracy = balanced_accuracy_score(y_test, yhat)
print(f'{model}\t F1\Acc\Bal_acc: {"%.3f" % score} {"%.3f" % accuracy} {"%.3f" % b_accuracy} ')
print(classification_report(y_test, yhat))



# import pickle
# pkl_filename = "data\\isolation_forest_model.pkl"
# with open(pkl_filename, 'wb') as file:
#     pickle.dump(model, file)


# for j in np.linspace(0.01, 0.5, num=20):
#     i = round(j, 3)
#     models = [
#         # OneClassSVM(gamma='scale', nu=i),
#         IsolationForest(contamination=i),
#         # EllipticEnvelope(contamination=i),
#         # LocalOutlierFactor(contamination=i, novelty=True)
#     ]
#
#     for model in models:
#         model.fit(X_train)
#
#         yhat = model.predict(X_test)
#         score = f1_score(y_test, yhat, pos_label=-1)
#         accuracy = accuracy_score(y_test, yhat)
#         b_accuracy = balanced_accuracy_score(y_test, yhat)
#         print(f'{model}\t F1\Acc\Bal_acc: {"%.3f" % score} {"%.3f" % accuracy} {"%.3f" % b_accuracy} ')
#         print(classification_report(y_test, yhat))


# model = IsolationForest(contamination=len(y_train[y_train == 1]) / len (y_train[y_train == 0]))
# model.fit(x_train)
# yhat = model.predict(x_test)
# score = f1_score(y_test, yhat, pos_label=-1)
# accuracy = accuracy_score(y_test, yhat)
# b_accuracy = balanced_accuracy_score(y_test, yhat)
# print(f'{model}\t F1\Acc\Bal_acc: {"%.3f" % score} {"%.3f" % accuracy} {"%.3f" % b_accuracy} ')
# print(classification_report(y_test, yhat))
#
# df_y = df.fraud_reported.values
# model = IsolationForest(contamination=len(df_y[df_y == 1]) / len (df_y[df_y == 0]))
# model.fit(x_train)
# yhat = model.predict(x_test)
# score = f1_score(y_test, yhat, pos_label=-1)
# accuracy = accuracy_score(y_test, yhat)
# b_accuracy = balanced_accuracy_score(y_test, yhat)
# print(f'{model}\t F1\Acc\Bal_acc: {"%.3f" % score} {"%.3f" % accuracy} {"%.3f" % b_accuracy} ')
# print(classification_report(y_test, yhat))
