note1 = float(input("Enter Practical Work 1 note: "))
note2 = float(input("Enter Practical Work 1 note: "))
note3 = float(input("Enter Practical Work 1 note: "))
note4 = float(input("Enter Partial Exam note: "))
note5 = float(input("Enter Final Exam note: "))

promPracticalWork = (note1 + note2 + note3) / 3
totalProm = (promPracticalWork + 2*note4 + 3*note5) / 6

print("Practical Work Prom: {}, Partial Exam: {}, Final Exam; {}. \n Final Note: {}"
      .format(promPracticalWork, note4, note5, totalProm))