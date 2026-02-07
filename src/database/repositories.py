from src.models.citizen import Citizen
from src.models.shelter import Shelter
import sqlite3

class Repository:
    def __init__(self, db_conn):
        self.conn = db_conn

    def get_all_shelters(self):
        query = """
        SELECT s.*, COUNT(a.id) as current_occupancy 
        FROM shelters s 
        LEFT JOIN assignments a ON s.code = a.shelter_code 
        GROUP BY s.code
        """
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Shelter(row['id'], row['code'], row['name'], row['capacity'], row['current_occupancy'], row['risk_level']) 
                for row in rows]

    def get_all_citizens(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM citizens")
        rows = cursor.fetchall()
        return [Citizen(row['id'], row['citizen_id'], row['first_name'], row['last_name'], 
                        row['age'], row['gender'], row['health_condition'], row['category'], row['registered_at']) 
                for row in rows]

    def get_unassigned_citizens(self):
        query = """
        SELECT c.* FROM citizens c 
        LEFT JOIN assignments a ON c.citizen_id = a.citizen_id 
        WHERE a.id IS NULL
        """
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Citizen(row['id'], row['citizen_id'], row['first_name'], row['last_name'], 
                        row['age'], row['gender'], row['health_condition'], row['category'], row['registered_at']) 
                for row in rows]

    def assign_citizen(self, citizen_id, shelter_code):
        try:
            self.conn.cursor().execute(
                "INSERT INTO assignments (citizen_id, shelter_code) VALUES (?, ?)", 
                (citizen_id, shelter_code)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_report_data(self):
        query = """
        SELECT c.citizen_id, c.first_name, c.last_name, c.category, c.health_condition, s.name as shelter_name, s.code
        FROM citizens c
        LEFT JOIN assignments a ON c.citizen_id = a.citizen_id
        LEFT JOIN shelters s ON a.shelter_code = s.code
        """
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
        
    def seed_data(self, shelters, citizens):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM assignments")
        cursor.execute("DELETE FROM citizens")
        cursor.execute("DELETE FROM shelters")
        
        for s in shelters:
            cursor.execute("INSERT INTO shelters (code, name, capacity, risk_level) VALUES (?, ?, ?, ?)", s)
            
        for c in citizens:
            cursor.execute("""
                INSERT INTO citizens (citizen_id, first_name, last_name, age, gender, health_condition, category, registered_at) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, c)
            
        self.conn.commit()