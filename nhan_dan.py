import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import schedule

# Bước 1: Tạo hàm Lấy nội dung bài viết

def lay_noi_dung_bai_viet(link_bai_viet):
    try:
        res = requests.get(link_bai_viet, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')
        noi_dung_div = soup.find('div', class_='fck')
        if noi_dung_div:
            cac_doan = noi_dung_div.find_all('p')
            return '\n'.join(p.text.strip() for p in cac_doan)
        return ''
    except Exception as e:
        print(f'Lỗi khi lấy nội dung bài viết: {e}')
        return ''
    
# Bước 2: Tạo hàm Lấy tin tức của bài báo

def lay_tin_nhan_dan():
    url = 'https://nhandan.vn/'
    print(f'Đang truy cập trang: {url}')
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, 'html.parser')

    bai_viet_list = []
    cac_bai = soup.find_all('article')

    print(f'Số bài viết tìm thấy: {len(cac_bai)}')

    for bai in cac_bai:
        try:
            the_a = bai.find('a')
            if not the_a or not the_a['href']:
                continue

            link = the_a['href']
            if not link.startswith('http'):
                link = 'https://nhandan.vn' + link

            tieu_de = the_a.get_text(strip=True)
            mo_ta_div = bai.find('div', class_='article-summary')
            mo_ta = mo_ta_div.get_text(strip=True) if mo_ta_div else ''
            hinh = bai.find('img')
            hinh_url = hinh['src'] if hinh and 'src' in hinh.attrs else ''

            # Lấy nội dung bài viết (có thể bỏ nếu bạn chỉ muốn tiêu đề + mô tả)
            noi_dung = lay_noi_dung_bai_viet(link)

            bai_viet_list.append({
                'Tiêu đề': tieu_de,
                'Mô tả': mo_ta,
                'Hình ảnh': hinh_url,
                'Nội dung': noi_dung,
                'Link': link
            })

            time.sleep(0.5)  # Dừng nhẹ để tránh bị chặn IP

        except Exception as e:
            print(f'Lỗi xử lý bài: {e}')
            continue

# Bước 3: Lưu dữ liệu thành file CSV

    if bai_viet_list:
        df = pd.DataFrame(bai_viet_list)
        df.to_csv('tin_nhandan.csv', index=False, encoding='utf-8-sig')
        print('Đã lưu dữ liệu vào file tin_nhandan.csv')
    else:
        print('Không có bài viết nào đủ dữ liệu để lưu.')

# Bước 4: Lên lịch tự động chạy lúc 6:00 sáng mỗi ngày

schedule.every().day.at("06:00").do(lay_tin_nhan_dan)
print("Chương trình đã khởi động. Đang chờ đến 06:00 sáng để chạy...")

# Bước 5: Vòng lặp chính để kiểm tra lịch

while True:
    schedule.run_pending()
    time.sleep(60)
