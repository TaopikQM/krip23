import streamlit as st
from PIL import Image

# Fungsi untuk mengenkripsi gambar
def encrypt_image(image_path):
    image = Image.open(image_path)  # Membuka gambar dari path

    # Mendapatkan data piksel dari gambar
    pixels = image.load()
    width, height = image.size

    # Proses enkripsi untuk setiap piksel
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]  # Mendapatkan nilai warna RGB
            # Logika enkripsi di sini
            r = (r + 100) % 256
            g = (g + 50) % 256
            b = (b + 150) % 256
            pixels[i, j] = (r, g, b)  # Memperbarui nilai piksel

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
            r, g, b = pixels[i, j]  # Mendapatkan nilai warna RGB
            # Logika dekripsi di sini
            r = (r - 100) % 256
            g = (g - 50) % 256
            b = (b - 150) % 256
            pixels[i, j] = (r, g, b)  # Memperbarui nilai piksel

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