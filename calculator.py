from tkinter import *

global textvalue
textvalue = ""
global textContainer
textContainer = ""



def press(calculate):
    global textvalue
    textvalue = textvalue + str(calculate)
    result.set(textvalue)

def equal():
    global textvalue
    textContainer.set(eval(textvalue))
    textvalue = ""
    result.set(textvalue)



def delete():
    global textvalue
    textvalue = ""
    result.set(textvalue)



if __name__ == "__main__":
    win = Tk()
    win.title("calculator")
    win.geometry("400x500")
    win.resizable(False,False)
    result = StringVar(win,value = '')
    textContainer = StringVar(win,value = '')


    Label(textvariable = textContainer, font = ('맑은 고딕',15,'bold'),width = 30,anchor = 'e').place(x = 35 ,y =5)
    Label(textvariable = result, font = ('맑은 고딕',20,'bold'),width = 24,anchor = 'e',relief = 'solid',bd = 2).place(x = 5,y =40)


    button1_1 = Button(win,command = lambda:press('('), text= '(',padx = 34,font = ('맑은 고딕',20,"bold"),bg = 'gray60').place(x = 0, y = 100)
    button1_2 = Button(win,command = lambda:press(')'), text= ')',padx = 34,font = ('맑은 고딕',20,"bold"),bg = 'gray60').place(x = 100, y = 100)
    button1_3 = Button(win,command = lambda:press('/'), text= '/',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray60').place(x = 200, y = 100)
    button1_4 = Button(win,command = lambda:delete(), text= 'AC',padx = 25,font = ('맑은 고딕',20,"bold"),bg = 'gray60').place(x = 300, y = 100)

    button2_1 = Button(win,command = lambda:press('7'), text= '7',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray80').place(x = 0, y = 180)
    button2_2 = Button(win,command = lambda:press('8'), text= '8',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray80').place(x = 100, y = 180)
    button2_3 = Button(win,command = lambda:press('9'), text= '9',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray80').place(x = 200, y = 180)
    button2_4 = Button(win,command = lambda:press('+'), text= '+',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray60').place(x = 300, y = 180)

    button3_1 = Button(win,command = lambda:press('4'), text= '4',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray80').place(x = 0, y = 260)
    button3_2 = Button(win,command = lambda:press('5'), text= '5',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray80').place(x = 100, y = 260)
    button3_3 = Button(win,command = lambda:press('6'), text= '6',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray80').place(x = 200, y = 260)
    button3_4 = Button(win,command = lambda:press('*'), text= 'x',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray60').place(x = 300, y = 260)

    button4_1 = Button(win,command = lambda:press('1'), text= '1',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray80').place(x = 0, y = 340)
    button4_2 = Button(win,command = lambda:press('2'), text= '2',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray80').place(x = 100, y = 340)
    button4_3 = Button(win,command = lambda:press('3'), text= '3',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray80').place(x = 200, y = 340)
    button4_4 = Button(win,command = lambda:press('-'), text= '-',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray60').place(x = 300, y = 340)

    button5_1 = Button(win,command = lambda:press('0'), text= '0',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray80').place(x = 0, y = 420)
    button5_2 = Button(win,command = lambda:press('.'), text= '.',padx = 36,font = ('맑은 고딕',20,"bold"),bg = 'gray60').place(x = 100, y = 420)
    button5_3 = Button(win,command = lambda:equal() , text= '=',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray60').place(x = 200, y = 420)
    button5_4 = Button(win,command = lambda:press('+'), text= '+',padx = 33,font = ('맑은 고딕',20,"bold"),bg = 'gray60').place(x = 300, y = 420)
    win.mainloop()
