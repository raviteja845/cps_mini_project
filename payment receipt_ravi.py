import datetime
import random

def generate_receipt():
    print("=== Payment Receipt Generator ===\n")
    
    store_name = "RaviTeja Superstore" 
    store_address = "Erchakulam, Nagercoil, 629901"
    customer_name = input("Enter Customer Name: ")
    payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payment_mode = input("Enter Payment Mode (Cash/Card/UPI): ")

    total_amount = 0
    items = []

    while True:
        try:
            total_items = int(input("Enter Total Number of Items: "))
            if total_items <= 0:
                print("Number of items must be greater than 0. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for total items.")
    
    for i in range(total_items):
        print(f"\nEnter details for item {i + 1}:")
        item_name = input("   Item Name: ").strip()
        if not item_name:
            print("Item name cannot be empty. Please enter a valid name.")
            continue
        
        item_quantity = input("   Quantity (e.g., 1 kg, 500 g, 2 pieces): ").strip()
        if not item_quantity:
            print("Quantity cannot be empty. Please enter a valid quantity.")
            continue
        
        while True:
            try:
                item_price = float(input("   Price per unit (in ₹): "))
                if item_price <= 0:
                    print("Price must be greater than 0. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid price.")
        
        while True:
            try:
                quantity_number = float(input("   Enter quantity in numeric form for calculation: "))
                if quantity_number <= 0:
                    print("Quantity must be greater than 0. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid numeric value for calculation.")

        item_total = quantity_number * item_price  
        total_amount += item_total  
        
        items.append((item_name, item_quantity, item_price, item_total))
    
    date_str = datetime.datetime.now().strftime("%Y%m%d")
    random_number = random.randint(1000, 9999)
    receipt_id = f"RaviTeja-{date_str}-{random_number}"

    receipt = f"""
    ============================================
                   {store_name}
                    
               {store_address}
    ============================================
    RECEIPT ID     : {receipt_id}
    DATE & TIME    : {payment_date}
    --------------------------------------------
    CUSTOMER NAME  : {customer_name}
    PAYMENT MODE   : {payment_mode}
    --------------------------------------------
    ITEM DETAILS
    --------------------------------------------
    {"Item Name":<15} {"Qty":<12} {"Price":<10} {"Total":<10}
    --------------------------------------------"""
    
    for item in items:
        receipt += f"\n    {item[0]:<15} {item[1]:<12} ₹{item[2]:<10.2f} ₹{item[3]:<10.2f}"
    
    receipt += f"""
    --------------------------------------------
    TOTAL AMOUNT   : ₹{total_amount:.2f}
    --------------------------------------------
              THANK YOU FOR YOUR PAYMENT!
                PLEASE VISIT US AGAIN!
    ============================================
    """
    
    print(receipt)
    
    with open("payment_receipt_new_format.txt", "a", encoding="utf-8") as file:
        file.write(receipt + "\n")
    print("                   RaviTeja SuperStore")

if __name__ == "__main__":
    generate_receipt()   
