
try:
	
	def replacer():
		a = input("Sentence: ")
		b = input("Letter you want to replace: ")
		c = input("By which letter: ")



		def restart():
			res = input("Would you like to try again? [yes/no]: ")
			if res.lower() == "yes":
				replacer()
			elif res.lower() == "no":
				print("Thank you for using this application.")
			else:
				print("Please enter either yes or no")
				restart()
		print(a.replace(b,c))
		restart()
	replacer()


except:
	print("There was an error. Please try again.")

