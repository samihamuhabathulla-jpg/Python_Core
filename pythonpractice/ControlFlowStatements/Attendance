held = int(input("Enter number of classes held: "))
attended = int(input("Enter number of classes attended: "))
attendance_percentage = (attended / held) * 100
if attendance_percentage >= 75:
    print(f"{int(attendance_percentage)}% Allowed")
else:
    medical_cause = input("Do you have a medical cause? (Y/N): ")
    if medical_cause == 'Y':
        print(f"{int(attendance_percentage)}% Allowed")
    else:
        print(f"{int(attendance_percentage)}% Not allowed")