import csv

with open('D:\\College Courses\\Software Development by Python\\M04\\M04ProgrammingAssignment\\Chapter 16\\books.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]
  
print(books)

#DictReader() did not handle the quotes and commas in the second book's title.
#It displays the title until the comma for the second title.