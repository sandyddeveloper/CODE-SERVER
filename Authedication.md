
### Step 1: Create a New Django Project
1. Run the following commands to create a new project and app:
   ```bash
   django-admin startproject myproject
   cd myproject
   python manage.py startapp users
   ```

2. Add `users` to your `INSTALLED_APPS` in `myproject/settings.py`:
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'users',
   ]
   ```

---

### Step 2: Create Simple Views for Registration and Login
In `users/views.py`, write basic functions to handle user registration and login.

```python
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Registration View
def register_view(request):
    if request.method == 'POST':  # Check if the form is submitted
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:  # Check if passwords match
            User.objects.create_user(username=username, password=password)
            return redirect('login')  # Redirect to login page
        else:
            return render(request, 'users/register.html', {'error': 'Passwords do not match'})
    return render(request, 'users/register.html')

# Login View
def login_view(request):
    if request.method == 'POST':  # Check if the form is submitted
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:  # If authentication is successful
            login(request, user)
            return redirect('home')  # Redirect to home page
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')
```

---

### Step 3: Create Simple Templates
1. Create a folder `templates/users` inside the `users` app.
2. Add the following templates:

#### `register.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h2>Register</h2>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
    <form method="post">
        {% csrf_token %}
        <label>Username:</label>
        <input type="text" name="username" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <label>Confirm Password:</label>
        <input type="password" name="confirm_password" required><br>
        <button type="submit">Register</button>
    </form>
    <p>Already have an account? <a href="{% url 'login' %}">Login here</a></p>
</body>
</html>
```

#### `login.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
    <form method="post">
        {% csrf_token %}
        <label>Username:</label>
        <input type="text" name="username" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <button type="submit">Login</button>
    </form>
    <p>Don't have an account? <a href="{% url 'register' %}">Register here</a></p>
</body>
</html>
```

#### `home.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h2>Welcome, {{ request.user.username }}</h2>
    <a href="{% url 'logout' %}">Logout</a>
</body>
</html>
```

---

### Step 4: Create URL Patterns
1. In `users/urls.py`, define the routes:
   ```python
   from django.urls import path
   from .views import register_view, login_view, logout_view

   urlpatterns = [
       path('register/', register_view, name='register'),
       path('login/', login_view, name='login'),
       path('logout/', logout_view, name='logout'),
   ]
   ```

2. Include the app URLs in the main `urls.py`:
   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('users.urls')),  # Include the users app URLs
   ]
   ```

---

### Step 5: Set Up a Home View (Optional)
In `users/views.py`, add a simple home view:
```python
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect unauthenticated users to login
    return render(request, 'users/home.html')
```

Update `users/urls.py`:
```python
from .views import home_view

urlpatterns += [
    path('home/', home_view, name='home'),
]
```

---

### Step 6: Run the Application
1. Apply migrations:
   ```bash
   python manage.py migrate
   ```

2. Run the server:
   ```bash
   python manage.py runserver
   ```

