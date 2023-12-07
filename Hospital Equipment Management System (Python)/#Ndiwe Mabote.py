#Ndiwe Mabote
#Tp067277

choice = input("Main Menu:\ninventory\nsuppliers\nhospitals\nreceive\ndistribute\ntotal\nsearch\nChoose an option: ").lower().strip() 

if choice == "inventory":													
		while True:
			item = input("Enter item code: ").upper()
			if item in open("ppe.txt").read():
				print("There is already stock of this item.")
				break

			supplier = int(input("Choose supplier from 1 to 4: "))
			if supplier < 1 or supplier > 4:
				print("Choose from 1 to 4")
				continue

			inventory_file.write(f"{item} : S{str(supplier)} : 100\n")	

			extra = input("Do you wish to continue(yes/no)? ")			
			if extra == "no":											
				break
if choice == "suppliers":
	with open("suppliers.txt", "a+") as suppliers_file:
		while True:
			supplier_code = int(input("Choose supplier from 1 to 4: "))
			if supplier_code < 1 or supplier_code > 4:
				continue
			if str(supplier_code) in open("suppliers.txt").read():
				print("This supplier has already been added to a list.")
				update_supplier = input("Do you want to update its data(yes/no)? ")    
				if update_supplier == "yes":
					update_supplier_data = input("What to update(name/number)? ").lower()

					with open("suppliers.txt", "r") as suppliers_file:
						suppliers_lines = open("suppliers.txt").readlines()
					with open("suppliers.txt", "w") as suppliers_file:
						for suppliers_line in suppliers_lines:
							if  str(supplier_code) in suppliers_line:						
								if update_supplier_data == "name":
									supplierName= suppliers_line.split (":")[1][1:-1]
									update_supplier_name = input("Enter new name: ")
									suppliers_line = suppliers_line.replace(supplierName, update_supplier_name)
								if update_supplier_data == "number":
									supplierPhoneNumber = suppliers_line.split(":")[2][1:-1]
									update_supplier_number = input("Enter new number: ")
									suppliers_line = suppliers_line.replace(supplierPhoneNumber, update_supplier_number)
							suppliers_file.write(suppliers_line)
						break
				else:
					continue
			else:
				supplierName = input("Enter a supplier name: ")
				supplierPhoneNumber = input("Enter a supplier number: ")
				suppliers_file.write(f"{supplierName} : {str(supplier_code)} : {supplierPhoneNumber} \n")
				break


if choice == "hospitals": 
	with open("hospitals.txt", "a+") as hospitals_file:
		while True:
			hospital = int(input("Choose hospital from 1 to 4: "))
			if hospital < 1 or hospital > 4:
				continue
			if "H" + str(hospital) in open("hospitals.txt").read():
				print("This hospital is already in a list")
				updatedHospital = input("Do you want to update its data(yes/no)? ")			
				if updatedHospital == "yes":
					update_hospitalInfo = input("What to update(name/number/email)? ").lower()

					with open("hospitals.txt", "r") as hospitals_file:
						hospital_lines = open("hospitals.txt").readlines()
					with open("hospitals.txt", "w") as hospitals_file:
						for hospital_line in hospital_lines:
							if "H" + str(hospital) in hospital_line:
								if update_hospitalInfo == "name":							
									hospital_name = hospital_line.split(":")[1][1:-1]
									update_hospital_name = input("Enter new name: ")
									hospital_line = hospital_line.replace(hospital_name, update_hospital_name)
								if update_hospitalInfo == "number":
									hospital_number = hospital_line.split(":")[2][1:-1]
									update_hospital_number = input("Enter new number: ")
									hospital_line = hospital_line.replace(hospital_number, update_hospital_number)
							hospitals_file.write(hospital_line)
						break
				else:
					continue
			else:
				hospital_name = input("Enter a hospital name: ")
				hospital_number = input("Enter a hospital number: ")
				hospital_mail = input("Enter a hospital email: ")
				hospitals_file.write(f"H{str(hospital)} : {hospital_name} : {hospital_number} \n")
				break

if choice == "receive":		
	with open("ppe.txt", "r") as inventory_file:
		lines = open("ppe.txt").readlines()
	with open("ppe.txt", "w") as inventory_file:
		item = input("Enter item being supplied: ").upper()
		for line in lines:
			if item in line:
				quantityInStock = line.split(":")[-1][1:-1]
				add_Quantity = int(input("Quantity to be supplied? "))
				newQuantity = int(quantityInStock) + add_Quantity			
				line = line.replace(quantityInStock, str(newQuantity))
			inventory_file.write(line)
	

if choice == "distribute":											
	with open("ppe.txt", "r") as inventory_file:	
		lines = open("ppe.txt").readlines()
	with open("ppe.txt", "w") as inventory_file:
		item = input("what item is being distributed: ").upper()
		for line in lines:
			if item in line:
				quantityInStock = line.split(":")[-1][1:-1]
				subtract_quantity = int(input("How much to be distributed? "))
				if int(quantityInStock) >= subtract_quantity:
					item_quantity = int(quantityInStock) - subtract_quantity	
					distributed = subtract_quantity
					line = line.replace(quantityInStock, str(item_quantity))
				else:
					print("Insufficient quantity in stock")					
					print(f"You only have {quantityInStock} items")
			inventory_file.write(line)

	with open("distribution.txt", "a") as distribution_file:			
		while True:
			hospital = int(input("Choose hospital from 1 to 4: "))
			if hospital < 1 or hospital > 4:
				continue
			else:
				distribution_file.write(f"{item} : H{str(hospital)} : {str(distributed)}\n")
				break

if choice == "total" :                              
	with open("ppe.txt", "r") as inventory_file:
		lines = open("ppe.txt").readlines()
		total = {}
		for line in lines:
			item = line.split(":")[0][:-1]
			quantity = int(line.split(":")[-1][1:-1])
			total[item] = quantity
			if choice == "25" and quantity < 25:			
				print(f"{item} :  {quantity}")
		if choice == "total":
			print(f"Sorted list: {sorted(total.items())[::-1]}")

if choice == "search":												
	with open("distribution.txt", "r") as distribution_file:
		item = input("Enter item code: ").upper().strip()
		lines = open("distribution.txt").readlines()
		readfile = open("distribution.txt").read()
		sum1=sum2=sum3=sum4=0
		for line in lines:
			if item in line:
				repeated = item + " : "+ line.split(":")[1][1:-1]
				hospital = line.split(":")[1][1:-1]
				quantity = int(line.split(":")[-1][1:-1])
				if readfile.count(repeated) > 1: 						
					if hospital == "H1":
						sum1 += quantity
						h1 = line.replace(str(quantity), str(sum1))
					if hospital == "H2":
						sum2 += quantity
						h2 = line.replace(str(quantity), str(sum2))
					if hospital == "H3":
						sum3 += quantity
						h3 = line.replace(str(quantity), str(sum3))
					if hospital == "H4":
						sum4 += quantity
						h4 = line.replace(str(quantity), str(sum4))
				else:
					print(line.replace("\n", ""))						

		if sum1 != 0:
			print(h1.replace("\n", ""))
		if sum2 != 0:
			print(h2.replace("\n", ""))
		if sum3 != 0:
			print(h3.replace("\n", ""))
		if sum4 != 0:
			print(h4.replace("\n", ""))	
		if item not in readfile:
			print("This item has not been distributed yet")				