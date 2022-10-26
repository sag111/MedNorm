import json 
import os
import numpy as np
from sklearn.model_selection import KFold

os.makedirs('./Data/RDRS_splits/review_ids/', exist_ok=True)
os.makedirs('./Data/CADEC_splits/review_ids/', exist_ok=True)

with open('./Data/Full_corps/RDRS_ADR.json') as rdrs_f, open('./Data/Full_corps/CADEC.json') as cadec_f:
    RDRS = json.load(rdrs_f)
    CADEC = json.load(cadec_f)

n_splits = 5
kf = KFold(n_splits=n_splits, random_state=42, shuffle=True)
folds = []

all_splits = {}

print('Creating splits...')
for ds_name, ds in {'RDRS': RDRS, 'CADEC': CADEC}.items():
    print(ds_name)
    ds = np.array(ds)
    id_folds=1
    for train_index, test_index in kf.split(ds):
        X_test = ds[test_index]
        X_train = ds[train_index]
        with open(f'./Data/{ds_name}_splits/{id_folds}_fold_test.json', 'w') as ts:
            json.dump(list(X_test), ts)
        with open(f'./Data/{ds_name}_splits/{id_folds}_fold_train.json', 'w') as tr:
            json.dump(list(X_train), tr)
        rev_ids_test = [rev['meta']['fileName'] for rev in X_test]
        rev_ids_train = [rev['meta']['fileName'] for rev in X_train]
        with open(f'./Data/{ds_name}_splits/review_ids/{id_folds}_test_review_ids.json', 'w') as ts:
            json.dump(rev_ids_test, ts)
        with open(f'./Data/{ds_name}_splits/review_ids/{id_folds}_train_review_ids.json', 'w') as tr:
            json.dump(rev_ids_train, tr)
        id_folds+=1