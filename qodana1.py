def calculate_gpa(grades):
    # 학점별 점수 매핑
    grade_dict = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

    total_point = 0
    total_credits = 0

    for grade, credit in grades:
        # 학점에 따른 점수를 가져와서 학점 수와 곱함
        point = grade_dict[grade.upper()] * credit
        total_point += point
        total_credits += credit

    # 총 점수를 총 학점수로 나눠서 평균 점수(학점) 계산
    gpa = total_point / total_credits

    return gpa

# 학점과 학점 수의 리스트
grades = [('A', 3), ('B', 3), ('C', 2), ('D', 1), ('F', 1)]

gpa = calculate_gpa(grades)
print(f"GPA: {gpa:.2f}")