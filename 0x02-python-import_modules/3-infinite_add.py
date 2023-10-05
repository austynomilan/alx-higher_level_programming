#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sums = 0
    
    for i, arg in enumerate(sys.argv[1:], start=1):
        sums += int(arg)
            
    print(sums)
