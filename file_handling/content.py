# # copy the content of one file to another file
# from pathlib import Path


# def copy_file(file1, file2):
#     base_dir = Path(__file__).resolve().parent
#     source = base_dir / file1
#     destination = base_dir / file2

#     with source.open("r") as f1:
#         with destination.open("w") as f2:
#             for line in f1:
#                 f2.write(line)


# copy_file("file1.txt", "file2.txt")

#create a program that reads a text file and counts the number of occurrences of specific word in it
def count_words(filename):
    word_count = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.strip().lower()
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Example usage
filename = "sample.txt"
word_counts = count_words(filename)
for word, count in word_counts.items():
    print(f"{word}: {count}")