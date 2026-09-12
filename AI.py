brain = {
    "hello": "Hello how can I help you?",
    "what is your model?": "Im just a simple bot."
}



def learning():
    while True:
        prompt = input("Prompt: ").strip().lower()
        
        if prompt=="q":
            print("Cya!")
            break
        
        if prompt in brain:
            print(f"Bot: {brain[prompt]}")

        else:
            learn=input("I dont know how to respond that! Teach Me! ")
            brain[prompt]=learn
            print("Bot: I get it!")
            print("-"*30)
learning()

#Explanation
#The dictionary system of the pyhton is creating basics of this system.
#The AI knows only two prompts and dont know anyother thing but when you write a prompt that AI dont know, AI will ask how to respond that prompt.
#By this loop you can teach everything to AI but it is not efficient than real AI system.
#Everytime you re-start the code it forgets every thing that you taught

#Written by Stickman
