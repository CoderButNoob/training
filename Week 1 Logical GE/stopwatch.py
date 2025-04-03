import time 

def stopwatch():
    input("Press Enter")
    start = time.time()
    input("Press Enter")
    end = time.time()

    time_consumed = end - start 
    print(f"Total Time : {time_consumed:.2f} seconds")

if __name__ == "__main__":
    stopwatch()
