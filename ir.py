from dataclasses import dataclass
# FIX 1: Removed unused `import re`

@dataclass
class TACInstruction:
    op: str = ""
    arg1: str = ""
    arg2: str = ""
    result: str = ""

    def __repr__(self):
        if self.op == "=":
            return f"{self.result} = {self.arg1}"
        return f"{self.result} = {self.arg1} {self.op} {self.arg2}"

class IRGenerator:
    @staticmethod
    def parse_tac(code):
        instructions = []
        lines = [line.strip() for line in code.split('\n') if line.strip()]

        for line in lines:
            if '=' in line:
                # FIX 2: Split on the FIRST '=' only so that expressions like
                #         `t1 = a == b` (future equality ops) don't break parsing
                left, right = line.split('=', 1)
                left = left.strip()
                right = right.strip()

                matched = False
                for op in ['+', '-', '*', '/']:
                    if op in right:
                        # FIX 3: Split on first occurrence only so negative
                        #         numbers or repeated operators don't mis-split
                        parts = right.split(op, 1)
                        a, b = parts[0].strip(), parts[1].strip()
                        instructions.append(TACInstruction(op, a, b, left))
                        matched = True
                        break

                if not matched:
                    instructions.append(TACInstruction("=", right, "", left))

        return instructions
