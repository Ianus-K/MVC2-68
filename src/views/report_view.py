from .base_view import BaseView

class ReportView(BaseView):
    def render(self, report_data):
        self.print_header("FINAL ALLOCATION REPORT")
        print(f"{'ID':<15} {'Name':<20} {'Status':<15} {'Shelter Code':<15}")
        print("-" * 75)
        
        allocated = 0
        stranded = 0
        
        for row in report_data:
            cid, fname, lname, cat, health, s_name, s_code = row
            full_name = f"{fname} {lname}"
            
            if s_name:
                status = "Allocated"
                loc = f"{s_code} ({s_name})"
                color = "\033[92m" 
                allocated += 1
            else:
                status = "STRANDED"
                loc = "-"
                color = "\033[91m" 
                stranded += 1
            
            print(f"{color}{cid:<15} {full_name:<20} {status:<15} {loc:<15}\033[0m")
            
        print("-" * 75)
        print(f"Summary: Safe = {allocated} | Stranded = {stranded}")
        self.pause()