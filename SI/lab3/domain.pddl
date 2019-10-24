;Header and description

(define (domain hanoi)

;remove requirements that are not needed
  (:requirements :adl)

  (:predicates ;todo: define predicates here
    (on-block ?x ?y)
    (on-stick ?x ?y)
    (empty ?x)
    (bigger ?x ?y)
  )

  (:action move-to-empty-last-block
    :parameters (?b ?s1 ?s2)
    :precondition (and 
      (on-stick ?s1 ?b)
      (not (on-stick ?s2 ?b))
      (not (empty ?s1))
      (empty ?s2)
      (not (exists (?b2) (on-block ?b ?b2)))
      (not (exists (?b2) (on-block ?b2 ?b)))
    )
    :effect (and 
      (empty ?s1)
      (not (empty ?s2))
      (on-stick ?s2 ?b)
      (not (on-stick ?s1 ?b))
    )
  )

  (:action move-not-empty-to-empty
    :parameters (?b1 ?b2 ?s1 ?s2)
    :precondition (and 
      (on-stick ?s1 ?b1)
      (on-stick ?s1 ?b2)
      (not (on-stick ?s2 ?b1))
      (not (on-stick ?s2 ?b2))
      (exists (?b) (on-block ?b1 ?b))
      (on-block ?b1 ?b2)
      (empty ?s2)
      (not (empty ?s1))
    )
    :effect (and 
      (not (empty ?s2))
      (not (on-block ?b1 ?b2))
      (not (on-stick ?s1 ?b1))
      (on-stick ?s2 ?b1)
    )
  )

  (:action move-not-empty-to-not-empty
      :parameters (?b1 ?b2 ?b3 ?s1 ?s2)
      :precondition (and
        (not (empty ?s2))
        (not (empty ?s1))
        (on-stick ?s1 ?b1)
        (on-stick ?s1 ?b2)
        (not (on-stick ?s1 ?b3))

        (not (on-stick ?s2 ?b1))
        (not (on-stick ?s2 ?b2))
        (on-stick ?s2 ?b3)

        (on-block ?b1 ?b2)
        (not (on-block ?b1 ?b3))
        (bigger ?b1 ?b3)
      )
      :effect (and
        (not (on-stick ?s1 ?b1))
        (on-stick ?s2 ?b1)
        (on-block ?b1 ?b3)
        (not (on-block ?b1 ?b2))
      )
  )

  (:action move-to-not-empty-last-block
      :parameters (?b1 ?b2 ?s1 ?s2)
      :precondition (and
        (not (empty ?s2))
        (not (empty ?s1))
        (on-stick ?s1 ?b1)
        (not (on-stick ?s1 ?b2))

        (not (on-stick ?s2 ?b1))
        (on-stick ?s2 ?b2)

        (not (on-block ?b1 ?b2))
        (bigger ?b1 ?b2)
      )
      :effect (and
        (empty ?s1)
        (on-block ?b1 ?b2)
        (not (on-stick ?s1 ?b1))
        (on-stick ?s2 ?b1)
      )
  )

)
