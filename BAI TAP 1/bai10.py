import os

FILENAME = "products.txt"


def nhap_san_pham():
    """Nhập thông tin và ghi thêm vào tệp"""
    code = input("Nhập mã sản phẩm: ")
    name = input("Nhập tên sản phẩm: ")
    try:
        price = float(input("Nhập giá sản phẩm: "))

        line = f"{code};{name};{price}\n"

        with open(FILENAME, "a", encoding="utf-8") as f:
            f.write(line)
        print("Đã thêm sản phẩm thành công!")
    except ValueError:
        print("Lỗi: Giá sản phẩm phải là một số.")


def doc_danh_sach():
    """Đọc dữ liệu từ tệp và trả về danh sách các object/dictionary"""
    products = []
    if not os.path.exists(FILENAME):
        return products

    with open(FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(';')
                if len(parts) == 3:
                    products.append({
                        'code': parts[0],
                        'name': parts[1],
                        'price': float(parts[2])
                    })
    return products


def hien_thi_danh_sach(products):
    """Hiển thị danh sách sản phẩm ra màn hình"""
    if not products:
        print("Danh sách sản phẩm trống.")
        return

    print(f"{'Mã SP':<10} | {'Tên sản phẩm':<20} | {'Giá':<10}")
    print("-" * 45)
    for p in products:
        print(f"{p['code']:<10} | {p['name']:<20} | {p['price']:<10}")


def sap_xep_giam_dan():
    """Sắp xếp sản phẩm theo giá giảm dần"""
    products = doc_danh_sach()
    if products:
        products.sort(key=lambda x: x['price'], reverse=True)
        print("\n--- DANH SÁCH SẢN PHẨM SẮP XẾP THEO GIÁ GIẢM DẦN ---")
        hien_thi_danh_sach(products)
    else:
        print("Không có dữ liệu để sắp xếp.")


while True:
    print("\n=== HỆ THỐNG QUẢN LÝ SẢN PHẨM ===")
    print("1. Nhập sản phẩm mới")
    print("2. Hiển thị danh sách sản phẩm")
    print("3. Sắp xếp sản phẩm theo giá giảm dần")
    print("0. Thoát")

    chon = input("Chọn chức năng: ")

    if chon == '1':
        nhap_san_pham()
    elif chon == '2':
        print("\n--- DANH SÁCH SẢN PHẨM HIỆN TẠI ---")
        hien_thi_danh_sach(doc_danh_sach())
    elif chon == '3':
        sap_xep_giam_dan()
    elif chon == '0':
        print("Đã thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ!")
