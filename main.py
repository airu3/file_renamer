import os
from datetime import datetime


def get_files(src_folder, file_name):
    """指定したフォルダから指定した名前を含むファイルのリストを取得する"""
    files = [file for file in os.listdir(src_folder) if file_name in file]
    print(
        f"'{file_name}'を含むファイルを{len(files)}件、{src_folder}から見つけました。"
    )
    return files


def rename_files(src_folder, dst_folder, files):
    """ファイルを新しい名前でリネームする"""
    for file in files:
        # ファイルのパスを作成
        src_path = os.path.join(src_folder, file)
        # ファイルの作成日時を取得
        creation_time = os.path.getctime(src_path)
        # ファイルの作成日時からファイル名を作成
        formatted_time = datetime.fromtimestamp(creation_time).strftime(
            "typing-%Y-%m%d-%H%M"
        )

        counter = 1
        new_file_name = f"{formatted_time}.png"
        # 保存先ファイルのパスを作成
        dst_path = os.path.join(dst_folder, new_file_name)

        # 既に同名のファイルが存在する場合は、ファイル名に連番を付ける
        while os.path.exists(dst_path):
            new_file_name = f"{formatted_time} ({counter}).png"
            dst_path = os.path.join(dst_folder, new_file_name)
            counter += 1

        # ファイルをリネームして移動
        os.rename(src_path, dst_path)
        # 20文字以上の場合は省略して表示
        dst_folder_display = (
            (dst_folder[:20] + "...") if len(dst_folder) > 20 else dst_folder
        )
        print(
            f"ファイル'{file}'を'{new_file_name}'にリネームし、'{dst_folder_display}'に移動しました。"
        )


def main():
    print("ファイルのリネームを開始します。")
    # ユーザーにフォルダパスを入力させる
    src_folder = input("検索するフォルダパスを入力してください: ")

    # 保存先フォルダを指定
    dst_folder = src_folder

    # ユーザーに検索ファイル名を入力させる
    file_name = input("検索するファイル名を入力してください: ")

    # スクリーンショットファイルのリストを取得
    screenshot_files = get_files(src_folder, file_name)
    # スクリーンショットファイルをリネーム
    rename_files(src_folder, dst_folder, screenshot_files)
    print("処理が完了しました。")


# このスクリプトを直接実行する場合にのみmain関数を呼び出す
if __name__ == "__main__":
    main()
