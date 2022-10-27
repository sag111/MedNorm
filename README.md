# MedNorm

This repository contains the neural network model code for linking phrases to their concepts in the dictionary. This model was used to link mentions of side effects of drugs from online reviews with the corresponding terms in the MedDRA dictionary, in the PT part (preffered terms). Also it contains a corpus of russian internet reviews with normalization markup: phrase from review and it's concept. Model weights for russian model can be found at [huggingface repo](https://huggingface.co/sagteam/rubert-base-cased-mcn), also the demonstration of the trained model can be found in `Demo.ipynb`: data loading and evaluating on the test set.

## Usage
At first, you should download [Anaconda](https://www.anaconda.com/products/distribution) and create a virtual env and activate it:
```
conda env create -f env.yml
conda activate normalization
```
### Train and test
To train model use `train.py` with this args:
 - -tr - train data path in a simple json format. This format is a list of reviews (python dicts), each review has nested fields: `['objects']['MedEntity']`, in `MedEntity` there is a list of entities which has `text` field and `MedDRA` field, which contain the text of the phrase and the PT phrase of the medDRA dictionary, respectively.
 - -res - result path, where model will be saved, with concept vectors and ConceptVectorizer object, which helps computing embeddings for dictionary
 - -args - Path to the configuration file, which have lr, epochs, batch size, use_cuda flag, **default:** `train_args.txt`
 - -model - Path to the initial transformer model, listed in https://huggingface.co/, which will be fine-tuned. **default:** `DeepPavlov/rubert-base-cased`
 - -dict - MedDRA (or another dictionary) in .asc format, .asc format is code and term separated by '$'
 - -val - Path to the validation data in sumilar to `-tr` json format. Validation data is used for early stopping and computing metrics. Whithout validation data no early stopping is used.
 - -load_pretrained - Path to already trained model from this repo for futher finetuning (training) with ConceptVectorizer and concept embeddings. When you define this param, you dont need to provide "transformer_model_path".
 - -ts - Path to the test data file in similar to `-tr` json format to evaluate after training.
 - -use_concept_less - If this flag is specified, then during the test all phrases that have an empty MedDRA field are replaced with the conceptless label, the model tries to determine by the threshold whether the phrase has a concept in the dictionary or not.
 - --use_cuda - If this flag is specified, gpu is used

### Demonstration and RDRS corpus
A demo on the RDRS drug review dataset is included in the `Demo.ipynb`. The demo case is presented in a simple .csv format with fields mention,tag,pt code,fold id. Tag is a type of mention: adverse drug reaction or indication of the disease. Fold id sets dataset split on 5 parts.
