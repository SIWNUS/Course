# #bugged code
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #chek bugs with print. print every value.
# print(pages)
# print(word_per_page)

# #Now we know the bug is in word_per_page. The corrected code will be available below.

#corrected code
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) #The bug here was corrected
total_words = pages * word_per_page
print(total_words)
print(word_per_page) #our previous bug.