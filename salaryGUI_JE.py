"""
Program: salaryGUI_JE.py
Author: Joey Esencan 7/19/2023

GUI-based salary calculator application that calculates employees salary and puts the state of their salary in readonly mode

NOTE: The file breezypythongui.py MUST be in the same directory
as this file for the app to run correctly.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Class header
class SalaryCalculator(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		EasyFrame.__init__(self, title = "Salary Calculator", width = 340, height = 280, background = "Khaki", resizable = False)

		# Calculator labels, buttons, and float fields
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, sticky = "NSEW", font = Font(family = "Arial", size = 20), columnspan = 2, background = "Khaki", foreground = "DimGray")
		self.addLabel(text = "Employee Hourly Wage:", row = 1, column = 0, font = Font(family = "Arial", size = 12), background = "Khaki", foreground = "DimGray", sticky = "NE")
		self.hourlyWage = self.addFloatField(value = 0, row = 1, column = 1, width = 12, sticky = "NW")
		self.addLabel(text = "Number of hours worked:", row = 2, column = 0, background = "Khaki", font = Font(family = "Arial", size = 12), foreground = "DimGray", sticky = "NE")
		self.hoursWorked = self.addFloatField(value = 0, row = 2, column = 1, width = 12, sticky = "NW")
		self.button = self.addButton(text = "Calculate", row = 3, column = 0, columnspan = 2, command = self.calculate)
		self.button["width"] = 10
		self.addLabel(text = "The employee's salary is:", row = 4, column = 0, background = "Khaki", font = Font(family = "Arial", size = 12), foreground = "DimGray", sticky = "NE")
		self.salary = self.addFloatField(value = 0, row = 4, column = 1, width = 12, state = "readonly", precision = 2, sticky = "NW")

	# Definition of the calculate() function
	def calculate(self):
		# Input Phase
		wage = self.hourlyWage.getNumber()
		hours = self.hoursWorked.getNumber()
		total = wage * hours


		# Output phase
		self.salary.setNumber(total) 



# Global definition of the main() method
def main():
	SalaryCalculator().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()