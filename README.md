# ToDO_APIs

## Description:
The Todo List API allows users to manage their todo items efficiently. It provides endpoints for creating, retrieving, updating, and deleting todo items.

Actually: Task 
Create a Simple Django project with Authentication and swagger API documentation for a todo list app.
The project should have rest APIs that can 
i. Add items 
ii. delete items 
iii. update existing items
 
 The APIs should through 403 error when the user is not logged in and build a simple login page using django templte.

![image](https://github.com/HackerajOfficial/TODO_APIs/assets/46445015/0fb47646-8254-46ad-af71-3d107bc583d5)


## Technologies Used:
- **Django:** Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It provides built-in features for handling authentication, routing, database interactions, and more.
- **Django REST Framework (DRF):** Django REST Framework is a powerful toolkit for building Web APIs in Django. It provides serializers for handling data conversion, class-based views for defining API endpoints, authentication and permission classes for securing endpoints, and much more.
- **Swagger/OpenAPI:** Swagger or OpenAPI is a specification for documenting RESTful APIs. Tools like Swagger UI or drf-yasg can be used to generate interactive API documentation based on the OpenAPI specification.
- **pipenv:** Pipenv is a tool used for managing dependencies and virtual environments in Python projects. It automatically creates and manages a virtual environment for your project and generates a Pipfile to specify dependencies.

## Features
- **Todo Item Management:**
Create Todo Item: Allow users to add new todo items with a title, description, and optional due date.
View Todo Items: Display a list of todo items for the logged-in user, sorted by priority or due date.
Update Todo Item: Enable users to edit the details of existing todo items, such as the title, description, priority, or due date.
Delete Todo Item: Allow users to remove todo items they no longer need.

## Usage:
1. Clone the repository to your local machine.
     ```
      git clone https://github.com/HackerajOfficial/TODO_APIs.git
     ```
2. Active environment
     ```
       pipenv shell
     ```
3. Install the necessary dependencies
    ```
      pipenv install -r requirements.txt
    ```
4. Start the Django development server:
    ```
      python manage.py runserver
    ```

5. Open your web browser and navigate to `http://localhost:8000`


## Contributing
Contributions to enhance the functionality and performance of the TODO_APIs are welcome. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request outlining the modifications.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code in accordance with the terms of the license.
## Contact:
For any inquiries or feedback regarding the project, please contact [RaazKapoorKuswaha](https://www.facebook.com/HackerajOfficial/) at hackeraj.np@gmail.com.
