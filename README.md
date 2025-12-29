🏘️ Xây dựng mô hình neural network dự đóan giá nhà trên tập dữ liệu gía nhà tự thu thập 

📌 Project Overview 
Dự án này tập trung vào xây dựng mô hình Multi-layer perceptron để dự đoán giá hà trên dữ liệu thực tế .

Quy trình thu thập dữ liệu giá nhà thô từ các trang web bất động sản, xử lý và lưu trữ dữ liệu đó ở định dạng có cấu trúc,
đồng thời chuẩn bị dữ liệu cho các mô hình học máy, phục vụ bài toán phân tích và dự đoán giá nhà.

🎯 Project Objectives 
+) Thu thập dữ liệu bất động sản từ các nguồn trực tuyến.
+) Làm sạch và xử lý dữ liệu thô , không có cấu trúc.
+) Lưu trữ dữ liệu đã xử lý trong cơ sở dữ liệu.
+) Chuẩn bị đặc trưng cho các mô hình dự đoán giá nhà.
+) Xây dựng các mô hình phục vụ bài tóa dự đóan giá. 
+) xây dựng giao diện demo 

🌐 Data source 
+) crawl dữ liệu từ trang web batdongsan.com.

🧱 Pineline Overview 
Web / CSV
→ Python Extract
→ Raw Data
→ Python Transform
→ Processed Data
→ Data Warehouse
→ (Optional) ML Prediction

🛠 Tech Stack
+) Programming Language: python
+) Web Scraping: Selenium + Beautifulsoup
+) Data Processing: Pandas , Numpy
+) Database: PostgreSQL 
+) Machine Learning: Scikit-learn 
+) Visualization: Matplotlib
+) Feauture: dbt, Airflow

