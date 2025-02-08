# TaskFlow - Task Manager Web App

As a software engineer, I am always seeking ways to expand my knowledge and experience in web development. This project involved developing a **Task Manager Web App** using the **Django Framework**.

The purpose of this application is to help users manage everyday tasks more effectively. With **TaskFlow**, users can create tasks and task lists while interacting with an intuitive, user-friendly interface.

## [Click Me to Visit The Live Website](https://hideously-pleased-puma.ngrok-free.app)



---

## 🚀 Getting Started

### **Quick Setup (Experienced Users)**

```sh
# Clone the repository
git clone https://github.com/Evankemp07/taskmanager.git
cd taskflow

# (Optional) Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate    # For Windows

# Install Required Dependencies
pip install -r requirements.txt

# Apply Migrations
python manage.py makemigrations tasks
python manage.py migrate

# Start the Django Server
python manage.py runserver
```

---

## **Setting Up a Virtual Environment (Recommended but Optional)**

### **1️⃣ (Optional) Create a Virtual Environment**

Run the following command inside your project directory:

```sh
python3 -m venv venv
```

This will create a virtual environment named **`venv`**.

### **2️⃣ (Optional) Activate the Virtual Environment**

- **For Linux/macOS:**
  ```sh
  source venv/bin/activate
  ```
- **For Windows (Command Prompt):**
  ```sh
  venv\Scripts\activate
  ```

After activation, your terminal should show `(venv)` at the beginning of the command line.

### **3️⃣ Install Required Dependencies**

Ensure your virtual environment is activated (if using one) before running:

```sh
pip install -r requirements.txt
```

### **4️⃣ Start the Django Server**

Run the following command to start the test server and create a superuser:

```sh
python manage.py createsuperuser
python manage.py makemigrations tasks
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Then, open a web browser and go to [**http://127.0.0.1:8000/**]() to access the main page of the application.

---

## 🎯 **Project Goals**

This project was developed to strengthen my skills in **full-stack web development**. My main focus areas include:

- **User Authentication & User Management**
- **PWA (Progressive Web App) Features for Mobile Compatibility**
- **Task & List Management System**

🎥 **Watch the Demo Video:** [Click here](https://vimeo.com/1054355840?share=copy) to see TaskFlow in action!

---

## 📌 Web Pages Overview

### **1️⃣ Home Page (/home/)**

- Displays all **task lists** created by the user.
- Allows users to **edit or delete** task lists via a modal.
- Users can mark tasks as **completed** or **edit them**.
- Button to **create a new task list** in a modal popup.

### **2️⃣ Login Page (/accounts/login/)**

- Users enter their **username** and **password** to log in.
- Includes a **spinner** for a smoother user experience.
- Redirects users to the **home page** upon successful login.

### **3️⃣ Register Page (/accounts/register/)**

- New users can create an account by entering a **username** and **password**.
- Registration form includes **password validation**.
- Redirects users to the login page upon successful registration.

### **4️⃣ Task Management (/task_lists/****/add_task/)**

- Users can **add new tasks** to a task list.
- Tasks can be **edited** or **marked as completed**.

### **5️⃣ Logout Page (/accounts/logout/)**

- Redirects users to a **logged-out page** after logging out.

---

## 🛠 **Development Environment**

- **Operating System** : Raspberry Pi OS Lite / Linux
- **Programming Language** : **Python 3.10.11**
- **Development Framework** : **Django 5.1.6**
- **Frontend** :  **Bootstrap 5.3.0** , HTML, CSS
- **Database** : **SQLite 3.22.0**
- **Tools Used** :
  - **Visual Studio Code** (Code Editor)
  - **Ngrok** (v3.4.2 – For external access testing)
  - **Django Admin Panel** (For managing users and tasks)
  - **Nginx Proxy Manager** (v2.10.3 – For routing traffic and serving assets)

---

## 📚 **Libraries Used**

- **Django** – **5.1.6** (Core web framework)
- **Django-PWA** – **2.0.1** (PWA integration)
- **Bootstrap** – **5.3.0** (Responsive design)
- **SQLite** – **3.22.0** (Lightweight database for development)

---

## 🔗 Useful Resources

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Bootstrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Django-PWA Setup](https://github.com/silviolleite/django-pwa)
- [RealFaviconGenerator](https://realfavicongenerator.net/) - For favicon and PWA icons

---

## 🚀 Future Work

✅ **Optimize PWA Experience** – Improve caching strategies to allow offline use.
✅ **Improve UI & UX** – Enhance transitions and make it fully responsive for mobile users.
✅ **Enhance Performance** – Reduce login times and optimize database queries.
✅ **Implement User Roles & Permissions** – Allow different access levels for managing tasks.

---

**📌 If you find this project useful, consider giving it a ⭐ on GitHub!**
