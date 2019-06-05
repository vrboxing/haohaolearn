(TeX-add-style-hook
 "test"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "pzq"
    "article"
    "art10"
    "amsmath")
   (LaTeX-add-labels
    "eq:pzq"))
 :latex)

