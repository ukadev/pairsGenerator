import tkinter as tk
from tkinter import ttk, scrolledtext, Button


class Application:
    def main(self):
        window = tk.Tk()
        window.title("Generador de Parejas")
        window.geometry("810x530")

        # Title Label
        ttk.Label(window,
                  text="Introduce las palabras en el bloque izquierdo, una por línea, sin separar por comas ni ningún símbolo y luego pulsa el botón 'Crear Parejas'",
                  background='green', foreground="white").grid(column=1, row=1, columnspan=3)

        # Words Textarea
        self.text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=30)
        self.text_area.grid(column=1, padx=10, pady=10, row=2)
        self.text_area.focus()

        # Pairs Textarea result
        self.text_area_result = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=30, state='disabled')
        self.text_area_result.grid(column=3, padx=25, row=2)

        # Submit Button
        self.submit = Button(window, text='Crear Parejas', command=self.execute)
        self.submit.grid(column=2, row=2, pady=10)

        window.mainloop()

    def execute(self):
        words = self.text_area.get("1.0", "end")
        wordsArray = list(filter(None, words.splitlines()))
        pairs = self.generatePairs(wordsArray)

        self.text_area_result.config(state="normal")
        self.text_area_result.delete('1.0', "end")
        self.text_area_result.insert("insert", pairs)
        self.text_area_result.config(state="disabled")

    def generatePairs(self, array):
        alreadyProcessed = []
        result = ""

        for first in array:
            for second in array:
                combination = [first, second]
                if(first == second):
                    continue
                result += first+":"+second+"\r\n"
                alreadyProcessed.append(combination)
        return result


if __name__ == "__main__":
    app = Application()
    app.main()
