(TeX-add-style-hook
 "code"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "tikz"))
 :latex)

