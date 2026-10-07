from datetime import datetime
class Book:
    def __init__(self,name,price,quantity):
        self.name= name
        self.price= price
        self.quantity=quantity
    def __str__(self):
        return f"Book: {self.name} | Price: {self.price} | Quantity: {self.quantity}"
    def inventory_value(self):
        return self.price*self.quantity
    def check_availability(self,quantity_order):
        if self.quantity == 0:
            print("Book Is Out Of Stock.")
            return 0
        elif quantity_order > self.quantity :
            print(f"This quantity not avaliable.You can take {self.quantity}")
            answer=input("Yes or No: ").capitalize()
            while answer!= "Yes" and answer!="No":
                answer=input("Yes or No: ").capitalize()
            if answer == "Yes":
                return self.quantity
            else:
                return 0            
        elif quantity_order<= self.quantity:
            return True
        
    def update_inventory(self,borrowed_quantity):
        self.quantity=self.quantity-borrowed_quantity
        
       

class Customer:
    def __init__(self,name_customer,phone_number):
        self.name_customer = name_customer
        self.phone_number= phone_number



class Order:
    def __init__(self,customer):
        self.customer= customer
        self.borrowed_books = []
        self.date = datetime.now()
    def add_borrowed_book(self,book,borrowed_quantity,number_Days):
        while borrowed_quantity<=0 :
            print("Please Enter valide Number.")
            borrowed_quantity=int(input("Enter borrowed Books: "))
            
        while number_Days<=0 :
            print("Please Enter valide Number.")
            number_Days=int(input("Enter Days Number: "))

        available_quantity =book.check_availability(borrowed_quantity) 
        if available_quantity is True:
            self.borrowed_books.append((book, borrowed_quantity,number_Days))
            book.update_inventory(borrowed_quantity)
            return True
        elif available_quantity > 0:
            self.borrowed_books.append((book, available_quantity,number_Days)) 
            book.update_inventory(available_quantity)
            return True
        else:
            return False
        
    def calculate_subtotal(self):
        total=0
        for book,borrowed_quantity,number_Days in self.borrowed_books:
            total += borrowed_quantity*book.price*number_Days
        return total

    def show_info(self):
        print("="*30)
        print("Customer: ",self.customer.name_customer)
        print("Customer: ",self.customer.phone_number)
        print("Date: ",self.date)
        print("="*30)
        for book, borrowed_quantity, number_Days in self.borrowed_books:
            print("Book:", book.name,"     |","Quantity:", borrowed_quantity,"     |","Days:", number_Days)
            print("="*30)
            
        print("Subtotal: ",self.calculate_subtotal())
        print("="*30)




class Library:
    def __init__(self,books,orders):
        self.books=books
        self.orders=orders
    def add_book(self,book):
        if self.search_book(book.name) != "Book not found.":
            return False
        else:
            self.books.append(book)
            return True
    def add_orders(self,order):
        self.orders.append(order)
    def Show_library_info(self):
        for book in self.books:
            print(book)
    def search_book(self,book):
        for current_book in self.books:
            if current_book.name.lower() ==book:
                return current_book
        return "Book not found."
    def Show_order_info(self):
            if not self.orders:
                print("No orders found.")
            else:
                for order in self.orders:
                    order.show_info()
    def borrow_book(self,order,book_name,quantity,days):
        book_search=self.search_book(book_name)
        if book_search in self.books:
            print(f"Book is found: {book_name} ")
            order.add_borrowed_book(book_search,quantity,days)         
        else:
            return "Book not found."
    def total_revenue(self):
        total=0
        for order in self.orders:
            total += order.calculate_subtotal()
        return total
    def report(self):
        number_orders=len(self.orders)
        customer=set()
        customer_totals={}
        today_revenue=0
        for order in self.orders:
            customer.add(order.customer.name_customer)
        for order in self.orders:
            if order.customer.name_customer in customer_totals:
                customer_totals[order.customer.name_customer] += order.calculate_subtotal()
            else:
                customer_totals[order.customer.name_customer] = order.calculate_subtotal()
        for order in self.orders:
            if order.date.date() == datetime.now().date() :
                today_revenue+=order.calculate_subtotal()

        print("=" * 32)
        print("          DAILY REPORT")
        print("=" * 32)
        print(f"Number of Orders: {number_orders}")
        print(f"Number of Customers: {len(customer)}")
        print("=" * 32)
        for key,value in customer_totals.items():
            print(f"Customer: {key}")
            print(f"Total: {value}")
            print("=" * 32)
        print(f"Day Revenue: {today_revenue}")
        print("=" * 32)
        print("Library Management System | Developed by Emad")
    def menu(self):
        while True:
            print("=" * 32)
            print("     LIBRARY MANAGEMENT SYSTEM")
            print("=" * 32)
            print("1. Add Book")
            print("2. Show Books")
            print("3. Search Book")
            print("4. Borrow Books")
            print("5. Show Orders")
            print("6. Daily Report")
            print("7. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                
                while True:
                    book_name = input("Enter book name: ").strip().lower()
                    if book_name =="":
                        print("Please enter a book name.")
                    else:
                        break
                while True:
                    try:
                        
                        book_price = float(input("Enter book price: "))
                        book_quantity = int(input("Enter book quantity: "))
                        if book_price <= 0 or book_quantity <= 0:
                            print("Please Enter a valid number.")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid number.")
                new_book=Book(book_name,book_price,book_quantity)
                result=self.add_book(new_book)
                if result:
                    print("Book added successfully!")
                else:
                    print("Book already exists.")
            elif choice == "2":
                self.Show_library_info()
            elif choice == "3":
                book_name = input("Enter book name: ").lower()
                result=self.search_book(book_name)
                print(result) 
            elif choice == "4":
                customer_name = input("Enter customer name: ")
                phone_number = input("Enter phone number: ")
                customer = Customer(customer_name, phone_number)
                order=Order(customer)
                while True:
                    book_name = input("Enter book name: ").strip().lower()
                    while True:
                        
                        try:
                            quantity = int(input("Enter quantity: "))
                            days=int(input("Enter Days: "))
                            if quantity <=0 or days<=0:
                                print("Please Enter a valid number.")
                            else:
                                break   
                        except ValueError:
                            print("Please enter a valid number.")
                    book = self.search_book(book_name)
                
                    if book == "Book not found.":
                        print("Book Not Found")
                        continue
                    else:
                        result=order.add_borrowed_book(book,quantity,days)
                        if not result:
                            continue
                    while True:
                        answer = input("Do you want to borrow another book? Yes or No: ").capitalize()
                        if answer== "Yes" or answer == "No":
                            break
                        else:
                            print("Please enter Yes or No.")
                    if answer == "No":
                        break
                if order.borrowed_books:
                    self.add_orders(order)
            elif choice == "5":
                self.Show_order_info() 
            elif choice == "6":
                self.report()
            elif choice == "7":
                print("Thank you for using Library Management System!")
                break

        



        
book1 = Book("Python", 50, 3)
book2 = Book("SQL", 20, 5)
book3 = Book("AI", 100, 4)
library1=Library([book1,book2,book3],[])
library1.menu()

        
    









