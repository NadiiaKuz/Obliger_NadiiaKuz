books_by_Tolkien = ["The Hobbit", "Farmer Giles of Ham", "Lord of the Rings: The Fellowship of the Ring",
                    "Lord of the Rings: The Two Towers", "Lord of the Rings: The Return of the King",
                    "The Adventures of Tom Bombadil", "Tree and Leaf"]

lord_of_the_rings_books_1_way = []

books_to_find = "Lord of the Rings:"

for book in books_by_Tolkien:
    if (books_to_find in book):
        lord_of_the_rings_books_1_way.append(book)

print(lord_of_the_rings_books_1_way)

print("--------------------------------------------------------------------------")

lord_of_the_rings_books_2_way = []

for index in range(len(books_by_Tolkien)):
    if books_to_find in books_by_Tolkien[index]:
        lord_of_the_rings_books_2_way.append(books_by_Tolkien[index])

print(lord_of_the_rings_books_2_way)