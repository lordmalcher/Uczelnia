(define
    (domain hanoi)
    (:requirements :adl)
    (:predicates
        (pusty ?x)
        (lezy-na ?x ?y)
        (wiekszy ?x ?y)
        (lezy-na-paliku ?x ?y)
    )
    (:action przesun-na-pusty-i-zrob-pusty
        :parameters (?x ?y ?z)
        :precondition
        (and
            (pusty ?y)  ;palik na ktory przesuwam jest pusty
            (not (pusty ?x)) ;palik z ktorego przesuwam nie jest pusty
            (lezy-na-paliku ?z ?x) ;krazek lezy na paliku z ktorego przesuwam
            
            (not (exists (?f) (lezy-na ?f ?z) )) ;nic nie lezy na krazku ktory przesuwam
            (not (exists (?f) (lezy-na ?z ?f) )) ;krazek ktory przesuwam nie lezy na innym krazku 
            
            (not (lezy-na-paliku ?z ?y))
        )
        :effect
        (and
            (not (pusty ?y))    ;palik na ktory przesuwam przestal byc pusty
            (pusty ?x)          ;palik z ktorego przesuwam zaczal byc pusty
            (lezy-na-paliku ?z ?y)  ;krazek ktory przesunalem lezy na innym paliku
            (not (lezy-na-paliku ?z ?x)) ; i przestal lezec na tamtym
        )
    )
    (:action przesun-na-pusty-i-tam-cos-nadal-lezy
        :parameters (?x ?y ?z ?w)
        :precondition
        (and
            (pusty ?y)          ;palik na ktory przesuwam jest pusty
            (not (pusty ?x))    ;palik z ktorego przesuwam nie jest pusty
            (lezy-na-paliku ?z ?x)  ;krazek lezy na paliku z ktorego przesuwam
            (not (exists (?f) (lezy-na ?f ?z) )) ;nic nie lezy na krazku ktory przesuwam
            (exists (?f) (lezy-na ?z ?f) ) ;krazek ktory przesuwam lezy na innym krazku
            (lezy-na ?z ?w) ;krazek lezy na innym krazku
            (lezy-na-paliku ?w ?x)
            (not (lezy-na-paliku ?z ?y))
        )
        :effect
        (and
            (not (pusty ?y))    ;palik na ktory przesuwam przestal byc pusty
            (lezy-na-paliku ?z ?y) ;krazek ktory przesunalem lezy na innym paliku
            (not (lezy-na-paliku ?z ?x)) ; i przestal lezec na tamtym
            (not (lezy-na ?z ?w))   ;krazek juz nie lezy na tamtym krazku
        )
    )
    (:action przesun-na-nie-pusty-i-zrob-pusty
        :parameters (?x ?y ?z ?w)
        :precondition
        (and
            (not (pusty ?y))  ;palik na ktory przesuwam nie jest pusty
            (not (pusty ?x)) ;palik z ktorego przesuwam nie jest pusty
            (lezy-na-paliku ?z ?x) ;krazek lezy na paliku z ktorego przesuwam
            (not (exists (?f) (lezy-na ?f ?z) )) ;nic nie lezy na krazku ktory przesuwam
            (not (exists (?f) (lezy-na ?z ?f) )) ;krazek ktory przesuwam nie lezy na innym krazku
            (not (exists (?f) (lezy-na ?f ?w))) ; na krazku w nic nie lezy
            (lezy-na-paliku ?w ?y)  ;inny krazek lezy na tym paliku
            (wiekszy ?w ?z) ;przesuwam mniejszy krazek na wiekszy 
            
            (not (lezy-na-paliku ?z ?y))
        )
        :effect
        (and
            (not (pusty ?y))    ;palik na ktory przesuwam przestal byc pusty
            (pusty ?x)          ;palik z ktorego przesuwam zaczal byc pusty
            (lezy-na-paliku ?z ?y)  ;krazek ktory przesunalem lezy na innym paliku
            (not (lezy-na-paliku ?z ?x)) ; i przestal lezec na tamtym 
            (lezy-na ?z ?w) ;przesuniety krazek lezy na wiekszym krazku
        )
    )
    (:action przesun-na-nie-pusty-i-tam-cos-nadal-lezy
        :parameters (?skad ?dokad ?z ?na-tym-bedzie-lezec ?na-tym-lezalo)
        :precondition
        (and
            (not (pusty ?dokad))  ;palik na ktory przesuwam nie jest pusty
            (not (pusty ?skad)) ;palik z ktorego przesuwam nie jest pusty
            (lezy-na-paliku ?z ?skad) ;krazek lezy na paliku z ktorego przesuwam
            (not (exists (?f) (lezy-na ?f ?z) )) ;nic nie lezy na krazku ktory przesuwam
            (exists (?f) (lezy-na ?z ?f) ) ;krazek ktory przesuwam lezy na innym krazku
            (not (exists (?f) (lezy-na ?f ?na-tym-bedzie-lezec)))
            (lezy-na-paliku ?na-tym-bedzie-lezec ?dokad)  ;inny krazek lezy na tym paliku
            (wiekszy ?na-tym-bedzie-lezec ?z) ;przesuwam mniejszy krazek na wiekszy 
            (lezy-na ?z ?na-tym-lezalo) ;moj krazek lezy na krazku w2
            (not (lezy-na-paliku ?z ?dokad))
        )
        :effect
        (and
            (lezy-na-paliku ?z ?dokad)  ;krazek ktory przesunalem lezy na innym paliku
            (not (lezy-na-paliku ?z ?skad)) ; i przestal lezec na tamtym 
            (lezy-na ?z ?na-tym-bedzie-lezec) ;przesuniety krazek lezy na wiekszym krazku
            (not (lezy-na ?z ?na-tym-lezalo))
        )
    )
)