import sys
text = open("sample.txt", "r") # Open the file in read mode
d = dict() # Creating empty dictionary
# reading the words in file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
    line = line.lower() # convert to lowercase to avoid case-sensitive mismatch
    words = line.split(" ") # Split the line into words
    for word in words:
        # if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            d[word] = 1 # Add the word to dictionary with count 1
# Print the contents of dictionary
sys.stdout = open("output.txt", "w")
for key in list(d.keys()):
    print(key, ":", d[key])