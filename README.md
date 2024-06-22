# 361 - HW4

2022-2023 Spring Semester

This program is a web server that handles one HTTP request at a time. This web server reads a html file in the server directory and displays it in the browser. If a file is requested that is not in the server directory, an error message will appear in the browser. 

## Modules
The following module(s) that were installed for this program are listed below: 
- socket: Socket programming. 

## Compilation
1. Open VScode or use a terminal.  
2. Change your terminal directory to that of which this project folder is saved to
3. In the terminal, type the following into the command line: 
    ```python webServer.py```
   * The following will display: 
    ```
        Ready to serve...
    ```
4. Open an Internet Browser and type the following: 
    ```
        http://localhost:6789/HelloWorld.html
    ```
   * The html file included in this project is titled ```HelloWorld.html```
5. The following will be displayed in the browser: 
    ```
        Hello World!
    ```
   * The title of the window will be ```361 HW 4```
6. For testing the 404 Error Message, set up the program as specified in step 3, then proceed to step 7.
7. Open an Internet Broswer and type 1 of the following: 
    ```
        http://localhost:6789/NotHelloWorld.html

        or...

        http://localhost:6789
    ```
   * The following will be displayed in the browser after either of the instance mentioned above: 
    ```
        404 Not Found
    ```
   * The title of the window will be either ```http://localhost:6789/NotHelloWorld.html``` or ```http://localhost:6789``` depending on which instance mentioned in step 7. 