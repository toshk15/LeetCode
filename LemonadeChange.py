def lemonadeChange(bills):
    five=0
    ten=0
    twenty=0

    for c in bills:
        if c==5:
            five+=1             
        if c==10:
            ten+=1
            five-=1
            if five<0:
                return False
        if c==20:
            twenty+=1                
            if ten<=0 and five<=0:
                return False
            elif ten<=0 and five>=3:
                five-=3                   
            elif five>0 and ten>0:
                ten-=1
                five-=1
            else:
                return False
        
    return True


"""
Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
"""