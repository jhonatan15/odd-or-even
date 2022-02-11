
active = True
def run():

    print("¿The number is odd or even?")
    

    def start():
        def choose():
            global active 
            choose_1 = input("¿Do you want to insert other number? Y/N ")   
            if choose_1.upper() == "Y":
                start()
            if choose_1.upper() == "N":
                active = False
            else: 
                print("You must insert Y for Yes or N for Not ")

    
        while active == True:
            number = input("Enter a number to know if it is even or odd ")
            if number.isdigit():
                if int(number) % 2 !=0:
                    print(f"The number {number} is even")
                    choose()   
                else:
                    print(f"The number {number} is odd")
                    choose()
            else:
                print("Please insert a number")
    start()


if __name__=='__main__':
    run()