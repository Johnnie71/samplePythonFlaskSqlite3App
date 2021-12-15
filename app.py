from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def db_connection(): ## creating the connection to the sql database
    connection = None
    try:
        connection = sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return connection

@app.route('/books', methods=["GET", "POST"])
def books():
    connection = db_connection()
    cursor = connection.cursor()

    if request.method == "GET":
        cursor = connection.execute('SELECT * FROM books')
        books = [
            dict(id=row[0], author=row[1], language=row[2], title=row[3])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)

    if request.method == "POST":
        print("get post req")
        new_author = request.form["author"]
        new_lang = request.form["language"]
        new_title = request.form["title"]
        sql = """INSERT INTO books (author, language, title) VALUES (?, ?, ?)"""
        cursor = cursor.execute(sql, (new_author, new_lang, new_title))
        connection.commit()
        return f"Book with the id: {cursor.lastrowid} created successfully"
    
@app.route("/book/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_book(id):
    connection = db_connection()
    cursor = connection.cursor()
    book = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM books WHERE id=?", (id))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something went wrong!", 404

    if request.method == "PUT":
        sql = """UPDATE book SET 
            title=?,
            author=?,
            language=? 
            WHERE id=?
        """
        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]
        updated_book = {
            "id": id,
            "author": author,
            "language": language,
            "title": title
        }
        connection.execute(sql, (title, author, language, id))
        connection.commit()
        return jsonify(updated_book)
    
    if request.method("DELETE"):
        sql = """ DELETE FROM book WHERE id=? """
        connection.execute(sql, (id))
        connection.commit()

@app.route('/')
def index():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)