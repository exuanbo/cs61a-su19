; https://github.com/yngz/cs61a/blob/master/lab/lab13/lab13_extra.scm#L46
(define-macro (switch expr cases)
  'YOUR-CODE-HERE
  (let ((val (eval expr)))
    (cons
      'cond
      (map
        (lambda (case) (cons (equal? val (car case)) (cdr case)))
        cases))))

(define (flatmap f x)
  'YOUR-CODE-HERE
  (define (helper x acc)
    (if (null? x)
      acc
      (helper
        (cdr x)
        (let ((val (f (car x))))
          (append
            acc
            (if (pair? val)
              val
              (list val)))))))
  (helper x nil))

(define (expand lst)
  'YOUR-CODE-HERE
  (define (helper s acc)
    (if (null? s)
      acc
        (helper
          (cdr s)
          (let ((first (car s)))
            (append
              acc
              (cond
                ((equal? first 'x) '(x r y f r))
                ((equal? first 'y) '(l f x l y))
                (else (list first))))))))
  (helper lst nil))

(define (interpret instr dist)
  'YOUR-CODE-HERE)

(define (apply-many n f x)
  (if (zero? n)
      x
      (apply-many (- n 1) f (f x))))

(define (dragon n d)
  (interpret (apply-many n expand '(f x)) d))
