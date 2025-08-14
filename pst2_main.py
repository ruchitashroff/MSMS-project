# pst2_main.py - The Persistent Application

import json
import datetime

DATA_FILE = "msms.json"
app_data = {}  # This global dictionary will hold ALL our data.

# --- Core Persistence Engine ---
def load_data(path=DATA_FILE):
    """Loads all application data from a JSON file."""
    global app_data
    try:
        with open(path, 'r') as f:
            app_data = json.load(f)
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("Data file not found. Initializing with default structure.")
        app_data = {
            "students": [],
            "teachers": [],
            "attendance": [],
            "next_student_id": 1,
            "next_teacher_id": 1
        }
        
def save_data(path=DATA_FILE):
    """Saves all application data to a JSON file."""
    # Open the file at 'path' in write mode ('w').
    # Use json.dump() to write the global 'app_data' dictionary to the file.
    # Use the 'indent=4' argument in json.dump() to make the file readable.
    with open(path, 'w') as f:
        json.dump(app_data, f, indent=4)
    print("Data saved successfully.")
    
def reset_data(path=DATA_FILE):
    """Resets the application data to its default structure."""
    global app_data
    app_data = {
        "students": [],
        "teachers": [],
        "attendance": [],
        "next_student_id": 1,
        "next_teacher_id": 1
    }
    save_data(path)
    print("Data has been reset to default")
    
def preview_data(path=DATA_FILE):
    """Prints a preview of the current application data."""
    print("Current Application Data:")
    print(f"Students: {len(app_data['students'])}")
    print(f"Teachers: {len(app_data['teachers'])}")
    print(f"Attendance Records: {len(app_data['attendance'])}")
    
# --- Full CRUD for Core Data ---
# Note: We are now working with lists of dictionaries, not lists of objects.

def add_teacher(name, speciality):
    """Adds a teacher dictionary to the data store."""
    # Get the next teacher ID from app_data['next_teacher_id'].
    teacher_id = app_data['next_teacher_id']
    # Create a new teacher dictionary with 'id', 'name', and 'speciality' keys.
    new_teacher = {"id": teacher_id, "name": name, "speciality": speciality}
    # Append the new dictionary to the app_data['teachers'] list.
    app_data['teachers'].append(new_teacher)
    # Increment the 'next_teacher_id' in app_data.
    app_data['next_teacher_id'] += 1
    print(f"Core: Teacher '{name}' added.")
    
    # Take a teacher's ID and any number of keyword arguments and update their record.
def update_teacher(teacher_id, **fields):
    """Finds a teacher by ID and updates their data with provided fields."""
    # Loop through the app_data['teachers'] list.
    for teacher in app_data['teachers']:
        # If a teacher's 'id' matches teacher_id:
        if teacher['id'] == teacher_id:
            # Use the .update() method on the teacher dictionary to apply the 'fields'.
            teacher.update(fields)
            print(f"Teacher {teacher_id} updated.")
            return
    print(f"Error: Teacher with ID {teacher_id} not found.")
    
    # Remove a teacher by their ID.
def remove_teacher(teacher_id):
    """Removes a teacher from the data store."""
    # Find the teacher dictionary in app_data['teachers'] with the matching ID.
    for teacher in app_data['teachers']:
        if teacher['id'] == teacher_id:
            # Use the .remove() method on the list to delete it.
            app_data['teachers'].remove(teacher)
            print(f"Teacher {teacher_id} removed.")
            return
    print(f"Error: Teacher with ID {teacher_id} not found.")
    
    # Add a student to the data store.
def add_student(name, instrument):
    """Registers a new student and enrolls them in a course."""
    # Get the next student ID from app_data['next_student_id'].
    student_id = app_data['next_student_id']
    # Create a new student dictionary with 'id', 'name', and 'enrolled_in' keys.
    new_student = {"id": student_id, "name": name, "enrolled_in": [instrument]}
    # Append the new dictionary to the app_data['students'] list.
    app_data['students'].append(new_student)
    # Increment the 'next_student_id' in app_data.
    app_data['next_student_id'] += 1
    print(f"Core: Student '{name}' registered.")
    
#TODO: Update a student's record by their ID.
def update_student(student_id, **fields):
    """Finds a student by ID and updates their data with provided fields."""
    # Loop through the app_data['students'] list.
    for student in app_data['students']:
        # If a student's 'id' matches student_id:
        if student['id'] == student_id:
            # Use the .update() method on the student dictionary to apply the 'fields'.
            student.update(fields)
            print(f"Student {student_id} updated.")
            return
    print(f"Error: Student with ID {student_id} not found.")
    
#TODO: Remove a student by their ID.
def remove_student(student_id):
    """Removes a student from the data store."""
    # Find the student dictionary in app_data['students'] with the matching ID.
    found = False
    for student in app_data['students']:
        if student['id'] == student_id:
            # Use the .remove() method on the list to delete it.
            app_data['students'].remove(student)
            print(f"Student {student_id} removed.")
            found = True
            break # Exit the loop once the student is found and removed.
        if found:
            save_data() 
        else:
            print(f"Error: Student with ID {student_id} not found.")
    
#TODO: Implemeent a helper function to ensure user does not input empty strings and removes extra spaces so the user can try again.
def sanitize_input(input_string):
    """Sanitizes user input by stripping whitespace and checking for empty strings."""
    sanitized = input_string.strip()
    if not sanitized:
        print("Input cannot be empty. Please try again.")
        return None
    return sanitized

# --- New Receptionist Features ---

    # Create a new record in the attendance list when a student checks in with validation.
def check_in(student_id, course_id, timestamp=None):
    """Records a student's attendance for a course with validation."""
    student_exists = any(s['id'] == student_id for s in app_data['students'])
    if not student_exists:
        print(f"Error: Student with ID {student_id} does not exist.")
        return
    # If already checked in, do not allow duplicate check-ins.
    for record in app_data['attendance']:
        if record['student_id'] == student_id and record['course_id'] == course_id:
            print(f"Error: Student {student_id} is already checked into {course_id}.")
            return
    if timestamp is None:
        # Get the current time as a string using datetime.datetime.now().isoformat()
        timestamp = datetime.datetime.now().isoformat()
    
    # Create a check-in record dictionary.
    check_in_record = {
        "student_id": student_id,
        "course_id": course_id,
        "timestamp": timestamp
    }
    # Append this new record to the app_data['attendance'] list.
    app_data['attendance'].append(check_in_record)
    print(f"Receptionist: Student {student_id} checked into {course_id}.")
    
    # Implement a function to see all check-ins for a student.
def view_check_ins(student_id):
    """Prints all attendance records for a student."""
    records = [record for record in app_data['attendance'] if record['student_id'] == student_id]
    if not records:
        print(f"No attendance records found for student {student_id}.")
        return
    for r in records:
        # Print each record in a readable format.
        print(f"Course: {r['course_id']}, Timestamp: {r['timestamp']}")
        
    # Implement a function to find a student and write their details to a new text file.
def print_student_card(student_id):
    """Creates a text file badge for a student."""
    # Find the student dictionary in app_data['students'].
    student_to_print = None
    for s in app_data['students']:
        if s['id'] == student_id:
            student_to_print = s
            break
    
    if student_to_print:
        # Create a filename, e.g., f"{student_id}_card.txt".
        filename = f"{student_id}_card.txt"
        # Open the file in write mode ('w').
        with open(filename, 'w') as f:
            # Write the student's details to the file in a nice format.
            f.write("========================\n")
            f.write(f"  MUSIC SCHOOL ID BADGE\n")
            f.write("========================\n")
            f.write(f"ID: {student_to_print['id']}\n")
            f.write(f"Name: {student_to_print['name']}\n")
            f.write(f"Enrolled In: {', '.join(student_to_print.get('enrolled_in', []))}\n")
        print(f"Printed student card to {filename}.")
    else:
        print(f"Error: Could not print card, student {student_id} not found.")
    
    # --- Main Application Loop ---
def main():
    """Main function to run the MSMS application."""
    load_data()  # Load all data from file at startup.

    while True:
        # Includes PST1 features and new PST2 features in the main loop.
        print("\n===== MSMS v2 (Persistent) =====")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Update Teacher")
        print("4. Update Student")
        print("5. Remove Teacher")
        print("6. Remove Student")
        print("7. Check-in Student")
        print("8. Print Student Card")
        print("9. View Student Check-in")
        print("q. Quit and Save")
        
        choice = input("Enter your choice: ")
        
        made_change = False # A flag to track if we need to save
        
        if choice == '1':
            # Input student name and instrument, and call add_student.
            name = input("Enter student name: ") 
            instrument = input("Enter instrument: ")
            add_student(name, instrument)
            made_change = True
            
        elif choice == '2':
            # Input teacher name and speciality, then call the function add_teacher.
            name = input("Enter teacher name: ")
            speciality = input("Enter teacher speciality: ")
            add_teacher(name, speciality)
            made_change = True
            
        elif choice == '3':
            # Input teacher_id and specaility, then call update_teacher function.
            try:
                teacher_id = int(input("Enter teacher ID: "))
                new_speciality = input("Enter new speciality: ")
                update_teacher(teacher_id, speciality=new_speciality)
            except ValueError:
                print("invalid teacher ID")
                
        elif choice == '4':
            # Input student ID and instrument from the user to be updated, then call update_student function.
            try:
                student_id = int(input("Enter student ID: "))
                new_instrument = input("Enter new instrument: ")
                update_student(student_id, enrolled_in=[new_instrument])
            except ValueError:
                print("Invalid student ID")
                
        elif choice == '5':
            # Get teacher_id, then call remove_teacher().
            try:
                teacher_id = int(input("Enter teacher ID to remove: "))
                remove_teacher(teacher_id)
            except ValueError:
                print("Invalid teacher ID")

        elif choice == '6':
            #  Get student_id, then call remove_student().
            try:
                student_id = int(input("Enter student ID to remove: "))
                remove_student(student_id)
            except ValueError:
                print("Invalid student ID")

        elif choice == '7':
            # Get student_id and course_id from user, then call check_in().
            try:
                student_id = int(input("Enter student ID: "))
                course_id = input("Enter course ID: ")
                check_in(student_id, course_id)
            except ValueError:
                print("Invalid student ID")

        elif choice == '8':
            # Get student_id, then call print_student_card().
            try:
                student_id = int(input("Enter student ID: "))
                print_student_card(student_id)
            except ValueError:
                print("Invalid student ID")

        elif choice == '9':
            # Get student_id from user, then call view_check_ins().
            try:
                student_id = int(input("Enter student ID: "))
                view_check_ins(student_id)
            except ValueError:
                print("Invalid student ID")

        elif choice == 'q':
            print("Saving final changes and exiting")
            break
        else:
            print("Invalid choice. Please select from 1–10.")
            
            # Auto-save if changes were made
        if made_change:
            save_data()
            
# --- Program Start ---
if __name__ == "__main__":
    main()
    
                
            
            
            
    
            
            