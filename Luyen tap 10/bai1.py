import os

path = "d:\\music\\muabui.mp3"

def get_filename_with_ext(file_path):
    """Trích xuất tên tệp bao gồm cả phần mở rộng (vd: muabui.mp3)"""
    return os.path.basename(file_path)

def get_filename_without_ext(file_path):
    """Trích xuất chỉ tên bài hát (vd: muabui)"""
    filename_with_ext = os.path.basename(file_path)
    return os.path.splitext(filename_with_ext)[0]

print(f"Tên đầy đủ: {get_filename_with_ext(path)}")
print(f"Tên bài hát: {get_filename_without_ext(path)}")
