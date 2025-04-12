'''Create a function called word_intersection '''
def word_intersection():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    common_letters = set(word1) & set(word2)  # Find common letters using set intersection

    print("Common letters:", "".join(sorted(common_letters)) if common_letters else "None")

# Example usage
word_intersection()
