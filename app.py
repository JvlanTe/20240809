import os
import shutil

folder_path = input("フォルダのパスを入力してください：")

if os.path.isdir(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            file_name, file_extension = os.path.splitext(item)

            if file_extension == "":
                file_extension = "no extension"
            else:
                file_extension = file_extension[1:]

                destination_folder = os.path.join(folder_path, file_extension)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.move(item_path, os.path.join(destination_folder, item))

print("ファイルの整理が完了しました。")
