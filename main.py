import math
import customtkinter as ctk


# default theme
ctk.set_appearance_mode('light')

# root class
class Calculator(ctk.CTk):
    __width  = 360
    __height = 405
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Calculator')

        # open in center position of screen
        x = (self.winfo_screenwidth() / 2) - (self.__width / 2)
        y = (self.winfo_screenheight() / 2) - (self.__height / 2)
        self.geometry('%dx%d+%d+%d' % (self.__width, self.__height, x, y))
        self.resizable(0, 0)

        self._font = ctk.CTkFont(size=30, weight='bold')
        self.initUI()

        
    # initial user interface
    def initUI(self):
        # display
        self.output = ctk.CTkEntry(self, width=350, height=50, corner_radius=10, border_width=3, font=self._font, justify=ctk.RIGHT)
        self.output.grid(row=0, column=0, columnspan=5, padx=5, pady=10)

        # button
        btn1 = ctk.CTkButton(self, text='1', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, 1))
        btn2 = ctk.CTkButton(self, text='2', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, 2))
        btn3 = ctk.CTkButton(self, text='3', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, 3))
        btn4 = ctk.CTkButton(self, text='4', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, 4))
        btn5 = ctk.CTkButton(self, text='5', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, 5))
        btn6 = ctk.CTkButton(self, text='6', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, 6))
        btn7 = ctk.CTkButton(self, text='7', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, 7))
        btn8 = ctk.CTkButton(self, text='8', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, 8))
        btn9 = ctk.CTkButton(self, text='9', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, 9))
        btn0 = ctk.CTkButton(self, text='0', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, 0))
        
        btn1.grid(row=2, column=0, padx=5, pady=5)
        btn2.grid(row=2, column=1, padx=5, pady=5)
        btn3.grid(row=2, column=2, padx=5, pady=5)
        btn4.grid(row=3, column=0, padx=5, pady=5)
        btn5.grid(row=3, column=1, padx=5, pady=5)
        btn6.grid(row=3, column=2, padx=5, pady=5)
        btn7.grid(row=4, column=0, padx=5, pady=5)
        btn8.grid(row=4, column=1, padx=5, pady=5)
        btn9.grid(row=4, column=2, padx=5, pady=5)
        btn0.grid(row=5, column=0, padx=5, pady=5)

        btn_point = ctk.CTkButton(self, text='.', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, '.'))
        btn_point.grid(row=5, column=1, padx=5, pady=5)

        btn_clear  = ctk.CTkButton(self, text='C', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.delete(0, ctk.END))
        btn_power  = ctk.CTkButton(self, text='x²', corner_radius=15, width=80, height=55, font=self._font, command=self.get_power) # x² = \u00B2
        btn_root   = ctk.CTkButton(self, text='√x', corner_radius=15, width=80, height=55, font=self._font, command=self.get_root)  # √  = \u221A
        btn_div    = ctk.CTkButton(self, text='/', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, '/'))
        btn_mult   = ctk.CTkButton(self, text='*', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, '*'))
        btn_sub    = ctk.CTkButton(self, text='-', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, '-'))
        btn_add    = ctk.CTkButton(self, text='+', corner_radius=15, width=80, height=55, font=self._font, command=lambda: self.output.insert(ctk.END, '+'))
        btn_change = ctk.CTkButton(self, text='+/-', corner_radius=15, width=80, height=55, font=self._font, command=self.change_sign)
        btn_equal  = ctk.CTkButton(self, text='=', corner_radius=15, width=80, height=55, font=self._font, command=self.calculate)
        
        btn_clear.grid(row=1, column=0, padx=5, pady=5)
        btn_power.grid(row=1, column=1, padx=5, pady=5)
        btn_root.grid(row=1, column=2, padx=5, pady=5)
        btn_div.grid(row=1, column=3, padx=5, pady=5)
        btn_mult.grid(row=2, column=3, padx=5, pady=5)
        btn_sub.grid(row=3, column=3, padx=5, pady=5)
        btn_add.grid(row=4, column=3, padx=5, pady=5)
        btn_change.grid(row=5, column=2, padx=5, pady=5)
        btn_equal.grid(row=5, column=3, padx=5, pady=5)


    # get power value
    def get_power(self):
        equation = self.output.get().strip()
        if equation:
            result = float(eval(equation))**2
            self.output.delete(0, ctk.END)
            self.output.insert(0, str(result))

    # get square root value
    def get_root(self):
        equation = self.output.get().strip()
        if equation:
            result = math.sqrt(float(eval(equation)))
            self.output.delete(0, ctk.END)
            self.output.insert(0, str(result))

    # change sign
    def change_sign(self):
        equation = self.output.get().strip()
        if equation:
            result =  -1 * float(eval(equation))
            self.output.delete(0, ctk.END)
            self.output.insert(0, str(result))


    # calculate result
    def calculate(self):
        equation = self.output.get().strip()
        if equation:
            result = eval(equation)
            self.output.delete(0, ctk.END)
            self.output.insert(0, result)


# root
if __name__ == '__main__':
    app = Calculator()
    app.mainloop()