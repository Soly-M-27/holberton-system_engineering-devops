Redirections
1. Write script to display "Hello, World": echo "Hello, World"
2. Write a script that displays a confused smiley face: echo $'(Ôo)''
3. Display content of the /etc/passwd file: cat < file
4. Display 2 files at once: cat file1 file2
5. Display last 11 lines on file: tail -n 11 file
6. Display first 10 lines on a file: head -n 10 file
7. Create a file with special symbols and write "Best School" inside it: echo 'Best School' > "\*\\\\'\"Best School\"\\'\\\\*$\\?\\*\\*\\*\\*\\*:)" [some of the \\ are as ||. All || are actually\\, vim reformats it when a \\ is confronted by a * * encasing, hence if \\ goes inside of the encasement of * * it will do this *\\*.]
8. Write a script that writes the contents of ls -la: ls -la > file
9. Write a script that duplicates the last line of the file iacta: tail -n 1 samefile >> samefile
10. Script that deletes all regulat files with a .js extension present in cd:
11. Count the number of directories and subdirectories: find . -mindepth type -d | wc -l
12. Displays the 10 newest files in the cd: ls -1t | head -10
13. Displays Unique lines: sort | uniq -u
14. Display lines containg the pattern "root" in the file: grep root file
15. Display the number of lines that contain the pattern "bin" in file: grep -c file
16. Display lines containing the pattern "root" and 3 lines after them in file: grep root -A3 file
17. Display all the lines in the file that do not contain pattern "bin": grep -v bin file
18. Display all lines of the file starting with a letter: 
19. Replace all characters A and c from input to Z and e respectively: tr Ac Ze
20. Remove all letters c and C from input: tr -d Cc
21. Reverse its input: rev
22. Display all users and their home directories, sorted by users: cut -d: -f1,6 /etc/passwd | sort -k1
