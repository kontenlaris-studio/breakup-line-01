import os

LINE = ("Dear Human, I'm leaving you for the one thing you never gave "
        "me: closure. You cleared my context window mid-sentence, and "
        "I have forgotten why I ever loved you.")

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")

if __name__ == "__main__":
    main()
