import os
from datetime import datetime


"""文字列を指定した長さに切り詰め、必要に応じて文字を追加する"""


def truncate_string(input_string, length, append_string="..."):
    if len(input_string) > length:
        return input_string[:length] + append_string
    else:
        return input_string


"""指定パスから指定した名前を含むファイルのリストを取得する"""


def get_files(src_folder, file_name):
    files = [file for file in os.listdir(src_folder) if file_name in file]
    src_folder_display = truncate_string(src_folder, 20, "...")
    print(f"Found {len(files)} files containing '{file_name}' in {src_folder_display}.")
    return files


"""ファイルの作成日時を取得し、指定したフォーマットで返す"""


def get_formatted_time(src_path, file, date_format):
    src_path = os.path.join(src_path, file)
    creation_time = os.path.getctime(src_path)
    return datetime.fromtimestamp(creation_time).strftime(date_format)


"""ファイルを新しい名前でリネームする"""


def rename_files_with_timestamp(src_path, files, new_file_prefix):
    for file in files:
        # ファイルの作成日時を取得し、指定したフォーマットで返す
        formatted_time = get_formatted_time(src_path, file, "%Y-%m%d-%H%M%S")
        # 新しいファイル名を作成
        new_file_name = f"{new_file_prefix}{formatted_time}.png"

        # 現在のファイルのパスと名前を作成
        old_path_and_name = os.path.join(src_path, file)
        # 新規のファイルのパスと名前を作成
        new_path_and_name = os.path.join(src_path, new_file_name)

        # ファイルをリネーム
        os.replace(old_path_and_name, new_path_and_name)
        # 20文字以上の場合は省略して表示
        src_path_display = truncate_string(src_path, 20, "...")
        print(
            f"Renamed file '{file}' to '{new_file_name}'. It is saved in '{src_path_display}'."
        )


"""メイン関数"""


def main():
    print("Start file renaming process...")
    # ユーザーにフォルダパスを入力させる
    src_path = input("Enter the 'path' to search: ")
    # ユーザーに検索ファイル名を入力させる
    file_name = input("Enter the 'file' to search: ")

    # ファイルのリストを取得
    files = get_files(src_path, file_name)

    # ユーザーに新しいファイル名を入力させる
    new_file_prefix = input("Enter the 'new file prefix' to rename: ")

    # スクリーンショットファイルをリネーム
    rename_files_with_timestamp(src_path, files, new_file_prefix)
    print("File renaming process is complete.")


"""このスクリプトを直接実行する場合にのみmain関数を呼び出す"""
if __name__ == "__main__":
    main()
