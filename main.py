class Voter:

    def __init__(self, arrival_time, voting_duration, is_impatient):
        self.arrival_time = arrival_time
        self.voting_duration = voting_duration
        self.is_impatient = is_impatient
        
        # These aren't inputted as an instance 
        # I have initialised them with the appropriate value
        self.start_time = None
        self.departure_time = None
        self.has_voted = False        
    