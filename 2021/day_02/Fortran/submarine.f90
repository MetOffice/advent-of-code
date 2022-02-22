PROGRAM submarine_prog
    ! Need a submarine module with submarine type in it
    ! TO COMPILE: from the day_02 dir 
    !     ifort -o day_02.out Fortran/reader_mod.f90 Fortran/submarine.f90
    ! TO RUN: ./day_02.out
    USE reader_mod, ONLY: &
        read_submarine_commands

    USE submarine_mod, ONLY: &
        Submarine

    IMPLICIT NONE

    CHARACTER(LEN=7), ALLOCATABLE :: commands(:)
    INTEGER, ALLOCATABLE :: values(:)
    INTEGER :: num_commands
    TYPE(Submarine) :: sub
    INTEGER :: i
    

    CALL read_submarine_commands("input.txt", num_commands, commands, values)
    
    WRITE(6, "(A10, I4, A6)") "There are ", num_commands, " lines"
    ! DO i=1, num_commands
    !     WRITE(6, "(A7, I2)") commands(i), values(i)
    ! END DO

    sub = Submarine()

    CALL sub % execute_course(commands, values)

    WRITE(6, *) "Result is :", sub % depth * sub % horizontal_position


END PROGRAM submarine_prog