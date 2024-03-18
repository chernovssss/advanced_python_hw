def generate_latex_table(data: list[list]) -> str:
    table = ""
    table += "\\begin{center}\n"
    table += "\\begin{tabular}{|" + "c|" * len(data[0]) + "}\n"
    for row in data:
        table += " & ".join(row) + r"\\" + "\n"
    table += "\\end{tabular}\n"
    table += "\\end{center}\n"
    return table


def wrap_latex_table(*tex_parts) -> str:
    joined_parts = '\\n'.join(tex_parts)
    return r"""\documentclass{article}
\usepackage{graphicx}
\graphicspath{ {./artifacts/} }
\begin{document}""" + f"\n{joined_parts}" + r"""
\end{document}"""


def generate_latex_image(filename: str) -> str:
    return r"""\includegraphics{""" + filename + "}\n"


def main():
    data = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    print(generate_latex_table(data))


if __name__ == "__main__":
    main()
