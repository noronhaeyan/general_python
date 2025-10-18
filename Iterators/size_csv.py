import os

file_path = 'code/general_python/Iterators/techcrunch.csv'
file_size = os.path.getsize(file_path)

print(f"Size of {file_path}: {file_size} bytes")
print(f"Size of {file_path}: {file_size / 1024:.2f} KB")
print(f"Size of {file_path}: {file_size / (1024 * 1024):.2f} MB")