#anagram means there are 2 words provided adn if one of them is restructure to form second if it is sucessfull then it is anagram 

string1 = input()
string2 = input()
if sorted(string1)==sorted(string2):
    print("The entered strngs are angrams")
else:
    print("entered string are not anagrams")    