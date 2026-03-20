import matplotlib.pyplot as plt

cities = [
    'California City', 'Los Angeles', 'San Diego', 'San Jose',
    'Palm Springs', 'Bakersfield', 'Fresno', 'Sacramento',
    'Lancaster', 'Palmdale'
]
area_total_km2 = [527.2, 1302.0, 964.5, 466.1, 245.7, 393.1, 296.2, 259.3, 244.9, 275.1]
data = sorted(zip(cities, area_total_km2), key=lambda x: x[1])
sorted_cities, sorted_areas = zip(*data)
plt.figure(figsize=(12, 7))
bars = plt.barh(sorted_cities, sorted_areas, color='skyblue', edgecolor='navy')
for bar in bars:
    width = bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height()/2,
             f'{width:.1f} $km^2$', va='center', fontsize=10)
plt.title('Top 10 Thành phố lớn nhất California theo Diện tích', fontsize=15, fontweight='bold')
plt.xlabel('Diện tích ($km^2$)', fontsize=12)
plt.ylabel('Thành phố', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
