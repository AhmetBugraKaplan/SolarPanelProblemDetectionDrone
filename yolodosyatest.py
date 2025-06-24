from ultralytics import YOLO
import os
from PIL import Image
import matplotlib.pyplot as plt


model = YOLO('runs/classify/train/weights/emir.pt')


folder_path = r'C:\Users\emirh\Desktop\gunespanel\PRoject\Snow_covered_generated'  


image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']


for filename in os.listdir(folder_path):
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        image_path = os.path.join(folder_path, filename)
        try:
            
            results = model(image_path)
            result = results[0]

            
            top1 = result.probs.top1
            conf = result.probs.top1conf
            label = result.names[top1]

         
            img = Image.open(image_path)
            plt.imshow(img)
            plt.title(f"{filename}\nTahmin: {label} ({conf*100:.2f}%)")
            plt.axis('off')
            plt.show()

        except Exception as e:
            print(f"Hata oluştu: {filename} işlenemedi. Hata: {e}")