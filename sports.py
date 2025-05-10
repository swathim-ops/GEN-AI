import cohere

# Initialize Cohere client with your API key
co = cohere.Client('0O3rK9F0u8emZ73DorMuAgayuqJnbz6QdIrqSePB')  # Replace with your actual API key

# Define your interest area
sport_interest = "popular outdoor sports for fitness and fun"

# Create a message prompt requesting sports details
message = (
    f"Give detailed information on {sport_interest}. Include the sport name, basic rules, required equipment, ideal age group, and fitness benefits."
)

# Generate the sports details using the chat API
response = co.chat(
    model='command-r',
    message=message
)

# Print the generated sports details
print("Sports Details:\n")
print(response.text.strip())
