import json

def add_snippet(snippets, name, code):
    """Add a new snippet to the snippets dictionary."""
    snippets[name] = code

def remove_snippet(snippets, name):
    """Remove a snippet from the snippets dictionary."""
    del snippets[name]

def edit_snippet(snippets, name, new_code):
    """Edit an existing snippet in the snippets dictionary."""
    snippets[name] = new_code

def view_snippet(snippets, name):
    """View a snippet from the snippets dictionary."""
    print(snippets[name])

def save_snippets(snippets, filename):
    """Save the snippets dictionary to a file."""
    with open(filename, 'w') as f:
        json.dump(snippets, f)

def load_snippets(filename):
    """Load the snippets dictionary from a file."""
    try:
        with open(filename, 'r') as f:
            snippets = json.load(f)
    except FileNotFoundError:
        snippets = {}
    return snippets

def main():
    filename = 'snippets.json'
    snippets = load_snippets(filename)

    while True:
        print('Code Snippet Manager')
        print('====================')
        print('1. Add a new snippet')
        print('2. Remove a snippet')
        print('3. Edit a snippet')
        print('4. View a snippet')
        print('5. Save snippets to file')
        print('6. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter the name of the snippet: ')
            code = input('Enter the code for the snippet: ')
            add_snippet(snippets, name, code)
        elif choice == '2':
            name = input('Enter the name of the snippet: ')
            remove_snippet(snippets, name)
        elif choice == '3':
            name = input('Enter the name of the snippet: ')
            new_code = input('Enter the new code for the snippet: ')
            edit_snippet(snippets, name, new_code)
        elif choice == '4':
            name = input('Enter the name of the snippet: ')
            view_snippet(snippets, name)
        elif choice == '5':
            save_snippets(snippets, filename)
        elif choice == '6':
            break
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    main()
