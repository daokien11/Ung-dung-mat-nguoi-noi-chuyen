import streamlit as st
from PIL import Image

# Tựa đề app
st.title("Virtual Assistant - Trợ lý ảo ghép mặt")

# Upload ảnh mặt
uploaded_face = st.file_uploader("Upload ảnh gương mặt của bạn", type=["jpg", "jpeg", "png"])

# Body mẫu (ảnh cố định)
body_image = "body.png"  # ảnh nhân vật mẫu

# Nếu đã upload mặt
if uploaded_face is not None:
    face = Image.open(uploaded_face)
    st.image(face, caption="Ảnh gương mặt của bạn", width=256)

    # Hiển thị body mẫu
    body = Image.open(body_image)
    st.image(body, caption="Body mẫu", width=400)

    # Ghép giả lập đơn giản (không deepfake)
    st.success("Giả lập ghép mặt hoàn tất!")

# Chatbox
st.subheader("Chat với trợ lý ảo")
user_input = st.text_input("Bạn hỏi gì nè?")

if user_input:
    # Trả lời đơn giản
    bot_response = f"Tôi là trợ lý ảo. Bạn vừa hỏi: {user_input}"
    st.write(bot_response)

    # Hiệu ứng mấp máy môi (giả lập bằng hiển thị lại ảnh body)
    st.image(body_image, width=400)