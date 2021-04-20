(DEFUN demo()
    (setq fp (open "theString.txt" :direction :input))
    (setq l (read fp "done"))
    (princ "processing ")
    (princ l)
    (fsa l)
)

(DEFUN fsa(l)
    (cond
        ((null l) (princ "String invalid"))
        (t(stateZero l))
    )
    
)

(DEFUN stateZero(l)
    (cond
        ((null l) (princ "String Rejected!"))
        ((equal 'x (car l)) (stateZero(cdr l)))
        ((equal 'y (car l)) (stateOne(cdr l)))
        (t (princ "String invalid"))
    )
)

(DEFUN stateOne(l)
    ;(cdr l)
    (cond
        ((null l) (princ "String Accepted!"))
        ((equal 'x (car l)) (stateTwo(cdr l)))
        (t (princ "State 1: String invalid"))
    )
)

(DEFUN stateTwo(l)
    (cond
        ((null l) (princ "String Rejected!"))
        ((equal 'x (car l)) (stateTwo(cdr l)))
        ((equal 'y (car l)) (stateThree(cdr l)))
        (t (princ "State 2: String invalid"))
    )
)

(DEFUN stateThree(l)
    (cond
        ((null l) (princ "String Accepted!"))
        ((equal 'x (car l)) (stateThree(cdr l)))
        ((equal 'z (car l)) (stateFour(cdr l)))
        (t (princ "State 3: String invalid"))
    )
)

(DEFUN stateFour(l)
    (cond
        ((null l) (princ "String Rejected!"))
        ((equal 'x (car l)) (stateFour(cdr l)))
        ((equal 'a (car l)) (stateOne(cdr l)))
        (t (princ "State 4: String invalid"))
    )
)