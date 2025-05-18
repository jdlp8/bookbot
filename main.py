def get_book_text(file_path):
	file_contents = ''
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

from stats import get_n_words

def main():
	franken_str = get_book_text("books/frankenstein.txt")
	n_w=0
	n_w= get_n_words(franken_str)
	#print(n_w)
	print(f"{n_w} words found in the document")

main()
