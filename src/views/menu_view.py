from .base_view import BaseView

class MainMenuView(BaseView):
    def show(self):
        self.clear_screen()
        self.print_header("EMERGENCY SHELTER SYSTEM (MVC)")
        print("1. View Registered Citizens")
        print("2. View Shelter Status")
        print("3. Run Allocation Algorithm")
        print("4. View Final Report")
        print("5. Reset & Seed Data (CSV)")
        print("0. Exit")
        return input("\nSelect Option: ")