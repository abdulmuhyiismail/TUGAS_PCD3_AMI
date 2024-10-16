import imageio
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def load_image(image_path):
    """
    Membaca gambar dari file dan mengembalikan array numpy.
    """
    if not Path(image_path).is_file():
        raise FileNotFoundError(f"Gambar tidak ditemukan di lokasi: {image_path}")
    return imageio.imread(image_path)

def rgb_to_grayscale(image):
    """
    Mengonversi gambar berwarna menjadi grayscale menggunakan rumus NTSC.
    """
    return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])

def save_image(image, output_path):
    """
    Menyimpan gambar dalam format grayscale.
    """
    imageio.imwrite(output_path, image.astype(np.uint8))
    print(f"Gambar grayscale disimpan sebagai: {output_path}")

def plot_histogram(image, output_path):
    """
    Menghitung dan menampilkan histogram gambar grayscale.
    """
    histogram, _ = np.histogram(image, bins=256, range=(0, 256))
    plt.figure(figsize=(10, 6))
    plt.title('Histogram Gambar Grayscale', fontsize=14)
    plt.xlabel('Intensitas Piksel', fontsize=12)
    plt.ylabel('Frekuensi', fontsize=12)
    plt.bar(range(256), histogram, color='gray', alpha=0.7)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
    print(f"Histogram disimpan sebagai: {output_path}")

def main():
    image_path = Path("C:\\Users\\Abdul\\OneDrive\\Documents\\TUGAS AMI\\PCD\\OIP.jpeg")
    grayscale_output_path = 'grayscale.jpg'
    histogram_output_path = 'histogram.png'

    try:
        # Membaca dan mengonversi gambar
        image = load_image(image_path)
        grayscale_image = rgb_to_grayscale(image)

        # Menyimpan gambar grayscale
        save_image(grayscale_image, grayscale_output_path)

        # Menampilkan dan menyimpan histogram
        plot_histogram(grayscale_image, histogram_output_path)
        
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
