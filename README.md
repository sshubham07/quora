# Quora Clone — Django Q&A App

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
- ✅ CSRF protection & \`@login_required\` decorators


## 🧪 Running Locally

1. **Clone the repo**

    git clone https://github.com/your-username/quora-clone.git  
    cd quora

3. **Create virtual environment**

    python -m venv env  
    source env/bin/activate  

4. **Install dependencies**

    pip install -r requirements.txt

5. **Apply migrations**

    python manage.py migrate

6. **Create superuser (optional)**

    python manage.py createsuperuser

7. **Run the server**

    python manage.py runserver

8. **Visit in browser**

    http://127.0.0.1:8000/

---

## 🧩 Models

### Question

    class Question(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)

### Answer

    class Answer(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
        content = models.TextField()
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)

### Like

    class Like(models.Model):
        answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='likes')
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)

        class Meta:
            unique_together = ('answer', 'user')

---

## 🔐 Authentication

- **Login:** /login/
- **Logout:** /logout/ (redirects to homepage)
- Pages like "Ask a Question" and "Answer" are protected with \`@login_required\`

---

## 📝 Future Improvements

- Add comments to answers
- Upvote/downvote system
- REST API (Django REST Framework)
- User profile pages
- Rich text editor

