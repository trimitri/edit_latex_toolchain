from anki import latex

latex.pngCommands = [
    ["xelatex", "-interaction=nonstopmode", "tmp.tex"],
    ["pdfcrop", "--margins", ".5 .5 .5 .5", "tmp.pdf", "tmp.pdf"],
    ["convert", "-trim", "-density", "600", "-resize", "50%", "tmp.pdf", "tmp.png"]
]

latex.svgCommands = [
    ["xelatex", "-interaction=nonstopmode", "-no-pdf", "tmp.tex"],
    ["dvisvgm", "--no-fonts", "-Z", "2", "tmp.xdv", "-o", "tmp.svg"]
]
