;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
)

(define (caddr s)
  'YOUR-CODE-HERE
)

(define (unique s)
  'YOUR-CODE-HERE
)

(define (cons-all first rests)
  'replace-this-line)

;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  'YOUR-CODE-HERE
  )

; Tail recursion

(define (replicate x n)
  'YOUR-CODE-HERE
  )

(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
)

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
)


; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
)