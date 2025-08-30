from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Dummy database (in-memory)
books = [
    {"id": uuid.uuid4().hex[:16], "title": "Python Basics", "author": "John"},
    {"id": uuid.uuid4().hex[:16], "title": "Flask Guide", "author": "Alice"}
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get single book
@app.route('/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    return jsonify(book) if book else ({"error": "Book not found"}, 404)

# Add a book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book["id"] = uuid.uuid4().hex[:16]   # Generate 16-char UUID
    books.append(new_book)
    return jsonify(new_book), 201

# Update a book
@app.route('/books/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    else:
        return {"error": "Book not found"}, 404

# Delete a book
@app.route('/books/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return {"message": "Book deleted"}, 200

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
# # Dummy database (in-memory)
# books = [
#     {"id": 1, "title": "Python Basics", "author": "John"},
#     {"id": 2, "title": "Flask Guide", "author": "Alice"}
# ]
#
# # Get all books
# @app.route('/books', methods=['GET'])
# def get_books():
#     return jsonify(books)
#
# # Get single book
# @app.route('/books/<int:book_id>', methods=['GET'])
# def get_book(book_id):
#     book = next((b for b in books if b["id"] == book_id), None)
#     return jsonify(book) if book else ({"error": "Book not found"}, 404)
#
# # Add a book
# @app.route('/books', methods=['POST'])
# def add_book():
#     new_book = request.get_json()
#     new_book["id"] = max([b["id"] for b in books], default=0) + 1
#     books.append(new_book)
#     return jsonify(new_book), 201
#
# # Update a book
# @app.route('/books/<int:book_id>', methods=['PUT'])
# def update_book(book_id):
#     book = next((b for b in books if b["id"] == book_id), None)
#     if book:
#         data = request.get_json()
#         book.update(data)
#         return jsonify(book)
#     else:
#         return {"error": "Book not found"}, 404
#
# # Delete a book
# @app.route('/books/<int:book_id>', methods=['DELETE'])
# def delete_book(book_id):
#     global books
#     books = [b for b in books if b["id"] != book_id]
#     return {"message": "Book deleted"}, 200
#
# if __name__ == '__main__':
#     app.run(debug=True)
