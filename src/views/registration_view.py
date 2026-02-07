from .base_view import BaseView

class RegistrationView(BaseView):
    def render(self, citizens):
        self.print_header("CITIZEN REGISTRATION")
        print(f"{'ID':<14} {'Full Name':<20} {'Age':<4} {'Gen':<7} {'Category':<10} {'Health':<8}")
        print("-" * 80)
        for c in citizens:
            print(f"{c.citizen_id:<14} {c.full_name:<20} {c.age:<4} {c.gender:<7} {c.category:<10} {c.health_condition:<8}")
        self.pause()