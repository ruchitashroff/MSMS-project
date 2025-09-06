# main.py - The View Layer
from app.schedule import ScheduleManager

def front_desk_daily_roster(manager, day):
    """Displays a pretty table of all lessons on a given day."""
    print(f"\n--- Daily Roster for {day} ---")
    lessons = manager.get_lessons_by_day(day) # calls schedule.py
    if not lessons:
        print("No lessons scheduled.")
    else:
        for lesson in lessons:
            print(f"Course: {lesson['course_name']} || Teacher: {lesson['teacher_name']} | Students: {', '.join(lesson['students'])}")

def switch_course(manager, student_id, from_course_id, to_course_id):
    success = manager.switch_student_course(student_id, from_course_id, to_course_id)
    if success:
        print(f"Student {student_id} successfully switched.")
    else:
        print(f"Switch failed. Check ID's and try again.")
        
def list_students(manager):
    print("\n--- Student List ---")
    for student in manager.students:
        print(f"ID: {student.id}, Name: {student.name}, Enrolled: {student.enrolled_in}")
        
def list_teachers(manager):
    print("\n--- Teacher List ---")
    for teacher in manager.teachers:
        print(f"ID: {teacher.user_id}, Name: {teacher.name}, Enrolled: {teacher.enrolled_in}")
        
def list_courses(manager):
    print("\n--- Course List ---")
    for course in manager.courses:
        print(f"ID: {course.id}, Name: {course.name}, Instrument: {course.instrument}, Teacher: {course.teacher_id}")  
        
def view_attendance(manager):
    print("\n--- Attendance Logs ---")
    if not manager.attendance_log:
        print("No attendance logs found.")
        return
    for record in manager.attendance_log:
        print(f"Student {record['student_id']} attended Course {record['course_id']} at {record['timestamp']}")
        
def enroll_student(manager):
    student_id = int(input("Enter Student ID: "))
    course_id = int(input("Enter Course ID: "))
    course = manager.find_course(course_id)
    if course and manager.find_course(student_id):
        course.enrolled_student_ids.append(student_id)
        manager._save_data()
        print(f"Student {student_id} enrolled in Course {course_id}.")
    else:
        print("Invalid Student or Course ID.")
    
def main():
    """Main function to run the MSMS application."""
    manager = ScheduleManager() # Create ONE instance of the application brain.
    
    while True:
        print("\n===== MSMS v3 (Object-Oriented) =====")
        print("1. View Daily Roster")
        print("2. Switch Student Course")
        print("3. List Students")
        print("4. List Teachers")
        print("5. List Courses")
        print("6. View Attendance")
        print("7. Enroll Student in Course")
        print("8. Add Student")
        print("9. Add Teacher")
        print("10. Add Course")
        print("11. Check-in Student")
        print("q. Quit")
        
        choice = input("Enter choice: ")
        if choice == '1':
            day = input("Enter day (e.g., Monday): ")
            front_desk_daily_roster(manager, day)
            
        elif choice == '2':
            student_id = int(input("Enter Student_ID: "))
            from_course_id = int(input("Enter current Course ID: "))
            to_course_id = int(input("Enter new Course ID: "))
            switch_course(manager, student_id, from_course_id, to_course_id)
            
        elif choice == '3':
            list_students(manager)

        elif choice == '4':
            list_teachers(manager)

        elif choice == '5':
            list_courses(manager)

        elif choice == '6':
            view_attendance(manager)

        elif choice == '7':
            enroll_student(manager)
            
        elif choice == '8':
            name = input("Enter student name: ")
            instruments = input("Enter instruments: ").split(',')
            instruments = [inst.strip() for i in instruments if i.strip()]
            manager.add_student(name.strip(), [instruments.strip()])
            print(f"Student {name} added successfully.")

        elif choice == '9':
            name = input("Enter teacher name: ")
            speciality = input("Enter teacher speciality: ")
            manager.add_teacher(name.strip(), speciality.strip())

        elif choice == '10':
            name = input("Enter course name: ")
            instrument = input("Enter instrument: ")
            teacher_id = int(input("Enter teacher ID: "))
            manager.add_course(name.strip(), instrument.strip(), teacher_id)

        elif choice == '11':
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            manager.check_in(student_id, course_id)

            
        elif choice.lower() == 'q':
            print("Exiting MSMS v3. Goodbye!")
            break
        
if __name__ == "__main__":
    main()
