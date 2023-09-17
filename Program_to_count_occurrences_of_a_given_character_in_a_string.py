'''Program to count occurrences of a given character in a string.
  Count character 'e' in the below string.
	Input "geeksforgeeks".
	Output: 4

	Count character 'a' in the below string.
	Input "abccdefgaa."
	Output : 3'''
def main():
    s = input("Enter the string: ")
    c = input("Enter character to be searched: ")
    count = 0

    for i in range(len(s)):
        if s[i] == c:
            count += 1

    print(f"Character '{c}' occurs {count} times")

if __name__ == "__main__":
    main()
