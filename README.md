# 🚀 SmartHire – AI Resume Screening System

SmartHire is a Django-based AI-powered resume screening and job application management system.  
It allows candidates to apply for jobs, upload resumes (PDF), and automatically calculates a match score based on required job skills.

Built with Django, MySQL, and Python.

---

## 📌 Features

- 👤 Custom User Authentication (Candidate / Recruiter)
- ✅ Admin Approval System for Recruiters
- 💼 Job Posting System
- 📄 Resume Upload (PDF)
- 🔎 Automatic Resume Text Extraction (PyPDF2)
- 🤖 AI-Based Match Score Calculation
- 📊 Candidate Ranking
- 🛠 Django Admin Panel Management
- 🔐 One Application Per Job Per Candidate (Unique Constraint)

---

## 🏗 Project Architecture

SmartHire contains 3 main Django applications:

### 1️⃣ Accounts App
Handles:
- Custom User Model (extends AbstractUser)
- Role-based system (Candidate / Recruiter)
- Recruiter approval logic
- Authentication

### 2️⃣ Jobs App
Handles:
- Job creation
- Job listing
- Application tracking
- Match score storage
- Unique application constraint

### 3️⃣ Matching App
Handles:
- Resume upload
- PDF text extraction
- AI keyword-based matching
- Resume storage
- Candidate ranking

---

## 🧠 How AI Matching Works

1. Recruiter adds required skills (comma-separated).
2. Candidate uploads resume (PDF).
3. System extracts text using PyPDF2.
4. Resume text is compared with job skills.
5. Match score is calculated:

```
Match Score = (Matched Keywords / Total Required Keywords) × 100
```

6. Score is stored in Application model.
7. Recruiter/Admin can view ranked candidates.

---

## 🛠 Tech Stack

- Python 3.11+
- Django 6.x
- MySQL
- PyPDF2
- scikit-learn (imported for future advanced matching)
- HTML, CSS
- Django Templates

---

## 🗄 Database Configuration

This project uses **MySQL**.

Example settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smarthire_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

# ⚙️ Installation Guide

Follow these steps to run the project locally.

---

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/smarthire.git
cd smarthire
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv myenv
```

Activate:

### Windows:
```bash
myenv\Scripts\activate
```

### Mac/Linux:
```bash
source myenv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install django
pip install mysqlclient
pip install PyPDF2
pip install scikit-learn
```

Or create a requirements file:

```bash
pip freeze > requirements.txt
```

Then future users can install using:

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create MySQL Database

Open MySQL:

```sql
CREATE DATABASE smarthire_db;
```

Make sure credentials in `settings.py` match your MySQL configuration.

---

## 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 7️⃣ Run Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin/
```

---

# 🔁 Project Flow

## 👨‍💼 Recruiter Flow

1. Register as Recruiter
2. Wait for Admin approval
3. Post jobs
4. View applications
5. View match scores

---

## 👩‍💻 Candidate Flow

1. Register as Candidate
2. Browse job list
3. Click Apply
4. Upload Resume (PDF)
5. System calculates match score
6. Application saved

---

## 🛡 Admin Flow

1. Approve recruiters
2. Manage users
3. Manage jobs
4. View resumes
5. View applications
6. Edit any database record

---

# 📂 Folder Structure

```
smarthire/
│
├── accounts/
├── jobs/
├── matching/
├── media/
├── static/
├── templates/
├── manage.py
└── README.md
```

---

# 🔐 Security Notes

Before deploying to production:

- Move SECRET_KEY to environment variable
- Set DEBUG = False
- Configure ALLOWED_HOSTS
- Use secure MySQL credentials

---

# 🚀 Future Improvements

- Implement TF-IDF & Cosine Similarity fully
- Add Resume Parsing (Skills Extraction)
- Add Email Notifications
- Add Dashboard Analytics
- Deploy on Render / AWS
- Add REST API (Django REST Framework)

---

# 📌 Learning Outcomes

This project demonstrates:

- Custom Django User Model
- Role-Based Authentication
- File Upload Handling
- PDF Text Extraction
- AI-Based Matching Logic
- MySQL Integration
- Django Admin Customization
- Model Relationships & Constraints

---

# 👨‍💻 Author

Developed by [vivek sai]

---

