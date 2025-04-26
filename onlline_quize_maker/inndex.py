import tkinter as tk
from tkinter import messagebox

class OnlineTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Quiz")
        self.master.geometry('600x400')
        
        self.q_no = 0
        self.correct = 0
        self.bookmark_buttons = []
        self.bookmarks = {}
        self.questions = [
            "Q1: Which of the following doesn't have a superclass?",
            "Q2: Which provides runtime environment for Java byte code to execute?",
            "Q3: Which of the following is not a Java feature?",
            "Q4: What is the return type of the hashCode() method in the Object class?",
            "Q5: In which process, a local variable has the same name as one of the instance variables?",
            "Q6: Which package contains the Random class?",
            "Q7: In Java, jar stands for_____?",
            "Q8: Which one is a template for creating different objects?",
            "Q9: Which of the following are not Java keywords?",
            "Q10: Which of these is returned by operator '&'?"
        ]
        self.options = [
            ["System", "Object", "Lang", "Exception"],
            ["JDK", "JVM", "JRE", "JAVAC"],
            ["Dynamic", "Architecture Neutral", "Use of pointers", "Object-oriented"],
            ["Object", "int", "long", "void"],
            ["Serialization", "Variable Shadowing", "Abstraction", "Multi-threading"],
            ["java.util package", "java.lang package", "java.awt package", "java.io package"],
            ["Java Archive Runner", "Java Application Resource", "Java Application Runner", "None of the above"],
            ["An Array", "A class", "Interface", "Method"],
            ["double", "switch", "then", "instanceof"],
            ["Integer", "Character", "Boolean", "Float"]
        ]

        self.answers = [1, 1, 2, 1, 1, 0, 3, 1, 2, 2]

        self.var = tk.IntVar()
        self.create_widgets()
        self.update_question()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="", font=("Arial", 16))
        self.label.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.master, text="", variable=self.var, value=i, font=("Arial", 14))
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        self.next_btn = tk.Button(self.master, text="Next", command=self.next_question)
        self.next_btn.place(x=100, y=300)

        self.bookmark_btn = tk.Button(self.master, text="Bookmark", command=self.bookmark_question)
        self.bookmark_btn.place(x=250, y=300)

    def update_question(self):
        self.var.set(-1)
        self.label.config(text=self.questions[self.q_no])
        for i, option in enumerate(self.options[self.q_no]):
            self.radio_buttons[i].config(text=option)

    def next_question(self):
        if self.check_answer():
            self.correct += 1
        if self.q_no < len(self.questions) - 1:
            self.q_no += 1
            self.update_question()
        else:
            self.show_result()

    def bookmark_question(self):
        bookmark_num = len(self.bookmark_buttons) + 1
        btn = tk.Button(self.master, text=f"Bookmark{bookmark_num}", command=lambda q=self.q_no: self.jump_to_bookmark(q))
        btn.place(x=480, y=20 + 30 * bookmark_num)
        self.bookmark_buttons.append(btn)
        self.bookmarks[bookmark_num] = self.q_no
        
        if self.q_no < len(self.questions) - 1:
            self.q_no += 1
            self.update_question()
        else:
            self.bookmark_btn.config(text="Result")
            self.next_btn.config(state="disabled")

    def jump_to_bookmark(self, q_no):
        if self.check_answer():
            self.correct += 1
        self.q_no = q_no
        self.update_question()

        for btn in self.bookmark_buttons:
            if btn.cget('text') == f"Bookmark{list(self.bookmarks.keys())[list(self.bookmarks.values()).index(q_no)]}":
                btn.config(state='disabled')

    def check_answer(self):
        if self.q_no >= len(self.answers):
            return False
        return self.var.get() == self.answers[self.q_no]

    def show_result(self):
        if self.check_answer():
            self.correct += 1
        messagebox.showinfo("Result", f"Total Correct Answers: {self.correct}")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineTest(root)
    root.mainloop()
