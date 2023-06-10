## Attendance Tracker

Microservice that tracks gym users activity.

## DB Set Up

Install MySQL. Instruction for Ubuntu: [Link](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04) \
Install WorkBench. Instruction for Ubuntu: [Link](https://phoenixnap.com/kb/mysql-workbench-ubuntu)

Run following commands.

```
CREATE DATABASE gym;
CREATE TABLE attendance (id INT AUTO_INCREMENT PRIMARY KEY, user_id CHAR(10), start_time DATETIME, end_time DATETIME);
```