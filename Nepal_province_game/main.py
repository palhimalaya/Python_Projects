import turtle
import pandas

screen = turtle.Screen()
screen.title("Nepal Province Game")
image = "nepal.gif"
screen.addshape(image)
turtle.shape(image)

# For finding coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

data = pandas.read_csv("nepal_cor.csv")
all_province = data.province.to_list()
print(all_province)
answered_province = []
unanswered_province = []
while len(answered_province) < 7:
    user_answer = screen.textinput(title=f"{len(answered_province)}/7 Guess the state",
                                   prompt="What is the another states name?").title()
    if user_answer == "Exit":
        for province in all_province:
            if province not in answered_province:
                unanswered_province.append(province)
        new_data = pandas.DataFrame(unanswered_province)
        new_data.to_csv("Missing_state.csv")
        break
    elif user_answer in all_province:
        answered_province.append(user_answer)
        data_province = data[data.province == user_answer]
        x_cor = int(data_province["x"])
        y_cor = int(data_province["y"])
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cor, y_cor)
        t.write(data_province.province.item())


