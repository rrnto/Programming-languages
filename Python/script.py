import tkinter as tk
from tkinter import messagebox
from questions import questions_by_section

class GalaxyQCM:
    def __init__(self, root):
        self.root = root
        self.root.title("🌌 GalaxyQCM")
        self.root.geometry("700x500")
        self.root.configure(bg="#0d1b2a")

        self.current_section = None
        self.questions = []
        self.q_index = 0
        self.score = 0
        self.selected = tk.IntVar()

        self.build_menu()

    def build_menu(self):
        self.clear_screen()
        title = tk.Label(self.root, text="🌌 Welcome to GalaxyQCM", font=("Helvetica", 20, "bold"), bg="#0d1b2a", fg="#e0e1dd")
        title.pack(pady=30)

        tk.Label(self.root, text="Choose a Section to Begin:", font=("Helvetica", 14), bg="#0d1b2a", fg="#e0e1dd").pack(pady=10)

        for section in questions_by_section:
            btn = tk.Button(self.root, text=section, font=("Helvetica", 12),
                            bg="#415a77", fg="#e0e1dd", width=30,
                            command=lambda s=section: self.start_section(s))
            btn.pack(pady=5)

    def start_section(self, section_name):
        self.current_section = section_name
        self.questions = questions_by_section[section_name]
        self.q_index = 0
        self.score = 0
        self.build_quiz_ui()

    def build_quiz_ui(self):
        self.clear_screen()

        self.q_label = tk.Label(self.root, text="", wraplength=600, justify="left",
                                font=("Helvetica", 13), bg="#0d1b2a", fg="#e0e1dd")
        self.q_label.pack(pady=20)

        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.selected, value=i,
                                font=("Helvetica", 12), bg="#1b263b", fg="#e0e1dd",
                                selectcolor="#778da9", wraplength=600)
            rb.pack(anchor='w', padx=50, pady=2)
            self.options.append(rb)

        self.submit_btn = tk.Button(self.root, text="✅ Submit", bg="#778da9", fg="#0d1b2a",
                                    command=self.check_answer)
        self.submit_btn.pack(pady=10)

        self.show_btn = tk.Button(self.root, text="👁 Show Answer", bg="#778da9", fg="#0d1b2a",
                                  command=self.show_answer)
        self.show_btn.pack(pady=5)

        self.explanation = tk.Label(self.root, text="", wraplength=600, font=("Helvetica", 10, "italic"),
                                    bg="#0d1b2a", fg="#c0c0c0")
        self.explanation.pack()

        self.next_btn = tk.Button(self.root, text="➡️ Next", bg="#415a77", fg="#e0e1dd", command=self.next_question)
        self.next_btn.pack(pady=10)

        self.progress = tk.Label(self.root, text="", bg="#0d1b2a", fg="#e0e1dd")
        self.progress.pack()

        self.load_question()

    def load_question(self):
        self.selected.set(-1)
        q = self.questions[self.q_index]
        self.q_label.config(text=f"Q{self.q_index + 1}: {q['question']}")
        for i, opt in enumerate(q["options"]):
            self.options[i].config(text=opt)
        self.explanation.config(text="")
        self.progress.config(text=f"Question {self.q_index + 1} of {len(self.questions)}")
        self.submit_btn.config(state="normal")
        self.show_btn.config(state="normal")

    def check_answer(self):
        if self.selected.get() == -1:
            messagebox.showinfo("Wait", "Please select an answer first.")
            return

        q = self.questions[self.q_index]
        correct = self.selected.get() == q["answer_index"]
        if correct:
            self.explanation.config(text="✅ Correct!\n" + q["explanation"])
            self.score += 1
        else:
            correct_opt = q["options"][q["answer_index"]]
            self.explanation.config(text=f"❌ Incorrect.\nCorrect: {correct_opt}\n{q['explanation']}")

        self.submit_btn.config(state="disabled")
        self.show_btn.config(state="disabled")

    def show_answer(self):
        q = self.questions[self.q_index]
        correct_opt = q["options"][q["answer_index"]]
        self.explanation.config(text=f"👁️ Revealed Answer: {correct_opt}\n{q['explanation']}")
        self.submit_btn.config(state="disabled")
        self.show_btn.config(state="disabled")

    def next_question(self):
        self.submit_btn.config(state="normal")
        self.show_btn.config(state="normal")

        if self.q_index < len(self.questions) - 1:
            self.q_index += 1
            self.load_question()
        else:
            messagebox.showinfo("Quiz Completed",
                                f"🎉 You've completed the quiz!\nScore: {self.score} / {len(self.questions)}")
            self.build_menu()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GalaxyQCM(root)
    root.mainloop()
