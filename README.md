# 📚 KL Tech Digital Library

KL Tech Digital Library is a modern, easy-to-use web application built with **Django**, **Tailwind CSS**, and **Razorpay** to provide a seamless online platform for library management.

[![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)](https://github.com/yourusername/kltech-digital-library/commits/main)  
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 🛠️ Technologies Used

- ![Python](https://img.icons8.com/color/48/000000/python--v1.png) Python  
- ![Django](https://img.icons8.com/color/48/000000/django.png) Django  
- ![Tailwind CSS](https://img.icons8.com/color/48/000000/tailwind_css.png) Tailwind CSS  
- ![Razorpay](https://razorpay.com/assets/razorpay-icon.svg) Razorpay  
- HTML5, CSS3, JavaScript  

---

## 🚀 Features

### For Everyone
- Browse and search books by title, author, or category
- Sort books and authors alphabetically
- Responsive and clean user interface

### Student Features
- Secure login/signup
- Request to borrow books
- View current and past book issues with filtering options
- Track due dates and fines clearly
- Pay fines online via Razorpay

### Admin Features
- Admin dashboard to manage books, students, and issues
- Add, edit, delete books and authors
- Approve or reject book issue requests
- View, calculate, and manage fines
- Toggle fine payment status (online or cash)
- Search and filter students by department and fines
- View student login details and activity
- Reset passwords for users securely

---

## 📥 Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/kltech-digital-library.git

# 1. Navigate to the project folder
cd Django-librarymanagement-main

# 2. Activate the virtual environment
.\env\Scripts\activate    # For Windows
# source env/bin/activate  # For Linux/Mac

# 3. Upgrade setuptools (if not already installed)
pip install --upgrade setuptools

# 4. Install project dependencies
pip install -r requirements.txt

# 5. Apply database migrations
python manage.py migrate

# 6. Run the development server
python manage.py runserver
