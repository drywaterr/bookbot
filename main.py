def main():
    text_path = "books/frankenstein.txt"
    text = get_book_text(text_path)
    print(generate_report(text, text_path))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def char_occurences(text):
    char_counts = {}
    for char in text.lower():
        if not char in char_counts.keys():
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def alpha_dictionary(dict):
    new_dict = {}
    for char in dict:
        if char.isalpha():
            new_dict[char] = dict[char]
    return new_dict

def sort_on(dict):
    return dict["num"]

def create_dict_list(dict):
    count_list = []
    for char in dict:
        count_list.append({char: dict[char], "num": dict[char], "char": char})
    return count_list

def generate_report(text, text_path):
    words = word_count(text)
    chars = char_occurences(text)
    alpha_dict = alpha_dictionary(chars)
    dict_list = create_dict_list(alpha_dict)
    
    report_str = f"--- Begin report of {text_path} ---\n {words} words found in the document"
    for dic in dict_list:
        report_str += f"\n '{dic["char"]}' occurs {dic["num"]} times"
    return report_str
main()