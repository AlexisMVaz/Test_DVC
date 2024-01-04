import os, sys, pathlib, random, shutil
from ruamel.yaml import YAML

#same as safe_load from pyyaml
yaml = YAML(typ='safe')

def classify_new_data(new_data, data_path):
    params = yaml.load(open("params.yaml", encoding="utf-8"))
    data = pathlib.Path(data_path)
    new_train = pathlib.Path(new_data)
    #Ultralytics searches for "train" and "val" folders
    #Each class has to be separated added to a different folder
    Classes = os.listdir(new_train)
    for j in Classes:
        (data / 'train' / j).mkdir(parents = True ,exist_ok = True)
        (data / 'val' / j).mkdir(parents = True ,exist_ok = True)

    #We prepare the files before moving them to the proper folder
    #in this case we just split and move the data
    for n in range(len(Classes)):
        Total_class = os.listdir(new_train / Classes[n])
        val_split = int(params['train']['validation_split']*len(Total_class))
        Val_images = random.sample(Total_class, val_split)
        for k in Val_images:
            shutil.move(new_train / Classes[n] / k, data / 'val' / Classes[n])
        for m in Total_class:
            if m not in Val_images:
                shutil.move(new_train / Classes[n] / m, data / 'train' / Classes[n])  

if __name__ == "__main__":
    new_data = sys.argv[1]
    data_path = sys.argv[2]
    classify_new_data(new_data, data_path)