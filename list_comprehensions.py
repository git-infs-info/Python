Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> even_numbers = [x for x in range(1,101)if x % 2 == 0]
>>> print(even_numbers)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50,
 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> 
>>> odd_numbers = [x for x in range(1,101) if x % 2 != 0]
>>> print(odd_numbers)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51,
 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> 
>>> words = ["the", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
>>> answer = [[w.upper(), w.lower(), len(w)] for w in words]
>>> print(answer)
[['THE', 'the', 3], ['BROWN', 'brown', 5], ['FOX', 'fox', 3], ['JUMPED', 'jumped', 6], ['OVER', 'over', 4],
 ['THE', 'the', 3], ['LAZY', 'lazy', 4], ['DOG', 'dog', 3]]
>>> 
