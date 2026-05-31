class PerformanceAnalyzer:
    @staticmethod
    def analyze(ir):
        total = len(ir)
        assignments = sum(1 for i in ir if i.op == "=")
        operations  = sum(1 for i in ir if i.op in ('+', '-', '*', '/'))

        return {
            "total_instructions": total,
            "assignments"       : assignments,
            "arithmetic_ops"    : operations,
        }
