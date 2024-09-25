from plyer import notification

notification.notify(
    title="Python Notification",
    message="This is a test notification from Python.",
    app_name="Your App"
)

print("Desktop notification sent!")
