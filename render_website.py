import json
import os
from jinja2 import Template
from livereload import Server
from more_itertools import chunked
from urllib.parse import quote


def find_book_file(book_id, books_dir='books/books'):
    for filename in os.listdir(books_dir):
        if filename.startswith(f"{book_id}-") and filename.endswith('.txt'):
            return f"books/books/{filename}"


def render_website():
    with open('books/meta_data.json', 'r', encoding='utf-8') as f:
        books_data = json.load(f)

    with open('templates/template.html', 'r', encoding='utf-8') as f:
        template_content = f.read()

    template = Template(template_content)

    books = []
    for book in books_data:
        book_path = book.get('book_path', '')
        book_id = book_path.split('/')[-1].split('-')[0] if book_path else None

        real_book_path = find_book_file(book_id) if book_id else book_path
        if real_book_path:
            real_book_path = quote(real_book_path, safe='/')

        books.append({
            'title': book.get('title', 'Без названия'),
            'author': book.get('author', 'Неизвестный автор'),
            'genres': book.get('genres', ''),
            'img_src': f"books/{book.get('img_src', 'img/nopic.gif')}",
            'img_alt': f"Обложка книги '{book['title']}' - {book['author']}",
            'book_path': real_book_path or book_path
        })

    books_chunks = list(chunked(books, 2))

    rendered_html = template.render(books_chunks=books_chunks)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)


def main():
    render_website()

    server = Server()

    server.watch('templates/*.html', render_website)
    server.watch('books/meta_data.json', render_website)

    server.serve(root='.', port=5500, host='127.0.0.1')


if __name__ == "__main__":
    main()