from aifc import Error
from ast import While
from distutils.log import error
import time
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import IntVar, messagebox
from tkinter import DoubleVar, StringVar, ttk
from tkinter.constants import CENTER, MULTIPLE, RAISED, SINGLE, X



if __name__ == '__main__':
    #create window and tabs:
    window = tk.Tk(className=' The Book Shop')
    #tabs
    SignIn_window =ttk.Frame(window)
    LogInOldAccount_window = ttk.Frame(window)
    Guest_window = ttk.Frame(window)
    BookShopOwner_window = ttk.Frame(window)




#classes needed in the code
#ِclass Accounts of Users
class Acount:
    def __init__(self):
        name = AccountName_variable.get()
        password = AccountPassword_variable.get()
        self.name = name
        self.password = password
        self.balance = 0

#class accont for user who wants to buy books
class guest(Acount):
    def __init__(self):
        super().__init__()
        Users[str(self.name)+'@guest'] = self.password

#class account for user who owe a book shop
class BookShopOwner(Acount):
    def __init__(self):
        super().__init__()
        Users[str(self.name)+'@BookShopOwner'] = self.password

#class of library of book store
class BookShop:
    def __init__(self):
        self.listBooks = list()
        self.listbooks_title = list()
        self.listbooks_price = list()
        self.listbooks_author = list()
        self.listBooks_stock = list()
        self.listBooks_category = list()
    def addBook(self,Book):
        self.listBooks.append(Book)
        self.listbooks_title.append(Book.name)
        self.listbooks_price.append(Book.price)
        self.listbooks_author.append(Book.author)
        self.listBooks_stock.append(Book.stock)
        self.listBooks_category.append(Book.category)
    def deleteBook(self,Book):
        self.listBooks.pop(Book)
        self.listbooks_title.pop(Book)
        self.listbooks_price.pop(Book)
        self.listbooks_author.pop(Book)
        self.listBooks_stock.pop(Book)
        self.listBooks_category.pop(Book)
        
    def number_of_books(self):
        return len(self.listBooks)

#super class item book
class Book:
    def __init__(self,name,price,author,stock,category):
        self.name = name
        self.price = price
        self.author = author
        self.stock = stock
        self.category = category
    def __str__(self):
        return self.name
    def __repr__(self):
        return '''
        Name: %s 
        Price: %s$ 
        Author: %s 
        Stock: %s 
        Category: %s
        ''' % (self.name,self.price,self.author, self.stock,self.category)
    def UpdateBook(self, name, price, author,stock,category):
        self.name = name
        self.price = price
        self.author = author
        self.stock = stock
        self.category = category

#subclass item novel books
class Novel(Book):
    def __init__(self, name, price, author,stock):
        super().__init__(name, price, author,stock)
        self.category = 'Novel'
    def __repr__(self):
        return '''
        Name: %s 
        Price: %s$ 
        Author: %s 
        Stock: %s 
        Category: %s
        ''' % (self.name,self.price,self.author, self.stock,self.category)

#subclass item fiction books
class Fiction(Book):
    def __init__(self, name, price, author, stock):
        super().__init__(name, price, author, stock)
        self.category = 'Fiction'
    def __repr__(self):
        return '''Name: %s 
        Price: %s$ 
        Author: %s 
        Stock: %s 
        Type: Fiction
        '''% (self.name,self.price,self.author, self.stock)

#subclass item peotry books
class Peotry(Book):
    def __init__(self, name, price, author, stock):
        super().__init__(name, price, author, stock)
        self.category = 'Peotry'
    def __repr__(self):
        return '''Name: %s 
        Price: %s$ 
        Author: %s 
        Stock: %s 
        Type: Peotry
        ''' % (self.name,self.price,self.author, self.stock)

#all categories of book
class Category():
    def __init__(self):
        self.Categories = dict()
    def __str__(self):
        return str(self.Categories)
    def create(self,name):
        self.Categories[name]=list()
    def add(self,book,category):
        if category in self.Categories:
            self.Categories[category].append(book)
        else:
            self.create(str(category).capitalize())
            self.Categories[category].append(book)
    def remove(self,book,category):
        self.Categories[category].remove(book)
    def delete(self,category):
        if self.Categories[category] == []:
            self.Categories.pop(category)
        else:
            raise Error
    def move(self,book,oldcategory,newcategory):
        self.Categories[oldcategory].remove(book)
        self.add(book,newcategory)
    def Edit(self,category,new_Name):
        value = self.Categories.pop(category)
        self.Categories[new_Name] = value

#balance program
class Bank_account:
    def __init__(self):
        self.balance = float()
        self.changes = dict()



if __name__ == '__main__':
    #create variables
    AccountName_variable = StringVar()
    AccountPassword_variable = StringVar()
    accountType_choice = StringVar()
    Owner_index = 0
    InsertedBookTitle = str()
    InsertedBookPrice = str()
    InsertedBookAuthor = str()
    InsertedBookstock = str()
    InsertedBookType = str()
    m = ''
    #list of accounts in the program
    Users = dict()
    #Owner book shop
    BooksShop = BookShop()
    #categories dict variable
    mycategories = Category()
    #balance variable
    BookShop_balance = Bank_account()

    #Luanching tabs function
    #open tab on window to create account and sign in
    def launch_SignIn_Window():
        #open tab
        SignIn_window.pack(padx=10,pady=10)


        #add widgets:

        # -design
        tk.Label(SignIn_window,text='Welcome user in BookShop Application!',foreground='red',anchor=tk.CENTER,font='Arial 35').pack(pady=6,padx=10)

        tk.Label(SignIn_window,text='First create an account:',foreground='blue',anchor=tk.CENTER,font='Arial 30',pady=5).pack(pady=2.5)


        # -name frame 
        name_frame = tk.LabelFrame(SignIn_window,pady=5,padx=5,text='Enter name:',font='Arial 25')
        name_frame.pack(padx=10,pady=5) 
        # --containing:
        # * name text box
        name_textBox = tk.Entry(name_frame,textvariable= AccountName_variable,font='Arial 25')
        name_textBox.grid(column=0,row=0,padx=5)
        name_textBox.focus()
        # * combo box for choosing the type of the account
        account_type_combobox = ttk.Combobox(name_frame,textvariable= accountType_choice,width=10,font='BoldArial 24')
        account_type_combobox['values'] = ['Guest','Book Shop Owner']
        account_type_combobox.grid(column=1,row=0,padx=5)


        # -password frame
        password_frame = tk.LabelFrame(SignIn_window,padx=5,pady=5,text='Enter password:',font='Arial 25')
        password_frame.pack(padx=5,pady=5)
        # -- containing
        #  * a password textbox
        password_textBox = tk.Entry(password_frame, textvariable= AccountPassword_variable,font='Arial 25')
        password_textBox.grid(column=0,row=0,padx=5)

        #helping function
        def clear():
            name_textBox.delete(0,'end')
            password_textBox.delete(0,'end')
            account_type_combobox.set('')

        # -function for signing in and moving to the appropriate tab according to the type of account
        def Sign_in():
            if AccountName_variable.get() == '':
                pass
            elif AccountPassword_variable.get() == '':
                pass
            elif len(AccountName_variable.get()) < 8:
                messagebox.showwarning(title='Attention',message='User name should be at least 8 charecters!')
            elif '@' in AccountName_variable.get():
                messagebox.showwarning(title='Attention',message='User name shouldn\'t contain the @ symbol!')
            elif len(AccountPassword_variable.get()) < 4:
                messagebox.showwarning(title='Attention',message='Account password should be at least 4 charecters!')
            else:
                 pas = True
                 for account in Users:
                    account_name = account[:str(account).index('@')]
                    if account_name == AccountName_variable.get():
                        messagebox.showwarning(title='Attention',message='Attention! Username already used!')
                        pas = False
                        break
                 if pas:
                    if accountType_choice.get() == 'Guest':
                        guest()
                        SignIn_window.pack_forget()
                        Guest_window.pack()
                        clear()
                    elif accountType_choice.get() == 'Book Shop Owner':
                        BookShopOwner()
                        SignIn_window.pack_forget()
                        BookShopOwner_window.pack()
                        clear()

        # * sign in button in order to sign in and move to the appropriate tab according to the type of the created account
        sign_in_btn = tk.Button(password_frame,text='Sign in',command= Sign_in,font='boldCalibri 27')
        sign_in_btn.grid(column=1,row=0,padx=5)


        # -function for moving to the log in window if already having an account
        def AlreadyHaveAccount():
            clear()
            SignIn_window.pack_forget()
            LogInOldAccount_window.pack()
        # - an already have an account button to move for log in tab
        already_have_account_btn = tk.Button(SignIn_window,text='Already have account?',foreground='blue',borderwidth=0,anchor=tk.CENTER,command= AlreadyHaveAccount,font='Arial 27')
        already_have_account_btn.pack(pady=8)

    #open tab on window to varify account and log in
    def launch_LogInOldAccount_Window():
        #open tab
        LogInOldAccount_window.pack(padx=10,pady=10)

        #add widgets:


        # -design:
        label_account = tk.Label(LogInOldAccount_window,text='Remember your account?',foreground='Orange',anchor=tk.CENTER,font='Calibri 30',pady=6,padx=10)
        label_account.pack(pady=5)


        # -name frame
        name_oldAccount_frame = tk.LabelFrame(LogInOldAccount_window,pady=5,padx=5,text='Enter name:',font='Arial 25')
        name_oldAccount_frame.pack(pady=5,padx=10)
        # * containing account name textBox
        name_OldAccount_textBox = tk.Entry(name_oldAccount_frame,textvariable= AccountName_variable,font='Arial 25')
        name_OldAccount_textBox.grid(column=0,row=0,padx=2)
        name_OldAccount_textBox.focus()


        # -password frame
        password_OldAccount_frame = tk.LabelFrame(LogInOldAccount_window,padx=5,pady=5,text='Enter password:',font='Arial 25')
        password_OldAccount_frame.pack(pady=5,padx=10)
        #containing account password testbox
        password_OldAccount_textBox = tk.Entry(password_OldAccount_frame,textvariable=AccountPassword_variable,font='Arial 25')
        password_OldAccount_textBox.grid(column=0,row=0,padx=2)


        #error label to indicate if a mistake had occured in typing the name or password
        Error_label = tk.Label(LogInOldAccount_window,foreground='Red',anchor=tk.CENTER,font='ItalicTimes 28')
        Error_label.pack()


        #verify account type
        def AccountType_function(Type):
            if Type == 'guest':
                Guest_window.pack()
            elif Type == 'BookShopOwner':
                BookShopOwner_window.pack()
            name_OldAccount_textBox.delete(0,'end')
            password_OldAccount_textBox.delete(0,'end')

        #call back function for verfying the inserted info then logging in if true
        def Verify_account():
            name = AccountName_variable.get()
            password = AccountPassword_variable.get()
            if Users == dict():
                Error_label.configure(text='Invalid name or password!')
            else:
                for account in Users:
                    account_name = account[:str(account).index('@')]
                    account_password = Users[account]
                    if account_name == name:
                        if account_password == password:
                            Type = account[(str(account).index('@')+1):]
                            Error_label.configure(text='')
                            name_OldAccount_textBox.delete(0,'end')
                            password_OldAccount_textBox.delete(0,'end')
                            LogInOldAccount_window.pack_forget()
                            AccountType_function(Type)
                        else:
                            Error_label.configure(text='Invalid name or password!')
                    else:
                        Error_label.configure(text='Invalid name or password!')

        #function to return and make a new account
        def Exit_OldAccountWindow_function():
            Error_label.configure(text='')
            name_OldAccount_textBox.delete(0,'end')
            password_OldAccount_textBox.delete(0,'end')
            LogInOldAccount_window.pack_forget()
            SignIn_window.pack()

        #buttons frame
        oldaccount_btn_frame = tk.Frame(LogInOldAccount_window)
        oldaccount_btn_frame.pack(pady=10)
        # -Log in button in order to log in your old account and to move to the appropriate tab according to the type this account
        log_in_btn = tk.Button(oldaccount_btn_frame,text='Log in',command=Verify_account,font='Arial 25')
        log_in_btn.grid(row=0,column=0,padx=5)
        # -back btn for returning to 'sign in window'
        New_back_btn = tk.Button(oldaccount_btn_frame,text='New',command=Exit_OldAccountWindow_function,font='Arial 25')
        New_back_btn.grid(row=0,column=1,padx=5)

    #open on window the Book Shop Owner tab with its options
    def luanch_BookShopOwner_Window():
        #open tab
        BookShopOwner_window.pack(padx=10,pady=10)


        #variables needed in this tab for creating and modifying a book
        NumberOfBooks_var = StringVar()
        NumberOfpurchase_var = IntVar()
        Profitsfrombooks_var = DoubleVar()
        BookName = StringVar()
        Bookauthor = StringVar()
        Bookcategory = StringVar()
        searchby_choice_Var = StringVar()
        BookType_chioce = StringVar()
        BookTitle = StringVar()
        BookPrice = StringVar()
        BookAuthor = StringVar()
        Bookstock = StringVar()
        ChangeTitle_choice = StringVar()
        newBookTitle = StringVar()
        ChangePrice_choice = StringVar()
        newBookPrice = StringVar()
        ChangeAuthor_choice = StringVar()
        newBookAuthor = StringVar()
        ChangeStock_choice = StringVar()
        newBookStock = StringVar()
        ChangeCategory_choice = StringVar()
        newBookCategory = StringVar()
        Balance_sent = StringVar()
        editBalance_variable = DoubleVar()
        editBalancedesc_variable = StringVar()
        CategoryName = StringVar()
        BookORCategory_chioce = StringVar()
        ModifyCategory_chioce = StringVar()
        CategoryNewName = StringVar()


        #Book shop owner tabs:
        BookShopOwner_window_tabs = ttk.Notebook(BookShopOwner_window)
        BookShopOwner_window_tabs.pack()

        BookShopOwner_main_tab = ttk.Frame(BookShopOwner_window_tabs)
        BookShopOwner_window_tabs.add(BookShopOwner_main_tab,text='Dashboard')

        BookShopOwner_AddBooks_tab = ttk.Frame(BookShopOwner_window_tabs)
        BookShopOwner_window_tabs.add(BookShopOwner_AddBooks_tab,text='Books')

        BookShopOwner_Balance_tab = ttk.Frame(BookShopOwner_window_tabs)
        BookShopOwner_window_tabs.add(BookShopOwner_Balance_tab,text='Balance')



        #The main tab widgets and functions
        frame = tk.Frame(BookShopOwner_main_tab)
        frame.grid(row=0,column=0,pady=15,padx=10)

        #log out
        #exit to "sign in window" function
        def ExitfromOwnerWindow_function():
            confirmition = messagebox.askyesno('Confirming','Log out?')
            if confirmition == True:
                BookShopOwner_window.pack_forget()
                LogInOldAccount_window.pack()
        # - exit button to return to the sign in window
        Owner_ExitButton = tk.Button(frame,text= 'Log out', font= 'BoldCalibari 28',padx=5,command=ExitfromOwnerWindow_function)
        Owner_ExitButton.pack(padx=5,pady=5,fill=X)

        #get book info function
        def Owner_getinfo_Selected(a):
            try:
                item = str(Owner_ListOfBooks.get(Owner_ListOfBooks.curselection()[0]))
                l = item.index('.')
                index = int(item[:l])-1
                book = BooksShop.listBooks[index]
                messagebox.showinfo('Book info',book.__repr__())
            except:
                pass
        #list of books you have in the library
        Owner_ListOfBooks = tk.Listbox(frame,width=82,height=28,font=50,selectmode=SINGLE)
        Owner_ListOfBooks.bind('<<ListboxSelect>>',Owner_getinfo_Selected)
        Owner_ListOfBooks.pack(pady=15,padx=10)

        #frame for other options
        Frame1 = tk.Frame(BookShopOwner_main_tab)
        Frame1.grid(row=0,column=1,padx=5,pady=5)

        #Number of book titles owner have
        NumberOfBooks_var.set(' You have: %d books' % BooksShop.number_of_books())
        Owner_noOfBooks_message = tk.Message(Frame1,textvariable= NumberOfBooks_var,relief=RAISED,width=360,font='Arial 25')
        Owner_noOfBooks_message.pack(padx=5,pady=5)

        NumberOfpurchase_var.set('0 purchase')
        Owner_noOfpurchase_message = tk.Message(Frame1,textvariable= NumberOfpurchase_var,relief=RAISED,width=260,font='Arial 25')
        Owner_noOfpurchase_message.pack(padx=5,pady=5)

        Profitsfrombooks_var.set('Profits = 0$')
        Owner_Profitsfrombooks_message = tk.Message(Frame1,textvariable= Profitsfrombooks_var,relief=RAISED,width=260,font='Arial 25')
        Owner_Profitsfrombooks_message.pack(padx=5,pady=5)

        #packing widgets associated with the 'search by' choice
        def booksearchby_title_f():
            owner_book_searchby_title_frame.pack(pady=5,padx=5)
            owner_booksearch_menubutton.pack_forget()
        def booksearchby_author_f():
            owner_book_searchby_author_frame.pack(pady=5,padx=5)
            owner_booksearch_menubutton.pack_forget()
        def booksearchby_category_f():
            owner_book_searchby_category_frame.pack(pady=5,padx=5)
            owner_booksearch_menubutton.pack_forget()

        #menubutton to choose how to 'search'
        owner_booksearch_menubutton = tk.Menubutton(Frame1,text="Find",relief=RAISED,font='BoldCalibari 30',width=25)
        owner_booksearch_menubutton.pack(pady=5,padx=5)
        owner_booksearch_menu = tk.Menu(owner_booksearch_menubutton,tearoff = False)
        owner_booksearch_menubutton["menu"] = owner_booksearch_menu

        owner_booksearch_menu.add_radiobutton(label="by Title",variable=searchby_choice_Var,value='title',command=booksearchby_title_f)
        owner_booksearch_menu.add_radiobutton(label="by Author",variable=searchby_choice_Var,value='author',command=booksearchby_author_f)
        owner_booksearch_menu.add_radiobutton(label="by Category",variable=searchby_choice_Var,value='category',command=booksearchby_category_f)

        def Owner_searchbooktitle_function():
            Owner_donesearching_function(False)
            found = False
            for item in Owner_ListOfBooks.get(0,'end'):
                l = item.index('.')
                if (BookName.get()).lower() in (str(item[l+2:]).strip()).lower():
                    found = True
                else:
                    index = (list(Owner_ListOfBooks.get(0,'end')).index(item))
                    Owner_ListOfBooks.delete(index)
            if not found:
                Owner_donesearching_function(False)
                messagebox.showerror(title='Error',message='Book not found!')
            Booktitle_index_owner_modify_textbox.delete(0,'end')

        def Owner_donesearching_function(Yes=True):
            if len(Owner_ListOfBooks.get(0,'end')) == len(BooksShop.listbooks_title):
                pass
            else: 
                index = 0
                Owner_ListOfBooks.delete(0,'end')
                for book in BooksShop.listbooks_title:
                    Owner_ListOfBooks.insert(index,' '+str(index+1)+'. '+str(book))
                    index += 1
                if Yes:
                    owner_booksearch_menubutton.pack(pady=5,padx=5)
                    owner_book_searchby_author_frame.pack_forget()
                    owner_book_searchby_title_frame.pack_forget()
                    owner_book_searchby_category_frame.pack_forget()
        
        #search frame
        owner_book_searchby_title_frame = tk.LabelFrame(Frame1,text='Search',font='Arial 30')
        #insert book name textbox
        Booktitle_index_owner_modify_frame = tk.LabelFrame(owner_book_searchby_title_frame,text='Insert name',font='Arial 30')
        Booktitle_index_owner_modify_frame.pack(pady=5,padx=2)
        Booktitle_index_owner_modify_textbox = tk.Entry(Booktitle_index_owner_modify_frame,textvariable=BookName,font='Arial 35')
        Booktitle_index_owner_modify_textbox.pack(padx=5,pady=5)
        #buttons frame
        SearchBooktitle_owner_btnframe = tk.Frame(Booktitle_index_owner_modify_frame)
        SearchBooktitle_owner_btnframe.pack(pady=5,padx=5)
        #search btn according to name
        SearchBooktitle_owner_btn = tk.Button(SearchBooktitle_owner_btnframe,text='Find',font='Arial 25',command=Owner_searchbooktitle_function)
        SearchBooktitle_owner_btn.grid(row=0,column=0,pady=5,padx=5)
        #done button to return to the regular state
        Done_searchBooktitle_owner_btn = tk.Button(SearchBooktitle_owner_btnframe,text='Done',font='Arial 25',command=Owner_donesearching_function)
        Done_searchBooktitle_owner_btn.grid(row=0,column=1,pady=5,padx=5)

        def Owner_searchbookauthor_function():
            Owner_donesearching_function(False)
            found = False
            index = 0
            for item in BooksShop.listbooks_author:
                if (Bookauthor.get()).lower() in (str(item).strip()).lower():
                    found = True
                    index += 1
                else:
                    Owner_ListOfBooks.delete(index)
            if not found:
                Owner_donesearching_function(False)
                messagebox.showerror(title='Error',message='Author not found!')
            Bookauthor_index_owner_modify_textbox.delete(0,'end')

        #search frame
        owner_book_searchby_author_frame = tk.LabelFrame(Frame1,text='Search',font='Arial 30')
        #insert book author name textbox
        Bookauthor_index_owner_modify_frame = tk.LabelFrame(owner_book_searchby_author_frame,text='Insert author',font='Arial 30')
        Bookauthor_index_owner_modify_frame.pack(pady=5,padx=2)
        Bookauthor_index_owner_modify_textbox = tk.Entry(Bookauthor_index_owner_modify_frame,textvariable=Bookauthor,font='Arial 35')
        Bookauthor_index_owner_modify_textbox.pack(padx=5,pady=5)
        #buttons frame
        SearchBookauthor_owner_btnframe = tk.Frame(Bookauthor_index_owner_modify_frame)
        SearchBookauthor_owner_btnframe.pack(pady=5,padx=5)
        #search btn according to author
        SearchBookauthor_owner_btn = tk.Button(SearchBookauthor_owner_btnframe,text='Find',font='Arial 25',command=Owner_searchbookauthor_function)
        SearchBookauthor_owner_btn.grid(row=0,column=0,pady=5,padx=5)
        #done button to return to the regular state
        Done_searchBookauthor_owner_btn = tk.Button(SearchBookauthor_owner_btnframe,text='Done',font='Arial 25',command=Owner_donesearching_function)
        Done_searchBookauthor_owner_btn.grid(row=0,column=1,pady=5,padx=5)

        def Owner_searchbookcategory_function(a):
            Owner_donesearching_function(False)
            found = False
            index = 0
            for item in BooksShop.listBooks_category:
                if Bookcategory.get() in item:
                    found = True
                    index += 1
                else:
                    Owner_ListOfBooks.delete(index)
            if not found:
                Owner_donesearching_function(False)
                messagebox.showerror(title='Error',message='category not found!')

        #search frame
        owner_book_searchby_category_frame = tk.LabelFrame(Frame1,text='Search by category',font='Arial 30')
        #insert book name textbox
        Bookcategory_index_owner_modify_combobox = ttk.Combobox(owner_book_searchby_category_frame,textvariable=Bookcategory,font='Arial 35')
        Bookcategory_index_owner_modify_combobox['value'] = (tuple(mycategories.Categories.keys()))
        Bookcategory_index_owner_modify_combobox.bind('<<ComboboxSelected>>',Owner_searchbookcategory_function)
        Bookcategory_index_owner_modify_combobox.pack(pady=5,padx=2)
        #done button to return to the regular state
        Done_searchBookcategory_owner_btn = tk.Button(owner_book_searchby_category_frame,text='Done',font='Arial 25',command=Owner_donesearching_function)
        Done_searchBookcategory_owner_btn.pack(pady=5,padx=2)



        #The Add Books tab widgets and functions
        def AddBook_Owner_function():
            global Owner_index
            try:
                Owner_donesearching_function(False)
                float(BookPrice.get())
                float(Bookstock.get())
                if BookTitle.get() == '':
                    pass
                elif BookPrice.get() == '':
                    pass
                elif BookType_chioce.get() == '':
                    pass
                elif BookAuthor.get() == '':
                    pass
                elif Bookstock.get() == '':
                    pass
                elif (BookTitle.get()).capitalize() in BooksShop.listbooks_title:
                    messagebox.showinfo('Alert','Book exists already!')
                else:
                    book = Book((BookTitle.get()).capitalize(),BookPrice.get(),BookAuthor.get(),Bookstock.get(),BookType_chioce.get())
                    BooksShop.addBook(book)
                    mycategories.add((book.name).capitalize(),book.category)
                    Owner_ListOfBooks.insert(Owner_index,' '+str(Owner_index+1)+'. '+str(book))
                    NumberOfBooks_var.set(' You have: %d books' % BooksShop.number_of_books())
                    Owner_index += 1
                    bookType_combobox['values'] = (tuple(mycategories.Categories.keys()))
                    owner_editbook_Category_combobox['values'] = (tuple(mycategories.Categories.keys()))
                    Bookcategory_index_owner_modify_combobox['value'] = (tuple(mycategories.Categories.keys()))
                    Owner_Modifycategory_combobox['values'] = (tuple(mycategories.Categories.keys()))
                    title_textBox.delete(0,'end')
                    price_textBox.delete(0,'end')
                    author_textBox.delete(0,'end')
                    Stock_textBox.delete(0,'end')
                    BookType_chioce.set('')
            except:
                messagebox.showerror('Error','Something went Wrong!')

        #insert a book to list of books of the BookShopOwner
        def InsertBook_Owner_function():
            try:
                Owner_donesearching_function(False)
                global Owner_index
                global InsertedBookPrice,InsertedBookTitle,InsertedBookAuthor,InsertedBookstock,InsertedBookType
                filename = askopenfilename()
                file1 = open(filename, 'r')
                Lines = file1.readlines()
                for line in Lines:
                    t = True
                    a = True
                    p = True
                    s = True
                    c = True
                    info = line.split()
                    #fill info
                    for i in info:
                        if i.isnumeric() and p:
                            InsertedBookPrice += i 
                            t = False
                        elif t:
                            InsertedBookTitle += ' '+i
                        elif i.isnumeric() and s:
                            a = False
                            InsertedBookstock += i
                        elif a:
                            p = False
                            InsertedBookAuthor += ' '+i
                        elif c:
                            s = False
                            InsertedBookType += ' '+i
                    #verify conditions
                    float(InsertedBookPrice.strip())
                    float(InsertedBookstock.strip())
                    if InsertedBookTitle == '':
                        pass
                    elif InsertedBookPrice == '':
                        pass
                    elif InsertedBookAuthor == '':
                        pass
                    elif InsertedBookstock == '':
                        pass
                    elif (InsertedBookTitle.strip()).capitalize() in BooksShop.listbooks_title:
                        pass
                        InsertedBookTitle = ' '
                        InsertedBookPrice = ' '
                        InsertedBookAuthor = ' '
                        InsertedBookstock = ' '
                        InsertedBookType = ' '
                    else:
                        book = Book((InsertedBookTitle.strip()).capitalize() ,(InsertedBookPrice.strip()).capitalize() ,(InsertedBookAuthor.strip()).capitalize() ,(InsertedBookstock.strip()).capitalize(),(InsertedBookType.strip()).capitalize())
                        BooksShop.addBook(book)
                        mycategories.add((book.name).capitalize(),book.category)
                        Owner_ListOfBooks.insert(Owner_index,' '+str(Owner_index+1)+'. '+str(book))
                        NumberOfBooks_var.set(' You have: %d books' % BooksShop.number_of_books())
                        Owner_index += 1
                        InsertedBookTitle = ' '
                        InsertedBookPrice = ' '
                        InsertedBookAuthor = ' '
                        InsertedBookstock = ' '
                        InsertedBookType = ' '
                bookType_combobox['values'] = (tuple(mycategories.Categories.keys()))
                owner_editbook_Category_combobox['values'] = (tuple(mycategories.Categories.keys()))
                Bookcategory_index_owner_modify_combobox['value'] = (tuple(mycategories.Categories.keys()))
                Owner_Modifycategory_combobox['values'] = (tuple(mycategories.Categories.keys()))
                file1.close()
            except:
                messagebox.showerror('Error','Something went Wrong!')

        # -Insert a book frame for giving information about book wanted for creation
        insertBook_frame = tk.LabelFrame(BookShopOwner_AddBooks_tab,text='Insert a book',font='Arial 30')
        insertBook_frame.grid(rowspan=3,column=0,padx=5,pady=5)
        #containing
        Owner_bookinfo_frame = tk.Frame(insertBook_frame)
        Owner_bookinfo_frame.pack()

        # * a Book title frame
        #clarifying label
        tk.Label(Owner_bookinfo_frame,text='Title:',padx=5,font='Arial 25',anchor='center').grid(row=0,column=0,padx=5,pady=5)
        #book title textbox
        title_textBox = tk.Entry(Owner_bookinfo_frame,textvariable=BookTitle,font='Arial 31')
        title_textBox.grid(row=0,column=1,padx=5,pady=5)
        
        # * a book price frame
        # * clarifying label
        tk.Label(Owner_bookinfo_frame,text='price:',padx=5,font='Arial 25',anchor='center').grid(row=1,column=0,padx=5,pady=5)
        # * book price textbox
        price_textBox = tk.Entry(Owner_bookinfo_frame,textvariable=BookPrice,font='Arial 31')
        price_textBox.grid(row=1,column=1,padx=5,pady=5)
        
        # * a Book author frame
        #clarifying label
        tk.Label(Owner_bookinfo_frame,text='Author:',padx=5,font='Arial 25',anchor=CENTER).grid(row=2,column=0,padx=5,pady=5)
        #book author textbox
        author_textBox = tk.Entry(Owner_bookinfo_frame,textvariable=BookAuthor,font='Arial 31')
        author_textBox.grid(row=2,column=1,padx=5,pady=5)

        # * a book stock frame
        #clarifying label
        tk.Label(Owner_bookinfo_frame,text='Stock:',padx=5,anchor=CENTER,font='Arial 25').grid(row=3,column=0,padx=5,pady=5)
        #book discription textbox
        Stock_textBox = tk.Entry(Owner_bookinfo_frame,textvariable=Bookstock,font='Arial 31')
        Stock_textBox.grid(row=3,column=1,padx=5,pady=5)

        # * A book type frame
        #clarifying label
        tk.Label(Owner_bookinfo_frame,text='Category:',padx=5,font='Arial 25',anchor='center').grid(row=4,padx=5,pady=5,column=0)
        #book category textbox
        bookType_combobox = ttk.Combobox(Owner_bookinfo_frame,textvariable=BookType_chioce,font='Arial 30')
        bookType_combobox['values'] = (tuple(mycategories.Categories.keys()))
        bookType_combobox.grid(row=4,column=1,padx=5,pady=5)

        # btn frame
        Owner_addbookbtn_frame = tk.Frame(insertBook_frame,padx=5,pady=5)
        Owner_addbookbtn_frame.pack()
        # * an add button
        AddBook_Button = tk.Button(Owner_addbookbtn_frame,text='Add',font= 'BoldCambriaMath 25',command= AddBook_Owner_function)
        AddBook_Button.grid(row=0,column=0,pady=5,padx=5)
        # * an insert file of books' info btn
        Owner_Insertfile_button = tk.Button(Owner_addbookbtn_frame,text='Insert file',font= 'BoldCambriaMath 25',command= InsertBook_Owner_function)
        Owner_Insertfile_button.grid(row=0,column=1,pady=5,padx=5)

        #function for choosing between category or book 
        def Owner_chooseBookOrCategory_function(a):
            if BookORCategory_chioce.get() == 'Book':
                Owner_category_frame.grid_forget()
                owner_modification_frame.grid(row=1,column=1,pady=5,padx=5)
            elif BookORCategory_chioce.get() == 'Category':
                owner_modification_frame.grid_forget()
                Owner_category_frame.grid(row=1,column=1,padx=5,pady=5)
        #combobox choosing between category or book 
        Owner_combobox_CategoryORbook = ttk.Combobox(BookShopOwner_AddBooks_tab,textvariable=BookORCategory_chioce,font='Arial 45')
        Owner_combobox_CategoryORbook['value'] = ('Book','Category')
        Owner_combobox_CategoryORbook.bind('<<ComboboxSelected>>',Owner_chooseBookOrCategory_function)
        Owner_combobox_CategoryORbook.grid(row=0,column=1,padx=5,pady=15)

        def Owner_CreateCategory_function():
            if CategoryName.get() == '':
                pass
            else:
                mycategories.create(CategoryName.get().capitalize())
                Owner_newcategory_textBox.delete(0,'end')
                bookType_combobox['values'] = (tuple(mycategories.Categories.keys()))
                owner_editbook_Category_combobox['values'] = (tuple(mycategories.Categories.keys()))
                Bookcategory_index_owner_modify_combobox['values'] = (tuple(mycategories.Categories.keys()))
                Owner_Modifycategory_combobox['values'] = (tuple(mycategories.Categories.keys()))
        
        # - new category creation frame
        Owner_category_frame = tk.LabelFrame(BookShopOwner_AddBooks_tab,text='New Category',font='Arial 25')
        # new frame widgets frame
        Owner_Newcategory_frame = tk.Frame(Owner_category_frame)
        Owner_Newcategory_frame.pack()
        #text box for new category name
        Owner_newcategory_textBox = tk.Entry(Owner_Newcategory_frame,font='Arial 30',textvariable=CategoryName)
        Owner_newcategory_textBox.grid(row=0,column=0,padx=5)
        #creat category btn
        Owner_newcategory_btn = tk.Button(Owner_Newcategory_frame, text='+',border=0,command=Owner_CreateCategory_function,font='BoldArial 40')
        Owner_newcategory_btn.grid(row=0,column=1)
        #Modify category frame
        Owner_Modifycategory_frame = tk.Frame(Owner_category_frame)
        Owner_Modifycategory_frame.pack()
        #delete category function
        def Owner_ModifyCategory_function():
            Owner_Newcategory_frame.pack_forget()
            Owner_Modifycategory_frame.pack_forget()
            Owner_Modifycategory_combobox.pack(padx=5,pady=2)
            Owner_Modifycategory_btn_frame.pack(padx=5,pady=2)
        #modify category btn to bring the delete and edit button
        Owner_Modifycategory_btn = tk.Button(Owner_Modifycategory_frame, text='Modify',command=Owner_ModifyCategory_function,font='BoldArial 25')
        Owner_Modifycategory_btn.grid(row=0,column=0,pady=2,padx=5)
        #combobox to display categories already have
        Owner_Modifycategory_combobox = ttk.Combobox(Owner_category_frame,textvariable=ModifyCategory_chioce,font='Arial 30')
        Owner_Modifycategory_combobox['values'] = (tuple(mycategories.Categories.keys()))
        #modification btns frame
        Owner_Modifycategory_btn_frame = tk.Frame(Owner_category_frame)
        #delete category funnction
        def Owner_DeleteCategory_function():
            try:
                mycategories.delete(ModifyCategory_chioce.get())
                ModifyCategory_chioce.set('')
                bookType_combobox['values'] = (tuple(mycategories.Categories.keys()))
                owner_editbook_Category_combobox['values'] = (tuple(mycategories.Categories.keys()))
                Bookcategory_index_owner_modify_combobox['values'] = (tuple(mycategories.Categories.keys()))
                Owner_Modifycategory_combobox['values'] = (tuple(mycategories.Categories.keys()))
                messagebox.showinfo('Info','Succefuly deleted!')
            except:
                messagebox.showerror('Error','Many books belong to this category!')
        #delete category btn
        Owner_Modifycategory_Deletebtn = tk.Button(Owner_Modifycategory_btn_frame, text='Delete',command=Owner_DeleteCategory_function,font='BoldArial 25')
        Owner_Modifycategory_Deletebtn.grid(row=0,column=0,padx=5,pady=5)
        #return back option function
        def Owner_Category_back_function():
            Owner_Newcategory_frame.pack(padx=5,pady=2)
            Owner_Modifycategory_frame.pack(padx=5,pady=2)
            Owner_Modifycategory_combobox.pack_forget()
            Owner_Modifycategory_btn_frame.pack_forget()
        #return back option btn
        Owner_Modifycategory_returnback = tk.Button(Owner_Modifycategory_btn_frame, text='Back',command=Owner_Category_back_function,font='BoldArial 25')
        Owner_Modifycategory_returnback.grid(row=0,column=3,padx=10,pady=5)
        #edit category function
        def Owner_EditCategory_function():
            if ModifyCategory_chioce.get() != '':
                Owner_Modifycategory_combobox.pack_forget()
                Owner_Modifycategory_btn_frame.pack_forget()
                Owner_ChangecategoryName_frame.pack(padx=5,pady=2)
        #edit category btn
        Owner_Modifycategory_Editbtn = tk.Button(Owner_Modifycategory_btn_frame, text='Edit',command=Owner_EditCategory_function,font='BoldArial 25')
        Owner_Modifycategory_Editbtn.grid(row=0,column=1,padx=5,pady=5)
        #change category name frame
        Owner_ChangecategoryName_frame = tk.Frame(Owner_category_frame)
        #textbox to insert the new name of the category
        Owner_ChangecategoryName_textbox = tk.Entry(Owner_ChangecategoryName_frame,font='Arial 30',textvariable=CategoryNewName)
        Owner_ChangecategoryName_textbox.grid(row=0,column=0,padx=5,pady=5)
        #change the category name function
        def Owner_ChangeCategoryName_function():
            for book in (mycategories.Categories)[ModifyCategory_chioce.get()]:
                i = list(BooksShop.listbooks_title).index(book)
                book = BooksShop.listBooks[i]
                book.UpdateBook(book.name,book.price,book.author,book.stock,CategoryNewName.get())
                BooksShop.listBooks[i] = book
                BooksShop.listBooks_category.pop(i)
                BooksShop.listBooks_category.insert(i,CategoryNewName.get())
            mycategories.Edit(ModifyCategory_chioce.get(),CategoryNewName.get())
            bookType_combobox['values'] = (tuple(mycategories.Categories.keys()))
            owner_editbook_Category_combobox['values'] = (tuple(mycategories.Categories.keys()))
            Bookcategory_index_owner_modify_combobox['values'] = (tuple(mycategories.Categories.keys()))
            Owner_Modifycategory_combobox['values'] = (tuple(mycategories.Categories.keys()))
            Owner_Modifycategory_combobox.pack(padx=5,pady=2)
            Owner_Modifycategory_btn_frame.pack(padx=5,pady=2)
            Owner_ChangecategoryName_frame.pack_forget()
            ModifyCategory_chioce.set('')
        #canceling editing category function
        def Owner_cancel_ChangeCategoryName_function():
            Owner_Modifycategory_combobox.pack(padx=5,pady=2)
            Owner_Modifycategory_btn_frame.pack(padx=5,pady=2)
            Owner_ChangecategoryName_frame.pack_forget()
        #canceling editing category btn
        Owner_Modifycategory_CancelEditbtn = tk.Button(Owner_ChangecategoryName_frame, text='Cancel',command=Owner_cancel_ChangeCategoryName_function,font='BoldArial 25')
        Owner_Modifycategory_CancelEditbtn.grid(row=1,columnspan=2,padx=5,pady=5)

        #Confirmation btn to change the category name
        Owner_ChangecategoryName_Confirm_btn = tk.Button(Owner_ChangecategoryName_frame, text='Confirm',command=Owner_ChangeCategoryName_function,font='BoldArial 25')
        Owner_ChangecategoryName_Confirm_btn.grid(row=0,column=1,padx=5,pady=5)

        # - books modification frame
        owner_modification_frame = tk.Frame(BookShopOwner_AddBooks_tab)
        #delete book frame
        owner_book_delete_frame = tk.LabelFrame(owner_modification_frame,text='Modify',font='Arial 25')
        owner_book_delete_frame.pack(padx=5,pady=7)
        #delete book textbox
        Owner_ModifyBookTextbox_frame = tk.Frame(owner_book_delete_frame)
        Owner_ModifyBookTextbox_frame.pack(padx=5,pady=3)
        tk.Label(Owner_ModifyBookTextbox_frame,text='Enter index:',font='Calibri 25').grid(row=0,column=0,padx=2,pady=2)
        Owner_ModifyBook_Textbox = tk.Entry(Owner_ModifyBookTextbox_frame,font='BoldArial 30',textvariable=BookName)
        Owner_ModifyBook_Textbox.grid(row=0,column=1,pady=2,padx=2)
        #delete book function
        def Owner_deleteBook_function():
            global Owner_index
            try:
                if len(list(Owner_ListOfBooks.get(0,'end'))) > (int(BookName.get())-1):
                    book = str(list(Owner_ListOfBooks.get(0,'end'))[int(BookName.get())-1])
                    l = book.index('.')+1
                    confirmation = messagebox.askquestion(title='Confirming',message='Delete "%s"?' % (book[l:]).strip())
                    if confirmation == 'yes':
                        mycategories.remove((book[l:]).strip(),BooksShop.listBooks_category[int(BookName.get())-1])
                        l = Owner_ListOfBooks.get(int(BookName.get())-1).index('.')+2
                        BooksShop.deleteBook(int(BookName.get())-1)
                        Owner_ListOfBooks.see(index=int(BookName.get())-1)
                        Owner_ListOfBooks.delete(int(BookName.get())-1)
                        Owner_ModifyBook_Textbox.delete(0,'end')
                        Owner_index = Owner_index-1
                        NumberOfBooks_var.set(' You have: %d books' % BooksShop.number_of_books())
                        for items in Owner_ListOfBooks.get(0,'end'):
                            book_index=list(Owner_ListOfBooks.get(0,'end')).index(items)
                            l = items.index('.')+1
                            Owner_ListOfBooks.delete(book_index)
                            Owner_ListOfBooks.insert(book_index,' '+str(int(book_index)+1)+'.'+items[l:])
                else:
                    raise ValueError()
            except:
                    messagebox.showerror(title='Error',message='Wrong input!')
        
        #modify book btn frame
        owner_book_btn_frame = tk.Frame(owner_modification_frame)
        owner_book_btn_frame.pack()
        #delete book btn
        Owner_deleteBook_btn = tk.Button(owner_book_btn_frame,font='BoldTimes 25',text='Delete',command=Owner_deleteBook_function)
        Owner_deleteBook_btn.grid(row=0,column=0,padx=5,pady=2)

        #delete book function
        def Owner_editBook_function():
            try:
                if (int(BookName.get())-1) < len(list(Owner_ListOfBooks.get(0,'end'))):
                    Owner_EditBook_newInfo_frame.pack(padx=5,pady=5)
                    Owner_editbook_btn_frame.pack(padx=5,pady=5)
                    book = str(list(Owner_ListOfBooks.get(0,'end'))[int(BookName.get())-1])
                    l = book.index('.')+1
                    text = 'Insert new info: %s' % (book[l:]).strip()
                    Owner_EditBook_newInfo_frame.configure(text=text)
                    owner_book_delete_frame.pack_forget()
                    owner_book_btn_frame.pack_forget()
                else:
                    raise ValueError()
            except:
                messagebox.showerror('Error','Wrong Input!')
        #functions for check buttons
        def Owner_editbooktitlecheckbtn_function():
            if ChangeTitle_choice.get() == '1':
                owner_editbook_title_textbox.configure(state='normal')
            elif ChangeTitle_choice.get() == '0':
                owner_editbook_title_checkbtn.deselect()
                owner_editbook_title_textbox.delete(0,'end')
                owner_editbook_title_textbox.configure(state='disabled')

        def Owner_editbookpricecheckbtn_function():
            if ChangePrice_choice.get() == '1':
                owner_editbook_Price_textbox.configure(state='normal')
            elif ChangePrice_choice.get() == '0':
                owner_editbook_Price_checkbtn.deselect()
                owner_editbook_Price_textbox.delete(0,'end')
                owner_editbook_Price_textbox.configure(state='disabled')

        def Owner_editbookauthorcheckbtn_function():
            if ChangeAuthor_choice.get() == '1':
                owner_editbook_Author_textbox.configure(state='normal')
            elif ChangeAuthor_choice.get() == '0':
                owner_editbook_Author_checkbtn.deselect()
                owner_editbook_Author_textbox.delete(0,'end')
                owner_editbook_Author_textbox.configure(state='disabled')

        def Owner_editbookstockcheckbtn_function():
            if ChangeStock_choice.get() == '1':
                owner_editbook_Stock_textbox.configure(state='normal')
            elif ChangeStock_choice.get() == '0':
                owner_editbook_Stock_checkbtn.deselect()
                owner_editbook_Stock_textbox.delete(0,'end')
                owner_editbook_Stock_textbox.configure(state='disabled')

        def Owner_editbookCategorycheckbtn_function():
            if ChangeCategory_choice.get() == '1':
                owner_editbook_Category_combobox.configure(state='normal')
            elif ChangeCategory_choice.get() == '0':
                owner_editbook_Category_checkbtn.deselect()
                owner_editbook_Category_combobox.delete(0,'end')
                owner_editbook_Category_combobox.configure(state='disabled')

        #Edit book btn
        Owner_EditBook_btn = tk.Button(owner_book_btn_frame,font='BoldTimes 25',text='Edit',command=Owner_editBook_function)
        Owner_EditBook_btn.grid(row=0,column=1,padx=5,pady=2)
        #new book info frame 
        Owner_EditBook_newInfo_frame = tk.LabelFrame(owner_modification_frame,text=m,font='Arial 25')
        #new book title
        owner_editbook_title_checkbtn = tk.Checkbutton(Owner_EditBook_newInfo_frame,onvalue=1,offvalue=0,text='Title',variable=ChangeTitle_choice,font='Arial 25',indicatoron=0,border=0,command=Owner_editbooktitlecheckbtn_function)
        owner_editbook_title_checkbtn.grid(row=0,column=0,padx=5,pady=5)
        #new book title textbox
        owner_editbook_title_textbox = tk.Entry(Owner_EditBook_newInfo_frame,state='disabled',font='BoldArial 31',textvariable=newBookTitle)
        owner_editbook_title_textbox.grid(row=0,column=1,padx=5,pady=5)
        #new book Price
        owner_editbook_Price_checkbtn = tk.Checkbutton(Owner_EditBook_newInfo_frame,text='Price',onvalue=1,offvalue=0,variable=ChangePrice_choice,font='Arial 25',indicatoron=0,border=0,command=Owner_editbookpricecheckbtn_function)
        owner_editbook_Price_checkbtn.grid(row=1,column=0,padx=5,pady=5)
        #new book Price textbox
        owner_editbook_Price_textbox = tk.Entry(Owner_EditBook_newInfo_frame,state='disabled',font='BoldArial 31',textvariable=newBookPrice)
        owner_editbook_Price_textbox.grid(row=1,column=1,padx=5,pady=5)
        #new book Author
        owner_editbook_Author_checkbtn = tk.Checkbutton(Owner_EditBook_newInfo_frame,text='Author',onvalue=1,offvalue=0,variable=ChangeAuthor_choice,font='Arial 25',indicatoron=0,border=0,command=Owner_editbookauthorcheckbtn_function)
        owner_editbook_Author_checkbtn.grid(row=2,column=0,padx=5,pady=5)
        #new book Author textbox
        owner_editbook_Author_textbox = tk.Entry(Owner_EditBook_newInfo_frame,state='disabled',font='BoldArial 31',textvariable=newBookAuthor)
        owner_editbook_Author_textbox.grid(row=2,column=1,padx=5,pady=5)
        #new book Stock
        owner_editbook_Stock_checkbtn = tk.Checkbutton(Owner_EditBook_newInfo_frame,text='Stock',onvalue=1,offvalue=0,variable=ChangeStock_choice,font='Arial 25',indicatoron=0,border=0,command=Owner_editbookstockcheckbtn_function)
        owner_editbook_Stock_checkbtn.grid(row=3,column=0,padx=5,pady=5)
        #new book Stock textbox
        owner_editbook_Stock_textbox = tk.Entry(Owner_EditBook_newInfo_frame,state='disabled',font='BoldArial 31',textvariable=newBookStock)                                                                            
        owner_editbook_Stock_textbox.grid(row=3,column=1,padx=5,pady=5)
        #new book Stock
        owner_editbook_Category_checkbtn = tk.Checkbutton(Owner_EditBook_newInfo_frame,text='Category',onvalue=1,offvalue=0,variable=ChangeCategory_choice,font='Arial 25',indicatoron=0,border=0,command=Owner_editbookCategorycheckbtn_function)
        owner_editbook_Category_checkbtn.grid(row=4,column=0,padx=5,pady=5)
        #new book Stock textbox
        owner_editbook_Category_combobox = ttk.Combobox(Owner_EditBook_newInfo_frame,state='disabled',font='BoldArial 30',textvariable=newBookCategory)                                                                            
        owner_editbook_Category_combobox.grid(row=4,column=1,padx=5,pady=5)                                                                                                                                               
        #save new book function
        def Owner_savenewbook_function():
            try:
                book = str(list(Owner_ListOfBooks.get(0,'end'))[int(BookName.get())-1])
                l = book.index('.')+1
                con = messagebox.askquestion(title='Confirming',message='Edit "%s"?' % (book[l:]).strip())
                if con ==  'yes':
                    index = int(BookName.get())-1
                    if newBookTitle.get() != '':
                        book = BooksShop.listBooks[index]
                        book.UpdateBook(newBookTitle.get(),book.price,book.author,book.stock,book.category)
                        BooksShop.listBooks[index] = book
                        BooksShop.listbooks_title[index] = newBookTitle.get()
                        Owner_ListOfBooks.delete(index)
                        Owner_ListOfBooks.insert(index,' '+str(index+1)+'.  '+str(book))
                    if newBookPrice.get() != '':
                        int(newBookPrice.get())
                        book = BooksShop.listBooks[index]
                        book.UpdateBook(book.name,newBookPrice.get(),book.author,book.stock,book.category)
                        BooksShop.listBooks[index] = book
                        BooksShop.listbooks_price[index] = newBookPrice.get()
                    if newBookAuthor.get() != '':
                        book = BooksShop.listBooks[index]
                        book.UpdateBook(book.name,book.price,newBookAuthor.get(),book.stock,book.category)
                        BooksShop.listBooks[index] = book
                        BooksShop.listbooks_author[index] = newBookAuthor.get()
                    if newBookStock.get() != '':
                        int(newBookStock.get())
                        book = BooksShop.listBooks[index]
                        book.UpdateBook(book.name,book.price,book.author,newBookStock.get(),book.category)
                        BooksShop.listBooks[index] = book
                        BooksShop.listBooks_stock[index] = newBookStock.get()
                    if newBookCategory.get() != '':
                        book = BooksShop.listBooks[index]
                        book.UpdateBook(book.name,book.price,book.author,book.stock,newBookCategory.get())
                        BooksShop.listBooks[index] = book
                        BooksShop.listBooks_category[index] = newBookCategory.get()
                    owner_editbook_title_checkbtn.deselect()
                    owner_editbook_title_textbox.delete(0,'end')
                    owner_editbook_title_textbox.configure(state='disabled')
                    owner_editbook_Price_checkbtn.deselect()
                    owner_editbook_Price_textbox.delete(0,'end')
                    owner_editbook_Price_textbox.configure(state='disabled')
                    owner_editbook_Author_checkbtn.deselect()
                    owner_editbook_Author_textbox.delete(0,'end')
                    owner_editbook_Author_textbox.configure(state='disabled')
                    owner_editbook_Stock_checkbtn.deselect()
                    owner_editbook_Stock_textbox.delete(0,'end')
                    owner_editbook_Stock_textbox.configure(state='disabled')
                    owner_editbook_Category_checkbtn.deselect()
                    owner_editbook_Category_combobox.configure(state='disabled')
                    Owner_ModifyBook_Textbox.delete(0,'end')
                    Owner_EditBook_newInfo_frame.pack_forget()
                    Owner_editbook_btn_frame.pack_forget()
                    owner_book_delete_frame.pack(padx=5,pady=7)
                    owner_book_btn_frame.pack()
            except:
                messagebox.showerror('Error','Wrong Input!')

        #edit book btn
        Owner_editbook_btn_frame = tk.Frame(owner_modification_frame)
        #new book confirm btn
        Owner_editbook_newBookConfirm_btn = tk.Button(Owner_editbook_btn_frame,text='Confirm',font='Arial 25',command=Owner_savenewbook_function)
        Owner_editbook_newBookConfirm_btn.grid(row=0,column=0,padx=2,pady=2)

        #function to show the book we're editing info
        def Owner_view_editbook_info_f():
            try:
                item = str(list(Owner_ListOfBooks.get(0,'end'))[int(BookName.get())-1])
                l = item.index('.')
                for book in BooksShop.listBooks:
                    if item[l+2:].strip() == str(book.name).strip():
                        break
                messagebox.showinfo('Book info',book.__repr__())
            except:
                pass

        #photo = tk.PhotoImage(file=r"C:/Users/user/Desktop/info.jpg")
        Owner_edit_bookInfo_btn = tk.Button(Owner_editbook_btn_frame,text='i',border=0,font='BoldArial 20',foreground='blue',background='lightblue',command=Owner_view_editbook_info_f)
        Owner_edit_bookInfo_btn.grid(row=0,column=1,padx=10,pady=2)
        
        

        #balance tab widget and function
        #function to view the selected 'balance editing' info
        def Owner_view_balanceEditin_info_f(a):
            try:
                item=str(Owner_balanceEdit.get(Owner_balanceEdit.curselection()[0]))
                i=item.index('-')
                messagebox.showinfo('Book info',BookShop_balance.changes[item[i+2:]])
            except:
                pass
        #history of balance edition
        Owner_balanceEdit = tk.Listbox(BookShopOwner_Balance_tab,width=82,height=33,font=50,selectmode=SINGLE)
        Owner_balanceEdit.grid(row=0,column=0,pady=15,padx=10)
        Owner_balanceEdit.bind('<<ListboxSelect>>',Owner_view_balanceEditin_info_f)
        #all balance frame
        balance_frame = tk.Frame(BookShopOwner_Balance_tab)
        balance_frame.grid(row=0,column=1,pady=5,padx=5)

        # frame to view balance
        ViewBalance_frame = tk.LabelFrame(balance_frame,pady=5,padx=5,text='Balance',font="Arial 30")
        ViewBalance_frame.pack(padx=5,pady=5)
        # * Balance textBox for viewing and editing balance
        Balance_sent.set('Your balance = %g$' % BookShop_balance.balance)
        Balance_TextBox = tk.Message(ViewBalance_frame,textvariable= Balance_sent,relief=RAISED,width=750,font='Arial 30')
        Balance_TextBox.pack(pady=10)

        #edit balance function
        def Edit_balance():
            BalanceEdit_textbox.configure(state='normal')
            BalanceEditdesc_textbox.configure(state='normal')
            EditBalance_Btn.configure(state='disabled')
            SaveNewBalance_btn.configure(state='normal')

        #save Modification of balance function
        def SaveNewBalance():
            try:
                if editBalancedesc_variable.get() == '':
                    raise error
                elif str(editBalance_variable.get())[0] == '-':
                    opperation = 'Withdrew'
                    t = 'from'
                    ammount = float(str(editBalance_variable.get())[1:])
                    BookShop_balance.balance = float(BookShop_balance.balance - ammount)
                else:
                    opperation = 'Added'
                    t = 'to'
                    ammount = float(editBalance_variable.get())
                    BookShop_balance.balance = float(BookShop_balance.balance + ammount)
                BookShop_balance.changes[(editBalancedesc_variable.get()).capitalize()]= '%s: %g$ succesfuly %s balance \n for:  %s \n at:  %s' % (opperation,float(ammount),t,editBalancedesc_variable.get(),time.asctime(time.localtime()))
                Balance_sent.set('Your balance = %g$' % BookShop_balance.balance)
                i = len(Owner_balanceEdit.get(0,'end'))
                Owner_balanceEdit.insert(i,str(i+1)+'- '+str(editBalancedesc_variable.get()).capitalize())
                BalanceEdit_textbox.delete(0,'end')
                BalanceEdit_textbox.configure(state='disabled')
                BalanceEditdesc_textbox.delete(0,'end')
                BalanceEditdesc_textbox.configure(state='disabled')
                SaveNewBalance_btn.configure(state='disabled') 
                EditBalance_Btn.configure(state='normal')
                messagebox.showinfo('Done','%s %g$ succesfuly %s balance' % (opperation,ammount,t))
            except:
               messagebox.showerror('Error','Something went wrong!')

        # balance buttons frame
        BalanceButton_frame = tk.Frame(balance_frame)
        BalanceButton_frame.pack(pady=5)
        # * edit balance button
        EditBalance_Btn = tk.Button(BalanceButton_frame,text='Edit',font='BoldCabilary 25',command=Edit_balance)
        EditBalance_Btn.grid(row=0,column=0,padx=5)
        # * save Modification of balance button
        SaveNewBalance_btn = tk.Button(BalanceButton_frame,text= 'Save', font= 'BoldArial 25',command=SaveNewBalance,state='disabled')
        SaveNewBalance_btn.grid(row=0,column=1,padx=5)

        #new balance textbox
        #edit  balance textbox
        BalanceEdit_textbox_frame = tk.Frame(balance_frame)
        BalanceEdit_textbox_frame.pack(pady=10)
        tk.Label(BalanceEdit_textbox_frame,text='New balance:',font='BoldArial 25').grid(row=0,column=0,pady=5,padx=2)
        BalanceEdit_textbox = tk.Entry(BalanceEdit_textbox_frame,textvariable=editBalance_variable,state='disabled',font='BoldArial 25')
        BalanceEdit_textbox.grid(row=0,column=1,pady=2,padx=5)

        #edit balnce discription textbox
        BalanceEdit_textboxdesc_frame = tk.Frame(balance_frame)
        BalanceEdit_textboxdesc_frame.pack(pady=10)
        tk.Label(BalanceEdit_textboxdesc_frame,text='Description:',font='BoldArial 25').grid(row=0,column=0,pady=5,padx=2)
        BalanceEditdesc_textbox = tk.Entry(BalanceEdit_textboxdesc_frame,textvariable=editBalancedesc_variable,state='disabled',font='BoldArial 25')
        BalanceEditdesc_textbox.grid(row=0,column=1,pady=2,padx=5)

    #open on window the Guest tab with its options
    def luanch_Guest_Window():
        #open tab
        Guest_window.pack(padx=10,pady=10)

        #add widgets:

        #design
        tk.Label(Guest_window,text='Welcome Guest!',foreground='magenta',font='BernardMTCondensed 20').grid(row=0,column=0,pady=10)

        #exit to "sign in window" function
        def ExitfromGuestWindow_function():
            res = messagebox.askyesno('Confirming','Log out?')
            if res == True:
                Guest_window.pack_forget()
                LogInOldAccount_window.pack()
        # - exit from Guest window to logIn Old account window btn
        Guest_ExitButton = tk.Button(Guest_window,text= 'Log out', font= 'BoldCalibari 12',padx=5,command=ExitfromGuestWindow_function)
        Guest_ExitButton.grid(row=0,column=3)

    #something crazy :)
    launch_SignIn_Window()
    SignIn_window.pack_forget()
    launch_LogInOldAccount_Window()
    LogInOldAccount_window.pack_forget()
    luanch_BookShopOwner_Window()
    BookShopOwner_window.pack_forget()
    luanch_Guest_Window()
    Guest_window.pack_forget()
    #start application with the sign in tab
    SignIn_window.pack()
    window.mainloop()