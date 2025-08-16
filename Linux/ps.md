## to only check a single process

> ### ps -eaf | grep <process name> 
- e
    - Meaning: Select all processes.
    - Explanation: This option ensures that processes for all users, including system processes, are displayed.

- a
    - Meaning: Show processes for all users except session leaders (e.g., login shells) and processes without a terminal.
    - Explanation: It includes processes not associated with the current terminal but excludes very low-level processes.

- f
    - Meaning: Full-format listing.
    - Explanation: Provides additional information about each process, including parent process IDs and start times.

> ### top -p <root id>
 from this take the root id of the process and do
