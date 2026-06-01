# Dữ liệu doanh thu và lợi nhuận các tháng
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dữ liệu các tháng
months = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
revenue = np.array([3, 6, 9, 10, 12, 15, 18, 20])
profit = np.array([1.1, 2, 3.2, 3.4, 3.9, 5, 6.2, 6.6])

# Huấn luyện mô hình dự đoán lợi nhuận dựa trên doanh thu
model = LinearRegression()
model.fit(revenue.reshape(-1, 1), profit)

# Doanh thu tháng 9
revenue_month9 = 25
predicted_profit9 = model.predict(np.array([[revenue_month9]]))[0]
print(f"Dự đoán lợi nhuận tháng 9 (doanh thu 25): {predicted_profit9:.2f}")

# Vẽ biểu đồ doanh thu và lợi nhuận
plt.figure(figsize=(8,5))
plt.scatter(revenue, profit, color='blue', label='Lợi nhuận thực tế')
plt.scatter([revenue_month9], [predicted_profit9], color='red', label='Dự đoán tháng 9')
plt.plot(revenue, model.predict(revenue.reshape(-1, 1)), color='green', linestyle='--', label='Hồi quy tuyến tính')
plt.xlabel('Doanh thu (triệu)')
plt.ylabel('Lợi nhuận (triệu)')
plt.title('Dự đoán lợi nhuận theo doanh thu')
plt.legend()
plt.grid(True)
plt.show()
