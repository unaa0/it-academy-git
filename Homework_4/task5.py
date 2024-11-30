def students_languages(n):
    for val in range(n):
        languages_num = int(input("Сколько языков знает школьник?: "))
        languages = []
        for num in range(languages_num):
            language = input("Введите какие языки школьник знает: ")
            languages.append(language)
        yield languages


def organize_languages(given_languages):

    known_by_all = []

    for student_langs in given_languages:
        if not known_by_all:
            for lang in student_langs:
                known_by_all.append(lang)
        else:
            temp_list = []
            for lang in known_by_all:
                if lang in student_langs:
                    temp_list.append(lang)
            known_by_all = temp_list

    known_by_at_least_one = []
    for student_langs in given_languages:
        for lang in student_langs:
            if lang not in known_by_at_least_one:
                known_by_at_least_one.append(lang)

    return known_by_all, known_by_at_least_one


total_students = int(input("Количество учеников: "))
languages_known = list(students_languages(total_students))

all_, at_least_one = organize_languages(languages_known)

print("Языки, которые знают все ученики: ")
for a in all_:
    print(a)

print("Языки, которые знает хотя бы один ученик: ")
for o in at_least_one:
    print(o)