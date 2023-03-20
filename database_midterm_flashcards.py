import tkinter as tk
import random

# Define the questions and answers

qa_dict = {
    "What are 2 differences between UNIQUE and PK": "pk can't have null values. Unique can. You can have many uniques in one table, but only 1 PK",
    "T or F: an ER diagram will always translate uniquely to a relational schema": "F. you can write schemas in different ways",
    "T or F: all attributes of a relation together form a super key for the relation(assume set semantics)": "T. If you're using set semantics(all tuples are unique), they'll serve as a super key",
    "T or F: in an ER model, miltiway relationships can have attributes": "T. Ternary relationships can have attributes",
    "T or F: in SQL, an INSERT statement always requires all column values to be specified": "F. INSERT INTO(a,b) VALUES(1,2): list of attributes doesn't need to be all the attributes in a relation",
    "The default policy for the foreign key constraint sets the value of a foreign key to null when the typle of its referenced attribute gets deleted": "F. the default policy is reject/abort. You need to set null yourself. ",
    "What are aggregate functions": "count, sum, avg, min, max",
    "what are assertions": "assertions are logical expressions that are checked to ensure that tthey are true for every database state",
    "what are triggers": "triggers are special procedures that are automatically executed when certain events occur(eg a row is inserted, uptadted, or deleted from table",
    "what are check statements": "they are used to ensure that data inserted or updated in a table satisfies certain conditions(eg age>18)",
    "what happens in bag semantics": "duplicates are allowed, order isn't important",
    "what happens in set semantics": "duplicates aren't allowed, order is not important",
    "what is a primary key": "it uniquely identifies each row in a table. Used to ensure there are no duplicate rows in a table ",
    "what is a foreign key": "a foreign key is a column or set of columns that refers to the pk of another table. Used to ensure referential integrity",
    "what is referential integrity": "ensures that data in one table corresponds to data in another table",
    "what does JOIN do": "JOIN is an operation that combines rows from two or more tables based on a related column between them.",
    "what are the dif types of JOIN and what do they do ": "",
    "what does UNION do and whats its result": "combines the result sets of two or more SELECT statements.The result set of a UNION contains only distinct rows, so duplicates are eliminated.",
    "What does INTERSECT do": "returns only the rows that appear in both of the result sets of two SELECT statements. The result set of an INTERSECT contains only distinct rows, so duplicates are eliminated.",
    "what does EXCEPT do": "returns only the distinct rows from the first result set that are not in the second result set of two SELECT statements.",
    "what does GROUP BY do": "GROUP BY is a clause that groups the rows in a table based on one or more columns.GROUP BY is often used with aggregate functions",
    "what does HAVING do": "filters the groups produced by a GROUP BY clause based on a condition. HAVING is similar to a WHERE clause, but operates on groups instead of individual rows",
    "what does ORDER BY do": " sort the rows of a result set in ascending or descending order based on one or more columns",
    "if you're comparing two join clauses which one won't have duplicates": "the one with IN in the subquery "


}


# Initialize the GUI
root = tk.Tk()
root.geometry("1000x300")
root.title("Flashcards")

# Create the question and answer labels
q_label = tk.Label(root, text="")
q_label.pack(pady=20)

a_label = tk.Label(root, text="")
a_label.pack(pady=20)

# Define the function to show the questions and answers


def show_q():
    # Get a list of questions to ask
    questions = list(qa_dict.keys())
    random.shuffle(questions)
    # Iterate over the list and show the questions and answers
    for question in questions:
        # Update the question label
        q_label.config(text=question)
        # Clear the answer label
        a_label.config(text="")
        # Wait for the user to click the "Show answer" button
        a_button.wait_variable(a_button_pressed)
        # Get the answer for the current question
        answer = qa_dict[question]
        # Update the answer label
        a_label.config(text=answer)
        # Wait for the user to click the "Show question" button
        q_button.wait_variable(q_button_pressed)


def show_a():
    # Get the answer for the current question
    question = q_label.cget("text")
    answer = qa_dict[question]
    # Update the answer label
    a_label.config(text=answer)


# Create the "show question" and "show answer" buttons
q_button_pressed = tk.BooleanVar()
q_button = tk.Button(root, text="Show question", command=show_q)
q_button.pack()

a_button_pressed = tk.BooleanVar()
a_button = tk.Button(root, text="Show answer", command=show_a)
a_button.pack()

# Start the GUI main loop
root.mainloop()
