import os
import shutil
"""
1.把提取过来的md文件【output\magic-pdf】移动到 【output\txt】 当中
2.有的没成功的或者没有md文件的要列个清单 写入output/no_md_files.log
3.把没有md文件的文件夹 也就是no_md_files.log中出现的名字 在output\magic-pdf中删除 无效文件夹

"""
# 把提取过来的md文件【9.1_MinerU\output\magic-pdf】移动到 【9.1_MinerU\output\txt】 当中
# 有的没成功的或者没有md文件的要列个清单 output/no_md_files.log
def process_md_files(source_directory, target_directory):
    # 创建目标目录和日志文件
    os.makedirs(target_directory, exist_ok=True)
    # 遍历源目录下的所有子文件夹
    for root, dirs, files in os.walk(source_directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            md_files = [f for f in os.listdir(dir_path) if f.endswith('.md')]

            if md_files:
                # 如果子文件夹中有.md文件，将其复制到目标目录，并更改后缀为.txt
                for md_file in md_files:
                    source_file_path = os.path.join(dir_path, md_file)
                    target_file_path = os.path.join(target_directory, md_file.replace('.md', '.txt'))
                    shutil.copyfile(source_file_path, target_file_path)
            else:
                pass

def find_missing_folders(source_directory, target_directory, log_file_path):
    # 获取目标目录中的所有txt文件名（不含扩展名）
    target_files = {os.path.splitext(f)[0] for f in os.listdir(target_directory) if f.endswith('.txt')}
    
    # 获取源目录中的所有子文件夹名
    source_folders = {dir_name for dir_name in os.listdir(source_directory) if os.path.isdir(os.path.join(source_directory, dir_name))}
    
    # 找到在源目录中有但在目标目录中没有对应.txt文件的文件夹
    missing_folders = source_folders - target_files
    
    # 写入日志文件
    with open(log_file_path, 'w', encoding='utf-8') as log_file:
        for folder_name in missing_folders:
            log_file.write(f"{folder_name}\n")

# 删除缺失文件夹
    for folder_name in missing_folders:
        folder_path = os.path.join(source_directory, folder_name)
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            print(f"Deleted folder: {folder_path}")

if __name__ == "__main__":
    source_directory = "all_tushu/output"  # 源目录路径
    target_directory = "all_tushu/outputxt"  # 目标目录路径
    log_file_path = "all_tushu"  # 日志文件路径

    process_md_files(source_directory, target_directory)
    find_missing_folders(source_directory, target_directory, log_file_path)
