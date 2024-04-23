from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


create_students_table = """
CREATE TABLE students (
    student_id int PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email text,
    enrollment_year integer
)
"""

insert_student = """
INSERT INTO students 
    (first_name, last_name, email, enrollment_year) 
    values ('Dove', 'Nelson', 'dovehansen@yahoo.com', 2024)
"""


# *** Same as using with but with is better as it will automatically close the file
        # conn = engine.connect()
        # conn.close()
with engine.connect() as conn:
    conn.execute(text(create_students_table))
    conn.execute(text(insert_student))
    conn.commit()
    result = conn.execute(text("select * from students"))
    conn.commit()
    print(result.all())