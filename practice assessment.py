# empty dictionary to add projects to
all_projects = {}
project_number = int(input("How many projects? "))

# Function to ask users how many projects they would like to create
def get_projects():
    for num in range(project_number):
        project_name = str(input("Please enter a project title: "))
        # add project name to dict.
        all_projects[project_name] = []
        print(all_projects)

# Function to let the users add names of people working on each project
def add_people(all_projects):
    for num in range(project_number):
        names = str(input("Next name please: "))
    # Need to figure out how to add to dict. Can't figure out how to add just a value..
        #all_projects.get(project_name:names})

# Function to print out info about the projects
def print_projects(all_projects):
    # getting error on 'for' loop- 'NoneType' object is not iterable
    for name in all_projects:
        print(name)

def main_program():
    pass

# Print everything
print (f'Here are the people in project {}')

all_projects = get_projects()
add_people(all_projects)
print_projects(all_projects)