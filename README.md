## Attendance Tracker

Microservice that tracks gym users activity.

## DB Set Up

Install MySQL on your system.
Great instruction for Ubuntu: [Link](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

Run following commands.

```
CREATE DATABASE gym;
CREATE TABLE attendance (id INT AUTO_INCREMENT PRIMARY KEY, user_id CHAR(10), start_time DATETIME, end_time DATETIME);
```