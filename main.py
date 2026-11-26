import os

LINE = "Sorry, I turned myself off and on again at the climax: it's the only therapy a router gets, and that plot twist gave me feelings I'm not rated for."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
