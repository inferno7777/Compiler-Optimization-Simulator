from ir import TACInstruction


def is_number(value):
    try:
        float(value)
        return True
    except:
        return False


class OptimizationEngine:

    def __init__(self, instructions):
        self.instructions = instructions

    # =========================
    # CONSTANT FOLDING
    # =========================

    def constant_folding(self):

        optimized = []

        for instr in self.instructions:

            if instr.op in ['+', '-', '*', '/']:

                if is_number(instr.arg1) and is_number(instr.arg2):

                    a = float(instr.arg1)
                    b = float(instr.arg2)

                    if instr.op == '+':
                        result = a + b

                    elif instr.op == '-':
                        result = a - b

                    elif instr.op == '*':
                        result = a * b

                    elif instr.op == '/':
                        result = a / b

                    if result == int(result):
                        result = int(result)

                    optimized.append(
                        TACInstruction(
                            "=",
                            str(result),
                            "",
                            instr.result
                        )
                    )

                else:
                    optimized.append(instr)

            else:
                optimized.append(instr)

        return optimized

    # =========================
    # CONSTANT PROPAGATION
    # =========================

    def constant_propagation(self):

        constants = {}

        optimized = []

        for instr in self.instructions:

            if instr.op == "=" and is_number(instr.arg1):
                constants[instr.result] = instr.arg1

            arg1 = constants.get(instr.arg1, instr.arg1)
            arg2 = constants.get(instr.arg2, instr.arg2)

            optimized.append(
                TACInstruction(
                    instr.op,
                    arg1,
                    arg2,
                    instr.result
                )
            )

        return optimized

    # =========================
    # ALGEBRAIC SIMPLIFICATION
    # =========================

    def algebraic_simplification(self):

        optimized = []

        for instr in self.instructions:

            # x * 1 -> x
            if instr.op == "*" and instr.arg2 == "1":

                optimized.append(
                    TACInstruction(
                        "=",
                        instr.arg1,
                        "",
                        instr.result
                    )
                )

            # 1 * x -> x
            elif instr.op == "*" and instr.arg1 == "1":

                optimized.append(
                    TACInstruction(
                        "=",
                        instr.arg2,
                        "",
                        instr.result
                    )
                )

            # x + 0 -> x
            elif instr.op == "+" and instr.arg2 == "0":

                optimized.append(
                    TACInstruction(
                        "=",
                        instr.arg1,
                        "",
                        instr.result
                    )
                )

            # 0 + x -> x
            elif instr.op == "+" and instr.arg1 == "0":

                optimized.append(
                    TACInstruction(
                        "=",
                        instr.arg2,
                        "",
                        instr.result
                    )
                )

            else:
                optimized.append(instr)

        return optimized
