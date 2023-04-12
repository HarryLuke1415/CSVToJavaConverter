import csv

with open('CSVFiles/product.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    with open('outputs/productOutput.txt', 'w') as txtfile:
        txtfile.write("List<String> sizes = new ArrayList<>();\n")
        txtfile.write("List<String> categories = new ArrayList<>();\n")
        txtfile.write("List<String> s3Links = new ArrayList<>();\n")
        x = 0
        for row in reader:
            x = x + 1
            sizes = row["sizes"].split(",")
            categories = row["categories"].split(",")
            s3Links = row["s3Links"].split(",")
            for size in sizes:
                if size != "null":
                    txtfile.write("sizes.add(\"" + size + "\");\n")
            for category in categories:
                if categories != "null":
                    txtfile.write("categories.add(\"" + category + "\");\n")
            for s3Link in s3Links:
                if s3Link != "null":
                    txtfile.write("s3Links.add(\"" + s3Link + "\");\n")
            txtfile.write(f"Product product" + str(x) + " = new Product(" + str(x) + "L,")
            txtfile.write(f"\"{row['productName']}\", ")
            txtfile.write(f"\"{row['businessEmail']}\", ")
            txtfile.write(f"\"{row['websiteURL']}\", ")
            txtfile.write(f"\"{row['description']}\", ")
            txtfile.write(f"\"{row['price']}\", ")
            txtfile.write(f"Currency.{row['currency']}, ")
            txtfile.write("sizes,")
            txtfile.write(f"\"{row['material']}\",")
            txtfile.write(f"{row['totalLikes']}, ")
            txtfile.write(f"{row['totalDislikes']}, ")
            txtfile.write(f"{row['rating']}, ")
            txtfile.write(f"null,")
            txtfile.write("categories,")
            txtfile.write("s3Links,")
            txtfile.write(f"Gender.{row['gender']}")
            txtfile.write(");\n")
            txtfile.write("productRepository.save(product" + str(x) + ");\n")
            txtfile.write("sizes.clear();\n")
            txtfile.write("categories.clear();\n")
            txtfile.write("s3Links.clear();\n")
