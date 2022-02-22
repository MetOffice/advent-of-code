MODULE reader_mod

    IMPLICIT NONE
    CONTAINS

        SUBROUTINE read_submarine_commands(input_file, &
                                           number_commands, &
                                           commands,  &
                                           values)
            CHARACTER(LEN=*), INTENT(IN)               :: input_file
            CHARACTER(LEN=7), ALLOCATABLE, INTENT(OUT) :: commands(:)
            INTEGER, ALLOCATABLE, INTENT(OUT)          :: values(:)
            INTEGER, INTENT(OUT)                       :: number_commands
            INTEGER, PARAMETER                         :: read_unit = 1 ! giving the UNIT NUMBER 
            
            INTEGER :: io
            INTEGER :: i
            CHARACTER(LEN=10) :: line
            
            number_commands = 0
            io=0
            OPEN(read_unit, file=input_file)

            DO 
                READ(read_unit, *, iostat=io) !TODO: whats iostat
                IF (io < 0) EXIT
                number_commands = number_commands + 1

            END DO
            
            ALLOCATE(commands(number_commands))
            ALLOCATE(values(number_commands))

            REWIND(read_unit)
            
            DO i = 1,number_commands
                READ(read_unit, "(A)") line
                
                IF (line(1:1) == "u") THEN
                    commands(i) = "up"
                    READ(line(4:), *) values(i)

                ELSE IF(line(1:1) == "d") THEN
                    commands(i) = "down"
                    READ(line(6:), *) values(i)

                ELSE 
                    commands(i) = "forward"
                    READ(line(9:), *) values(i)
                END IF

            END DO

            CLOSE(read_unit)
        END SUBROUTINE read_submarine_commands
END MODULE reader_mod
