# Mad Libs Generator in Python

import random

def get_input(prompt):
    """
    Get user input for the given prompt.
    """
    return input(prompt)

def mad_libs():
    """
    Generates a DevOps and SRE-themed Mad Libs story based on user input.
    """
    # User input prompts
    userName = get_input("Enter your name: ")
    favoriteTool = get_input("Enter your favorite DevOps tool: ")
    cloudProvider = get_input("Enter a cloud provider: ")
    incidentType = get_input("Enter a type of incident (e.g., network outage, server crash): ")
    teamMember = get_input("Enter the name of a teammate: ")
    favoriteService = get_input("Enter your favorite cloud service: ")
    favoriteDay = get_input("Enter your favorite day of the week: ")
    favoriteSnack = get_input("Enter your favorite snack: ")

    # Adding randomness to make the story more interesting
    recoveryMethods = [
        "rerouting traffic to a backup server 🚀",
        "applying a hotfix to the service 🛠️",
        "resetting the affected instances 🔄",
        "using chaos engineering to identify weaknesses 🔮"
    ]
    celebrationActivities = [
        "took a well-deserved nap 🛌",
        "had a team video game session 🎮",
        "ordered pizza for everyone 🍕",
        "shared a round of high-fives ✋"
    ]

    randomRecoveryMethod = random.choice(recoveryMethods)
    randomCelebration = random.choice(celebrationActivities)

    # Mad Libs story
    story = (
        f"One {favoriteDay}, {userName} was in the middle of deploying a new feature using {favoriteTool}. "
        f"Everything was going smoothly until a sudden {incidentType} occurred on {cloudProvider}. "
        f"The entire team was alerted, and {userName} quickly jumped into action. "
        f"{userName} and {teamMember} worked tirelessly, analyzing logs and running diagnostics on the {favoriteService}. "
        f"After a few intense hours, they finally identified the root cause – a misconfigured load balancer that caused the outage. "
        f"Using {randomRecoveryMethod}, they restored the service and brought everything back online. "
        f"To celebrate the successful recovery, {userName} and {teamMember} {randomCelebration}, while enjoying some {favoriteSnack} 🍫. "
        f"From that day forward, {userName} became known as the hero who saved the {favoriteService} from disaster, and their expertise with {favoriteTool} became legendary. "
        f"The whole team learned valuable lessons that day, and {userName} was even asked to share their experience during the next all-hands meeting. "
        f"It was a reminder to everyone that no matter how tough the incident, with teamwork, the right tools, and maybe a little {favoriteSnack}, anything is possible."
    )
    
    # Output the generated story
    print("\nHere is your Mad Libs story:\n")
    print(story)

if __name__ == "__main__":
    mad_libs()