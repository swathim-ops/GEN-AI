import cohere

# Initialize Cohere client with your API key
co = cohere.Client('0O3rK9F0u8emZ73DorMuAgayuqJnbz6QdIrqSePB')  # Replace with your actual API key

# Define your input ingredients
ingredients = "chicken, garlic, and tomatoes"

# Create a message prompt
message = f"Create a detailed cooking recipe using the following ingredients: {ingredients}"

# Generate the recipe using chat API
response = co.chat(
    model='command-r',
    message=message
)

# Print the generated recipe
print("Recipe:\n")
print(response.text.strip())
