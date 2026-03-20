import matplotlib.pyplot as plt

labels = ['Sản phẩm A', 'Sản phẩm B', 'Sản phẩm C', 'Sản phẩm D', 'Sản phẩm E']
sizes = [30, 25, 15, 20, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

plt.figure(figsize=(8, 8))
explode = (0.1, 0, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title('Tỷ trọng doanh số của 5 sản phẩm', fontsize=14)

plt.axis('equal')

plt.show()
