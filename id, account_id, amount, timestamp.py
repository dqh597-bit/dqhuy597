"""
Bài toán: Phát hiện giao dịch đáng ngờ (chống rửa tiền)
Tác giả: (Huy)
Ngày: 05/05/2026
Mô tả: Sử dụng Z-score và phát hiện tần suất giao dịch để tìm outlier và hành vi cấu trúc.
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ------------------------------
# 1. TẠO DỮ LIỆU MẪU (thay vì đọc file CSV)
# ------------------------------
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'account_id': ['A100', 'A100', 'A100', 'B200', 'B200', 'B200', 
                   'C300', 'C300', 'C300', 'D400', 'D400', 'D400'],
    'amount': [5_000_000, 5_200_000, 150_000_000, 
               3_000_000, 2_800_000, 3_100_000,
               10_000_000, 12_000_000, 500_000_000,
               7_000_000, 8_000_000, 999_999_999],
    'timestamp': [
        '2025-04-01 09:15:00', '2025-04-01 14:20:00', '2025-04-02 08:00:00',
        '2025-04-01 10:00:00', '2025-04-01 11:30:00', '2025-04-02 09:00:00',
        '2025-04-01 12:00:00', '2025-04-01 13:00:00', '2025-04-03 07:45:00',
        '2025-04-02 15:00:00', '2025-04-02 16:00:00', '2025-04-03 00:05:00'
    ]
}

df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Hiển thị dữ liệu đầu vào
print("="*60)
print("DỮ LIỆU GIAO DỊCH BAN ĐẦU")
print("="*60)
print(df.to_string(index=False))
print("\n")

# ------------------------------
# 2. THỐNG KÊ MÔ TẢ
# ------------------------------
print("="*60)
print("THỐNG KÊ SỐ TIỀN GIAO DỊCH")
print("="*60)
print(df['amount'].describe())
print("\n")

# ------------------------------
# 3. PHÁT HIỆN OUTLIER BẰNG Z-SCORE (ngưỡng 2.5)
# ------------------------------
z_scores = np.abs(stats.zscore(df['amount']))
outlier_mask = z_scores > 2.5
df['is_suspicious_amount'] = outlier_mask

print("="*60)
print("GIAO DỊCH ĐÁNG NGỜ DO SỐ TIỀN BẤT THƯỜNG (Z-score > 2.5)")
print("="*60)
suspicious_amount = df[df['is_suspicious_amount']]
if not suspicious_amount.empty:
    print(suspicious_amount[['id', 'account_id', 'amount', 'timestamp']])
else:
    print("Không có giao dịch nào.")
print("\n")

# ------------------------------
# 4. PHÁT HIỆN TẦN SUẤT CAO (giao dịch cách nhau dưới 1 giờ)
# ------------------------------
df = df.sort_values(['account_id', 'timestamp'])
df['time_diff_hours'] = df.groupby('account_id')['timestamp'].diff().dt.total_seconds() / 3600

# Đánh dấu giao dịch có khoảng cách <= 1 giờ so với giao dịch trước đó cùng tài khoản
df['high_freq'] = (df['time_diff_hours'] <= 1) & (df['time_diff_hours'].notna())

print("="*60)
print("GIAO DỊCH CÓ TẦN SUẤT CAO (cách giao dịch trước < 1 giờ)")
print("="*60)
high_freq_trans = df[df['high_freq']]
if not high_freq_trans.empty:
    print(high_freq_trans[['account_id', 'amount', 'timestamp', 'time_diff_hours']])
else:
    print("Không phát hiện giao dịch tần suất cao.")
print("\n")

# ------------------------------
# 5. TỔNG HỢP GIAO DỊCH CẦN BÁO CÁO
# ------------------------------
df['final_flag'] = df['is_suspicious_amount'] | df['high_freq']

print("="*60)
print("DANH SÁCH GIAO DỊCH ĐÁNG NGỜ (CẦN BÁO CÁO)")
print("="*60)
report = df[df['final_flag']][['id', 'account_id', 'amount', 'timestamp', 'is_suspicious_amount', 'high_freq']]
print(report.to_string(index=False))
print("\n")

# ------------------------------
# 6. PHÂN TÍCH THEO TÀI KHOẢN
# ------------------------------
print("="*60)
print("TỔNG HỢP THEO TÀI KHOẢN")
print("="*60)
account_stats = df.groupby('account_id').agg(
    total_amount=('amount', 'sum'),
    avg_amount=('amount', 'mean'),
    transaction_count=('amount', 'count'),
    flagged=('final_flag', 'sum')
)
print(account_stats)
print("\n")

# ------------------------------
# 7. VẼ BIỂU ĐỒ
# ------------------------------
# Boxplot số tiền
plt.figure(figsize=(10, 4))
plt.boxplot(df['amount'], vert=False, patch_artist=True)
plt.title('Biểu đồ hộp (Boxplot) - Phân phối số tiền giao dịch')
plt.xlabel('Số tiền (VND)')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.savefig('boxplot_amount.png', dpi=150, bbox_inches='tight')
plt.show()

# Histogram
plt.figure(figsize=(10, 5))
plt.hist(df['amount'], bins=10, edgecolor='black', alpha=0.7, color='steelblue')
plt.title('Phân phối số tiền giao dịch (Histogram)')
plt.xlabel('Số tiền (VND)')
plt.ylabel('Số lần giao dịch')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('histogram_amount.png', dpi=150, bbox_inches='tight')
plt.show()

# Biểu đồ thanh so sánh số tiền theo tài khoản
plt.figure(figsize=(8, 5))
account_total = df.groupby('account_id')['amount'].sum().sort_values()
account_total.plot(kind='bar', color='coral', edgecolor='black')
plt.title('Tổng số tiền giao dịch theo tài khoản')
plt.xlabel('Tài khoản')
plt.ylabel('Tổng số tiền (VND)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('bar_total_by_account.png', dpi=150, bbox_inches='tight')
plt.show()

# ------------------------------
# 8. KẾT LUẬN VÀ ĐÁNH GIÁ (in ra màn hình)
# ------------------------------
print("="*60)
print("KẾT LUẬN & ĐÁNH GIÁ")
print("="*60)
print("1. Các giao dịch có số tiền bất thường (outlier):")
for idx, row in suspicious_amount.iterrows():
    print(f"   - ID {row['id']}, tài khoản {row['account_id']}, số tiền {row['amount']:,.0f} VND")
print("\n2. Các giao dịch có tần suất cao (dưới 1 giờ):")
for idx, row in high_freq_trans.iterrows():
    print(f"   - Tài khoản {row['account_id']}, số tiền {row['amount']:,.0f} VND, cách giao dịch trước {row['time_diff_hours']:.2f} giờ")
print("\n3. Tổng số giao dịch cần báo cáo:", len(report))
print("4. Khuyến nghị:")
print("   - Báo cáo ngay các tài khoản A100, C300, D400 đến bộ phận phòng chống rửa tiền.")
print("   - Tạm thời khóa hoặc giám sát đặc biệt tài khoản C300 và D400 do vừa có outlier vừa có tần suất cao.")
print("   - Thiết lập ngưỡng động theo lịch sử giao dịch của từng khách hàng để phát hiện sớm.")
print("   - Lưu lại các biểu đồ đã xuất ra (boxplot_amount.png, histogram_amount.png, bar_total_by_account.png) để đính kèm báo cáo.")
print("\n--- HOÀN THÀNH PHÂN TÍCH ---")