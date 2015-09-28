# Imports
import msvcrt
import sys
import urllib2

# Method definitions
def binary_search(text,list_,low,high,count=0):
	middle = (high + low) / 2

	if middle >= len(list_) or low > high:
		print "\nNumber of comparisons: ",count
		return False
	elif text < list_[middle]:
		return binary_search(text,list_,low,middle-1,count+1)
	elif text > list_[middle]:
		return binary_search(text,list_,middle+1,high,count+1)
	elif text == list_[middle]:
		print "\nNumber of comparisons: ",count+1
		return True

def find_common_pwd(password):
	lower_pwd = password.lower()

	# Read file from URL
	targetURL = "http://www.piazza.com/class_profile/get_resource/idsyiiw5dth8q/iebgfncv51c5gi"
	data = urllib2.urlopen(targetURL).read().split()

	flag = binary_search(lower_pwd,data,0,len(data)-1)
	print "The number of comparisions is related to the length of the list by log n where n is the length of the list."
	return flag


def write_password(prompt):
	"""
	This method prints asterisks instead of the password when the user enters it.
	Credit : http://stackoverflow.com/questions/10990998/how-to-have-password-echoed-as-asterisks
	"""
	write = sys.stdout.write

	password = ""
	# Print the prompt
	print prompt

	while True:
		char = msvcrt.getch()

		# Figure out when to stop
		if char == '\r':
			break
		# If user presses Backspace, remove last character of password
		elif char == '\b':
			write('\x08 \x08')
			password = password[:-1]
		else:
			write("*")
			password += char

	return password

def condition_feedback(strength_list):
	criteria = ["The password must have at least one uppercase and at least one lowercase letter.",
				"The password must have at least one digit.",
				"The password must have at least one character that is not a letter or a digit.",
				"The password should have at least 6 characters."]
	strength = []
	weakness = []

	if strength_list.count(True) == 0:
		pwd_strength = "Very Weak Password"
	elif strength_list.count(True) == 1:
		pwd_strength = "Weak Password"
	elif strength_list.count(True) == 2:
		pwd_strength = "Medium Strength Password"
	elif strength_list.count(True) == 3:
		pwd_strength = "High Medium Strength Password"
	elif strength_list.count(True) == 4:
		pwd_strength = "Strong Password"

	for index,flag in enumerate(strength_list):
		if flag == True:
			strength.append(criteria[index])
		else:
			weakness.append(criteria[index])

	feedback = "The following conditions were not met: \n" + '\n'.join(weakness) + \
	           "\nThe following conditions were met: \n" + '\n'.join(strength)
	return  pwd_strength + "\n" + feedback


def password_strength(password):
	case_flag = any(char.isupper() for char in password) and any(char.islower() for char in password)
	number_flag = any(char.isdigit() for char in password)
	special_flag = any(not(char.isdigit() or char.isalpha()) for char in password)
	length = len(password)

	strength_list = [case_flag,number_flag,special_flag,True if length >= 6 else False]
	feedback = condition_feedback(strength_list)

	flag = find_common_pwd(password)
	if flag:
		print "\nThis is a common word."

	return feedback

def main():
	while True:
		input = write_password("Enter a password > ")
		if len(input) == 0:
			print "Empty password entered. Please enter atleast one character."
		elif input.lower() == "finish":
			break
		else:
			feedback = password_strength(input)
			print feedback

if __name__ == '__main__':
	main()
