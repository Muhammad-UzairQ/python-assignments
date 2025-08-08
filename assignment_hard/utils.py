import csv

def compare_list(original_list,guessed_list, guessed_char):
    for i in range(0, len(original_list)):
        if original_list[i] == guessed_char:
            original_list[i] = "_"
            guessed_list[i] = guessed_char
            return original_list, guessed_list, True
    return original_list, guessed_list, False


def get_list_from_file(file_name):
    with open(f'../files/{file_name}', 'r', newline='') as file:
        # Create a csv.reader object
        reader = csv.reader(file)
        # Optionally, skip the header row if present
        header = next(reader)
        # print(f"Header: {header}")
        # Iterate over each row in the CSV file
        words_list = []
        for row in reader:
            words_list.append(row[0])
    return words_list