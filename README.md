# Inventory Management System

This is an inventory management system built using Django to efficiently manage products, stock levels, suppliers, and sales. The system supports CRUD operations, stock management, and enables tracking of sales orders.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB

## Database Models

### Product
- `name` (string)
- `description` (text)
- `category` (string)
- `price` (decimal)
- `stock_quantity` (integer)
- `supplier` (foreign key to Supplier)

### Supplier
- `name` (string)
- `email` (email)
- `phone` (string, 10 digits)
- `address` (text)

### Sale Order
- `product` (foreign key to Product)
- `quantity` (integer)
- `total_price` (decimal)
- `sale_date` (date)
- `status` (string: Pending/Completed/Cancelled)

### Stock Movement
- `product` (foreign key to Product)
- `quantity` (integer)
- `movement_type` (string: "In" for incoming stock, "Out" for sales)
- `movement_date` (date)
- `notes` (text)

## Features

- **Add Product**: Add a new product to the inventory, including validation for stock quantity, price, and product details. Ensure no duplicate product records exist.
- **List Products**: Retrieve a list of all products in the inventory, including their name, description, price, stock quantity, and supplier details.
- **Add Supplier**: Add a new supplier to the system by validating email and phone number format. Ensure that no duplicate supplier records exist.
- **List Suppliers**: Retrieve a list of all suppliers, including their name, email, phone, and address details.
- **Add Stock Movement**: Record incoming stock ("In") or outgoing stock ("Out") and update the stock levels accordingly. Ensure proper validation of stock levels.
- **Create Sale Order**: Allow users to create sale orders by selecting products, verifying sufficient stock, and calculating the total price. Ensure that the stock levels are updated.
- **Cancel Sale Order**: Cancel an existing sale order, ensuring that the status is set to "Cancelled" and stock is updated back if the sale is canceled.
- **Complete Sale Order**: Mark an order as "Completed" and update the stock levels accordingly. Ensure the sale is valid and the status is updated to "Completed."
- **List Sale Orders**: Retrieve a list of all sale orders, including the product name, quantity, total price, sale date, status, and any additional notes.
- **Stock Level Check**: Implement a function to check and return the current stock level for each product.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/theayushgupta08/inventoryManagement.git
    cd inventoryManagement
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure MongoDB**:
    Ensure that your MongoDB server is running. 

5. **Apply migrations**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

8. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/inventory/`.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

