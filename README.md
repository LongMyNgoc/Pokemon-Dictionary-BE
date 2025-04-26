# Pokemon Dictionary (Back-End)

## Giới Thiệu
Pokemon Dictionary là một hệ thống quản lý và tra cứu thông tin về các Pokémon. Dự án này cung cấp một API RESTful cho phép người dùng lấy thông tin chi tiết về các Pokémon thông qua PokeAPI. Hệ thống sử dụng **FastAPI** để xây dựng API, mang lại hiệu suất cao và dễ dàng mở rộng.

## Tính Năng Chính
- Lấy danh sách các Pokémon.
- Lấy thông tin chi tiết về một Pokémon (bao gồm tên, loại, và ảnh).
- Hỗ trợ tìm kiếm và phân trang cho dữ liệu.

## Công Nghệ Sử Dụng
- **FastAPI**: Đây là framework API hiện đại và mạnh mẽ giúp xây dựng các dịch vụ web với hiệu suất cao và khả năng dễ dàng phát triển. FastAPI hỗ trợ xây dựng các API RESTful và sinh tự động tài liệu API qua OpenAPI, giúp quá trình phát triển trở nên nhanh chóng và hiệu quả.
- **uvicorn**: Server ASGI để chạy ứng dụng FastAPI.

## Yêu Cầu Hệ Thống
Trước khi bắt đầu, bạn cần cài đặt phiên bản **Python 3.10.11** (hoặc phiên bản tương thích) trên hệ thống của mình.

### Các thư viện cần thiết:
1. **FastAPI**: Framework để xây dựng các endpoint API.
2. **uvicorn**: Chạy ứng dụng FastAPI trên môi trường phát triển.
3. **httpx**: Thư viện để gọi các API bên ngoài (như PokeAPI).
4. **asyncio**: Thư viện để thực hiện các tác vụ bất đồng bộ.
## Hướng Dẫn Cài Đặt & Chạy Dự Án

### 1. Cài Đặt Dependencies
Trước tiên, bạn cần cài đặt tất cả các thư viện phụ thuộc của dự án. Mở terminal và chạy lệnh sau:
```bash
pip install -r requirements.txt
```

### 2. Khởi động server phát triển
Chạy lệnh sau để khởi động dự án:
```bash
python main.py
```

Hệ thống sẽ chạy trên **localhost**, bạn có thể truy cập bằng trình duyệt để kiểm tra giao diện và tính năng.

## Liên kết hệ thống
- **Back-End (GitHub)**: https://github.com/LongMyNgoc/Pokemon-Dictionary-BE.git
- **Back-End (Railway)**: https://pokemon-dictionary-be-production.up.railway.app/
- **Front-End (GitHub)**: https://github.com/LongMyNgoc/Pokemon-Dictionary-App.git

## Đóng góp & Phát triển
Chúng tôi luôn chào đón sự đóng góp từ cộng đồng! Nếu bạn có bất kỳ ý tưởng, cải tiến hoặc báo lỗi nào, vui lòng gửi qua hệ thống quản lý mã nguồn của dự án. Bạn cũng có thể liên hệ trực tiếp với nhóm phát triển để thảo luận thêm.

## Thông tin liên hệ
📧 Email: nguyenphilong.dev@gmail.com 
🌐 Portfolio: https://nguyenphilongportfolio.vercel.app/
