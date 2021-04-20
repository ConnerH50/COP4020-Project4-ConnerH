(DEFUN demo()
    (setq fp (open "theString.txt" :direction :input))
    (setq l (read fp "done"))
    (princ "processing ")
    (princ l)
    (fsa l)
)

(DEFUN fsa(l)
    (stateZero l)
)

(DEFUN stateZero(l)
    ;(cdr l)
    (cond
        ((null l) (princ "List invalid"))
        ((equal 'x (car l)) (stateZero(cdr l)))
        ((equal 'y (car l)) (stateOne(cdr l)))
        (t (princ "List invalid"))
    )
)

(DEFUN stateOne(l)
    (cdr l)
)

(DEFUN stateTwo(l)

)

(DEFUN stateThree(l)

)

(DEFUN stateFour(l)

)