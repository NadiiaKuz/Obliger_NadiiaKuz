books_by_Tolkien = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers", "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]

# Skriv ut de to første og de to siste bøkene i listen
print(f"de to første bøkene: {books_by_Tolkien[:2]}")
print(f"de to siste bøkene: {books_by_Tolkien[-2:]}")

#Legg til to av bøkene som ble utgitt etter hans død
books_by_Tolkien.append("The Silmarillion")
books_by_Tolkien.append("Unfinished Tales")

#Legg til "Lord of the Rings: " foran de tre bøkene i trilogien
for book in range(2, 5):
    books_by_Tolkien[book] = "Lord of the Rings: " + books_by_Tolkien[book]

#Sorter lista og skriv den ut
print(sorted(books_by_Tolkien))