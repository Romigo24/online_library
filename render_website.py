import json
import os
import argparse
from jinja2 import Template
from livereload import Server
from more_itertools import chunked
from urllib.parse import quote


def get_config():
    parser = argparse.ArgumentParser(description='Генератор сайта библиотеки книг')

    parser.add_argument(
        '--data-path',
        default=os.getenv('LIBRARY_DATA_PATH', 'meta_data.json'),
        help='Путь к файлу с метаданными книг (переменная: LIBRARY_DATA_PATH)'
    )
    parser.add_argument(
        '--template-path',
        default=os.getenv('LIBRARY_TEMPLATE_PATH', 'templates/template.html'),
        help='Путь к шаблону HTML (переменная: LIBRARY_TEMPLATE_PATH)'
    )
    parser.add_argument(
        '--output-dir',
        default=os.getenv('LIBRARY_OUTPUT_DIR', 'pages'),
        help='Папка для сгенерированных страниц (переменная: LIBRARY_OUTPUT_DIR)'
    )
    parser.add_argument(
        '--books-dir',
        default=os.getenv('LIBRARY_BOOKS_DIR', 'media/books'),
        help='Папка с текстами книг (переменная: LIBRARY_BOOKS_DIR)'
    )
    parser.add_argument(
        '--books-per-page',
        type=int,
        default=int(os.getenv('LIBRARY_BOOKS_PER_PAGE', '20')),
        help='Количество книг на странице (переменная: LIBRARY_BOOKS_PER_PAGE)'
    )

    return parser.parse_args()


def find_book_file(book_id, books_dir):
    for filename in os.listdir(books_dir):
        if filename.startswith(f"{book_id}-") and filename.endswith('.txt'):
            return f"{books_dir}/{filename}"


def render_website():
    config = get_config()

    with open(config.data_path, 'r', encoding='utf-8') as f:
        books_data = json.load(f)

    with open(config.template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    template = Template(template_content)

    books = []
    for book in books_data:
        book_path = book.get('book_path', '')
        book_id = book_path.split('/')[-1].split('-')[0] if book_path else None

        real_book_path = find_book_file(book_id, config.books_dir) if book_id else book_path

        if real_book_path:
            path_parts = real_book_path.split('/')
            encoded_parts = []
            for part in path_parts:
                if '.' in part:
                    encoded_parts.append(quote(part))
                else:
                    encoded_parts.append(part)
            encoded_book_path = '/'.join(encoded_parts)
        else:
            encoded_book_path = ""

        books.append({
            'title': book.get('title', 'Без названия'),
            'author': book.get('author', 'Неизвестный автор'),
            'genres': book.get('genres', ''),
            'img_src': f"../media/{book.get('img_src', 'img/nopic.gif')}",
            'img_alt': f"Обложка книги '{book['title']}' - {book['author']}",
            'book_path': f"../{encoded_book_path}" if encoded_book_path else ""
        })

    books_pages = list(chunked(books, config.books_per_page))

    os.makedirs(config.output_dir, exist_ok=True)
    for page_num, page_books in enumerate(books_pages, 1):
        books_chunks = list(chunked(page_books, 2))

        rendered_html = template.render(
            books_chunks=books_chunks,
            current_page=page_num,
            total_pages=len(books_pages)
        )

        if page_num == 1:
            filename = 'index.html'
        else:
            filename = f'index{page_num}.html'

        with open(f'{config.output_dir}/{filename}', 'w', encoding='utf-8') as f:
            f.write(rendered_html)


def main():
    render_website()

    config = get_config()
    server = Server()

    server.watch(config.template_path, render_website)
    server.watch(config.data_path, render_website)

    server.serve(root='.', port=5500, host='127.0.0.1')


if __name__ == "__main__":
    main()