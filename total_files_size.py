# total_files_size
"""
Count total size of files in dir
"""

import os


total_size = 0
os_path = '/home/alex/dev/news'
if os.path.exists(os_path):
    for file in os.listdir(os_path):
        print(os.path.join(os_path, file))
        total_size += os.path.getsize(os.path.join(os_path, file))
    print('-'*30)
    print(f'Total files size in /home/dev/news = {total_size}kB')
else:
    print('Path does not exist')
