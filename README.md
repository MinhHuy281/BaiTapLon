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
