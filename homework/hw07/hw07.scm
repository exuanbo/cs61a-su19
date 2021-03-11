(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  'YOUR-CODE-HERE
)

(define (rle s)
  'YOUR-CODE-HERE
)