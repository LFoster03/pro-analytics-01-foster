"""
color_user.py - A simple Python script that asks the user for their favorite color and responds.

"""

#####################################
# Imports At the Top
#####################################

# Import from external dependencies (must be installed)
# See requirements.txt 
import pyttsx3

# Import from local project modules
from utils_logger import logger

#####################################
# Define Helper Functions
#####################################

def speak_message(message: str) -> None:
    """
    Speak the given message using text-to-speech.

    Args:
        message (str): The text to speak out loud.
    """
    try:
        engine = pyttsx3.init()  # Initialize the text-to-speech engine
        engine.say(message)  # Queue the message to be spoken
        engine.runAndWait()  # Wait for the speech to complete
    except Exception as e:
        logger.error(f"Error with text-to-speech: {e}")

#####################################
# Define main Function
#####################################

def main() -> None:
    """
    Main function to ask the user for their favorite color and respond with a message.
    """
    logger.info("Starting main function.")

    # Ask the user for their name
    user_name: str = input("Enter your name to continue: ")

    # Ask the user for their favorite color
    favorite_color: str = input(f"Hi {user_name}, what's your favorite color? ").strip()

    # Create a response message based on the user's favorite color
    response_message = f"Great choice, {user_name}! {favorite_color} is a wonderful color."

    # Add a user confirmation at the start
    caution_message = "Caution: This program can speak. Do you want to hear your favorite color response? (Y/N): "

    # Ask the user if they want to proceed
    response = input(caution_message).strip().lower()

    # Print and speak the response message
    logger.info(response_message)
    if response == 'y':
        speak_message(response_message)

    logger.info("Exiting main function.")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    logger.info("HELLO - Ready for work.")
    main()
    logger.info("HELLO - Execution complete.")


def write_to_file(user_name: str, favorite_color: str) -> None:
    """
    Write the user's name and favorite color to a text file.

    Args:
        user_name (str): The name of the user.
        favorite_color (str): The user's favorite color.
    """
    try:
        with open("favorite_color_results.txt", "a") as file:
            file.write(f"Name: {user_name}\nFavorite Color: {favorite_color}\n\n")
        logger.info(f"Results written to 'favorite_color_results.txt'.")
    except Exception as e:
        logger.error(f"Error writing to file: {e}")

#####################################
# Define main Function
#####################################

def main() -> None:
    """
    Main function to ask the user for their favorite color, respond, and save results to a file.
    """
    logger.info("Starting main function.")

    # Ask the user for their name
    user_name: str = input("Enter your name to continue: ")

    # Ask the user for their favorite color
    favorite_color: str = input(f"Hi {user_name}, what's your favorite color? ").strip()

    # Create a response message based on the user's favorite color
    response_message = f"Great choice, {user_name}! {favorite_color} is a wonderful color."

    # Add a user confirmation at the start
    caution_message = "Caution: This program can speak. Do you want to hear your favorite color response? (Y/N): "

    # Ask the user if they want to proceed
    response = input(caution_message).strip().lower()

    # Print and speak the response message
    logger.info(response_message)
    if response == 'y':
        speak_message(response_message)

    # Save results to a text file
    write_to_file(user_name, favorite_color)

    logger.info("Exiting main function.")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    logger.info("HELLO - Ready for work.")
    main()
    logger.info("HELLO - Execution complete.")
