MAT_KHAU_DUNG = "python123"
mat_khau_nhap = ""
while mat_khau_nhap != MAT_KHAU_DUNG:
    mat_khau_nhap = input("Vui lòng nhập mật khẩu: ")
    
    if mat_khau_nhap == MAT_KHAU_DUNG:
        print("Đăng nhập thành công! Chào mừng bạn.")
    else:
        print("Mật khẩu sai rồi. Vui lòng thử lại!")
