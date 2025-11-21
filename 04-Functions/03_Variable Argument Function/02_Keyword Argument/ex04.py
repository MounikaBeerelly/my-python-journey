#!python3

import os
os.system("cls")

def sendNotification(**kwargs) :
    notificationMessage = kwargs.get("Message",  "Hey! You have a notification")
    messageSender = kwargs.get("Sender", "System")
    messagePriority = kwargs.get("Priority", "Normal")
    
    print(f"Message Received: {notificationMessage}")
    print(f"From: {messageSender}")
    print(f"Priority: {messagePriority}")
    
print("\nThis is the main module..", end="\n")
print("---------------------------", end="\n")

sendNotification(Message = "Your order has been shipped", Sender = "Amazon", Priority = "High")
sendNotification(Message = "Meeting is scheduled at 10 AM", Sender = "Delivery Manager", Priority = "High")
sendNotification(Message = "The next friday is an optional holiday", Sender = "HR Manager")
sendNotification(Message = "You are found to be late for your shift")

"""
Output :
=======


This is the main module..
---------------------------
Message Received: Your order has been shipped
From: Amazon
Priority: High
Message Received: Meeting is scheduled at 10 AM
From: Delivery Manager
Priority: High
Message Received: The next friday is an optional holiday
From: HR Manager
Priority: Normal
Message Received: You are found to be late for your shift
From: System
Priority: Normal

"""