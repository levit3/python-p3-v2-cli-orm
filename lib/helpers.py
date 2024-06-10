from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    id_ = input("Enter the department id: ")
    department = Department.find_by_id(id_)
    print (department) if department else print(f"Department with id {id_} not found") 


def create_department():
    name = input("Enter department name: ")
    location = input("Enter enter department location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)

def update_department():
    id_ = input("Enter the department id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter new department name: ")
            location = input("Enter new department location: ")
            department.name = name
            department.location = location
            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print(f'Error updating department', exc)
    else:
        print(f'Department {id_} not found')
            
def delete_department():
    id_ = input("Enter department id: ")
    if department := Department.find_by_id(id_):
        try:
            department.delete()
            print(f"Successfully deleted {department}")
        except Exception as exc:
            print(f'Error deleting department', exc)
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    pass


def find_employee_by_name():
    pass


def find_employee_by_id():
    pass


def create_employee():
    pass


def update_employee():
    pass


def delete_employee():
    pass


def list_department_employees():
    pass