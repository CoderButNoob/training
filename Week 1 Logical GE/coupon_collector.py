import random

class CouponCollector:
    @staticmethod

    def generate_coupons(n):

        """
        Generate a random coupon number between 1 to n
        Args:
            n(int): Ranges between 1 to n 

        Result:
            int: A random generated coupon number
        """

        return random.randint(1,n)


    @staticmethod

    def collect_coupon(n):
        """
        Simulates collectiong all n distinct coupon number 

        Args:
            n(int) : 
        """
        if n<=0: 
            print("Invalid")
        

        coupons = set()
        random_number = 0 

        while len(coupons) < n:
            new = CouponCollector.generate_coupons(n)
            random_number += 1
            coupons.add(new)
        
        return random_number
    

n = int(input("Enter number of distinct coupons: "))

total_unique_number = CouponCollector.collect_coupon(n)

print(f"Total Random Number generated - {total_unique_number}")


