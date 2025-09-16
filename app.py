import streamlit as st
from PIL import Image
import io
import os
import base64

# Page config
st.set_page_config(page_title="🖼️ Image Compressor", page_icon="🗜️")

st.title("🖼️ Image Compressor")
st.write("Upload an image, compress it, and download the smaller version.")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open image
    image = Image.open(uploaded_file)
    
    st.subheader("📥 Original Image")
    st.image(image, caption=f"Original Size: {uploaded_file.size / 1024:.2f} KB", use_container_width=True)

    # Compression quality slider
    quality = st.slider("Compression Quality", 10, 95, 70)

    # Compress image
    img_bytes = io.BytesIO()
    if image.format == "PNG":
        # For PNG, convert to RGB and save as JPEG to reduce size
        image = image.convert("RGB")
        image.save(img_bytes, format="JPEG", quality=quality, optimize=True)
        file_ext = "jpg"
    else:
        image.save(img_bytes, format="JPEG", quality=quality, optimize=True)
        file_ext = "jpg"

    img_bytes.seek(0)

    compressed_size = len(img_bytes.getvalue()) / 1024

    st.subheader("📤 Compressed Image")
    st.image(img_bytes, caption=f"Compressed Size: {compressed_size:.2f} KB", use_container_width=True)

    # Download button
    st.download_button(
        label="⬇️ Download Compressed Image",
        data=img_bytes,
        file_name=f"compressed_image.{file_ext}",
        mime="image/jpeg"
    )
