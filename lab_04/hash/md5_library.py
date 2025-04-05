<<<<<<< HEAD
import hashlib

def calculate_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_string = input("Nhập chuỗi cần băm: ")
md5_hash = calculate_md5(input_string)

print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))
=======
import hashlib

def calculate_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_string = input("Nhập chuỗi cần băm: ")
md5_hash = calculate_md5(input_string)

print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))
>>>>>>> 7643494659739fc8d5214eb15562c4496023e197
