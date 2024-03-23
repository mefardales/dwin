<h1 align="center">
    <img alt="dwin Logo" width="250px" src="logo/dwin_logo.png"><br>
    <i style="display: block; font-style: italic; font-size:15px;">Asynchronous manager for development environments</i>
</h1>

## Details
`dwin` is a tool designed to facilitate the management of dependencies in Python projects asynchronously, allowing developers to focus on development without worrying about dependency management.

## Features

The main features of Dwin include:

1. **Management of Multiple Virtual Environments**: Dwin allows managing different virtual environments with distinct dependencies as required by the project.

2. **Dependency Separation**: Dwin distinguishes between different types of dependencies (development, production, QA, hybrid) to ensure that only the necessary ones are installed in each environment.

3. **Automatic Generation of Requirements Files**: Dwin automates the creation of `requirements.txt` files, eliminating the need to manually execute `pip freeze`.

4. **Optimization of Development Time**: Reduces the time and effort required to manage and update the project's dependencies.

## Using Dwin

To use Dwin in the management of dependencies and virtual environments, follow the commands according to your needs:

- **Development Dependencies**: `dwin -d`
  Manages and installs the necessary dependencies for the development environment.

- **Production Dependencies**: `dwin -p`
  Focuses on the dependencies needed for the production environment.

- **QA (Testing) Dependencies**: `dwin -qa`
  Manages the specific dependencies for the quality testing environment.

- **Hybrid Dependencies**: `dwin -y`
  Allows the management of dependencies that are common across different environments.

- **Dependency Details**: `dwin -rundoc`
   Runs a server with all the information about the libraries and examples of usage for each of them.

## Initial Instructions

Before starting with Dwin, perform the following steps:

1. **Creation of the Requirements File**: Make sure to generate and keep the `requirements.txt` file of your project up-to-date.

2. **Activation of the Virtual Environment**: Activate the virtual environment of your project to ensure that the dependencies are installed correctly in the isolated environment.

3. **Installation of New Libraries**: In case of adding new dependencies, it is not necessary to execute `pip freeze > requirements.txt` manually; Dwin will take care of updating your requirements files as necessary.

By following these instructions, you can maximize your efficiency and focus on the development of your project with Dwin.
