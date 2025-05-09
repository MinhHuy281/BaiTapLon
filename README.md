# Nhân Dân News Scraper 📰

Script Python này giúp bạn tự động thu thập tin tức từ **trang chủ báo Nhân Dân** tại [https://nhandan.vn](https://nhandan.vn) và lưu dữ liệu vào file CSV hàng ngày lúc 6h sáng.

---

## 🚀 Tính năng

- Truy cập trang: `https://nhandan.vn/`
- Thu thập thông tin từ các bài viết trên trang chủ:
  - ✅ Tiêu đề
  - ✅ Mô tả
  - ✅ Hình ảnh
  - ✅ Nội dung chi tiết bài viết
  - ✅ Link bài viết gốc
- Tự động lưu vào file CSV tên: `tin_nhandan.csv`
- Có thể thiết lập **lên lịch chạy tự động hàng ngày** lúc `06:00` sáng bằng thư viện `schedule`.

---
## ⚙️ Các Bước đẩy File lên GitHub
- Bước 1: git init
- Bước 2: git add .
- Bước 3: git commit -m "first commit"
- Bước 4: git branch -M main
- Bước 5: git remote add origin https://github.com/MinhHuy281/BaiTapLon.git
- Bước 6: git push -u origin main

## 🧰 Yêu cầu

- Python 3.6 trở lên
- Các thư viện Python:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `schedule`

Cài đặt nhanh bằng lệnh:

```bash
pip install requests beautifulsoup4 pandas schedule
