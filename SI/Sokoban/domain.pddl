(define
    (domain sokoban)
    (:requirements :adl)
    (:predicates
        (paczka ?x)
        (cel ?x)
        (robot ?x)
        (poziomo ?x ?y)
        (pionowo ?x ?y)

    )
    (:action idz-poziomo
        :parameters (?x ?y)
        :precondition
        (and
            (poziomo ?x ?y)
            (robot ?x)
            (not (paczka ?y))
            (not (robot ?y))
        )
        :effect
        (and
            (robot ?y)
            (not (robot ?x))
        )
    )
    (:action idz-pionowo
        :parameters (?x ?y)
        :precondition
        (and
            (pionowo ?x ?y)
            (robot ?x)
            (not (paczka ?y))
            (not (robot ?y))
        )
        :effect
        (and
            (robot ?y)
            (not (robot ?x))
        )
    )
    (:action pchaj-poziomo
        :parameters (?x ?y ?z)
        :precondition
        (and
            (robot ?x)
            (poziomo ?x ?y)
            (poziomo ?y ?z)
            (not (poziomo ?x ?z))
            (paczka ?y)
            (not (paczka ?z))
            (not (robot ?y))
            (not (robot ?z))
        )
        :effect
        (and
            (robot ?y)
            (paczka ?z)
            (not (robot ?x))
            (not (paczka ?y))
        )
    )
    (:action pchaj-pionowo
        :parameters (?x ?y ?z)
        :precondition
        (and
            (robot ?x)
            (pionowo ?x ?y)
            (pionowo ?y ?z)
            (not (pionowo ?x ?z))
            (paczka ?y)
            (not (paczka ?z))
            (not (robot ?y))
            (not (robot ?z))
        )
        :effect
        (and
            (robot ?y)
            (paczka ?z)
            (not (robot ?x))
            (not (paczka ?y))
        )
    )
)