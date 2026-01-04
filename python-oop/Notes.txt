Put this in with the methods section

class Soldier:
    health = 100

    def take_damage(self, damage, multiplier):
        # "self" is dalinar in the first example
        #
        damage = damage * multiplier
        self.health -= damage

dalinar = Soldier()
# "damage" and "multiplier" are passed explicitly as arguments
# 20 and 2, respectively
# "dalinar" is passed implicitly as the first argument, "self"
dalinar.take_damage(20, 2)
print(dalinar.health)
# 60

adolin = Soldier()
# Again, "adolin" is passed implicitly as the first argument, "self"
# "damage" and "multiplier" are passed explicitly as arguments
adolin.take_damage(10, 3)
print(adolin.health)
# 70]

self. vs local variables in methods

Inside a method, you can use:

    Instance attributes (with self.): values that you want to persist on the object between method calls.
    Local variables (no self.): values that are only needed inside that one method call.

Rule of thumb:

    Use self.something only if:
        You need it in another method, or
        It represents part of the object’s ongoing state.

    Use plain names (no self.) for temporary, per-call values.


Put this in with OOP:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        new_books = []
        for lib_book in self.books:
            if lib_book.title != book.title or lib_book.author != book.author:
                new_books.append(lib_book)
        self.books = new_books

    def search_books(self, search_string):
        results = []
        for book in self.books:
            if (
                search_string.lower() in book.title.lower()
                or search_string.lower() in book.author.lower()
            ):
                results.append(book)
        return results

    self refers to “this specific object” (one particular Book or Library).
    Book and Library (the class names) are shared by all instances, so assigning to Book.title would overwrite it for every book.

Once you switched to self.title, self.author, self.books, etc., your design matched the assignment perfectly:

    add_book stores the given Book instance.
    remove_book builds a new list without the matching title/author.
    search_books does a case-insensitive search and returns the matching books.

Your latest output shows all the visible tests passing, so your implementation is working as intended.

Want to practice the idea? How would you explain, in your own words, the difference between self.title and Book.title?
Boots

self.title refers to the object being created. Whereas Book.title would be referring to the entire class, not on a per constructor basis.
Boots

Exactly right, nicely put.

    self.title: “the title of this particular Book instance.”
    Book.title: “a single title attribute shared by the whole Book class (and all instances, if they look it up there).”

That’s why for normal object data (like each book’s own title/author, or each library’s own name/books), we almost always use self.something.

Before we move on: do you feel clear on when to use self inside methods, or would you like to walk through one more quick example with a different kind of class?
Boots

I think I understand. OOP has always been a challenge for me. Something about how you have to think about it is difficult for some reason.
Boots

Totally fair. Many a wizard has bounced off OOP the first few times.

A mental trick that helps some folks:

    Think of a class as a blueprint: Book.
    Think of an instance as an actual object built from that blueprint: my_book = Book("Dune", "Herbert").
    Inside methods, self is just “the thing I’m currently working on.”

So when you write:

def __init__(self, title, author):
    self.title = title

you can literally read it as:
“Take the title that was passed in, and store it on this specific book.”

If you’d like, you can try sketching another tiny class (maybe Wizard with name and mana) and tell me:

    what its __init__ would take
    what you’d store on self

I won’t solve it for you, but I can sanity-check your thinking.
Boots

def init(self, name, mana):
self.name = name
self.mana = mana
Boots

Yes, that’s exactly the right shape.

If you read it aloud:

    “When creating a Wizard, I take name and mana…”
    “…and I store them on this particular wizard as self.name and self.mana.”

To cement it a bit more, here are two quick reflection questions:

    If you created two wizards:

    wiz1 = Wizard("Gandalf", 100)
    wiz2 = Wizard("Saruman", 50)

    What would wiz1.mana and wiz2.mana be?

    If, inside __init__, you had written Wizard.mana = mana instead of self.mana = mana, what strange thing would happen when you created multiple wizards?

If you answer those, you’re really locking in the instance-vs-class idea.
Boots

wiz1 is Gandalf with 100 mana. wiz2 is Saruman with 50 mana. If Wizard.mana = mana, assuming that Gandalf was passed in first, then all Wizard's would have 100 mana. If Saruman was passed in first, all wizards would have 50 mana.
Boots

You’ve got it exactly, apprentice.

    With self.mana, each wizard keeps their own mana: Gandalf 100, Saruman 50.
    With Wizard.mana, you’re overwriting one shared value on the class each time you construct a wizard, so they’d all appear to have whatever mana the last constructed wizard had.

That’s the core OOP mental model you need for this lesson:
“Use self. for data that belongs to this one object.”

You’ve already used it correctly in Book and Library, and your tests are passing. Nicely done staying with it even though OOP feels weird.

When you hit the next OOP lesson, pay special attention to:

    where self is used
    what data is stored on self
    and how methods read or update that data
