(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(initial-frame-alist (quote ((fullscreen . maximized))))
 '(markdown-command "pandoc -f markdown -t html -s --mathjax --highlight-style pygments")
)

(define-key global-map (kbd "C-x e") 'multi-term)

;; ansys-mode

(add-to-list 'load-path "~/.emacs.d/ansys-mode")
(autoload 'ansys-mode "ansys-mode" "Activate ANSYS-Mode." 'interactive)

(add-to-list 'auto-mode-alist '("\\.mac$" . ansys-mode))
(add-to-list 'auto-mode-alist '("\\.dat$" . ansys-mode))
(add-to-list 'auto-mode-alist '("\\.inp$" . ansys-mode))
;; this is the suffix for "ANSYS Neutral Files" which include some APDL.
(add-to-list 'auto-mode-alist '("\\.anf$" . ansys-mode))

 (set-frame-font "Monaco:pixelsize=14") ;
  (dolist (charset '(han kana symbol cjk-misc bopomofo))
  (set-fontset-font (frame-parameter nil 'font)
                    charset
                   (font-spec :family "文泉驿微米黑" :size 16)
 ))

 ;;;;;;;;;;;;;;;;;
 ;;Auctex
 ;;;;;;;;;;;;;;;;;
 (load "auctex.el" nil t t)
 (load "preview-latex.el" nil t t)
 (setq TeX-auto-save t)
 (setq TeX-parse-self t)
 (setq-default TeX-master nil)
 (mapc (lambda (mode)
 (add-hook 'LaTeX-mode-hook mode))
       (list ;'auto-complete-mode
    'auto-fill-mode
    'LaTeX-math-mode
    'turn-on-reftex
    'linum-mode))
 (add-hook 'LaTeX-mode-hook
           (lambda ()
             (setq TeX-auto-untabify t     ; remove all tabs before saving
                   TeX-engine 'xetex       ; use xelatex default
                   TeX-show-compilation t) ; display compilation windows
             (TeX-global-PDF-mode t)       ; PDF mode enable, not plain
             (setq TeX-save-query nil)
             (imenu-add-menubar-index)
             (define-key LaTeX-mode-map (kbd "TAB") 'TeX-complete-symbol)))
 ; set pdf view tool
 (setq TeX-view-program-list '(("Evince" "evince %o")))
 (cond
  ((eq system-type 'windows-nt)
   (add-hook 'LaTeX-mode-hook
             (lambda ()
               (setq TeX-view-program-selection '((output-pdf "SumatraPDF")
                                                  (output-dvi "Yap"))))))

  ((eq system-type 'gnu/linux)
   (add-hook 'LaTeX-mode-hook
             (lambda ()
               (setq TeX-view-program-selection '((output-pdf "Evince")
                                                  (output-dvi "Evince")))))))
 ; XeLaTeX
 (add-hook 'LaTeX-mode-hook (lambda()
     (add-to-list 'TeX-command-list '("XeLaTeX" "%`xelatex%(mode)%' %t" TeX-run-TeX nil t))
     (setq TeX-command-default "XeLaTeX")
     (setq TeX-save-query  nil )
     (setq TeX-show-compilation t)
     ))


 (require 'cdlatex)

 (add-hook 'LaTeX-mode-hook 'turn-on-cdlatex)

;; (require 'ess-site)

(load-theme 'zenburn t)
