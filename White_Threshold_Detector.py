import cv2
import numpy as np
import matplotlib.pyplot as plt

# Načti obrázek
image_path = 'C:\Project\skripty\images\Originbw.jpg'  # Změň na cestu k tvému obrázku
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Urči prahové hodnoty pro konverzi
thresholds = np.arange(0, 256, 1)
mean_errors = []

# Pro každý prah testuj prahování
for thresh in thresholds:
    _, binary_image = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)
    white_pixels = np.sum(binary_image == 255)
    total_pixels = binary_image.size
    mean_error = white_pixels / total_pixels
    mean_errors.append(mean_error)

# Najdi optimální prah
optimal_thresh = thresholds[np.argmax(mean_errors)]

print(f'Optimální prahová hodnota je: {optimal_thresh}')

# Ukaž obrázek s optimálním prahováním
_, optimal_binary_image = cv2.threshold(image, optimal_thresh, 255, cv2.THRESH_BINARY)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Původní obrázek')
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Optimalizovaný binární obrázek')
plt.imshow(optimal_binary_image, cmap='gray')
plt.axis('off')
plt.show()