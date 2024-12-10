"""
Social network connectivity. Given a social network containing nn members and a log file containing mm timestamps at which times pairs of members formed friendships, design an algorithm to determine the earliest time at which all members are connected (i.e., every member is a friend of a friend of a friend ... of a friend). Assume that the log file is sorted by timestamp and that friendship is an equivalence relation. The running time of your algorithm should be mlog⁡nmlogn or better and use extra space proportional to nn.
"""    

class unionFind:
    def ___init___(self,n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n
        
