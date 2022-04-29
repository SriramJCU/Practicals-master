from programming_languages import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [ruby, python, visual_basic]

dynamic_languages = []
for language in languages:
    if language.is_dynamic():
        dynamic_languages.append(language.name)

print("The dynamically typed languages are: ")
for language in dynamic_languages:
    print(language)