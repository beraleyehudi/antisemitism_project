In the project, we need to do two main things:

1. Study statistics in a text column.
2. Do small cleaning.

For these two actions, there is a folder called operational
It has two files:

1. Statistics – a general class with functions for statistics.
2. Cleaner – a general class for cleaning.

For each class, there is another class that runs it, uses it, and keeps the results for this project. The folder with them is called managers

For joining the classes and for saving the files, there is a file called manager with special information for this project – folder paths, dictionary shape, and more.

Also, there is a folder called file_actions It has files for each file type. These files have classes for working with the file types (here, they only write to files).
