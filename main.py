#!./bin/python3.11

import akzeptor

def main():
    word = input("enter a word: ")
    allowed_signs = input("enter allowed signs: ")

    result = akzeptor.run(word, allowed_signs)

    print(result)

if __name__ == "__main__":
    main()
