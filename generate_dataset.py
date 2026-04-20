import random
import csv

phishing_templates = [
    "Urgent! Your account has been suspended. Click here to verify now",
    "Congratulations! You won a prize. Claim now",
    "Your password expires today. Login immediately",
    "Verify your bank details to avoid suspension",
    "Click this link to secure your account",
    "Update your payment information now",
    "Unusual activity detected. Confirm immediately",
    "You have received a reward. Click to claim",
    "Security alert! Login required",
    "Your account will be blocked. Act now"
]

legit_templates = [
    "Meeting scheduled tomorrow at 10 AM",
    "Please review the attached document",
    "Let's catch up this weekend",
    "Your order has been delivered",
    "Happy birthday! Have a great day",
    "Project meeting next week",
    "Invoice attached for your purchase",
    "Team meeting rescheduled",
    "Lunch plan today?",
    "Reminder: submit assignment"
]

def generate_dataset(filename="phishing_emails.csv", size=1200):
    data = []

    for _ in range(size // 2):
        text = random.choice(phishing_templates) + " " + str(random.randint(100,999))
        data.append([text, 1])

    for _ in range(size // 2):
        text = random.choice(legit_templates) + " " + str(random.randint(100,999))
        data.append([text, 0])

    random.shuffle(data)

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["text", "label"])
        writer.writerows(data)

    print(f"✅ Dataset created with {size} rows")

if __name__ == "__main__":
    generate_dataset()