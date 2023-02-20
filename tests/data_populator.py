from .conftest import get_db

def populate_dashboard_users():
    with get_db() as cursor:
        cursor.execute("""
            INSERT INTO dashboard_users (username, email, password_hash, user_id, create_datetime) VALUES
            ('test_user', 't@gmail.com', '$2y$04$Lfxl0lAeEvh1/ek62Z81Yuaq7h.Qa2oGxh9l7uItscmkMGaDIon.C', '9fe2c4e93f654fdbb24c02b15259716c', NOW())
        """)

table_map = {
    'dashboard_users': populate_dashboard_users
}
def populate_tables(tables: list):
    for table in tables:
        table_map[table]()
