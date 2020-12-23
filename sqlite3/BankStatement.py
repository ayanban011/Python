It is an basic application of Python GUI.Here I am using tkinter module to create the graphical interface.So lets start the action.
INPUT:-Here you have to give the input of Annual Interest Rate,Number of Years and Loan Amount.
OUTPUT:-When you Click the Compute Payment Button you get the output of Monthly Payment and Monthly Payment.

SAMPLE INPUT:-
Annual Interest Rate=10
Number of Years=12
Loan Amount=1234567

SAMPLE OUTPUT:-
Monthly Payment:-14754.04
Monthly Payment:-2124581.76

Let's take a look about the program.
[sourcecode language="Python3"]

# Write Python3 code here
from tkinter import * # Import tkinter
class LoanCalculator:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Loan Calculator") # Set title
        Label(window, text = "Annual Interest Rate").grid(row = 1,
        column = 1, sticky = W)
        Label(window, text = "Number of Years").grid(row = 2,
        column = 1, sticky = W)
        Label(window, text = "Loan Amount").grid(row = 3,
        column = 1, sticky = W)
        Label(window, text = "Monthly Payment").grid(row = 4,
        column = 1, sticky = W)
        Label(window, text = "Total Payment").grid(row = 5,
        column = 1, sticky = W)
        self.annualInterestRateVar = StringVar()    
        Entry(window, textvariable = self.annualInterestRateVar,
        justify = RIGHT).grid(row = 1, column = 2)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar,
        justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar,
        justify = RIGHT).grid(row = 3, column = 2)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable =
        self.monthlyPaymentVar).grid(row = 4, column = 2,
        sticky = E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable =
        self.totalPaymentVar).grid(row = 5,
        column = 2, sticky = E)
        btComputePayment = Button(window, text = "Compute Payment",
        command = self.computePayment).grid(
        row = 6, column = 2, sticky = E)
        window.mainloop() # Create an event loop
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
        float(self.loanAmountVar.get()),
        float(self.annualInterestRateVar.get()) / 1200,
        int(self.numberOfYearsVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
        * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))
    def getMonthlyPayment(self,
        loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1
        - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;
        root=Tk()
LoanCalculator()
[/sourcecode]

EXPLANATION:-
tkinter module content the tk toolkit.Here in this example we are importing whole module of tkinter in the firstline. 
Next, I am creating a userdefined Class named Loan Calculator.It holds it's own data member and member functions.
def__init__(self) is a special method in Python Class. It is a constructor of a Python class.
Next we create a window using Tk().
Then we set the title of the window using window.title function.
Then the label function create a display box to take input and use grid method to give it a table like structure.
Why we used sticky argument?
by default widgets are create in the center using sticky argument we can change it. It takes 4 values:N,S,E,W.
i.e. North,East,South,West.
Then we create some object named self.annualInterestRateVar,self.numberOfYearsVar,self.loanAmountVar,self.monthlyPaymentVar,self.totalPaymentVar
and for the first 3 object we take the input using entry() function.
Then we create the button namely compute payment,when you click the button it calls the compute payment function which is belongs to the class loan calculator.
Then using mainloop function we run our application program. It is basically an infinite loop.
Then we create a function computepayment () inside the class. Here we store our inputs of the object in some variables,for simplify our mathematical calculation.then we use an well known  mathematical equattion to calculate 
the total payment.
In the next step we create another function named getMonthlyPayment() inside the class.After getting the required inputs it's compute the monthly payment using the simple mathematical function given in the program.This program is also an example of inheritence.
Now root=Tk() means to initialize tkinter we have to create a widget which is a window.Note that root widget must be created before any other widget.

lastly we call the class to create GUI and run the program.