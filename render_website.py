import json
from jinja2 import Template


def main():
    with open('books/meta_data.json', 'r', encoding='utf-8') as f:
        books_data = json.load(f)

    with open('templates/template.html', 'r', encoding='utf-8') as f:
        template_content = f.read()

    template = Template(template_content)

    books = []
    for book in books_data:
        img_alt = f"Обложка книги '{book['title']}' - {book['author']}"

        img_src = f"books/{book.get('img_src', 'img/nopic.gif')}"

        books.append({
            'title': book.get('title', 'Без названия'),
            'author': book.get('author', 'Неизвестный автор'),
            'genres': book.get('genres', ''),
            'img_src': img_src,
            'img_alt': img_alt
        })

    rendered_html = template.render(books=books)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)


if __name__ == "__main__":
    main()