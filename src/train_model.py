from ultralytics import YOLO
from ruamel.yaml import YAML
import sys

#The parameter file has to be introduced as a yaml file
yaml = YAML(typ='safe')

def train(data_train):
    params = yaml.load(open("params.yaml", encoding="utf-8"))

    model = YOLO(params['model'])
    if ~params['train']['resume']:
        model.train(data=data_train, epochs=params['train']['epochs']\
                    , plots = True, device = params['train']['device'])
    else:
        model.train(data=data_train, resume = True)
    

if __name__ == "__main__":
    data_path = sys.argv[1]
    train(data_path)