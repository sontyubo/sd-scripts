from pathlib import Path
from argparse import ArgumentParser

NG_WORDS = [
    "japanese_clothes",
    "sword",
    "kimono",
    "sandals",
    "hakama",
    "hakama_skirt",
    "haori",
    "fake_screenshot",
    # --- 新規 ---
    "skirt",
    "black_hakama",
    "green_kimono",
]


def read_textfile(file_path: str) -> str:
    with open(f"{file_path}", "r", encoding="utf-8") as f:
        content = f.read()
    return content


def remove_tags(tags: str) -> str:
    tags_list = [tag.strip() for tag in tags.split(",")]
    removed_tags = [tag for tag in tags_list if tag not in NG_WORDS]
    return ", ".join(removed_tags)


def normalize_text_file(file_path: str) -> None:
    text_file_path = Path(file_path)
    tags_text = read_textfile(text_file_path)
    removed_tags_text = remove_tags(tags_text)
    text_file_path.write_text(removed_tags_text, encoding="utf-8")  # ファイルに保存


def normalize_text_directory(text_dir_path: str) -> None:
    dir_path = Path(text_dir_path)
    for text_file_path in dir_path.glob("*.txt"):
        normalize_text_file(text_file_path)


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--dataset-dir", "-d", required=True, type=str, help="画像ディレクトリを指定"
    )
    args = parser.parse_args()

    normalize_text_directory(args.dataset_dir)


if __name__ == "__main__":
    main()
