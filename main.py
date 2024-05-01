import os
from datetime import datetime

"""
前方部分一致でリネームできるようにしたい
B: typing-2021-0615-1234.png
A: typing_2021-0615-1234.png

入力してファイルの新しい名前を指定できるようにしたい
B: typing-2021-0615-1234.png
A: input()-2021-0615-1234.png
保存先のフォルダ変更機能を削除したい

"""


def truncate_string(input_string, length, append_string="..."):
    """文字列を指定した長さに切り詰め、必要に応じて文字を追加する"""
    if len(input_string) > length:
        return input_string[:length] + append_string
    else:
        return input_string


def get_files(src_folder, file_name):
    """指定したフォルダから指定した名前を含むファイルのリストを取得する"""
    files = [file for file in os.listdir(src_folder) if file_name in file]
    src_folder_display = truncate_string(src_folder, 20, "...")
    print(f"Found {len(files)} files containing '{file_name}' in {src_folder_display}.")
    return files


def rename_files(src_folder, files, new_file_prefix):
    """ファイルを新しい名前でリネームする"""
    for file in files:
        # ファイルのパスを作成
        src_path = os.path.join(src_folder, file)
        # ファイルの作成日時を取得
        creation_time = os.path.getctime(src_path)
        # ファイルの作成日時からファイル名を作成
        formatted_time = datetime.fromtimestamp(creation_time).strftime("%Y-%m%d-%H%M")

        new_file_name = f"{new_file_prefix}{formatted_time}.png"
        # 保存先ファイルのパスを作成
        dst_path = os.path.join(src_folder, new_file_name)

        # ファイルをリネーム
        os.replace(src_path, dst_path)
        # 20文字以上の場合は省略して表示
        src_folder_display = truncate_string(src_folder, 20, "...")
        print(
            f"Renamed file '{file}' to '{new_file_name}'. It is saved in '{src_folder_display}'."
        )


def main():
    print("Start file renaming process...")
    # ユーザーにフォルダパスを入力させる
    src_folder = input("Enter the 'path' to search: ")
    # ユーザーに検索ファイル名を入力させる
    file_name = input("Enter the 'file' to search: ")

    # スクリーンショットファイルのリストを取得
    screenshot_files = get_files(src_folder, file_name)

    # ユーザーに新しいファイル名を入力させる
    new_file_prefix = input("Enter the 'new file name' to rename: ")

    # スクリーンショットファイルをリネーム
    rename_files(src_folder, screenshot_files, new_file_prefix)
    print("File renaming process is complete.")


# このスクリプトを直接実行する場合にのみmain関数を呼び出す
if __name__ == "__main__":
    main()
