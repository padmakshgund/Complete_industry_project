import pandas as pd
import numpy as np
import traceback
import sys
import warnings
warnings.filterwarnings("ignore")
import pickle as pk
import json as js

class MedicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = "region_"+region
    def load_model(self):
        with open("linear_model.pkl","rb") as file:
            self.model = pk.load(file)  
        with open ("project.json","rb") as file:
            self.project = js.load(file) 
            
    def insuranace_charges(self):
        self.load_model()
        self.index = self.project['columns'].index(self.region)
        self.test_array = np.zeros(len(self.project["columns"]))
        self.test_array[0] = self.age
        self.test_array[1] = self.project["sex"][self.sex]
        self.test_array[2] = self.bmi
        self.test_array[3] = self.children
        self.test_array[4] = self.project["smoker"][self.smoker]
        self.test_array[self.index] = 1
        self.charges = self.model.predict([self.test_array])[0]
        print(self.test_array)
        return print(f"Insurance predicted charges: {round(self.charges,2)} ")
if __name__ == '__main__':
    age = float(input("Enter your Age"))
    sex = str(input("Enter your Gender").lower())
    bmi = float(input ("Enter your bmi"))
    children = int(input("Enter number of child"))
    smoker = str(input("Your smoke or not").lower())
    region = str(input("Enter your region").lower())
    md =MedicalInsurance(age,sex,bmi,children,smoker,region)
    md.insuranace_charges()