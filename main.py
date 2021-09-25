from tkinter import *;



# Variable deklaration

root                  = Tk();

img_starfleet         = PhotoImage(file='./__recources__/starfleet_logo.png');
img_enter             = PhotoImage(file='./__recources__/search.png');

title                 = Label(root, text='Starfleet Command Library 1.0');
subtitle              = Label(root, text='Programmed by HeSchy');
main_logo             = Label(root, image=img_starfleet);
search_btn            = Button(root, image=img_enter);

# Settings

root.title('Starfleet Command Library');
root.resizable(False, False);

title['font'] = 'Arial 15 bold';
title['width'] = 40;
title['height'] = 2;

subtitle['fg'] = '#555';


title.grid(row=1, column=1);
subtitle.grid(row=2, column=1);
main_logo.grid(row=3, column=2);

root.mainloop();
