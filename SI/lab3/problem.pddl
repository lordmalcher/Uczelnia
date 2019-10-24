(define (problem phanoi) (:domain hanoi)
(:objects 
  s1 s2 s3 b1 b2 b3 b4 b5
)

(:init
    ;todo: put the initial state's facts and numeric values here
  (on-block b5 b4)
  (on-block b4 b3)
  (on-block b3 b2)
  (on-block b2 b1)
  
  (empty s2)
  (empty s3)

  (bigger b1 b2)
  (bigger b1 b3)
  (bigger b1 b4)
  (bigger b1 b5)

  (bigger b2 b3)
  (bigger b2 b4)
  (bigger b2 b5)

  (bigger b3 b4)
  (bigger b3 b5)

  (bigger b4 b5) 

  (on-stick s1 b1) 
  (on-stick s1 b2) 
  (on-stick s1 b3) 
  (on-stick s1 b4) 
  (on-stick s1 b5) 
)

(:goal (and
  ;todo: put the goal condition here
  (on-stick s3 b1)
  (on-stick s3 b2)
  (on-stick s3 b3)
  (on-stick s3 b4)
  (on-stick s3 b5)

  (on-block b5 b4)
  (on-block b4 b3)
  (on-block b3 b2)
  (on-block b2 b1)
))

;un-comment the following line if metric is needed
; (
  :metric minimize (???))
)
