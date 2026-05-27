from lexer import Lexer
from ir import IRGenerator
from analyzer import PerformanceAnalyzer

def main():
    print("Compiler Optimization Simulator\n")

    print("Enter TAC (blank line to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    code = "\n".join(lines)

    # Lexical Analysis
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    print("\n🔹 Tokens:")
    for tok in tokens:
        if tok.type.value != "EOF":
            print(f"  {tok}")

    # IR Generation
    ir = IRGenerator.parse_tac(code)

    print("\n🔹 IR (Three Address Code):")
    for instr in ir:
        print(f"  {instr}")

    # Analysis
    print("\n🔹 Analysis:")
    result = PerformanceAnalyzer.analyze(ir)
    for k, v in result.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
