import random
import pandas as pd

TEMPLATES = {
    "billing": [
        "I was charged {amount} twice for order {order}",
        "Why is my bill {amount} higher than the website price?",
        "I can't download the invoice for order {order}",
        "My card was charged but I got no payment receipt",
        "Please fix the wrong amount on invoice {order}",
        "The discount code did not work and I paid {amount} more",
    ],
    "delivery": [
        "My package for order {order} has not arrived yet",
        "Order {order} arrived damaged",
        "I got the wrong item in order {order}",
        "The tracking page has shown no update since {day}",
        "My package was supposed to come on {day} but it did not",
        "The delivery man left my order {order} at the wrong door",
    ],
    "technical": [
        "The reset-password page doesn't open",
        "I can't log in to my account since {day}",
        "The app closes when I open my orders",
        "The website shows an error when I pay for order {order}",
        "I never got the verification code by email",
        "The search box on the website does not work",
    ],
    "other": [
        "Refund order {order} please",
        "I was charged {amount} twice and my package never arrived",
        "This is the worst service ever!!!",
        "Do you have a store near my city?",
        "I want my money back",
        "Can someone call me about my account?",
    ],
}

AMOUNTS = ["$12", "$25", "$40", "$99"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def make_tickets(total, seed):
    data = {
    "id": [],
    "message": [],
    "category": [],
    "template_id": []
    }

    id_count = 1
    proportions = [0.25, 0.30, 0.25, 0.20]
    random.seed(seed)
    for i in range(total):
        
        choice = random.choices(list(TEMPLATES.keys()), weights=proportions, k=1)[0]
        
        text = random.choice(TEMPLATES[choice])
        data["template_id"].append(TEMPLATES[choice].index(text))
        text = text.format(amount= random.choice(AMOUNTS), order= "#" + str(random.randint(1000 , 9999)), day=DAYS[random.randint(0,4)])
        data["message"].append(text)
        data["id"].append(id_count)
        id_count += 1
        data["category"].append(choice)

    df = pd.DataFrame(data)
    return df

    
df = make_tickets(400, 42)
print(df.shape)
print(df["category"].value_counts())
print(df["message"].duplicated().sum())
print(df.isna().sum())
df.to_csv("data/tickets_raw.csv", index=False)
print(df["message"].head(3))
