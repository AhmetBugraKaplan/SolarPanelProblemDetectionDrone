#  Solar Panel Problem Detection with Custom Drone
>  Real-time solar panel fault detection using a handcrafted drone and deep learning.

---

##  Demo Video

[![Watch the video](https://img.youtube.com/vi/enpU312Wr6s/0.jpg)](https://www.youtube.com/watch?v=enpU312Wr6s&t=385s)

_Click the image to watch the project demo starting at 6:25._

---



In our project, we built a **handmade drone** from scratch to detect problems on solar panels. You can find all the components, datasheets, and technical details in the `DroneDonanım.pdf` file.

Initially, our drone used an **ESP32-CAM module** for live streaming. However, due to power limitations of the ESP-CAM, we modified it to **capture an image every 5 seconds** instead of continuous streaming. (You can find the related code in `CameraWebServer2.rar`.)

Thanks to the **Wi-Fi module of the ESP-CAM**, it establishes a local network and transmits the captured images directly to the computer. These images are then analyzed using a **YOLO-based deep learning model**, which detects whether there is a problem in the solar panel **in real time**.

> Note: This project is still under development. If you're interested, stay tuned for our upcoming commits.

Feel free to contact me for any questions. I'm happy to help!

📧 bugrakaplann5@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ahmetbugrakaplan/)  
🐙 [GitHub](https://github.com/AhmetBugraKaplan)

---



El yapımı drone ile güneş panellerindeki sorunları tespit ettiğimiz projemizde öncelikle tüm parçalarını kendimizin birleştirdiği bir drone yaptık.  
(Data sheet’ler ve gerekli tüm detaylar için `DroneDonanım.pdf` dosyasını inceleyebilirsiniz.)

Drone'a bağladığımız **ESP32-CAM** modülü sayesinde canlı yayın yapabiliyorduk. Ancak ESP-CAM’in gücü hem canlı yayın hem de fotoğraf çekmeye yetmediği için cihazı **her 5 saniyede bir fotoğraf çeker hale** getirdik.  
(İlgili kodlara `CameraWebServer2.rar` dosyası içinde ulaşabilirsiniz.)

ESP-CAM'in Wi-Fi modülü sayesinde yerel bir internet ağı oluşturduk ve çekilen görüntüleri bilgisayara anlık olarak aktardık. Aktarılan görüntüler, YOLO algoritmasıyla eğittiğimiz **derin öğrenme modelimiz** tarafından analiz edilerek **güneş panelinde sorun olup olmadığı gerçek zamanlı olarak algılanmaktadır.**

> Not: Proje üzerinde çalışmaya devam etmekteyiz. İlginizi çektiyse yeni commitlerimizi takip edebilirsiniz.

Aklınıza takılan herhangi bir soru olursa bana iletişim bilgilerimden ulaşabilirsiniz. Yardımcı olmaktan memnuniyet duyarım!

📧 bugrakaplann5@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ahmetbugrakaplan/)  
🐙 [GitHub](https://github.com/AhmetBugraKaplan)

---
