Đây là github repository của nhóm Qual gals

Trước khi chạy, cần đảm bảo bạn đang sử dụng Python phiên bản 3.x(note: chương trình được viết bằng Python 3.7). Các bước để chạy bao gồm
1. Tạo môi trường ảo bằng command python3 -m venv [tên môi trường ảo]
2. Kích hoạt môi trường ảo bằng command source [tên môi trường ảo]/bin/activate
3. Tải requirement bằng command pip install -r requirements.txt
4. Chạy bằng command flask run trong , truy cập trang web bằng cách ấn vào link hiện lên trong terminal.

Folders
api - back end logic code
templates - chứa các file html
static - chứa file script/css
models - chứa các model tượng trưng cho object

Files
config.py - configuration của project
init.py - tạo ra app