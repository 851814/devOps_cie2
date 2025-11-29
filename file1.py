import sys
if(sys.argv)!=4:
   print("error:Python file1.py number,name,age & birth")
   sys.exit(1)
   num=int(sys.argv[1])
   name=int(sys.argv[2])
   age=int(sys.argv[3])
   birth=int(sys.argv[4])
   print("Train Ticket Reservation:")
   print("Train Number:",num)
   print("Name of the passenger:",name)
   print("Age of passenger:",age)
else:
    num="101"
    name="John"
    age=30
    print("Train Number:",101)
    print("Name of the passenger:","John")
    print("Age of passenger:",30)
   



   