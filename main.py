class Lesson:
    def __init__(self, title):
        self.title = title
        self.done = False

class Course:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, title):
        self.lessons.append(Lesson(title))

    def progress(self):
        done = sum(1 for l in self.lessons if l.done)
        return (done / len(self.lessons)) * 100 if self.lessons else 0

class Student:
    def __init__(self, name):
        self.courses = {}

    def join(self, course):
        self.courses[course.name] = course

    def mark_done(self, course_name, index):
        self.courses[course_name].lessons[index].done = True

def run():
    py = Course("Python")
    py.add_lesson("Variables")
    py.add_lesson("Loops")
    py.add_lesson("OOP")

    s = Student("Jahongir")
    s.join(py)

    while True:
        print("\n1. Progress\n2. Dars tugatish\n3. Chiqish")
        c = input("Tanlang: ")

        if c == "1":
            print("Progress:", s.courses["Python"].progress(), "%")
        elif c == "2":
            for i, l in enumerate(py.lessons):
                print(i+1, l.title, "✔" if l.done else "❌")
            s.mark_done("Python", int(input("Tanlang: ")) - 1)
        elif c == "3":
            break

run()
