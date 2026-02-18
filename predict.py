symptoms = {
    "fever": "Flu",
    "headache": "Migraine",
    "cough": "Cold",
    "stomach pain": "Food Poisoning",
    "chest pain": "Heart Problem"
}

print("Enter your symptom:")
user_input = input().lower()

if user_input in symptoms:
    print("Possible disease:", symptoms[user_input])
else:
    print("No disease found in database")
