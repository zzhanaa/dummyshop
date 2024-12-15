from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


# Fungsi untuk connect ke database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route ke halaman utama
@app.route('/')
def index():
    conn = get_db_connection()
    content = conn.execute('SELECT content_text FROM content WHERE section_name = "title"').fetchone()
    conn.close()
    return render_template('index.html', title=content['content_text'] if content else "Judul Default")

# Route untuk connect admin
@app.route('/admin')
def admin():
    return render_template('admin.html')

#  API untuk memperbarui konten
@app.route('/update-content', methods=['POST'])
def update_content():
    new_content = request.form.get('content')
    section_name = request.form.get('section')

    if not new_content or not section_name:
        return jsonify({"error": "Invalid Data"}), 400
    
    print(f"Section Name: {section_name}, New Content: {new_content}")  # Debugging
    
    conn = get_db_connection()
    conn.execute('UPDATE content SET content_text = ? WHERE section_name = ?', (new_content, section_name))
    conn.commit()
    conn.close()
    
    return jsonify({"massage": "Content updated successfully"})

if __name__ == '__main__':
    app.run(debug=True)