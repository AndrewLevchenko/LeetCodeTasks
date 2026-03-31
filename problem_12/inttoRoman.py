class Solution:
    thousands = ['','M','MM','MMM']
    hundreds =  ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    tenth =     ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    ones =      ['','I','II','III','IV','V','VI','VII','VIII','IX']
    def inttoRoman(self, num: int) -> str:
        return self.thousands[num//1000] + self.hundreds[num%1000//100] + self.tenth[num%100//10] + self.ones[num%10]
