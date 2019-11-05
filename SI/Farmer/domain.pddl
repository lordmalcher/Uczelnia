(define
  (domain farmer)

  (:requirements :adl)

  (:predicates
    (side ?item ?side)
    (eats ?item1 ?item2)
    (person ?farmer)
  )



  (:action move-to-other-side
    :parameters (?item ?side ?other-side ?farmer)
    :precondition (and 
      (side ?farmer ?side) ;farmer na lewej stronie
      (side ?item ?side) ;rzecz do przesunięcia na lewej stronie
      (not (= ?side ?other-side))
      (person ?farmer)
      ;(not (exists (?f ?g) ;nie istnieją f i g które
      ;  (and 
      ;    (eats ?f ?g) ;się zjadają
      ;    (side ?f ?side) ;i są na lewej stronie
      ;    (side ?g ?side)
      ;  )
      ;  )
      ;)
    )
    :effect (and
      (side ?farmer ?other-side)
      (side ?item ?other-side)
    )
  )

  (:action swim-alone
    :parameters (?side ?other-side ?farmer)
    ::precondition (and 
      (side ?farmer ?side)
      (person ?farmer)
      (not (= ?side ?other-side))
    )
    :effect (and 
      (side ?farmer ?other-side)
    )
  )


)