from src.database.connection import DatabaseConnection
from src.database.repositories import Repository
from src.services.allocator import AllocationService
from src.seeder import DataSeeder
from src.views.menu_view import MainMenuView
from src.views.registration_view import RegistrationView
from src.views.allocation_view import AllocationView
from src.views.report_view import ReportView

class SystemController:
    def __init__(self):
        self.db_conn = DatabaseConnection()
        self.db_conn.initialize_schema()
        self.conn = self.db_conn.get_connection()
        
        self.repo = Repository(self.conn)
        self.service = AllocationService()
        
        self.view_menu = MainMenuView()
        self.view_reg = RegistrationView()
        self.view_alloc = AllocationView()
        self.view_report = ReportView()

    def start(self):
        while True:
            choice = self.view_menu.show()
            
            if choice == '1':
                data = self.repo.get_all_citizens()
                self.view_reg.render(data)
                
            elif choice == '2':
                data = self.repo.get_all_shelters()
                self.view_alloc.render(data)
                
            elif choice == '3':
                citizens = self.repo.get_unassigned_citizens()
                shelters = self.repo.get_all_shelters()
                plan = self.service.execute(citizens, shelters)
                
                count = 0
                for cid, s_code in plan:
                    if self.repo.assign_citizen(cid, s_code):
                        count += 1
                print(f"\nAllocation Processed. {count} citizens assigned.")
                input("Press Enter...")
                
            elif choice == '4':
                data = self.repo.get_report_data()
                self.view_report.render(data)
                
            elif choice == '5':
                seeder = DataSeeder(self.repo)
                seeder.run()
                input("\nPress Enter...")
                
            elif choice == '0':
                break