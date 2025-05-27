from lab7 import boyer_moore_search

def load_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def find_fraudulent_words(templates, messages):
    found_words = set()
    for template in templates:
        for msg in messages:
            if boyer_moore_search(msg.lower(), template.lower()):
                found_words.add(template)
                break
    return sorted(found_words)

if __name__ == "__main__":
    templates = load_lines("shablons.txt")
    messages = load_lines("sms.txt")

    suspicious_words = find_fraudulent_words(templates, messages)

    print(" Знайдені шахрайські слова:")
    if suspicious_words:
        for word in suspicious_words:
            print(f"! {word}")
    else:
        print("✅ Шахрайських слів не знайдено.")
