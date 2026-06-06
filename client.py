import socket
import os
# Địa chỉ server muốn kết nối tới
HOST = "127.0.0.1"

# Port server đang mở
PORT = 5000

# Tạo socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối tới server
client.connect((HOST, PORT))


# Gửi tên file trước
filename = "error_log.txt"
client.send(os.path.basename(filename).encode())
client.recv(1024)  # ACK

# Gửi nội dung file
with open(filename, "rb") as f:
    while True:
        chunk = f.read(1024) # đọc từng khối

        if not chunk:
            break

        client.send(chunk) # gui liên tục
        
        
# Đọc file
# with open("error_log.txt", "r", encoding="utf-8") as f:
#     content = f.read()

# # Gửi nội dung file
# client.send(content.encode("utf-8"))

# Vòng lặp chat
# while True:
#     # Nhập dữ liệu từ bàn phím
#     message = input("Bạn: ")

#     # Nếu gõ exit thì thoát
#     if message.lower() == "exit":
#         break

#     # Gửi dữ liệu lên server
#     client.send(message.encode())

#     # Chờ server phản hồi
#     response = client.recv(1024)

#     # In phản hồi
#     print(response.decode())

# Đóng kết nối
client.close()
