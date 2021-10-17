tutors = [
    'Евгений', 'Алексей', 'Владимир', 'Вячеслав',
    'Василий', 'Мадлен', 'Анастасия', 'Анна'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б',
]


def gen_of_students():
    i = 0
    j = 0
    while i < len(tutors):
        if i >= len(klasses):
            yield (tutors[i], None)
            i += 1
            j += 1
            break
        else:
            yield (tutors[i], klasses[j])
            i += 1
            j += 1


for gen in gen_of_students():
    print(gen)