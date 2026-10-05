class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        for review in self.reviews:
            print(review)


book = Book("Atomic Habits", "James Clear")

book.add_review("Very useful book")
book.add_review("Easy to understand")
book.add_review("Highly recommended")

print("Title:", book.title)
print("Author:", book.author)

print("Number of reviews:", book.count_reviews())

print("Reviews:")
book.display_reviews()