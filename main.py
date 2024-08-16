
def count_words(file_contents):
    words = file_contents.split()
    nb = 0
    for word in words:
        nb += 1
    return nb

def count_characters(file_contents):
    nb = {}
    for c in file_contents.lower():
        if c not in nb: nb[c] = 0
        nb[c] += 1
    
    return nb

def sort_on(dict):
    return dict["num"]

def report(path_to_file, file_contents):
    result = [f"--- Begin report of {path_to_file} ---"]
    result.append(f"{count_words(file_contents)} words found in the document\n")

    list = []
    char = count_characters(file_contents)
    for c in char:
        if c.isalpha():
            list.append({'name': c, 'num': char[c]})
    
    list.sort(reverse=True, key=sort_on)
    for c in list:
        result.append(f"The '{c['name']}' character was found {c['num']} times")

    result.append("--- End report ---")

    for r in result:
        print(r)

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    
    #nb_words = count_words(file_contents)
    #nb_char = count_characters(file_contents)
    report(path_to_file, file_contents)

main()
