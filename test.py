#Using colorama to change the color of output to blue
from colorama import Fore
import pyfiglet 


styled_text=pyfiglet.figlet_format('dwin',font= 'doom')
print("\n")
print(Fore.BLUE + styled_text) 
print(Fore.GREEN +"Welcome to dwin CLI  for * Render Cloud * v1.0.0 🚀 \n")
print("This is a command line interface for Render Cloud\n")
print(Fore.GREEN + "📚 Full documentation visit: www.clidwin.io \n")
# print(Fore.GREEN + "📚 Full documentation visit: www.clidwin.io \n")
