(define (problem pfarmer)
(:domain farmer)

  (:objects 
    wilk owca kapusta left-side right-side farmer
  )

  (:init
    (side wilk left-side)
    (side owca left-side)
    (side kapusta left-side)
    (side farmer left-side)

    (eats wilk owca)
    (eats owca wilk)
    (eats owca kapusta)
    (eats kapusta owca)

    (person farmer)
  )

  (:goal (and
    (side wilk right-side)
    (side owca right-side)
    (side kapusta right-side)
    (side farmer right-side)
  ))
)
