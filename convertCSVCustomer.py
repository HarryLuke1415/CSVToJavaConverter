import csv

with open('CSVFiles/customer.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    with open('outputs/customerOutput.txt', 'w') as txtfile:
        txtfile.write("\n")
        txtfile.write("List<Long> bagItems = new ArrayList<>();\n")
        txtfile.write("List<Long> likedItems = new ArrayList<>();\n")
        txtfile.write("List<Long> dislikedItems = new ArrayList<>();\n")
        txtfile.write("List<String> interestedCategories = new ArrayList<>();\n")
        x = 0
        for row in reader:
            x = x + 1
            bagItems = row["bagItems"].split(",")
            likedItems = row["likedItems"].split(",")
            dislikedItems = row["dislikedItems"].split(",")
            interestedCategories = row["interestedCategories"].split(",")
            for bagItem in bagItems:
                if bagItem != "null":
                    txtfile.write("bagItems.add(" + bagItem + "L);\n")
            for likedItem in likedItems:
                if likedItem != "null":
                    txtfile.write("likedItems.add(" + likedItem + "L);\n")
            for dislikedItem in dislikedItems:
                if dislikedItem != "null":
                    txtfile.write("dislikedItems.add(" + dislikedItem + "L);\n")
            for interestedCategory in interestedCategories:
                if interestedCategory != "null":
                    txtfile.write("interestedCategories.add(\"" + interestedCategory + "\");\n")
            txtfile.write(f"Customer customer" + str(x) + " = new Customer(")
            txtfile.write(f"\"{row['email']}\", ")
            txtfile.write(f"Country.{row['country']}, ")
            txtfile.write(f"UserRole.{row['userRole']}, ")
            txtfile.write(f"\"{row['password']}\", ")
            txtfile.write(f"\"{row['firstName']}\", ")
            txtfile.write(f"\"{row['lastName']}\", ")
            txtfile.write(f"\"{row['username']}\", ")
            txtfile.write(f"Gender.{row['gender']}, ")
            txtfile.write(f"{row['age']}, ")
            txtfile.write("bagItems,")
            txtfile.write("likedItems,")
            txtfile.write("dislikedItems,")
            txtfile.write("interestedCategories")
            txtfile.write(");\n")
            txtfile.write("customerRepository.save(customer" + str(x) + ");\n")
            txtfile.write("bagItems.clear();\n")
            txtfile.write("likedItems.clear();\n")
            txtfile.write("dislikedItems.clear();\n")
            txtfile.write("interestedCategories.clear();\n")
        txtfile.write("\n")