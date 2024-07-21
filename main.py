import os, pickle
import tkinter as tk
import tkinter.ttk as ttk

'''
- 2 parts : Nutritional and exercise
- Weekly schedule planner
- Nutrition :
    - Plan for breakfast, lunch, snack, dinner
    - Provide choices for types of 'healthy' foods
- Exercise :
    - Select 3 exercises from exercises good for senior citizens walk, jog, yoga, pilates, swimming, water aerobics, bowling etc.)
    - Also suggest helpful tips for how to incorporate it in your daily life

- Planner and days completed stored in separate files ON DISK!! They are imported at the beginning.
- Planner is a dictionary of lists; each key is for a day, and lists the relevant info



'''

class Day:
    def __init__(self, breakfast, lunch, snack, dinner, ex1, ex2, ex3):
        self.breakfast = breakfast
        self.lunch = lunch
        self.snack = snack
        self.dinner = dinner
        self.ex1 = ex1
        self.ex2 = ex2
        self.ex3 = ex3

def load_variables():
    if os.path.isfile('planner.pkl'):
        with open('planner.pkl', 'rb') as file:
            planner = pickle.load(file)
    else:
        planner = {
            'sun': Day('Sunday 1', 'Sunday 2', 'Sunday 3', 'Sunday 4', 'Sunday 5', 'Sunday 6', 'Sunday 7'),
            'mon': Day('Monday 1', 'Monday 2', 'Monday 3', 'Monday 4', 'Monday 5', 'Monday 6', 'Monday 7'),
            'tue': Day('Tuesday 1', 'Tuesday 2', 'Tuesday 3', 'Tuesday 4', 'Tuesday 5', 'Tuesday 6', 'Tuesday 7'),
            'wed': Day('Wednesday 1', 'Wednesday 2', 'Wednesday 3', 'Wednesday 4', 'Wednesday 5', 'Wednesday 6', 'Wednesday 7'),
            'thu': Day('Thursday 1', 'Thursday 2', 'Thursday 3', 'Thursday 4', 'Thursday 5', 'Thursday 6', 'Thursday 7'),
            'fri': Day('Friday 1', 'Friday 2', 'Friday 3', 'Friday 4', 'Friday 5', 'Friday 6', 'Friday 7'),
            'sat': Day('Saturday 1', 'Saturday 2', 'Saturday 3', 'Saturday 4', 'Saturday 5', 'Saturday 6', 'Saturday 7'),
        }
    
    if os.path.isfile('completed.pkl'):
        with open('completed.pkl', 'rb') as file:
            completed = pickle.load(file)
    else:
        completed = 0
    return planner, completed

def save_variables(planner, completed):
    with open('planner.pkl', 'wb') as file:
        pickle.dump(planner, file)
    with open('completed.pkl', 'wb') as file:
        pickle.dump(completed, file)

def update(num, day, planner, completed, new_text):
    match num:
        case 0:
            planner[day].breakfast = new_text
        case 1:
            planner[day].lunch = new_text
        case 2:
            planner[day].snack = new_text
        case 3:
            planner[day].dinner = new_text
        case 4:
            planner[day].ex1 = new_text
        case 5:
            planner[day].ex2 = new_text
        case 6:
            planner[day].ex3 = new_text
        case 7:
            completed = int(new_text)

    save_variables(planner, completed)

def suggestions():
    window_3 = tk.Toplevel()
    window_3.title('SUGGESTIONS')
    window_3.geometry('1280x720')
    window_3.configure(background='#ffffff')

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('bar.TLabel', font='Helvetica 48', foreground='#ffffff', background='#89cff0')
    style.configure('names.TLabel', font='Helvetica 24', foreground='#808080', background='#ffffff')
    style.configure('intro.TLabel', font='Helvetica 24', foreground='#404040', background='#ffffff')
    style.configure('new.TEntry', font='Helvetica 24', foreground='#404040', background='#ffffff', width=40)
    style.configure('new.TButton', font='Helvetica 24', foreground='#404040', background='#ffffff')
    style.configure('new.TEntry', font='Helvetica 24', foreground='#404040', background='#ffffff')
    style.configure('copyright.TLabel', font='Helvetica 14', foreground='#404040', background='#ffffff')

    bar = ttk.Label(
        window_3,
        text=f'SUGGESTIONS',
        style='bar.TLabel',
        anchor=tk.CENTER
    )
    breakfast = [
        ttk.Label(
            window_3,
            text='Breakfast',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Label(
            window_3,
            text='- Oatmeal with fruits',
            style='intro.TLabel',
            anchor=tk.W
        ),
        ttk.Label(
            window_3,
            text='- Veggie omelet with whole-grain toast',
            style='intro.TLabel',
            anchor=tk.W
        ),
        ttk.Label(
            window_3,
            text='- Hard-boiled eggs with fruit',
            style='intro.TLabel',
            anchor=tk.W
        )
    ]

    lunch = [
        ttk.Label(
            window_3,
            text='Lunch',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Label(
            window_3,
            text='- Quinoa salad',
            style='intro.TLabel',
            anchor=tk.W
        ),
        ttk.Label(
            window_3,
            text='- Eggs and red potatoes',
            style='intro.TLabel',
            anchor=tk.W
        ),
        ttk.Label(
            window_3,
            text='- Tuna salad',
            style='intro.TLabel',
            anchor=tk.W
        )
    ]

    snack = [
        ttk.Label(
            window_3,
            text='Snack',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Label(
            window_3,
            text='- Cheese and crackers',
            style='intro.TLabel',
            anchor=tk.W
        ),
        ttk.Label(
            window_3,
            text='- Mixed nuts',
            style='intro.TLabel',
            anchor=tk.W
        ),
        ttk.Label(
            window_3,
            text='- Some fruits',
            style='intro.TLabel',
            anchor=tk.W
        )
    ]

    dinner = [
        ttk.Label(
            window_3,
            text='Dinner',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Label(
            window_3,
            text='- Beans and rice',
            style='intro.TLabel',
            anchor=tk.W
        ),
        ttk.Label(
            window_3,
            text='- Shrimp and pasta',
            style='intro.TLabel',
            anchor=tk.W
        ),
        ttk.Label(
            window_3,
            text='- Caesar salad',
            style='intro.TLabel',
            anchor=tk.W
        )
    ]

    exercise = [
        ttk.Label(
            window_3,
            text='Exercises',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Label(
            window_3,
            text='- Walking',
            style='intro.TLabel',
            anchor=tk.W
        ),
        ttk.Label(
            window_3,
            text='- Yoga',
            style='intro.TLabel',
            anchor=tk.W
        ),
        ttk.Label(
            window_3,
            text='- Pilates',
            style='intro.TLabel',
            anchor=tk.W
        ),
        ttk.Label(
            window_3,
            text='- Swimming',
            style='intro.TLabel',
            anchor=tk.W
        ),
    ]

    window_3.rowconfigure(0, weight=2, uniform='a')
    window_3.rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20), weight=1, uniform='a')

    window_3.columnconfigure(0, weight=2)
    window_3.columnconfigure((1, 2), weight=1)

    bar.grid(row=0, column=0, columnspan=3, sticky='news')
    
    breakfast[0].grid(row=2, column=0, sticky='news')
    breakfast[1].grid(row=1, column=2, sticky='news')
    breakfast[2].grid(row=2, column=2, sticky='news')
    breakfast[3].grid(row=3, column=2, sticky='news')

    lunch[0].grid(row=6, column=0, sticky='news')
    lunch[1].grid(row=5, column=2, sticky='news')
    lunch[2].grid(row=6, column=2, sticky='news')
    lunch[3].grid(row=7, column=2, sticky='news')

    snack[0].grid(row=10, column=0, sticky='news')
    snack[1].grid(row=9, column=2, sticky='news')
    snack[2].grid(row=10, column=2, sticky='news')
    snack[3].grid(row=11, column=2, sticky='news')

    dinner[0].grid(row=14, column=0, sticky='news')
    dinner[1].grid(row=13, column=2, sticky='news')
    dinner[2].grid(row=14, column=2, sticky='news')
    dinner[3].grid(row=15, column=2, sticky='news')

    exercise[0].grid(row=18, column=0, sticky='news')
    exercise[1].grid(row=17, column=2, sticky='news')
    exercise[2].grid(row=18, column=2, sticky='news')
    exercise[3].grid(row=19, column=2, sticky='news')
    exercise[4].grid(row=20, column=2, sticky='news')

def choose_day(day, planner, completed):
    days = {'sun': 'SUNDAY',
            'mon': 'MONDAY',
            'tue': 'TUESDAY',
            'wed': 'WEDNESDAY',
            'thu': 'THURSDAY',
            'fri': 'FRIDAY',
            'sat': 'SATURDAY'
        }
    
    window_2 = tk.Toplevel()
    window_2.title(f'SCHEDULE FOR {days[day]}')
    window_2.geometry('1280x720')
    window_2.configure(background='#ffffff')

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('bar.TLabel', font='Helvetica 48', foreground='#ffffff', background='#89cff0')
    style.configure('names.TLabel', font='Helvetica 24', foreground='#808080', background='#ffffff')
    style.configure('intro.TLabel', font='Helvetica 24', foreground='#404040', background='#ffffff')
    style.configure('new.TEntry', font='Helvetica 24', foreground='#404040', background='#ffffff', width=40)
    style.configure('new.TButton', font='Helvetica 24', foreground='#404040', background='#ffffff')
    style.configure('new.TEntry', font='Helvetica 24', foreground='#404040', background='#ffffff')
    style.configure('copyright.TLabel', font='Helvetica 14', foreground='#404040', background='#ffffff')

    bar = ttk.Label(
        window_2,
        text=f'SCHEDULE FOR {days[day]}',
        style='bar.TLabel',
        anchor=tk.CENTER
    )

    names = [
        ttk.Label(
            window_2,
            text='ITEM',
            style='names.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Label(
            window_2,
            text='CURRENT',
            style='names.TLabel',
            anchor=tk.CENTER
        )
    ]

    breakfast = [
        ttk.Label(
            window_2,
            text='Breakfast',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Entry(
            window_2,
            text=f'{planner[day].breakfast}',
            style='new.TEntry'
        )
    ]
    breakfast_button = ttk.Button(
            window_2,
            text='Update',
            style='new.TButton',
            command=lambda: update(0, day, planner, completed, breakfast[1].get())
        )
    breakfast[1].delete(0, tk.END)
    breakfast[1].insert(0, planner[day].breakfast)

    lunch = [
        ttk.Label(
            window_2,
            text='Lunch',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Entry(
            window_2,
            text=f'{planner[day].lunch}',
            style='new.TEntry'
        )
    ]
    lunch_button = ttk.Button(
            window_2,
            text='Update',
            style='new.TButton',
            command=lambda: update(1, day, planner, completed, lunch[1].get())
        )
    lunch[1].delete(0, tk.END)
    lunch[1].insert(0, planner[day].lunch)

    snack = [
        ttk.Label(
            window_2,
            text='Snack',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Entry(
            window_2,
            text=f'{planner[day].snack}',
            style='new.TEntry'
        )
    ]
    snack_button = ttk.Button(
            window_2,
            text='Update',
            style='new.TButton',
            command=lambda: update(2, day, planner, completed, snack[1].get())
        )
    snack[1].delete(0, tk.END)
    snack[1].insert(0, planner[day].snack)

    dinner = [
        ttk.Label(
            window_2,
            text='Dinner',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Entry(
            window_2,
            text=f'{planner[day].dinner}',
            style='new.TEntry'
        )
    ]
    dinner_button = ttk.Button(
            window_2,
            text='Update',
            style='new.TButton',
            command=lambda: update(3, day, planner, completed, dinner[1].get())
        )
    dinner[1].delete(0, tk.END)
    dinner[1].insert(0, planner[day].dinner)

    ex1 = [
        ttk.Label(
            window_2,
            text='Exercise #1',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Entry(
            window_2,
            text=f'{planner[day].ex1}',
            style='new.TEntry'
        )
    ]
    ex1_button = ttk.Button(
            window_2,
            text='Update',
            style='new.TButton',
            command=lambda: update(4, day, planner, completed, ex1[1].get())
        )
    ex1[1].delete(0, tk.END)
    ex1[1].insert(0, planner[day].ex1)
  
    ex2 = [
        ttk.Label(
            window_2,
            text='Exercise #2',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Entry(
            window_2,
            text=f'{planner[day].ex2}',
            style='new.TEntry'
        )
    ]
    ex2_button = ttk.Button(
            window_2,
            text='Update',
            style='new.TButton',
            command=lambda: update(5, day, planner, completed, ex2[1].get())
        )
    ex2[1].delete(0, tk.END)
    ex2[1].insert(0, planner[day].ex2)

    ex3 = [
        ttk.Label(
            window_2,
            text='Exercise #3',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Entry(
            window_2,
            text=f'{planner[day].ex3}',
            style='new.TEntry'
        )
    ]
    ex3_button = ttk.Button(
            window_2,
            text='Update',
            style='new.TButton',
            command=lambda: update(6, day, planner, completed, ex3[1].get())
        )
    ex3[1].delete(0, tk.END)
    ex3[1].insert(0, planner[day].ex3)

    days = [
        ttk.Label(
            window_2,
            text='# of Days Completed',
            style='intro.TLabel',
            anchor=tk.CENTER
        ),
        ttk.Entry(
            window_2,
            text=f'{completed}',
            style='new.TEntry'
        ),
    ]
    days_button = ttk.Button(
            window_2,
            text='Update',
            style='new.TButton',
            command=lambda: update(7, day, planner, completed, days[1].get())
        )
    
    tip = ttk.Button(
        window_2,
        text='SUGGESTIONS',
        style='new.TButton',
        command=suggestions
    )

    days[1].delete(0, tk.END)
    days[1].insert(0, str(completed))
    
    window_2.rowconfigure((0, 1), weight=2, uniform='a')
    window_2.rowconfigure((2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), weight=1, uniform='a')

    window_2.columnconfigure((0, 1), weight=2, uniform='a')
    window_2.columnconfigure((2, 3), weight=1, uniform='a')

    bar.grid(row=0, column=0, columnspan=4, sticky='news')
    names[0].grid(row=1, column=0, sticky='e')
    names[1].grid(row=1, column=2, sticky='w')
    
    breakfast[0].grid(row=2, column=0, sticky='e', padx=40)
    breakfast[1].grid(row=2, column=2, sticky='w', ipady=10)
    breakfast_button.grid(row=2, column=3, sticky='e', padx=20)

    lunch[0].grid(row=3, column=0, sticky='e', padx=40)
    lunch[1].grid(row=3, column=2, sticky='w', ipady=10)
    lunch_button.grid(row=3, column=3, sticky='e', padx=20)

    snack[0].grid(row=4, column=0, sticky='e', padx=40)
    snack[1].grid(row=4, column=2, sticky='w', ipady=10)
    snack_button.grid(row=4, column=3, sticky='e', padx=20)

    dinner[0].grid(row=5, column=0, sticky='e', padx=40)
    dinner[1].grid(row=5, column=2, sticky='w', ipady=10)
    dinner_button.grid(row=5, column=3, sticky='e', padx=20)

    ex1[0].grid(row=7, column=0, sticky='e', padx=40)
    ex1[1].grid(row=7, column=2, sticky='w', ipady=10)
    ex1_button.grid(row=7, column=3, sticky='e', padx=20)

    ex2[0].grid(row=8, column=0, sticky='e', padx=40)
    ex2[1].grid(row=8, column=2, sticky='w', ipady=10)
    ex2_button.grid(row=8, column=3, sticky='e', padx=20)

    ex3[0].grid(row=9, column=0, sticky='e', padx=40)
    ex3[1].grid(row=9, column=2, sticky='w', ipady=10)
    ex3_button.grid(row=9, column=3, sticky='e', padx=20)

    days[0].grid(row=11, column=0, sticky='e', padx=40)
    days[1].grid(row=11, column=2, sticky='w', ipady=10)
    days_button.grid(row=11, column=3, sticky='e', padx=20)

    tip.grid(row=13, column=0, columnspan=4, sticky='news')

    window_2.mainloop()

if __name__ == '__main__':
    planner, completed = load_variables()

    window = tk.Tk()
    window.title('THE FITBOOK')
    window.geometry('1280x720')
    window.configure(background='#ffffff')
    
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('bar.TLabel', font=('Helvetica', 48), foreground='#ffffff', background='#89cff0')
    style.configure('intro.TLabel', font=('Helvetica', 24), foreground='#404040', background='#ffffff')
    style.configure('new.TButton', font=('Helvetica', 28), foreground='#404040', background='#ffffff')
    style.configure('copyright.TLabel', font=('Helvetica', 14), foreground='#404040', background='#ffffff')
    
    bar = ttk.Label(
        window,
        text='THE FITBOOK',
        style='bar.TLabel',
        anchor=tk.CENTER
    )

    intro = ttk.Label(
        window,
        text='Nearly 1 out of 3 senior citizens don\'t get enough exercise.',
        style='intro.TLabel',
        anchor=tk.CENTER
    )
    
    intro_continued = ttk.Label(
        window,
        text='Let\'s change that by creating a personalized plan for your diet and exercise!',
        style='intro.TLabel',
        anchor=tk.CENTER
    )

    instructions = ttk.Label(
        window,
        text='Click on one of the days to see/update your schedule.',
        style='intro.TLabel',
        anchor=tk.CENTER
    )

    copyright = ttk.Label(
        window,
        text='Made by RASH',
        style='copyright.TLabel',
        anchor=tk.CENTER
    )

    sunday = ttk.Button(window, text='SUN', command=lambda: choose_day('sun', planner, completed), style='new.TButton', width=3)
    monday = ttk.Button(window, text='MON', command=lambda: choose_day('mon', planner, completed), style='new.TButton', width=3)
    tuesday = ttk.Button(window, text='TUE', command=lambda: choose_day('tue', planner, completed), style='new.TButton', width=3)
    wednesday = ttk.Button(window, text='WED', command=lambda: choose_day('wed', planner, completed), style='new.TButton', width=3)
    thursday = ttk.Button(window, text='THU', command=lambda: choose_day('thu', planner, completed), style='new.TButton', width=3)
    friday = ttk.Button(window, text='FRI', command=lambda: choose_day('fri', planner, completed), style='new.TButton', width=3)
    saturday = ttk.Button(window, text='SAT', command=lambda: choose_day('sat', planner, completed), style='new.TButton', width=3)

    window.rowconfigure(0, weight=2, uniform='a')
    window.rowconfigure((1, 3, 4, 5, 6), weight=1, uniform='a')

    window.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform='a')

    bar.grid(row=0, column=0, columnspan=7, sticky='news')
    intro.grid(row=1, column=0, columnspan=7, sticky='news')
    intro_continued.grid(row=2, column=0, columnspan=7, sticky='news')
    instructions.grid(row=3, column=0, columnspan=7, sticky='news')
    
    sunday.grid(row=4, column=0, sticky='news')
    monday.grid(row=4, column=1, sticky='news')
    tuesday.grid(row=4, column=2, sticky='news')
    wednesday.grid(row=4, column=3, sticky='news')
    thursday.grid(row=4, column=4, sticky='news')
    friday.grid(row=4, column=5, sticky='news')
    saturday.grid(row=4, column=6, sticky='news')

    copyright.grid(row=6, column=0, columnspan=7, sticky='news')

    window.mainloop()
    
