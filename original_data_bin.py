# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:24:20 2019

@author: Petra
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:04:28 2019

@author: Petra
"""

import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.naive_bayes import GaussianNB
import create_models

X, Y= create_models.get_data_for_original_model(mode='evaluacija-bin-bez')

seed = 7
models = []
models.append(('Naive Bayes', GaussianNB()))
models.append(('DT Class.', DecisionTreeClassifier()))
models.append(('DT Regr.', DecisionTreeRegressor()))

results = []
names = []
print("Evaluacija binarnog bez slanoce")
print("\nBez suhih 1/3+2/3 ")
for name, model in models:
    kfold = model_selection.KFold(n_splits=3, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('{}: mean {} std({})'.format(name,
                               cv_results.mean(),
                               cv_results.std()))

fig = plt.figure('Usporedba rezultata dobivenih za podatke bez slanoce,-bez suhih,1/3+2/3')
fig.suptitle('Usporedba rezultata dobivenih za podatke bez slanoce,-bez suhih,1/3+2/3')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()
print("\nBez suhih leave one put ")

results2 = []
names =[]
for name, model in models:
    kfold = model_selection.KFold(n_splits=len(X), random_state=seed)
    cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring='accuracy')
    results2.append(cv_results)
    names.append(name)
    print('{}: mean {} std({})'.format(name,
                               cv_results.mean(),
                               cv_results.std()))

fig = plt.figure('Usporedba rezultata dobivenih za podatke bez slanoce,bez suhih,leave one out')
fig.suptitle('Usporedba rezultata dobivenih za podatke bez slanoce,bez suhih,leave one out')
ax = fig.add_subplot(111)
plt.boxplot(results2)
ax.set_xticklabels(names)
plt.show()
##suhi

X, Y= create_models.get_data_for_original_model(mode='evaluacija-bin-suhi')
print("\nSa suhih 1/3+2/3 ")

results3 = []
names=[]
for name, model in models:
    kfold = model_selection.KFold(n_splits=3, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring='accuracy')
    results3.append(cv_results)
    names.append(name)
    print('{}: mean {} std({})'.format(name,
                               cv_results.mean(),
                               cv_results.std()))

fig = plt.figure('Usporedba rezultata dobivenih za podatke bez slanoce, sa suhih,1/3+2/3')
fig.suptitle('Usporedba rezultata dobivenih za podatke bez slanoce, sa suhih,1/3+2/3')
ax = fig.add_subplot(111)
plt.boxplot(results3)
ax.set_xticklabels(names)
plt.show()

results4 = []
names=[]
print("\nSa suhih leave one put ")

for name, model in models:
    kfold = model_selection.KFold(n_splits=len(X), random_state=seed)
    cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring='accuracy')
    results4.append(cv_results)
    names.append(name)
    print('{}: mean {} std({})'.format(name,
                               cv_results.mean(),
                               cv_results.std()))

fig = plt.figure('Usporedba rezultata dobivenih za podatke bez slanoce, sa suhim,leave one out')
fig.suptitle('Usporedba rezultata dobivenih za podatke bez slanoce, sa suhim,leave one out')
ax = fig.add_subplot(111)
plt.boxplot(results4)
ax.set_xticklabels(names)
plt.show()


