class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # In 12 hours Hour hand complete whole circle and cover 360°
        # So, 1 hour = 360° / 12 = 30°
        # In 60 minutes Minute Hand completes whole circle and cover 360°.
        # So, 1 minute -> 360° / 60 = 6°
        h,m =  hour,minutes
        # Convert the hour hand to another minute hand
        m2 = (h%12 + m/60)*5
        # Calculate the difference between the two minute hands
        diff = abs(m-m2)
        
        # Convert the difference to an angle
        ang = diff*(360/60)
        
        # Return the smallest angle
        return min(360-ang, ang)


        