from anki import latex

latex.pngCommands = [
    ["xelatex", "-interaction=nonstopmode", "tmp.tex"],
    ["dvipng", "-D", "200", "-T", "tight", "tmp.dvi", "-o", "tmp.png"]
]

latex.svgCommands = [
    ["xelatex", "-interaction=nonstopmode", "tmp.tex"],
    ["dvisvgm", "--no-fonts", "-Z", "2", "tmp.dvi", "-o", "tmp.svg"]
]
