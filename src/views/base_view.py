import os

class BaseView:
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title):
        print(f"\n{'='*80}\n {title.center(78)} \n{'='*80}")
        
    def pause(self):
        input("\nPress Enter to return to the menu...")