from .base_view import BaseView

class AllocationView(BaseView):
    def render(self, shelters):
        self.print_header("SHELTER STATUS")
        print(f"{'Code':<6} {'Name':<20} {'Risk':<10} {'Occupancy':<15}")
        print("-" * 60)
        for s in shelters:
            status = f"{s.current_occupancy}/{s.capacity}"
            if s.current_occupancy >= s.capacity: status += " [FULL]"
            print(f"{s.code:<6} {s.name:<20} {s.risk_level:<10} {status:<15}")
        self.pause()