from .conftest import get_db

def populate_dashboard_users():
    with get_db() as cursor:
        cursor.execute("""
            INSERT INTO dashboard_users (username, email, password_hash, user_id, create_datetime) VALUES
            ('test_user', 't@gmail.com', '$2y$04$Lfxl0lAeEvh1/ek62Z81Yuaq7h.Qa2oGxh9l7uItscmkMGaDIon.C', '9fe2c4e93f654fdbb24c02b15259716c', NOW())
        """)

def populate_routine():
    with get_db() as cursor:
        cursor.execute("""
            INSERT INTO routine (name, description, create_datetime, modify_datetime) VALUES
            ('Test Routine', 'Just a test', NOW(), NOW()),
            ('Routine 2', 'Testing the routine', NOW(), NOW())
        """)

def populate_exercises():
    with get_db() as cursor:
        cursor.execute("""
            INSERT INTO exercises (name, is_unilateral, is_bodyweight, details) VALUES 
            ('Bench Press', 0, 1, '{}'),
            ('Pullup', 0, '1', '{}'),
            ('Meadows Row', 1, 0, '{}')
        """)

def populate_routine_map():
    with get_db() as cursor:
        cursor.execute("""
            INSERT INTO routine_user_map (routine_id, user_id, config) VALUES
            (1, 1, ''),
            (2, 1, '')
        """)

table_map = {
    'dashboard_users': populate_dashboard_users,
    'routine': populate_routine,
    'exercises': populate_exercises,
    'routine_map': populate_routine_map
}
def populate_tables(tables: list):
    for table in tables:
        table_map[table]()
