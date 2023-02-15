import StudentClass as sc

def main():
    s = input("Enter your Student ID:")
    n = input("Enter your Name:")
    d = input("Enter your Date of Birth (MM/DD/YYYY):")
    c = input ("Enter your Class Classification (Sr, Jr, S, F):")

    student1 = sc.Student(s,n,d,c)

    student1.age()
    student1.reg()

    print (f"Student age is: {student1.get_age()}")
    print(f"Student Registration Date: {student1.get_reg()}")

main()