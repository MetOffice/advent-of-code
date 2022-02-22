MODULE submarine_mod
    IMPLICIT NONE 
    ! Define the type here and any method names
    ! PROCEDURE, PASS (this) :: proc
    TYPE :: Submarine
        INTEGER :: depth
        INTEGER :: horizontal_position

        CONTAINS
            PROCEDURE, PASS(this) :: move
            PROCEDURE, PASS(this) :: execute_course

    END TYPE

    INTERFACE Submarine
        MODULE PROCEDURE submarine_constructor 
    END INTERFACE

    CONTAINS 

        TYPE (Submarine) FUNCTION submarine_constructor()

            IMPLICIT NONE
            submarine_constructor % depth = 0
            submarine_constructor % horizontal_position = 0

        END FUNCTION submarine_constructor
    ! all the methods
        SUBROUTINE move(this, command, value)
            IMPLICIT NONE
            CLASS (Submarine), INTENT(INOUT) :: this
            CHARACTER(LEN=*), INTENT(IN) :: command
            INTEGER, INTENT(IN) :: value

            IF (command == "forward") THEN
                this % horizontal_position = this % horizontal_position + value
            ELSEIF (command == "down") THEN
                this % depth = this % depth + value
            ELSEIF (command == "up") THEN !up
                this % depth = this % depth - value
            ELSE
                WRITE(6, *) "Unrecognised command:", command
            END IF

        END SUBROUTINE move

        SUBROUTINE execute_course(this, commands, values)
            IMPLICIT NONE
            CLASS(Submarine), INTENT(INOUT) :: this
            CHARACTER(LEN=*), INTENT(IN) :: commands(:)
            INTEGER, INTENT(IN) :: values(:) 

            INTEGER :: i

            DO i=1,SIZE(commands)
                CALL this % move(commands(i), values(i))
            END DO
        END SUBROUTINE execute_course
    ! setters tend to be subroutines

    ! getters tend to be functions
END MODULE submarine_mod