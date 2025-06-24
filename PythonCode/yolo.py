from ultralytics import YOLO
import matplotlib.pyplot as plt
import pandas as pd


model = YOLO('yolov8n-cls.pt')

model.train(
    data=r'C:\Users\emirh\Desktop\gunespanel\PRoject', 
    epochs=50,          
    imgsz=224,            
    batch=16,             
    device='cpu'         
)


results = pd.read_csv(r'C:\Users\emirh\Desktop\gunespanel\runs\classify\train\results.csv')


