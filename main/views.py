from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
import json
import os
from datetime import datetime


temp_users = []


# Функция для получения пути к файлу данных
def get_data_file_path():
    return os.path.join(os.path.dirname(__file__), '..', 'data', 'users.json')


# Функция для загрузки пользователей из файла
def load_users():
    file_path = get_data_file_path()
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []


# Функция для сохранения пользователей в файл
def save_users(users):
    file_path = get_data_file_path()
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(users, file, ensure_ascii=False, indent=2)


def list_users(request):
    users = load_users()

    # Рассчитываем статистику
    total_users = len(users)
    average_age = 0
    if users:
        total_age = sum(user.get('age', 0) for user in users)
        average_age = total_age / total_users

    return render(request, 'main/list_users.html', {
        'users': users,
        'total_users': total_users,
        'average_age': round(average_age, 1)
    })


def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        # Валидация
        if not name or not age or not email:
            messages.error(request, 'Все поля обязательны для заполнения!')
            return render(request, 'main/register.html')

        try:
            age = int(age)
        except ValueError:
            messages.error(request, 'Возраст должен быть числом!')
            return render(request, 'main/register.html')

        # Загружаем существующих пользователей
        users = load_users()

        # Создаем нового пользователя
        new_user = {
            'id': len(users) + 1,
            'name': name,
            'age': age,
            'email': email,
            'created_at': datetime.now().isoformat()
        }

        # Добавляем пользователя и сохраняем
        users.append(new_user)
        save_users(users)

        messages.success(request, f'Пользователь {name} успешно добавлен!')
        return redirect('list_users')  # Убедитесь, что это имя существует в urls.py

    return render(request, 'main/register.html')


def user_detail(request, user_id):
    users = load_users()
    user = None

    # Ищем пользователя по ID
    for u in users:
        if u.get('id') == user_id:
            user = u
            break

    if not user:
        from django.http import Http404
        raise Http404("Пользователь не найден")

    return render(request, 'main/user_detail.html', {'user': user})
def main(request):
    return render(request,'main/list.html')

def registration(request):
    return render(request,'main/reg.html')





def main_list(request):
    return render(request,'main/main_list.html')




def register(request):
    if request.method == 'POST':
        # логика регистрации
        messages.success(request, 'Пользователь успешно зарегистрирован!')
        return redirect('list_users')
    return render(request, 'main/register.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from datetime import datetime
import json
import os


# Функция для получения пути к файлу данных
def get_data_file_path():
    # Получаем базовую директорию проекта
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')

    # Создаем папку data, если она не существует
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    return os.path.join(data_dir, 'users.json')


# Функция для загрузки пользователей из файла
def load_users():
    file_path = get_data_file_path()

    # Если файл не существует, создаем его с пустым списком
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=2)
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            users = json.load(file)

            # === ВАЖНО: Преобразуем строки created_at в объекты datetime ===
            for user in users:
                if 'created_at' in user and isinstance(user['created_at'], str):
                    try:
                        # ISO формат: "2025-12-19T19:24:51.123456"
                        # Убираем микросекунды если они есть
                        date_str = user['created_at'].split('.')[0]  # Убираем .123456
                        user['created_at'] = datetime.fromisoformat(date_str)
                    except (ValueError, AttributeError):
                        # Если не получается преобразовать, оставляем строку
                        pass
            return users
    except (json.JSONDecodeError, FileNotFoundError):
        # Если файл поврежден, возвращаем пустой список
        return []


# Функция для сохранения пользователей в файл
def save_users(users):
    file_path = get_data_file_path()

    # Убедимся, что папка существует
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Перед сохранением преобразуем datetime обратно в строку
    users_to_save = []
    for user in users:
        user_copy = user.copy()  # Создаем копию, чтобы не менять исходный объект

        if 'created_at' in user_copy and isinstance(user_copy['created_at'], datetime):
            # Преобразуем datetime в строку ISO формата
            user_copy['created_at'] = user_copy['created_at'].isoformat()

        users_to_save.append(user_copy)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(users_to_save, file, ensure_ascii=False, indent=2)


# ==============================================
# ВИДЫ (VIEWS)
# ==============================================

def list_users(request):
    """
    Показать список всех пользователей
    """
    users = load_users()

    # Рассчитываем статистику
    total_users = len(users)
    average_age = 0
    min_age = None
    max_age = None

    if users:
        # Собираем все возраста
        ages = [user.get('age', 0) for user in users if user.get('age') is not None]

        if ages:  # Проверяем, что есть хотя бы один возраст
            total_age = sum(ages)
            average_age = total_age / len(ages)
            min_age = min(ages)
            max_age = max(ages)

    # Передаем данные в шаблон
    return render(request, 'main/list_users.html', {
        'users': users,
        'total_users': total_users,
        'average_age': round(average_age, 1) if average_age else 0,
        'min_age': min_age,
        'max_age': max_age
    })


def register_view(request):
    """
    Регистрация нового пользователя
    """
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name', '').strip()
        age = request.POST.get('age', '').strip()
        email = request.POST.get('email', '').strip()

        # Валидация
        if not name or not age or not email:
            messages.error(request, 'Все поля обязательны для заполнения!')
            return render(request, 'main/register.html')

        try:
            age = int(age)
            if age <= 0 or age > 150:
                messages.error(request, 'Возраст должен быть от 1 до 150 лет!')
                return render(request, 'main/register.html')
        except ValueError:
            messages.error(request, 'Возраст должен быть числом!')
            return render(request, 'main/register.html')

        # Загружаем существующих пользователей
        users = load_users()

        # Генерируем ID (максимальный существующий ID + 1)
        max_id = max([user.get('id', 0) for user in users], default=0)

        # Создаем нового пользователя с объектом datetime
        new_user = {
            'id': max_id + 1,
            'name': name,
            'age': age,
            'email': email,
            'created_at': datetime.now()  # Здесь уже объект datetime!
        }

        # Добавляем пользователя и сохраняем
        users.append(new_user)
        save_users(users)

        messages.success(request, f'✅ Пользователь "{name}" успешно добавлен!')
        return redirect('/list_users/')

    # Если GET запрос - просто показываем форму
    return render(request, 'main/register.html')


def user_detail(request, user_id):
    """
    Показать детальную информацию о пользователе
    """
    users = load_users()

    # Ищем пользователя по ID
    user = None
    for u in users:
        if u.get('id') == int(user_id):
            user = u
            break

    if not user:
        # Если пользователь не найден
        raise Http404("Пользователь не найден")

    # Передаем пользователя в шаблон
    return render(request, 'main/user_detail.html', {'user': user})
