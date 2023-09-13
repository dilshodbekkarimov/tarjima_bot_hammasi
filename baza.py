import sqlite3 


# ushbu baza botdagi foydalanuvchilar idsini olish ucun kerak bo'ladi.===============================================
#1- baza yaratamiz========================================================
class Database():
	def __init__(self):
		self.conn = sqlite3.connect("tarjima_baza.db")
		self.cur = self.conn.cursor()

	def create_db(self):
		self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
			tel_id varchar(30),
			name varchar(50)
			)""")
			
	
# /start bosgan obunachi idsi qo'shiladi.============================================
	def insert_users(self,tel_id,name):
		self.cur.execute(f"INSERT into users values ('{tel_id}','{name}')")	
		return self.conn.commit()
	

# obunachillarni idsini olish imkoni ========================================================

	def select_users_all(self):
		self.cur.execute("SELECT * FROM users")
		data = self.cur.fetchall() 
		return data

## obunachilar idsini olish imkoni=====================================================

	def select_user_id(self,id):
		self.cur.execute(f"SELECT * FROM users WHERE tel_id = '{id}' ")
		data = self.cur.fetchone()
		return data

