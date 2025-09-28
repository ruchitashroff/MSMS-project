# Music School Management System (MSMS)

A receptionist-facing **management system** for a music school, built with **Streamlit** for the GUI and a modular Python backend for business logic.  

This project was developed incrementally through PST tasks, with each fragment adding functionality to the system.

---

## Features

### **1. Receptionist Dashboard**
- Sidebar navigation for switching between pages:
  - Student Management
  - Daily Roster & Check-in
  - (Future) Payments  

### **2. Student Management Page**
- Search students by name.  
- Register new students (linked to instrument availability).  
- Edit student details (name, instruments).  
- Delete students.  
- View all enrolled students and their courses.  

### **3. Daily Roster & Check-in**
- Select a day to view scheduled lessons in a clean table.  
- Check-in students dynamically (with success/error feedback).  
- Attendance log for today, with course & time.  
- Export attendance as CSV.  
- Summary stats: scheduled, checked-in, pending.  

### **4. Backend Logic (app/schedule.py)**
- Add/find students, teachers, courses.  
- Enroll students and switch courses.  
- Handle attendance with duplicate prevention.  
- Save & load data from JSON.  

---

## How to Run

1. **Clone this repo** or download the project folder.  

2. **Create a virtual environment** (important, avoids system conflicts):
   cd PST4
   python3 -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows

3. **Install dependencies:**
    Copy code
    pip install streamlit pandas

4. **Run the app:**
    Copy code
    streamlit run main.py
    Open your browser at the link Streamlit provides (usually http://localhost:8501).

## How to Test
- **Student Registration:** Try adding a student. If no teacher covers the instrument, the system blocks registration.  
- **Search & Edit:** Search for a student, update their info, and confirm changes persist after refresh.  
- **Roster & Check-in:** Pick a day, check-in a student for a course, then see them in the attendance log.  
- **Persistence:** Quit and restart the app — data is saved in `data/msms.json`.  

## Design Choices & Assumptions
- **Streamlit for GUI**: Chosen for speed, interactivity, and easy receptionist workflow.  
- **JSON persistence**: Lightweight, human-readable, and avoids needing a full database at this stage.  
- **Single source of truth**: `ScheduleManager` controls all business logic to keep consistency across pages.  
- **Validation**: Prevents duplicate check-ins and invalid enrollments.  
- **Extensibility**: Future fragments (e.g., Payments) can be plugged into the GUI without rewriting the backend.  

## Future Extensions
- Payments & billing integration.  
- Teacher management dashboard.  
- Advanced attendance analytics (late arrivals, absentees).  
- Export to Excel/PDF reports.  
- Multi-user authentication for staff vs admin.  

