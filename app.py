import streamlit as st
from PIL import Image
import random

# Fungsi untuk mengenkripsi gambar
# Fungsi untuk mengenkripsi gambar
# Fungsi untuk mengenkripsi gambar dengan efek blur acak
def encrypt_image(image_path):
    image = Image.open(image_path)  # Membuka gambar dari path

    # Mendapatkan data piksel dari gambar
    pixels = image.load()
    width, height = image.size

    # Proses enkripsi dengan efek blur acak untuk setiap piksel
    for i in range(width):
        for j in range(height):
            if random.random() < 0.3:  # Menerapkan efek blur acak pada 30% piksel
                r, g, b = pixels[i, j]  # Mendapatkan nilai warna RGB
                # Logika blur acak titik-titik di sini
                rand_i = random.randint(max(0, i - 1), min(i + 1, width - 1))
                rand_j = random.randint(max(0, j - 1), min(j + 1, height - 1))
                rand_r, rand_g, rand_b = pixels[rand_i, rand_j]
                pixels[i, j] = ((r + rand_r) // 2, (g + rand_g) // 2, (b + rand_b) // 2)  # Memperbarui nilai piksel

    encrypted_image = image  # Mengembalikan gambar yang sudah dienkripsi
    return encrypted_image
# Fungsi untuk mendekripsi gambar
def decrypt_image(image_path):
    image = Image.open(image_path)  # Membuka gambar dari path

    # Mendapatkan data piksel dari gambar
    pixels = image.load()
    width, height = image.size

    # Proses dekripsi untuk setiap piksel
    for i in range(width):
        for j in range(height):
            if random.random() < 0.3:  # Menerapkan efek dekripsi untuk 30% piksel yang terenkripsi
                r, g, b = pixels[i, j]  # Mendapatkan nilai warna RGB
                # Logika dekripsi untuk mengembalikan gambar ke keadaan semula
                rand_i = random.randint(max(0, i - 1), min(i + 1, width - 1))
                rand_j = random.randint(max(0, j - 1), min(j + 1, height - 1))
                rand_r, rand_g, rand_b = pixels[rand_i, rand_j]
                pixels[i, j] = ((r * 2) - rand_r, (g * 2) - rand_g, (b * 2) - rand_b)  # Memperbarui nilai piksel

    decrypted_image = image  # Mengembalikan gambar yang sudah didekripsi
    return decrypted_image
# Fungsi utama
def main():
    st.title("Image Encryption and Decryption")

    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button("Encrypt"):
            encrypted_image = encrypt_image(uploaded_file)
            st.image(encrypted_image, caption='Encrypted Image', use_column_width=True)

        if st.button("Decrypt"):
            decrypted_image = decrypt_image(uploaded_file)
            st.image(decrypted_image, caption='Decrypted Image', use_column_width=True)

if __name__ == '__main__':
    main()
