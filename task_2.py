def read_students(file_name):
    students = {}
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, scores_str = line.split(":")
            scores = list(map(int, scores_str.split(",")))
            students[name] = scores
    return students

def average_scores(students):
    return {name: sum(scores)/len(scores) for name, scores in students.items()}

def write_above_average(students_avg, threshold, file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        for name, avg in students_avg.items():
            if avg > threshold:
                f.write(f"{name}:{avg:.2f}\n")

def main():
    filename_input = "resource/students.txt"
    filename_output = "resource/result.txt"
    threshold = 4.0

    students = read_students(filename_input)
    students_avg = average_scores(students)

    write_above_average(students_avg, threshold, filename_output)

    if students_avg:
        top_student = max(students_avg.items(), key=lambda x: x[1])
        print(f"Студент с наивысшим средним баллом: {top_student[0]} - {top_student[1]:.2f}")
    else:
        print("Студенты не найдены")

if __name__ == "__main__":
    main()