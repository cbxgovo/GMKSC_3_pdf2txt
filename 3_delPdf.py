import os
"""
    删除已经获取到解析结果的pdf  只保留还没获取到的pdf【output/magic-pdf已有的在pdf1文件夹删除对应pdf】
"""
def delete_matching_pdfs(base_dir):
    # 路径设置
    pdf1_dir = 'pdf1'
    output_dir = base_dir

    # 统计变量初始化
    found_count = 0
    not_found_count = 0

    # 遍历pdf1文件夹中的所有文件
    for file_name in os.listdir(pdf1_dir):
        if file_name.endswith('.pdf'):
            folder_name = file_name[:-4]  # 获取不带扩展名的文件名
            folder_path = os.path.join(output_dir, folder_name)
            pdf_path = os.path.join(pdf1_dir, file_name)

            if os.path.isdir(folder_path):
                os.remove(pdf_path)
                found_count += 1
                print(f"Deleted {pdf_path}")
            else:
                not_found_count += 1

    # 输出统计结果
    print(f"Found and deleted: {found_count}")
    print(f"Not found: {not_found_count}")

# 主函数
if __name__ == "__main__":
    base_directory = "output/magic-pdf"  # 根据需要修改路径
    delete_matching_pdfs(base_directory)
