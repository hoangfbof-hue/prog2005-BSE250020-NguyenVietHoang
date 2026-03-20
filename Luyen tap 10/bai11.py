def menu():
    while True:
        print("\n" + "=" * 20 + " MENU BÀI TẬP " + "=" * 20)
        print("1. Trích xuất tên file từ đường dẫn")
        print("2. Đếm số lần xuất hiện của ký tự")
        print("3. Tính giai thừa (Đệ quy)")
        print("4. Tính độ dài chuỗi (Kiểm tra rỗng)")
        print("5. Vẽ đồ thị Subplots (Matplotlib)")
        print("6. Đảo ngược chuỗi (Vòng lặp)")
        print("7. Sắp xếp chuỗi Bubble Sort (Giảm dần độ dài)")
        print("0. Thoát chương trình")
        print("=" * 54)

        choice = input("Mời bạn chọn bài tập (0-7): ")

        if choice == '1':
            import os
            path = "d:\\music\\muabui.mp3"
            print(f"Đường dẫn: {path}")
            print(f"Tên file: {os.path.basename(path)}")
            print(f"Tên bài hát: {os.path.splitext(os.path.basename(path))[0]}")

        elif choice == '2':
            s = input("Nhập chuỗi: ")
            c = input("Nhập ký tự cần đếm: ")
            print(f"Kết quả: {s.count(c)}")

        elif choice == '3':
            def giai_thua(n):
                return 1 if n <= 1 else n * giai_thua(n - 1)

            num = int(input("Nhập số nguyên dương: "))
            print(f"{num}! = {giai_thua(num)}")

        elif choice == '4':
            s = input("Nhập chuỗi: ")
            if not s.strip():
                print("Lỗi: Chuỗi rỗng!")
            else:
                print(f"Độ dài: {len(s)}")

        elif choice == '5':
            import matplotlib.pyplot as plt
            import numpy as np
            x = np.linspace(0, 10, 100)
            fig, (ax1, ax2) = plt.subplots(1, 2)
            ax1.plot(x, x ** 2);
            ax1.set_title("y=x^2")
            ax2.plot(x, np.sqrt(x));
            ax2.set_title("y=sqrt(x)")
            plt.tight_layout()
            print("Đang hiển thị đồ thị...")
            plt.show()

        elif choice == '6':
            s = input("Nhập chuỗi: ")
            rev = ""
            for char in s: rev = char + rev
            print(f"Chuỗi đảo ngược: {rev}")

        elif choice == '7':
            arr = [input(f"Nhập chuỗi {i + 1}: ") for i in range(5)]
            for i in range(len(arr)):
                for j in range(0, len(arr) - i - 1):
                    if len(arr[j]) < len(arr[j + 1]):
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"Bước {i + 1}: {arr}")

        elif choice == '0':
            print("Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


if __name__ == "__main__":
    menu()
