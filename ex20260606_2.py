import streamlit as st
import re
import base64

email = st.text_input(
    "📧 Địa chỉ Email",
    placeholder="Nhập email theo mẫu hợp lệ..."
)


with open("pass.png", "rb") as img:
    icon = base64.b64encode(img.read()).decode()

st.markdown(f"""
<div style="display:flex;align-items:center;gap:2px;margin-bottom:4px;">
    <img src="data:image/png;base64,{icon}" width="20">
    <span style="
        font-size:14px;
    ">
        Mật khẩu
    </span>
</div>
""", unsafe_allow_html=True)

password = st.text_input(
    "",
    type="password",
    label_visibility="collapsed",
    placeholder="Nhập mật khẩu theo quy tắc trên"
)
# Kiểm tra email theo định dạng Gmail
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email)

# Kiểm tra độ mạnh mật khẩu
def validate_password(password):
    pattern = (
        r'^(?=.*[a-z])'      # ít nhất 1 chữ thường
        r'(?=.*[A-Z])'      # ít nhất 1 chữ hoa
        r'(?=.*\d)'         # ít nhất 1 số
        r'(?=.*[@$!%*?&])'  # ít nhất 1 ký tự đặc biệt
        r'.{8,}$'           # tối thiểu 8 ký tự
    )
    return re.match(pattern, password)

if st.button("Tạo Tài Khoản"):

    if not validate_email(email):
        st.error(
            "Email của bạn không hợp lệ. Vui lòng kiểm tra định dạng (ví dụ: ten.ban@domain.com)."
        )

    elif not validate_password(password):
        st.error(
            "Mật khẩu không đáp ứng các yêu cầu về độ mạnh (8 ký tự, hoa, thường, số, đặc biệt)."
        )

    else:
        st.success("Tạo tài khoản thành công!")
        st.balloons()