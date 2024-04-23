from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

# Global variables for storing budget and expenses
global_budget = {'amount': 0}
global_expenses = []


# Define Screens
class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.budget_label = Label(text='No budget set')
        self.expenses_label = Label(text='No expenses added')
        self.layout.add_widget(self.budget_label)
        self.layout.add_widget(self.expenses_label)
        self.add_widget(self.layout)

    def on_pre_enter(self, *args):
        # Update the budget display
        self.budget_label.text = f'Current Budget: ${global_budget["amount"]}'

        # Update the expenses display
        if global_expenses:
            expenses_text = '\n'.join([f'{exp["name"]}: ${exp["amount"]}' for exp in global_expenses])
            self.expenses_label.text = f'Expenses:\n{expenses_text}'
        else:
            self.expenses_label.text = 'No expenses added'


class BudgetScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.budget_input = TextInput(hint_text='Enter your budget')
        self.save_button = Button(text='Save Budget')
        self.save_button.bind(on_press=self.save_budget)
        layout.add_widget(self.budget_input)
        layout.add_widget(self.save_button)
        self.add_widget(layout)

    def save_budget(self, instance):
        global_budget['amount'] = self.budget_input.text  # Update global budget
        print("Budget set to:", global_budget['amount'])

class ExpenseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.expense_name = TextInput(hint_text='Expense name')
        self.expense_amount = TextInput(hint_text='Expense amount')
        self.add_button = Button(text='Add Expense')
        self.add_button.bind(on_press=self.add_expense)
        layout.add_widget(self.expense_name)
        layout.add_widget(self.expense_amount)
        layout.add_widget(self.add_button)
        self.add_widget(layout)

    def add_expense(self, instance):
        expense = {'name': self.expense_name.text, 'amount': self.expense_amount.text}
        global_expenses.append(expense)  # Add to global expenses list
        print("Added expense:", expense['name'], "Amount:", expense['amount'])

# Main layout
class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'

        # Side bar for navigation
        self.sidebar = BoxLayout(orientation='vertical', size_hint_x=0.2)
        self.add_widget(self.sidebar)

        # Dashboard button
        btn_dashboard = Button(text='Dashboard')
        btn_dashboard.bind(on_press=self.change_to_dashboard)
        self.sidebar.add_widget(btn_dashboard)

        # Budget button
        btn_budget = Button(text='Budget')
        btn_budget.bind(on_press=self.change_to_budget)
        self.sidebar.add_widget(btn_budget)

        # Expenses button
        btn_expenses = Button(text='Expenses')
        btn_expenses.bind(on_press=self.change_to_expenses)
        self.sidebar.add_widget(btn_expenses)

        # Screen manager
        self.screen_manager = ScreenManager()
        self.add_widget(self.screen_manager)

        # Adding screens
        self.screen_manager.add_widget(DashboardScreen(name='dashboard'))
        self.screen_manager.add_widget(BudgetScreen(name='budget'))
        self.screen_manager.add_widget(ExpenseScreen(name='expenses'))

    def change_to_dashboard(self, instance):
        self.screen_manager.current = 'dashboard'

    def change_to_budget(self, instance):
        self.screen_manager.current = 'budget'

    def change_to_expenses(self, instance):
        self.screen_manager.current = 'expenses'

# App class
class BudgetApp(App):
    def build(self):
        return MainLayout()

# Run the app
if __name__ == '__main__':
    BudgetApp().run()
