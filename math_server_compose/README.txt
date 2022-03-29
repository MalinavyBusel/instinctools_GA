running the application:
    open in cmd the directory with docker-compose file
    and run the command "docker compose up -d"

flask server:
    open in your browser the address "localhost:5000"
    '/' - main page
    '/calculator' - page for processing calculations
                    format of input - a string like 'operator number1 number2'
    '/operations' - full list of available operations
    '/full_hist' - the history of operations with filtering options

socket server:
    With the help of socket client listen to localhost:65432
    format of input - a string like 'operator number1 number2'
