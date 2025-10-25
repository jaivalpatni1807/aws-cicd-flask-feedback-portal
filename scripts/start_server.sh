#!/bin/bash
cd /home/ec2-user/employee-feedback-app
sudo pkill -f "python3 app.py"
nohup python3 app.py > app.log 2>&1 &
