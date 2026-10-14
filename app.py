import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# 1. DỮ LIỆU & XỬ LÝ TÍNH TOÁN
# =========================================================
data = {
    'Họ tên': [
        'Năng Châu Tuấn Anh', 
        'Hồ Ngọc Bảo', 
        'Nguyễn Ngọc Đạt', 
        'Thiên Đại Dũng', 
        'Trần Nguyễn Trung Hậu', 
        'Lê Trung Hiếu', 
        'Dương Trí Khang', 
        'Đặng Thành Khoa', 
        'Châu Minh Khôi', 
        'Nguyễn Văn Ngọc'
    ],
    'Chuyên cần': [9.0, 8.5, 7.0, 10.0, 8.0, 6.0, 9.5, 7.5, 8.0, 10.0],
    'Giữa kỳ': [8.0, 9.0, 6.5, 9.5, 7.0, 5.5, 8.5, 6.0, 7.5, 9.0],
    'Cuối kỳ': [8.5, 9.0, 7.0, 9.0, 7.0, 6.0, 8.5, 7.0, 7.5, 9.5]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết: 20% Chuyên cần + 30% Giữa kỳ + 50% Cuối kỳ
df['Tổng kết'] = (0.2 * df['Chuyên cần'] + 
                  0.3 * df['Giữa kỳ'] + 
                  0.5 * df['Cuối kỳ']).round(2)

# Xếp loại sinh viên
def xep_loai(score):
    if score >= 8.5:
        return 'Giỏi'
    elif score >= 7.0:
        return 'Khá'
    elif score >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)

# Thống kê
dtb_lop = df['Tổng kết'].mean()
sv_cao_nhat = df.loc[df['Tổng kết'].idxmax()]
sv_thap_nhat = df.loc[df['Tổng kết'].idxmin()]
so_sv_dat = (df['Tổng kết'] >= 5.0).sum()

# =========================================================
# 2. GIAO DIỆN STREAMLIT
# =========================================================

# Tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Bảng điểm
st.subheader("Bảng điểm sinh viên")
st.dataframe(df)

# Thống kê chung
st.subheader("Thống kê chung")
st.write(f"- **Điểm trung bình của lớp:** {dtb_lop:.2f}")
st.write(f"- **Sinh viên có điểm tổng kết cao nhất:** {sv_cao_nhat['Họ tên']} ({sv_cao_nhat['Tổng kết']} điểm)")
st.write(f"- **Sinh viên có điểm tổng kết thấp nhất:** {sv_thap_nhat['Họ tên']} ({sv_thap_nhat['Tổng kết']} điểm)")
st.write(f"- **Số sinh viên đạt (Điểm TK ≥ 5.0):** {so_sv_dat}/{len(df)} sinh viên")

# Selectbox chọn sinh viên
st.subheader("Tra cứu thông tin sinh viên")
selected_student = st.selectbox("Chọn một sinh viên:", df['Họ tên'])

sv_info = df[df['Họ tên'] == selected_student].iloc[0]
st.write(f"**Thông tin chi tiết sinh viên:** {selected_student}")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Chuyên cần", sv_info['Chuyên cần'])
col2.metric("Giữa kỳ", sv_info['Giữa kỳ'])
col3.metric("Cuối kỳ", sv_info['Cuối kỳ'])
col4.metric("Tổng kết", sv_info['Tổng kết'])
col5.metric("Xếp loại", sv_info['Xếp loại'])

# Biểu đồ cột
st.subheader("Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(df['Họ tên'], df['Tổng kết'], color='#4a90e2')
ax.set_xlabel('Điểm tổng kết')
ax.set_ylabel('Họ tên')
ax.set_title('Biểu đồ điểm tổng kết')
ax.set_xlim(0, 10)
ax.invert_yaxis()

st.pyplot(fig)

# Họ tên & MSSV ở cuối trang
st.markdown("---")
st.markdown("<h4 style='text-align: center; color: #4a90e2;'>Người thực hiện: Võ Trần Lâm - MSSV: 060208004640</h4>", unsafe_allow_html=True)
