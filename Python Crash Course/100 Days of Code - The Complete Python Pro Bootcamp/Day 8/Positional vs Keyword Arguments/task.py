# Functions with input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Crawling back to {location} after your vacation, eh?")


# greet_with("Jack Bauer", "Toronto")


def calculate_love_score(name1="name1", name2="name2"):
    true = "true"
    love = "love"
    true_cnt = 0
    love_cnt = 0

    for letters in name1:
        for trues in true:
            if letters.lower() == trues:
                true_cnt += 1
        for loves in love:
            if letters.lower() == loves:
                love_cnt += 1

    for chars in name2:
        for trues in true:
            if chars.lower() == trues:
                true_cnt += 1
        for loves in love:
            if chars.lower() == loves:
                love_cnt += 1

    print(f"{true_cnt}{love_cnt}")


calculate_love_score("Shane", "Ainsley")