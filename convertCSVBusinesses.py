import csv

with open('CSVFiles/business.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    with open('outputs/businessOutput.txt', 'w') as txtfile:
        txtfile.write("List<Long> products = new ArrayList<>();\n")
        txtfile.write("List<String> categories = new ArrayList<>();\n")
        x = 0
        for row in reader:
            x = x + 1
            products = row["products"].split(",")
            categories = row["categories"].split(",")
            for product in products:
                if product != "null":
                    txtfile.write("products.add(" + product + "L);\n")
            categories = row["categories"].split(",")
            for category in categories:
                if category != "null":
                    txtfile.write("categories.add(\"" + category + "\");\n")
            txtfile.write(f"Business business" + str(x) + " = new Business(")
            txtfile.write(f"\"{row['email']}\", ")
            txtfile.write(f"Country.{row['country']}, ")
            txtfile.write(f"UserRole.{row['userRole']}, ")
            txtfile.write(f"\"{row['password']}\", ")
            txtfile.write(f"\"{row['businessName']}\", ")
            txtfile.write(f"\"{row['ABN']}\", ")
            txtfile.write(f"\"{row['phoneNumber']}\", ")
            txtfile.write(f"null,")
            txtfile.write(f"{row['rating']}, ")
            txtfile.write("categories,")
            txtfile.write("products,")
            txtfile.write(f"\"{row['description']}\", ")
            txtfile.write(f"\"{row['businessURL']}\"")
            # Reviews go below
            txtfile.write(");\n")
            txtfile.write("businessRepository.save(business" + str(x) + ");\n")
            txtfile.write("products.clear();\n")
            txtfile.write("categories.clear();\n")
