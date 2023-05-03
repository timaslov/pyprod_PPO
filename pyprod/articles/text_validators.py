from django.conf import settings


def validate_text(text: str):
    banned_words_file_path = settings.BASE_DIR / "articles" / "banned_words.txt"
    with open(banned_words_file_path, "r") as file:
        for line in file:
            word = line.strip()
            if word in text:
                return False

    return True
