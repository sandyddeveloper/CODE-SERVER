Here’s a comprehensive guide to Linux commands organized by category:

---

### **1. File and Directory Commands**  
- **`ls`**: List files and directories.  
  - `ls -a`: Include hidden files.  
  - `ls -l`: Long format with permissions.  
- **`pwd`**: Print the current working directory.  
- **`cd [directory]`**: Change the current directory.  
- **`mkdir [directory]`**: Create a new directory.  
  - `mkdir -p [parent/child]`: Create parent and child directories.  
- **`rmdir [directory]`**: Remove an empty directory.  
- **`rm [file]`**: Remove a file.  
  - `rm -r [directory]`: Remove a directory recursively.  
- **`cp [source] [destination]`**: Copy files and directories.  
- **`mv [source] [destination]`**: Move or rename files and directories.  
- **`find [path] -name [name]`**: Search for files or directories.  
- **`locate [name]`**: Quickly locate files (use `updatedb` to update the database).  
- **`touch [file]`**: Create an empty file.  

---

### **2. File Viewing and Editing**  
- **`cat [file]`**: Display the contents of a file.  
- **`less [file]`**: View file content with scrolling.  
- **`more [file]`**: Similar to `less`, but simpler.  
- **`head [file]`**: Display the first 10 lines of a file.  
- **`tail [file]`**: Display the last 10 lines of a file.  
  - `tail -f [file]`: Monitor a file in real-time.  
- **`nano [file]`**: Edit a file with the Nano editor.  
- **`vim [file]`**: Edit a file with Vim.  
- **`diff [file1] [file2]`**: Compare two files line by line.  

---

### **3. Permissions and Ownership**  
- **`chmod [mode] [file]`**: Change file permissions.  
  - Example: `chmod 755 file` (rwxr-xr-x).  
- **`chown [user]:[group] [file]`**: Change file owner and group.  
- **`umask [permissions]`**: Set default permissions for new files.  

---

### **4. Process Management**  
- **`ps`**: View active processes.  
  - `ps aux`: Detailed view of all processes.  
- **`top`**: Real-time view of system processes.  
- **`htop`**: Enhanced process viewer (if installed).  
- **`kill [PID]`**: Kill a process by its ID.  
- **`killall [name]`**: Kill processes by name.  
- **`jobs`**: List background jobs.  
- **`bg [job]`**: Resume a background job.  
- **`fg [job]`**: Bring a background job to the foreground.  

---

### **5. Networking**  
- **`ping [host]`**: Check connectivity to a host.  
- **`ifconfig`**: Display network interfaces (deprecated; use `ip addr`).  
- **`ip addr`**: Show IP address and interface info.  
- **`netstat -tuln`**: View open ports and connections.  
- **`curl [url]`**: Fetch a URL's content.  
- **`wget [url]`**: Download files from a URL.  
- **`scp [source] [destination]`**: Securely copy files between systems.  
- **`ssh [user]@[host]`**: Securely log into a remote system.  

---

### **6. Disk and Storage**  
- **`df -h`**: Display free disk space.  
- **`du -sh [directory]`**: Show size of a directory.  
- **`mount [device] [directory]`**: Mount a device.  
- **`umount [device]`**: Unmount a device.  
- **`fdisk -l`**: Show disk partition information.  
- **`mkfs`**: Format a disk partition.  

---

### **7. Archiving and Compression**  
- **`tar -cvf [file.tar] [files]`**: Create a tar archive.  
- **`tar -xvf [file.tar]`**: Extract a tar archive.  
- **`gzip [file]`**: Compress a file.  
- **`gunzip [file.gz]`**: Decompress a `.gz` file.  
- **`zip [file.zip] [files]`**: Create a zip archive.  
- **`unzip [file.zip]`**: Extract a zip archive.  

---

### **8. User Management**  
- **`whoami`**: Display the current user.  
- **`who`**: See who is logged in.  
- **`id`**: Show user ID and group info.  
- **`adduser [user]`**: Add a new user.  
- **`deluser [user]`**: Remove a user.  
- **`passwd [user]`**: Change a user's password.  

---

### **9. System Monitoring and Information**  
- **`uptime`**: Show system uptime.  
- **`uname -a`**: Display system information.  
- **`free -h`**: Show memory usage.  
- **`vmstat`**: View system performance.  
- **`iostat`**: Display CPU and I/O statistics.  
- **`dmesg`**: Display boot and kernel messages.  

---

### **10. Package Management (Ubuntu/Debian)**  
- **`apt update`**: Update package lists.  
- **`apt upgrade`**: Upgrade all installed packages.  
- **`apt install [package]`**: Install a package.  
- **`apt remove [package]`**: Remove a package.  
- **`dpkg -i [package.deb]`**: Install a `.deb` package.  
- **`snap install [package]`**: Install Snap packages.  

---

### **11. Search and Grep**  
- **`grep [pattern] [file]`**: Search for a pattern in a file.  
- **`grep -r [pattern] [directory]`**: Recursive search.  
- **`awk`**: Advanced text processing.  
- **`sed`**: Stream editor for modifying text.  

---

### **12. System Shutdown and Restart**  
- **`shutdown now`**: Shut down immediately.  
- **`shutdown -r now`**: Restart the system.  
- **`reboot`**: Restart the system.  

---

### **13. Miscellaneous Commands**  
- **`alias [name]='[command]'`**: Create a shortcut command.  
- **`history`**: View command history.  
- **`clear`**: Clear the terminal screen.  
- **`echo [text]`**: Print text to the terminal.  
- **`date`**: Show the current date and time.  

---

This covers a broad range of Linux commands. Let me know if you need detailed explanations or examples for any of them!
