;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s)))

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cdr (cdr s))))

(define (unique s)
  'YOUR-CODE-HERE
  (if (null? s)
    nil
    (cons
      (car s)
      (unique
        (filter
          (lambda (x) (not (equal? x (car s))))
          (cdr s))))))

(define (cons-all first rests)
  (map (lambda (s) (cons first s)) rests))

;; List all ways to make change for TOTAL with DENOMS
; https://github.com/sgalal/cs61a/blob/master/Homework/hw06/hw06.scm#L48
(define (list-change total denoms)
  'YOUR-CODE-HERE
  (define (helper n xs)
    (if (null? xs)
      nil
      (if (= 0 n)
        '(nil)
        (if (< n (car xs))
          (helper n (cdr xs))
          (append
            (cons-all (car xs) (helper (- n (car xs)) denoms))
            (list-change n (cdr xs)))))))
  (helper total denoms))

; Tail recursion

(define (replicate x n)
  'YOUR-CODE-HERE
  (define (helper n acc)
    (if (= n 0)
      acc
      (helper (- n 1) (cons x acc))))
  (helper n nil))

(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (if (= n 0)
    start
    (combiner (term n) (accumulate combiner start (- n 1) term))))

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
  (define (helper n acc)
    (if (= n 0)
      acc
      (helper (- n 1) (combiner acc (term n)))))
  (helper n start))


; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst)))
