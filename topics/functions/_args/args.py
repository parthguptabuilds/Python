def calculate_total_marks(*args):
    total_marks=0
    for i in args:
        total_marks+=i
    print(total_marks)

calculate_total_marks(18,20,17,19)