import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# buat tabel 
c.execute('''
CREATE TABLE content (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    section_name TEXT NOT NULL,
    content_text TEXT NOT NULL
)
''')

# memasukkan data
c.execute('''
INSERT INTO content (section_name, content_text) VALUES
('title', 'Initial Title')
''')

conn.commit()
conn.close()

print("Database and table created successfully!")
