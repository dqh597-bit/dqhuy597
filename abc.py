import streamlit as st
import sys
if __name__ == "__main__":
    print("\n[!] Không chạy file này bằng python abc.py hoặc Run trong IDE.\n[!] Hãy chạy đúng bằng lệnh:\n    streamlit run d:/abc/abc.py\n")
    sys.exit(1)

import os
import google.generativeai as genai

import streamlit as st
import os
try:
    import google.generativeai as genai
except ImportError:
    genai = None

# API Key Gemini 2.5 Flash
API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyD0mbaQaH8GYh-0cxQPfe7oI5jfbm_yGt8")
if genai:
    genai.configure(api_key=API_KEY)

def summarize_cluster(cluster_text):
    if not genai:
        return "Chưa cài đặt thư viện google-generativeai. Vui lòng chạy: pip install google-generativeai"
    prompt = f"Tóm tắt ý nghĩa chủ đề chính của các ý sau:\n{cluster_text}\nChỉ trả về 1-2 câu ngắn gọn, súc tích."
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

st.title("Tóm tắt ý nghĩa các Cluster Survey Data bằng Gemini 2.5 Flash")

clusters = {
    "Cluster 1": [
        "Tăng cường bảo trì dự phòng để giảm thiểu sự cố và thời gian ngừng hoạt động.",
        "Giảm thiểu tác động môi trường để tránh các khoản phạt.",
        "Giảm thiểu chi phí quảng cáo và tiếp thị.",
        "Giám sát hoạt động của hệ thống mạng.",
        "Đánh giá rủi ro an ninh mạng.",
        "Giám sát việc tuân thủ chính sách an ninh mạng.",
        "Sử dụng hệ thống giám sát an ninh."
    ],
    "Cluster 2": [
        "Thương lượng lại hợp đồng với các nhà cung cấp.",
        "Quản lý chặt chẽ chi phí nhân công.",
        "Thực hiện các biện pháp chống tham nhũng.",
        "Đo lường và theo dõi hiệu quả của các biện pháp tiết kiệm chi phí.",
        "Thực hiện các biện pháp phòng ngừa rủi ro tài chính.",
        "Thực hiện các biện pháp phòng chống gian lận.",
        "Cập nhật phần mềm thường xuyên.",
        "Sao lưu dữ liệu thường xuyên.",
        "Thực hiện các biện pháp phòng ngừa tai nạn."
    ],
    "Cluster 3": [
        "Quản lý tốt hơn các dự án đầu tư.",
        "Sử dụng các vật liệu thay thế có chi phí thấp hơn.",
        "Quản lý tốt hơn các khoản nợ.",
        "Quản lý chặt chẽ quyền truy cập vào hệ thống.",
        "Cải thiện liên tục các biện pháp an toàn.",
        "Số hóa các quy trình làm việc."
    ],
    "Cluster 4": [
        "Sử dụng các công nghệ bảo mật tiên tiến.",
        "Hợp tác với các chuyên gia bảo mật.",
        "Tuân thủ các quy định về bảo mật dữ liệu.",
        "Khắc phục các lỗ hổng bảo mật.",
        "Bảo vệ các thiết bị khỏi bị mất cắp hoặc hư hỏng."
    ],
    "Cluster 5": [
        "Thực hiện kiểm toán năng lượng định kỳ.",
        "Khuyến khích nhân viên đóng góp ý tưởng tiết kiệm chi phí.",
        "Đa dạng hóa hoạt động kinh doanh.",
        "Thực hiện kiểm tra an ninh mạng định kỳ.",
        "Chuẩn hóa quy trình để dễ kiểm soát chi phí."
    ],
    "Cluster 6": [
        "Tối ưu hóa việc sử dụng các thiết bị và máy móc.",
        "Tối ưu hóa việc sử dụng nước.",
        "Tối ưu hóa cấu trúc vốn.",
        "Kiểm soát truy cập vật lý vào các khu vực nhạy cảm.",
        "Học hỏi từ các sự cố an toàn.",
        "Tối ưu hóa việc sử dụng các nguồn lực."
    ],
    "Cluster 7": [
        "Cải thiện quản lý chuỗi cung ứng.",
        "Cải thiện quy trình quản lý rủi ro.",
        "Cải thiện quy trình xử lý nước thải.",
        "Cải thiện quy trình mua sắm.",
        "Tối ưu hóa quy trình sản xuất.",
        "Cải thiện quy trình bảo trì sửa chữa.",
        "Cải thiện quy trình báo cáo tài chính.",
        "Xử lý an toàn các thiết bị cũ.",
        "Xử lý các sự cố an toàn một cách nhanh chóng và hiệu quả."
    ],
    "Cluster 8": [
        "Sử dụng các dịch vụ thuê ngoài khi thích hợp.",
        "Cải thiện quản lý hàng tồn kho.",
        "Xây dựng thương hiệu mạnh.",
        "Cải thiện dịch vụ khách hàng.",
        "Mở rộng thị trường.",
        "Cải thiện quản trị doanh nghiệp.",
        "Xây dựng chính sách an ninh mạng.",
        "Thực thi chính sách an ninh mạng.",
        "Cải tiến chính sách an ninh mạng."
    ],
    "Cluster 9": [
        "Tối ưu hóa việc sử dụng hóa chất trong quá trình khai thác.",
        "Tối ưu hóa thiết kế giếng khoan.",
        "Thực hiện các chương trình tiết kiệm chi phí trên toàn công ty.",
        "Xây dựng văn hóa tiết kiệm trong công ty.",
        "Tập trung vào các kênh tiếp thị hiệu quả.",
        "Tìm kiếm các nguồn cung cấp dầu khí mới.",
        "Thoái vốn khỏi các tài sản kém hiệu quả.",
        "Sáp nhập hoặc mua lại các công ty khác.",
        "Tái cấu trúc công ty.",
        "Thử nghiệm kế hoạch khôi phục dữ liệu."
    ],
    "Cluster 10": [
        "Sử dụng năng lượng tái tạo khi có thể.",
        "Sử dụng các công nghệ khoan tiên tiến.",
        "Tăng cường tái chế và tái sử dụng.",
        "Tăng cường minh bạch thông tin.",
        "Tăng cường giữ chân khách hàng.",
        "Tăng cường kiểm soát nội bộ.",
        "Tăng cường an ninh mạng.",
        "Xây dựng kế hoạch ứng phó sự cố an ninh mạng.",
        "Phát hiện và ngăn chặn các cuộc tấn công mạng.",
        "Xây dựng hệ thống lương thưởng khuyến khích tiết kiệm."
    ],
    "Cluster 11": [
        "Đào tạo nhân viên để nâng cao hiệu quả làm việc.",
        "Tăng cường an toàn lao động để giảm thiểu tai nạn.",
        "Tối ưu hóa việc sử dụng tài sản cố định.",
        "Cải thiện quan hệ với các nhà đầu tư.",
        "Đầu tư vào đào tạo an ninh mạng cho nhân viên.",
        "Nâng cao nhận thức của nhân viên về các mối đe dọa an ninh mạng.",
        "Sử dụng các thiết bị di động an toàn.",
        "Đảm bảo an toàn vật lý cho các trung tâm dữ liệu.",
        "Đảm bảo an toàn cho nhân viên.",
        "Cung cấp đào tạo về an toàn cho nhân viên.",
        "Thực hiện các buổi đánh giá hiệu suất làm việc của nhân sự."
    ],
    "Cluster 12": [
        "Giảm thiểu lãng phí năng lượng.",
        "Giảm thiểu chi phí vận chuyển.",
        "Giảm thiểu chi phí bảo hiểm.",
        "Giảm thiểu chi phí lưu kho.",
        "Giảm thiểu chi phí pháp lý.",
        "Giảm thiểu giấy tờ."
    ],
    "Cluster 13": [
        "Tích hợp hệ thống thông tin."
    ],
    "Cluster 14": [
        "Áp dụng công nghệ tự động hóa trong các hoạt động vận hành.",
        "Đầu tư vào nghiên cứu và phát triển (R&D) để tìm ra các giải pháp tiết kiệm chi phí.",
        "Áp dụng các giải pháp công nghệ thông tin (CNTT) để quản lý dữ liệu và ra quyết định.",
        "Tăng cường hợp tác với các đối tác để chia sẻ chi phí.",
        "Sử dụng các công nghệ mô phỏng để tối ưu hóa hoạt động.",
        "Áp dụng các nguyên tắc sản xuất tinh gọn (Lean Manufacturing).",
        "Sử dụng các công cụ phái sinh để phòng ngừa rủi ro.",
        "Thực hiện các chương trình trách nhiệm xã hội của doanh nghiệp (CSR) để nâng cao uy tín.",
        "Áp dụng các tiêu chuẩn quốc tế về quản lý.",
        "Sử dụng các phần mềm quản lý doanh nghiệp (ERP).",
        "Áp dụng các giải pháp điện toán đám mây.",
        "Bảo vệ dữ liệu của công ty.",
        "Sử dụng các công cụ quét virus và phần mềm độc hại.",
        "Xây dựng kế hoạch khôi phục dữ liệu."
    ]
}

cluster_names = list(clusters.keys())
selected_cluster = st.selectbox("Chọn Cluster để tóm tắt", cluster_names)

if st.button("Tóm tắt Cluster"):
    cluster_text = "\n".join(clusters[selected_cluster])
    summary = summarize_cluster(cluster_text)
    st.subheader("Tóm tắt chủ đề chính:")
    st.write(summary)
# Load API key từ biến môi trường
API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyD0mbaQaH8GYh-0cxQPfe7oI5jfbm_yGt8")
genai.configure(api_key=API_KEY)

def summarize_cluster(cluster_text):
    prompt = f"Tóm tắt ý nghĩa chủ đề chính của các ý sau:\n{cluster_text}\nChỉ trả về 1-2 câu ngắn gọn, súc tích."
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

st.title("Tóm tắt ý nghĩa các Cluster Survey Data bằng Gemini 2.5 Flash")

clusters = {
    "Cluster 1": [
        "Tăng cường bảo trì dự phòng để giảm thiểu sự cố và thời gian ngừng hoạt động.",
        "Giảm thiểu tác động môi trường để tránh các khoản phạt.",
        "Giảm thiểu chi phí quảng cáo và tiếp thị.",
        "Giám sát hoạt động của hệ thống mạng.",
        "Đánh giá rủi ro an ninh mạng.",
        "Giám sát việc tuân thủ chính sách an ninh mạng.",
        "Sử dụng hệ thống giám sát an ninh."
    ],
    # ... (Thêm các Cluster 2-14 tương tự)
}

cluster_names = list(clusters.keys())
selected_cluster = st.selectbox("Chọn Cluster để tóm tắt", cluster_names)

if st.button("Tóm tắt Cluster"):
    cluster_text = "\n".join(clusters[selected_cluster])
    summary = summarize_cluster(cluster_text)
    st.subheader("Tóm tắt chủ đề chính:")
    st.write(summary)