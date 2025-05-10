import cohere

# Initialize Cohere client with your API key
co = cohere.Client('0O3rK9F0u8emZ73DorMuAgayuqJnbz6QdIrqSePB')  # Replace with your actual API key

# Define your preferences or dress theme
dress_preferences = "casual summer dresses for women"

# Create a message prompt requesting shopping dress details
message = (
    f"Suggest a list of {dress_preferences}. Include dress names, short descriptions, recommended fabric, ideal occasions, and estimated prices."
)

# Generate the shopping dress details using the chat API
response = co.chat(
    model='command-r',
    message=message
)

# Print the generated dress shopping details
print("Shopping Dress Details:\n")
print(response.text.strip())
