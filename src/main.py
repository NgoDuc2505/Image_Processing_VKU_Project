from absPath import *

# Hàm nhận 2 tham số:
#   -tên folder chứa ảnh gốc
#   -tên folder chứa kết quả của ảnh được xử lý
#   -giá trị ngưỡng iso
def main():
    dictionaryImageSet = duplicate_folder_image("img","Result_collection", isoValue= 50)
    print("dictionaryImageSet: ",dictionaryImageSet)

if __name__ == "__main__":
    main()