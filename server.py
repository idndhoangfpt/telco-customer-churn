import socket
# socket()
# bind()
# listen()
# accept()
# send()
# recv()
# close()

# IP mà server sẽ chạy
# 127.0.0.1 nghĩa là chỉ cho phép máy hiện tại kết nối
HOST = "127.0.0.1"

# Port của ứng dụng
PORT = 5000

# Tạo socket TCP
# AF_INET = IPv4
# SOCK_STREAM = TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Gắn socket vào địa chỉ IP + Port
server.bind((HOST, PORT))

# Bắt đầu lắng nghe kết nối
# Số 1 là số lượng kết nối chờ tối đa
server.listen(1)

print(f"Server đang lắng nghe tại {HOST}:{PORT}")

# Chờ client kết nối tới
# Chương trình sẽ đứng đây cho đến khi có client
conn, addr = server.accept()

# In ra địa chỉ client
print(f"Kết nối từ: {addr}")

# Vòng lặp nhận dữ liệu liên tục
# while True:
#     # Đọc tối đa 1024 bytes
#     data = conn.recv(1024)

#     # Nếu client ngắt kết nối
#     if not data:
#         break

#     # Chuyển bytes thành string
#     message = data.decode()

#     print("Client:", message)

#     # Gửi phản hồi lại client
#     conn.send(f"Server nhận: {message}".encode())


# Nhận dữ liệu
# data = conn.recv(4096)

# content = data.decode("utf-8")

# print("===== NOI DUNG FILE =====")
# print(content)


filename = conn.recv(1024).decode()

print("Nhan file:", filename)

conn.send(b"OK")

# Lưu file
with open("received_" + filename, "wb") as f:

    while True:
        data = conn.recv(1024)

        if not data:
            break

        f.write(data)

with open("received_error_log.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("===== NOI DUNG FILE =====")
    print(content)

# Đóng kết nối với client
conn.close()

# Tắt server
server.close()
