if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    grades = sorted(set(score for name, score in students))
    second = grades[1]

    names = [name for name, score in students if score == second]

    names.sort()

    for name in names:
        print(name)
