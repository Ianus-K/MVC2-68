from typing import List
from src.models.citizen import Citizen
from src.models.shelter import Shelter

class AllocationService:

    # คำนวณลำดับความสำคัญ เด็ก/คนแก่ ผู้ป่วยวิกฤต และ VIP ตามลำดับ
    def execute(self, citizens: List[Citizen], shelters: List[Shelter]) -> List[tuple]:
        assignments = []
        
        def priority_score(c: Citizen):
            score = 0
            if c.age < 15 or c.age > 60: score += 100
            if c.health_condition in ['Critical', 'Chronic']: score += 50
            if c.category == 'VIP': score += 10
            return score

        sorted_citizens = sorted(citizens, key=priority_score, reverse=True)
        shelter_state = {s.code: {'obj': s, 'remaining': s.capacity - s.current_occupancy} for s in shelters}

        for citizen in sorted_citizens:
            for s_code, s_data in shelter_state.items():
                shelter = s_data['obj']
                if s_data['remaining'] <= 0: continue
                
                # ผู้ป่วยวิกฤตเข้าได้แค่พื้นที่ความเสี่ยงต่ำ
                if citizen.health_condition == 'Critical' and shelter.risk_level != 'Low': continue
                
                assignments.append((citizen.citizen_id, s_code))
                s_data['remaining'] -= 1
                break
                
        return assignments