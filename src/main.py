from absPath import *

# Hàm nhận 2 tham số:
#   -tên folder chứa ảnh gốc
#   -tên folder chứa kết quả của ảnh được xử lý
#   -giá trị ngưỡng iso
def main():
    dictionaryImageSet = duplicate_folder_image("img","Rs", isoValue= 50)
    rename_file_in_folder("Rs",80)


if __name__ == "__main__":
    main()