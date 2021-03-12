(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  ; 'YOUR-CODE-HERE
  (cons-stream 3 (map-stream (lambda (x) (+ x 3)) multiples-of-three)))

; https://github.com/sgalal/cs61a/blob/master/Homework/hw07/hw07.scm#L9
(define (rle s)
  ; 'YOUR-CODE-HERE
  (define (insert-or-incr x xs)
    (cond
      ((null? xs) (cons-stream (list x 1) nil))
      ((equal? x (car (car xs)))
        (cons-stream
          (list (car (car xs)) (+ 1 (car (cdr (car xs)))))
          (cdr-stream xs)))
      (else (cons-stream (car xs) (insert-or-incr x (cdr-stream xs))))))
  (define (helper xs acc)
    (if (null? xs)
      acc
      (helper (cdr-stream xs) (insert-or-incr (car xs) acc))))
  (helper s nil))
