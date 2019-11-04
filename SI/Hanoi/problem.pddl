(define (problem phanoi)
(:domain hanoi)
(:objects x y z k1 k2 k3 k4 k5)
(:init
    (lezy-na k1 k2)
    (lezy-na k2 k3)
    (lezy-na k3 k4)
    (lezy-na k4 k5)
    
    (pusty y)
    (pusty z)
    
    (wiekszy k5 k4)
    (wiekszy k5 k3)
    (wiekszy k5 k2)
    (wiekszy k5 k1)
    (lezy-na-paliku k5 x)
    
    (wiekszy k4 k3)
    (wiekszy k4 k2)
    (wiekszy k4 k1)
    (lezy-na-paliku k4 x)

    (wiekszy k3 k2)
    (wiekszy k3 k1)
    (lezy-na-paliku k3 x)

    (wiekszy k2 k1)
    (lezy-na-paliku k2 x)
    
    (lezy-na-paliku k1 x)
)
(:goal 
    (and

        (lezy-na-paliku k1 z)
        (lezy-na-paliku k2 z)
        (lezy-na-paliku k3 z)
        (lezy-na-paliku k4 z)
        (lezy-na-paliku k5 z)
        (lezy-na k1 k2)
        (lezy-na k2 k3)
        (lezy-na k3 k4)
        (lezy-na k4 k5)
        
        
        
    )
)
)