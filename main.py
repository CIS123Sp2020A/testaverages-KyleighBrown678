#Kyleigh Brown
#CIS 123

import tkinter

class TestAvg:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the six frames.
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.test4_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for test 1.
        self.test1_label = tkinter.Label(self.test1_frame,
                                         text='Enter the score for test 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame,
                                         width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # Create and pack the widgets for test 2.
        self.test2_label = tkinter.Label(self.test2_frame,
                                         text='Enter the score for test 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame,
                                         width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        # Create and pack the widgets for test 3.
        self.test3_label = tkinter.Label(self.test3_frame,
                                         text='Enter the score for test 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame,
                                         width=10)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        #Create and pack the widgets for test 4.
        self.test4_label = tkinter.Label(self.test4_frame,
                                         text='Enter the score for test 4:')
        self.test4_entry = tkinter.Entry(self.test4_frame,
                                         width=10)
        self.test4_label.pack(side='left')
        self.test4_entry.pack(side='left')

        # Create and pack the widgets for the average.
        self.result_label = tkinter.Label(self.avg_frame,
                                          text='Average:')
        self.avg = tkinter.StringVar()  # To update avg_label
        self.avg_label = tkinter.Label(self.avg_frame,
                                       textvariable=self.avg)

        #Create a self.letter_grade result and the StringVar self.letter_grade
        self.letter = tkinter.StringVar()
        self.letter_grade_label = tkinter.Label(self.avg_frame,
                                                textvariable = self.letter)

        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        self.letter_grade_label.pack(side='left')

        # Create and pack the button widgets.
        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Average',
                                          command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.test4_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()

    # The calc_avg method is the callback function for
    # the calc_button widget.

    def calc_avg(self):
        # Get the four test scores and store them
        # in variables.
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())
        self.test4 = float(self.test4_entry.get())

        # Calculate the average.
        self.average = (self.test1 + self.test2 +
                        self.test3 + self.test4) / 4.0

        if self.average >= 90:
            self.letter.set('A')
        elif self.average >= 80 and self.average < 90:
            self.letter.set('B')
        elif self.average >= 70 and self.average < 80:
            self.letter.set('C')
        elif self.average >= 60 and self.average < 70:
            self.letter.set('D')
        else:
            self.letter.set('F')
            
        # Update the avg_label widget by storing
        # the value of self.average in the StringVar
        # object referenced by avg.
        self.avg.set(round(self.average,2))

# Create an instance of the TestAvg class.
test_avg = TestAvg()
