from dialogs import Menu, Option
import dialogs

## for this example Iam using psutil \\ pip install psutil
import psutil

# call this to enable colors
dialogs.enable_colors()


def pid_process(caller):
	
	try:
		pid = int(input("Select pid\n > "))

	except ValueError:

		print("\nInvalid number\n")
		caller.print()
		caller.get_input()
		return

	try:
		process = psutil.Process(pid)
		process_name = process.name()

		print(f'PID {pid} has name "{process_name}"')

	except psutil.NoSuchProcess:
		print(f"Can't find process with pid {pid}")
	
	caller.print()
	caller.get_input()

def taskkill(caller):

	taskkill_menu = Menu(caller)
	taskkill_menu.add_option(Option("Process name by PID", "Get process's name by PID (Process Identifier)", pid_process, color="blue;bold"))
	taskkill_menu.print()
	taskkill_menu.get_input()

if __name__ == "__main__":

	category_menu = Menu(title="Select your category:", help=False)
	category_menu.add_option(Option("Process", "Process category.", taskkill, color="red;underline"))
	category_menu.print()
	category_menu.get_input()
