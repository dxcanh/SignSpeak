import pyrebase

# Cấu hình Firebase
config = {
    "apiKey": "AIzaSyCOM6-zvV2OhCWM76NS0xYI2_mIsvcgpD4",
    "authDomain": "signspeak-5b1bd.firebaseapp.com",
    "projectId": "signspeak-5b1bd",
    "storageBucket": "signspeak-5b1bd.firebasestorage.app",
    "messagingSenderId": "605753446406",
    "appId": "1:605753446406:web:fcc1e3734c65a5ab28f387",
    "measurementId": "G-S6KTFVCY0W",
    "databaseURL": "https://signspeak-5b1bd-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

# Khởi tạo ứng dụng Firebase
firebase = pyrebase.initialize_app(config)

# Khởi tạo các dịch vụ
auth = firebase.auth()
db = firebase.database()

# Thông tin người dùng
email = 'docanhsm@gmail.com'
password = '1609200416092004'

# Đăng ký tài khoản
auth.create_user_with_email_and_password(email, password)

# Gửi email xác nhận
auth.send_email_verification(email)

# Đăng nhập
user = auth.sign_in_with_email_and_password(email, password)
print(user['localId'])

# Gửi email đặt lại mật khẩu
# auth.send_password_reset_email(email)

# Lấy user_id từ email (trong Realtime Database)
# user_id = next((id for id, data in db.child("users").get().val().items() if data["email"] == "docanhsm@gmail.com"), None)
# if user_id:
#     print("User ID is:", user_id)

# # Cập nhật thông tin người dùng
# user_id = '1'  # Thay thế bằng user_id chính xác
# data = {'email': 'docanhsm'}
# db.child('users').child(user_id).update(data)

# # Lấy thông tin người dùng từ Realtime Database
# user = db.child('users').child(user_id).get()
# print(user.val())  # OrderedDict([('email', 'docanhsm'), ('name', 'dat')])

# # In ra tên người dùng
# print(user.val()['email'])  # docanhsm