import tkinter as tk
from tkinter import scrolledtext, messagebox

from lexer import Lexer
from ir import IRGenerator
from analyzer import PerformanceAnalyzer
from optimizer import OptimizationEngine


class CompilerGUI:

    def __init__(self, root):

        self.root = root

        # =====================================
        # WINDOW SETTINGS
        # =====================================

        self.root.title("Compiler Optimization Simulator")

        self.root.geometry("1000x780")

        self.root.configure(bg="#1e1e1e")

        self.root.resizable(False, False)

        # =====================================
        # TITLE
        # =====================================

        title = tk.Label(
            root,
            text="Compiler Optimization Simulator",
            font=("Arial", 22, "bold"),
            bg="#1e1e1e",
            fg="#00ffff"
        )

        title.pack(pady=15)

        # =====================================
        # SUBTITLE
        # =====================================

        subtitle = tk.Label(
            root,
            text="Lexical Analysis • TAC Generation • Optimization • Performance Analysis",
            font=("Arial", 11),
            bg="#1e1e1e",
            fg="lightgray"
        )

        subtitle.pack(pady=5)

        # =====================================
        # INPUT LABEL
        # =====================================

        input_label = tk.Label(
            root,
            text="Enter Three Address Code (TAC):",
            font=("Arial", 13, "bold"),
            bg="#1e1e1e",
            fg="white"
        )

        input_label.pack(anchor="w", padx=15, pady=(15, 5))

        # =====================================
        # INPUT TEXT BOX
        # =====================================

        self.input_text = scrolledtext.ScrolledText(
            root,
            width=115,
            height=10,
            font=("Consolas", 12),
            bg="#2d2d2d",
            fg="white",
            insertbackground="white",
            relief="flat",
            borderwidth=5
        )

        self.input_text.pack(padx=15)

        # =====================================
        # DEFAULT SAMPLE CODE
        # =====================================

        sample_code = """a = 3 + 4
b = a + 2
c = b * 1
d = c + 0"""

        self.input_text.insert(tk.END, sample_code)

        # =====================================
        # BUTTON FRAME
        # =====================================

        button_frame = tk.Frame(
            root,
            bg="#1e1e1e"
        )

        button_frame.pack(pady=15)

        # =====================================
        # RUN BUTTON
        # =====================================

        run_button = tk.Button(
            button_frame,
            text="▶ Run Compiler",
            font=("Arial", 12, "bold"),
            bg="#00adb5",
            fg="white",
            padx=20,
            pady=8,
            relief="flat",
            command=self.run_compiler
        )

        run_button.grid(row=0, column=0, padx=10)

        # =====================================
        # CLEAR BUTTON
        # =====================================

        clear_button = tk.Button(
            button_frame,
            text="✖ Clear Output",
            font=("Arial", 12, "bold"),
            bg="#ff4c4c",
            fg="white",
            padx=20,
            pady=8,
            relief="flat",
            command=self.clear_output
        )

        clear_button.grid(row=0, column=1, padx=10)

        # =====================================
        # OUTPUT LABEL
        # =====================================

        output_label = tk.Label(
            root,
            text="Compiler Output:",
            font=("Arial", 13, "bold"),
            bg="#1e1e1e",
            fg="white"
        )

        output_label.pack(anchor="w", padx=15)

        # =====================================
        # OUTPUT BOX
        # =====================================

        self.output_text = scrolledtext.ScrolledText(
            root,
            width=115,
            height=24,
            font=("Consolas", 11),
            bg="black",
            fg="#00ff00",
            insertbackground="white",
            relief="flat",
            borderwidth=5
        )

        self.output_text.pack(padx=15, pady=10)

        # =====================================
        # FOOTER
        # =====================================

        footer = tk.Label(
            root,
            text="Developed by Team Syntax Squad",
            font=("Arial", 10),
            bg="#1e1e1e",
            fg="gray"
        )

        footer.pack(side="bottom", pady=8)

    # =====================================
    # CLEAR OUTPUT FUNCTION
    # =====================================

    def clear_output(self):

        self.output_text.delete(
            "1.0",
            tk.END
        )

    # =====================================
    # MAIN COMPILER EXECUTION
    # =====================================

    def run_compiler(self):

        try:

            code = self.input_text.get(
                "1.0",
                tk.END
            ).strip()

            if not code:

                messagebox.showwarning(
                    "Warning",
                    "Please enter TAC code."
                )

                return

            # Clear previous output

            self.output_text.delete(
                "1.0",
                tk.END
            )

            # =====================================
            # LEXICAL ANALYSIS
            # =====================================

            lexer = Lexer(code)

            tokens = lexer.tokenize()

            self.output_text.insert(
                tk.END,
                "==============================\n"
            )

            self.output_text.insert(
                tk.END,
                "        TOKENS GENERATED\n"
            )

            self.output_text.insert(
                tk.END,
                "==============================\n\n"
            )

            for tok in tokens:

                if tok.type.value != "EOF":

                    self.output_text.insert(
                        tk.END,
                        f"{tok}\n"
                    )

            # =====================================
            # IR GENERATION
            # =====================================

            ir = IRGenerator.parse_tac(code)

            self.output_text.insert(
                tk.END,
                "\n==============================\n"
            )

            self.output_text.insert(
                tk.END,
                "     ORIGINAL IR (TAC)\n"
            )

            self.output_text.insert(
                tk.END,
                "==============================\n\n"
            )

            for instr in ir:

                self.output_text.insert(
                    tk.END,
                    f"{instr}\n"
                )

            # =====================================
            # OPTIMIZATION
            # =====================================

            optimizer = OptimizationEngine(ir)

            optimized_ir = optimizer.constant_folding()

            optimizer2 = OptimizationEngine(
                optimized_ir
            )

            optimized_ir = optimizer2.constant_propagation()

            optimizer3 = OptimizationEngine(
                optimized_ir
            )

            optimized_ir = optimizer3.algebraic_simplification()

            optimizer4 = OptimizationEngine(
                optimized_ir
            )

            optimized_ir = optimizer4.constant_folding()

            # =====================================
            # SHOW OPTIMIZED IR
            # =====================================

            self.output_text.insert(
                tk.END,
                "\n==============================\n"
            )

            self.output_text.insert(
                tk.END,
                "        OPTIMIZED IR\n"
            )

            self.output_text.insert(
                tk.END,
                "==============================\n\n"
            )

            for instr in optimized_ir:

                self.output_text.insert(
                    tk.END,
                    f"{instr}\n"
                )

            # =====================================
            # PERFORMANCE ANALYSIS
            # =====================================

            analysis = PerformanceAnalyzer.analyze(
                optimized_ir
            )

            self.output_text.insert(
                tk.END,
                "\n==============================\n"
            )

            self.output_text.insert(
                tk.END,
                "     PERFORMANCE ANALYSIS\n"
            )

            self.output_text.insert(
                tk.END,
                "==============================\n\n"
            )

            for k, v in analysis.items():

                self.output_text.insert(
                    tk.END,
                    f"{k}: {v}\n"
                )

            self.output_text.insert(
                tk.END,
                "\nOptimization completed successfully.\n"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )


# =====================================
# MAIN PROGRAM
# =====================================

if __name__ == "__main__":

    root = tk.Tk()

    app = CompilerGUI(root)

    root.mainloop()
