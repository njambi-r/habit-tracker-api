# habit-tracker-api
A Django-based Habit Tracker web application that helps users track their habits.

# 🚀 Features

🔐**User Authentication**
Register, log in, and manage your habits.

📆 **Habit Management**
Create, read, edit, delete, duplicate, mark complete, close, and reactivate habits.

🔎 **Search, Filter, and Sort Habits**
Filter Habits by Day, Week, Month, and Year

⏰ **Reminders**
Set custom reminder times for your habits. Automatically deactivate reminders when associated habit is marked as closed.

📊 **Analytics**
Track streaks and total completions.

🔁 **Auto-Reset Habit Completion Logic**
Habits reset based on frequency and completion status—automatically handled using lazy evaluation logic.

# 🛠️ Tech Stack
**Backend:** Django REST Framework

**Database:** SQLite for development

**Auth:** Token-based authentication via DRF

**Frontend:** Bring your own 

**Documentation:** Swagger/OpenAPI (drf-yasg)

# 🧪 API Endpoints
**Register**

POST *api/register/*    - Register new account

**Login**

POST *api/login/*   - Log into account

**Profile**

GET *api/profile/*  - View profile

PUT *api/profile/*  - Fully update profile

PATCH *api/profile/*    - Partially update profile

**Habits**

GET *api/habits/*   - View all habits

POST *api/habits/*  - Create habit

GET *api/habits/{id}/*  - Read specific habit

PUT *api/habits/{id}/*  - Update habit

PATCH *api/habits/{id}/*    - Partially update habit

DELETE *api/habits/{id}/*   - Delete habit

PATCH *api/habits/{id}/mark_closed/*    - Close habit

PATCH *api/habits/{id}/mark_complete/*  - Complete habit

PATCH *api/habits/{id}/reactivate_habit/*   - Reactivate a closed habit

GET *api/filter-habits/*    - filter habits by day, week, month, year, or custom dates

**Reminders**

GET *api/reminders/*    - List reminders

POST *api/reminders/*   - Create reminder

GET *api/reminders/{id}/*   - Read specific reminder

PUT *api/reminders/{id}/*   - Update reminder

PATCH *api/reminders/{id}/* - Partially update reminder

DELETE *api/reminders/{id}/*    - Delete reminder

PATCH *api/reminders/{id}/activate_reminder/*   - Activate inactive reminder

PATCH *api/reminders/{id}/deactivate_reminder/* - Deactivate active reminder

**Analytics**

GET *api/analytics/*    - List habit performance

GET *api/analytics/{id}/*   - List for specific habit

# 🚦 Getting Started
**1. Clone the repository**

git clone https://github.com/njambi-r/habit-tracker-api.git
cd habit_tracker

**2. Set up a virtual environment**

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate.ps1`

**3. Install dependencies**

pip install -r requirements.txt

**4. Run migrations**

python manage.py migrate

**5. Run the server**
python manage.py runserver

# 📝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

# 📃 License
MIT License © 2025 [Rose Kihungu]