# Онлайн библиотека
Онлайн библиотека для хранения и чтения книг, созданная с использованием Python, Jinja2 и Bootstrap.

Сайт доступен по ссылке https://romigo24.github.io/online_library/pages/index.html
<img width="1582" height="897" alt="Снимок экрана 2025-10-24 в 23 24 54" src="https://github.com/user-attachments/assets/36fda52f-0c50-42e2-b33f-e41b2aefcac2" />

## 🌟 Особенности

- 📖 Удобный просмотр - книги отображаются в виде карточек с обложками

- 🔍 Постраничная навигация - разбивка на страницы по 20 книг

- 🏷️ Жанры книг - отображение жанров в виде бейджиков

- 📱 Адаптивный дизайн - корректное отображение на всех устройствах

- ⚡ Полностью оффлайн - все ресурсы загружаются локально

- 🌐 Публикация на GitHub Pages - автоматический деплой при обновлении

## 🛠 Технологии

- Backend: Python 3.8+

- Templates: Jinja2

- Frontend: Bootstrap 4.3

- Deployment: GitHub Pages

- Development: Livereload для горячей перезагрузки

## 🚀 Быстрый старт

1. Клонируйте репозиторий:
```bash
git clone https://github.com/romigo24/online-library.git
```

2. Установите зависимости:
```bash
pip install requirements.txt
```

3. Запустите генерацию сайта:
```bash
python render_website.py
```

4. Откройте в браузере http://127.0.0.1:5500/pages/index.html

## ⚙️ Настройки запуска

Программа поддерживает гибкую настройку через аргументы командной строки и переменные окружения.

### Аргументы командной строки

```bash
python render_website.py --data-path meta_data.json --template-path templates/template.html --output-dir pages --books-dir media/books --books-per-page 20
```

### Переменные окружения

```bash
export LIBRARY_DATA_PATH="meta_data.json"
export LIBRARY_TEMPLATE_PATH="templates/template.html"
export LIBRARY_OUTPUT_DIR="pages"
export LIBRARY_BOOKS_DIR="media/books"
export LIBRARY_BOOKS_PER_PAGE="20"
python render_website.py
```

### Параметры настройки
```
--data-path / LIBRARY_DATA_PATH - путь к файлу с метаданными книг (по умолчанию: meta_data.json)
--template-path / LIBRARY_TEMPLATE_PATH - путь к HTML шаблону (по умолчанию: templates/template.html)
--output-dir / LIBRARY_OUTPUT_DIR - папка для сгенерированных страниц (по умолчанию: pages)
--books-dir / LIBRARY_BOOKS_DIR - папка с текстами книг (по умолчанию: media/books)
--books-per-page / LIBRARY_BOOKS_PER_PAGE - количество книг на странице (по умолчанию: 20)
```
## 📊 Функциональность

### Генерация сайта

- Автоматическое создание HTML-страниц из JSON данных
- Разбивка книг на страницы (по 20 на страницу)
- Генерация правильных относительных путей
### Пользовательский интерфейс

- Адаптивная сетка карточек книг
- Пагинация с навигацией "Назад/Вперед"
- Отображение жанров в виде бейджиков
- Кнопки "Читать" для открытия текстов книг

### Оптимизация

- Локальное хранение Bootstrap ресурсов
- Поддержка оффлайн-режима
- Валидная HTML-разметка
- Оптимизированные изображения

## 🔧 Настройка

### Добавление новых книг

1. Добавьте текстовые файлы книг в books/books/

2. Добавьте обложки в books/img/

3. Обновите books/meta_data.json с информацией о новых книгах

4. Запустите python render_website.py

### Изменение дизайна

Отредактируйте templates/template.html для изменения:

- Макета страницы
- Стилей Bootstrap
- Структуры карточек книг
- Пагинации

### Настройка пагинации

В render_website.py измените:
```python
books_per_page = 20  # Количество книг на странице
```

# Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
