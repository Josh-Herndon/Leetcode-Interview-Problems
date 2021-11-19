class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        div_by_60 = 0
        output = 0
        
        time_appearance_map = {}
        
        for i in range(len(time)):
            if time[i] % 60 == 0:
                div_by_60 += 1
            
            time[i] /= 60
            time[i] = round(float(str(time[i])[str(time[i]).index('.'):]), 3)
            
            if time[i] not in time_appearance_map:
                time_appearance_map[time[i]] = 1
            else:
                time_appearance_map[time[i]] += 1
    
        j = 1
        while j < 60:
            key = round(j/60, 3)
            if key in time_appearance_map:
                target = round(1 - key, 3)
                if target in time_appearance_map:
                    if key == target:
                        output += (time_appearance_map[key]*(time_appearance_map[key] - 1))/2
                        del time_appearance_map[key]
                    else:
                        output += time_appearance_map[key]*time_appearance_map[target]
                        del time_appearance_map[key]
                        del time_appearance_map[target]
                else:
                    del time_appearance_map[key]
                
            j += 1
                
        if div_by_60 > 0:
            output += (div_by_60 * (div_by_60 - 1))/2
        
        return int(output)