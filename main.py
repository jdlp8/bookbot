import sys

def get_book_text(file_path):
	file_contents = ''
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

from stats import get_n_words
from stats import get_n_chars
from stats import lists_dicts

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_str = get_book_text(sys.argv[1])
	n_w = 0
	n_w = get_n_words(book_str)
	n_c = get_n_chars(book_str)
	res = lists_dicts(n_c)
	#print(n_c)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {n_w} total words")
	print("--------- Character Count -------")
	for dict in res:
		if dict["char"].isalpha() == True:
			print(f'{dict["char"]}: {dict["num"]}')
	print("============= END ===============")

main()
