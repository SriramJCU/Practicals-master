class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Initial Variables for the class"""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check whether the programming language is dynamically typed"""
        if self.typing.title() == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)