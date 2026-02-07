import csv
import os

class DataSeeder:
    def __init__(self, repository):
        self.repo = repository
        self.seeds_path = os.path.join("data", "seeds")

    def run(self):
        print(f"Reading CSV from: {self.seeds_path}")
        shelters = self._load_shelters()
        citizens = self._load_citizens()

        if shelters and citizens:
            self.repo.seed_data(shelters, citizens)
            print(f"Seeding Complete: ({len(shelters)} Shelters, {len(citizens)} Citizens)")

    def _load_shelters(self):
        data = []
        try:
            with open(os.path.join(self.seeds_path, "shelters.csv"), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 4:
                        data.append((row[0].strip(), row[1].strip(), int(row[2]), row[3].strip()))
            return data
        except Exception as e:
            print(f"Error loading shelters: {e}")
            return []

    def _load_citizens(self):
        data = []
        try:
            with open(os.path.join(self.seeds_path, "citizens.csv"), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 7:
                        cid = row[0].strip()
                        if len(cid) == 13 and cid[0] != '0' and cid.isdigit():
                            data.append((
                                cid, 
                                row[1].strip(), 
                                row[2].strip(), 
                                int(row[3]), 
                                row[4].strip(),
                                row[5].strip(), 
                                row[6].strip()
                            ))
            return data
        except Exception as e:
            print(f"Error loading citizens: {e}")
            return []