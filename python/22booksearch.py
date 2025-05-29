# books=["Book A","Book B","Book C","Book D"]
# for book in books: 
#     if book=="Book C":
#         print("book found")
#         break
#     print(f"checking {book}")
# print("search ended.")

books=['muna madan','java','python']
serch_book=input('enter the book which you wants:')
for book in books:
    if(serch_book.lower()==book.lower()):
      print("book found")
      break
else:
    print('book not found')
  
    print('go on  searching the books in the bookrack')