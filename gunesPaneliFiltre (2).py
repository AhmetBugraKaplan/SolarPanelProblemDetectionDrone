import cv2
import os
import numpy as np
import shutil

def is_possible_solar_panel(image_path, debug=False, use_color_mask=True, scale_factor=2.0):
    image = cv2.imread(image_path)
    if image is None:
        if debug:
            print(f"Görüntü okunamadı: {image_path}")
        return False

    h, w = image.shape[:2]
    new_w, new_h = int(w * scale_factor), int(h * scale_factor)
    image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
    if debug:
        print(f"{image_path}: Görsel {w}×{h} → {new_w}×{new_h} boyutuna INTER_CUBIC ile büyütüldü.")

    if use_color_mask:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([140, 255, 255])
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        if debug:
            print(f"{image_path}: Renk maskesi uygulandı (mavi tonları).")
        image_masked = cv2.bitwise_and(image, image, mask=mask_blue)
    else:
        image_masked = image.copy()
        if debug:
            print(f"{image_path}: Renk maskesi KAPALI (orijinal büyütülmüş görüntü kullanılıyor).")

    gray = cv2.cvtColor(image_masked, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    possible_panels = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 500:
            continue
        approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            possible_panels += 1
            if debug:
                x, y, w_box, h_box = cv2.boundingRect(approx)
                cv2.rectangle(image, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)
                (cx, cy), radius = cv2.minEnclosingCircle(approx)
                center = (int(cx), int(cy))
                radius = int(radius)
                cv2.circle(image, center, radius, (255, 0, 0), 2)

    if debug:
        print(f"{image_path}: {possible_panels} adet dikdörtgen-benzeri yapı bulundu.")
    return possible_panels >= 2

if __name__ == "__main__":
    image_folder = r"C:\Users\Utku\Desktop\gorseller"
    solar_folder = os.path.join(image_folder, "solar")
    nonsolar_folder = os.path.join(image_folder, "nonsolar")

    for folder in [solar_folder, nonsolar_folder]:
        if os.path.exists(folder) and os.path.isfile(folder):
            os.remove(folder)

    os.makedirs(solar_folder, exist_ok=True)
    os.makedirs(nonsolar_folder, exist_ok=True)

    valid_exts = ['.jpg', '.jpeg', '.png']
    solar_count = 0
    nonsolar_count = 0

    for img_name in os.listdir(image_folder):
        path = os.path.join(image_folder, img_name)
        if not os.path.isfile(path) or not any(img_name.lower().endswith(ext) for ext in valid_exts):
            continue

        try:
            if is_possible_solar_panel(path, debug=True, use_color_mask=True, scale_factor=2.0):
                shutil.copy(path, os.path.join(solar_folder, img_name))
                solar_count += 1
                print(f"[✓] {img_name} → solar/")
            else:
                shutil.copy(path, os.path.join(nonsolar_folder, img_name))
                nonsolar_count += 1
                print(f"[✗] {img_name} → nonsolar/")
        except Exception as e:
            print(f"Hata oluştu: {img_name} → {e}")

    print("\n İşlem tamamlandı.")
    print(f" Solar (panel içeren) görsel sayısı : {solar_count}")
    print(f" Nonsolar (panel içermeyen) görsel sayısı : {nonsolar_count}")
