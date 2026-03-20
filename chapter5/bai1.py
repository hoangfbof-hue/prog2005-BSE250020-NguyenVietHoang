import matplotlib.pyplot as plt
x = ['Xuất sắc', 'Giỏi', 'Khá', 'Trung bình', 'Yếu', 'Kém']
y = [6, 10, 15, 12, 4, 1]

plt.figure(figsize=(10, 6))

plt.bar(x, y)

plt.title('Biểu đồ cột thể hiện kết quả học tập của lớp', fontsize=16)
plt.xlabel('Xếp loại học tập', fontsize=12)
plt.ylabel('Số lượng học sinh', fontsize=12)
plt.grid(True, axis='y', linestyle='--')
plt.xticks(fontsize=11)
plt.yticks(range(0, 17, 2), fontsize=11)
plt.show()
