# 🧠 Quora Clone — Django Q&A App

A simple, functional **Quora-like Question & Answer web app**, built using Django.

Users can:
- 📝 Ask questions
- 💬 Post answers
- 👍 Like answers
- 🔐 Register & log in
- 📋 View recent questions

---

## 🚀 Features

- ✅ User authentication (login/logout)
- ✅ Post questions
- ✅ Answer questions
- ✅ Like answers (with "Like"/"Liked" toggle)
- ✅ Recent questions list
- ✅ Clean UI using Bootstrap
- ✅ CSRF protection & `@login_required` decorators

---

## 📸 Screenshots

_Add your screenshots here if needed_

---

## 🛠️ Tech Stack

- Python 3.8+
- Django 4.x
- SQLite (default)
- HTML + CSS + Bootstrap 5
- Django Templates

---

## 📁 Project Structure

quora_clone/ │ ├── project_name/ │ ├── settings.py │ ├── urls.py │ ├── app_name/ │ ├── models.py │ ├── views.py │ ├── urls.py │ ├── templates/ │ │ ├── home.html │ │ ├── question_detail.html │ │ ├── navbar.html │ ├── templates/ │ ├── base.html │ ├── login.html │ ├── static/ │ ├── db.sqlite3 ├── manage.py ├── requirements.txt └── README.md

🧪 Running Locally
Clone the repo

bash
Copy
Edit
git clone https://github.com/your-username/quora-clone.git
cd quora-clone
Create virtual environment

bash
Copy
Edit
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations

bash
Copy
Edit
python manage.py migrate
Create superuser (optional)

bash
Copy
Edit
python manage.py createsuperuser
Run the server

bash
Copy
Edit
python manage.py runserver
Visit in browser

cpp
Copy
Edit
http://127.0.0.1:8000/
📝 Future Improvements
Add comments to answers

Upvote/downvote system

REST API (Django REST Framework)

User profile pages

Rich text editor

