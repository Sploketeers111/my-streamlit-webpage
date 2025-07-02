import streamlit as st
from PIL import Image
import base64
import os

# --- Convert local image to Base64 ---
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- Set local image as background ---
def set_bg_from_local(file_path):
    encoded = get_base64(file_path)
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# --- Page Settings ---
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ✅ Use relative path to the image (important when deployed)
set_bg_from_local("Py.jpg")

# --- Contact Form Styling (CSS) ---
st.markdown("""
<style>
form {
    background-color: rgba(255, 255, 255, 0.95);
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
    font-family: 'Segoe UI', sans-serif;
    max-width: 500px;
    margin: 40px auto;
}
input, textarea {
    width: 100%;
    padding: 14px;
    margin: 12px 0;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 15px;
    box-sizing: border-box;
    resize: vertical;
}
textarea {
    min-height: 150px;
}
button {
    background-color: #4CAF50;
    color: white;
    padding: 14px;
    width: 100%;
    font-size: 16px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}
button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

# ---- Load Image Asset ----
img_contact_form = Image.open("images/p1.png")

# ---- HEADER ----
with st.container():
    st.subheader("Hi, I am Ian :wave:")
    st.title("An App Developer From Earth")
    st.write("I am passionate about making programs in Python.")
    st.write("[Learn More >](https://youtu.be/wVeaW6N7IKk)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write("""
            On my webpage, this is a practice project where I'm:
            - Creating my website
            - Uploading my website
            - Eager to learn more every day!
        """)
        st.write("[YouTube Channel >](https://youtu.be/FBjGtN6BqkU)")

            
# ---- PHOTO ALBUM ----
with st.container():
    st.write("---")
    st.header("📸 My Photo Album")
    st.write("##")

    album_dir = "images/albums"

    if os.path.exists(album_dir):
        image_files = [
            f for f in os.listdir(album_dir)
            if f.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        if image_files:
            cols = st.columns(3)
            for i, image_file in enumerate(image_files):
                img_path = os.path.join(album_dir, image_file)
                img = Image.open(img_path)
                with cols[i % 3]:
                    st.image(img, use_container_width=True, caption=image_file)
        else:
            st.info("📂 The album folder is empty. Add some images to display them here.")
    else:
        st.error(f"❌ Album folder not found: {album_dir}")
        
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form, use_container_width=True)
    with text_column:
        st.subheader("Intelligent Programming")
        st.write("Learn to create a program")
        st.markdown("[Watch Video...](https://youtu.be/M6o1Z8fajsU)")

        # ✅ Dropbox Download Integration
        st.markdown("### 📥 Download Project Installer")
        st.markdown(
            "[🗂️ Download Sugar Cane Monitoring Program (ZIP)](https://www.dropbox.com/scl/fi/iw0j8hn74dgob9swhpeby/SCFMvGDPrime-Installer.zip?rlkey=1cng3cgw50as74p7vavcj4zg3&st=sblq5xyg&dl=1)",
            unsafe_allow_html=True
        )

#----- DOWNLOAD SECTION ------
with st.container():
    st.write("---")
    st.header("📂 Download My Files")
    st.write("##")

    st.markdown("### 🗂️ Download DTR (ZIP)")
    st.markdown(
        "[📥 Download DTR (MDTR_71.zip)](https://www.dropbox.com/scl/fi/iw0j8hn74dgob9swhpeby/SCFMvGDPrime-Installer.zip?rlkey=1cng3cgw50as74p7vavcj4zg3&st=sblq5xyg&dl=1)",
        unsafe_allow_html=True
    )

    st.markdown("### 🗂️ Download Sugar Cane Monitoring Program (ZIP)")
    st.markdown(
        "[📥 Download SCFMvGDPrime-Installer.zip](https://www.dropbox.com/scl/fi/iw0j8hn74dgob9swhpeby/SCFMvGDPrime-Installer.zip?rlkey=1cng3cgw50as74p7vavcj4zg3&st=sblq5xyg&dl=1)",
        unsafe_allow_html=True
    )

    st.markdown("### 📁 Available Downloads")




        
# ---- CONTACT FORM ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/ianp39171@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_subject" value="New Contact Form Submission!">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
