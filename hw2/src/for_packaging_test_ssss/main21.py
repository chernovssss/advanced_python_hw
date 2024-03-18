import os

from pdflatex import PDFLaTeX

from latex_generator import generate_latex_table, wrap_latex_table, generate_latex_image


def save_latex(doc: str, save_dir: str,
               filename: str) -> None:
    with open(os.path.join(save_dir, filename), 'w+') as f:
        f.write(doc)


def main():
    data = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    table = generate_latex_table(data)
    image = generate_latex_image('image')
    document = wrap_latex_table(table, image)
    print(document)
    save_latex(document, 'artifacts', 'table.tex')
    tex_file = "artifacts/table.tex"
    pdl = PDFLaTeX.from_texfile(tex_file)
    pdl.create_pdf(keep_pdf_file=True)


if __name__ == "__main__":
    main()
