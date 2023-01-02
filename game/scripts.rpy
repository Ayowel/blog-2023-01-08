label start():
    "Hi!"
    show screen appear_square
    "There should be a square if you move your cursor toward the middle of the screen."
    "If you click once more the game ends."
    $ renpy.quit()

image square:
    "#00b"
    size (200, 200)

screen appear_square():
    add Appearing("square", 80, 250):
        align (0.5, 0.5)

screen yesno_prompt(message="Are you sure?", yes_action=[], no_action=[]):
    image "#000":
        alpha 0.7
    vbox:
        align (0.5, 0.5)
        text message:
            xalign 0.5
        textbutton "Yes":
            xalign 0.5
            action yes_action
        textbutton "No":
            xalign 0.5
            action no_action
