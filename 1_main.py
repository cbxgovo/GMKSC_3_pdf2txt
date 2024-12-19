import os
import subprocess
"""
检查pdf1将要执行的指令  该即将处理的pdf文件夹是否已经存在于输出目录中，如果存在那么跳过 不存在那么执行解析命令
可能的问题：大写PDF结尾需要改成小写才能识别
            部分硕士论文和其他pdf文件 因为太长哈还是什么转化失败没有md文件 需要WPS转成图片pdf重新运行
"""
# 定义PDF文件目录
# pdf_directory = "pdf1" # pdf输入
pdf_directory = "all_tushu/pdf" # pdf输入
output_directory = "all_tushu/output/magic-pdf" # 每次执行前在这个输出目录下检查是否已经有解析过的文件夹  有的话就跳过
# output_directory = "all/pdf_output" 

# 初始化计数器
existing_folders_count = 0

# 遍历目录中的所有文件
for filename in os.listdir(pdf_directory):
    # 检查文件扩展名是否为PDF
    if filename.endswith(".pdf"):
        folder_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_directory, folder_name)
        # 检查文件夹是否已经存在于输出目录中  有时候中断了避免重现进行转换浪费时间
        if os.path.exists(output_path):
            print(f"Folder {folder_name} already exists in the output directory. Skipping.")
            existing_folders_count += 1
            continue

        pdf_path = os.path.join(pdf_directory, filename)
        # 定义要执行的命令
        command = [
            "magic-pdf", 
            "pdf-command", 
            "--pdf", pdf_path, 
            "--inside_model", "true", 
            "--model_mode", "lite"  # :"full"全精度 慢
        ]
        # 打印命令（可选）
        print(f"Executing: {' '.join(command)}")
        # 执行命令
        subprocess.run(command)

print("All PDF files have been processed.")
print(f"Number of existing folders skipped: {existing_folders_count}")
