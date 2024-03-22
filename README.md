
<h1 align="center">
    <img alt="cookiecutter Logo" width="200px" src="https://raw.githubusercontent.com/dwin/dwin/3ac078356adf5a1a72042dfe72ebfa4a9cd5ef38/logo/dwin_logo.png">
</h1>

# Dwin - Gestión de Entornos Virtuales

Dwin es una herramienta diseñada para facilitar la gestión de múltiples entornos virtuales en proyectos Python, permitiendo a los desarrolladores enfocarse en el desarrollo sin preocuparse por la gestión de dependencias.

## Características

Las principales características de Dwin incluyen:

1. **Gestión de Múltiples Entornos Virtuales**: Dwin permite administrar diferentes entornos virtuales con distintas dependencias, según lo requerido por el proyecto.

2. **Separación de Dependencias**: Dwin distingue entre diferentes tipos de dependencias (desarrollo, producción, QA, híbridas) para asegurar que solo se instalen las necesarias en cada entorno.

3. **Generación Automática de Archivos de Requisitos**: Dwin automatiza la creación de archivos `requirements.txt`, evitando la necesidad de ejecutar manualmente `pip freeze`.

4. **Optimización del Tiempo de Desarrollo**: Reduce el tiempo y esfuerzo requerido para gestionar y actualizar las dependencias del proyecto.

## Uso de Dwin

Para utilizar Dwin en la gestión de dependencias y entornos virtuales, siga los siguientes comandos según sus necesidades:

- **Dependencias de Desarrollo**: `dwin -d`
  Gestiona e instala las dependencias necesarias para el entorno de desarrollo.

- **Dependencias de Producción**: `dwin -p`
  Se enfoca en las dependencias necesarias para el entorno de producción.

- **Dependencias de QA (Pruebas)**: `dwin -qa`
  Maneja las dependencias específicas para el entorno de pruebas de calidad.

- **Dependencias Híbridas**: `dwin -y`
  Permite la gestión de dependencias que son comunes entre diferentes entornos.

-- **Detalles de dependencias**: `dwin -rundoc`
   Corre un servidor con toda la info de las librerias y ejemplo de uso de cada una de ellas.

## Instrucciones Iniciales

Antes de empezar con Dwin, realice los siguientes pasos:

1. **Creación del Archivo de Requisitos**: Asegúrese de generar y mantener actualizado el archivo `requirements.txt` de su proyecto.

2. **Activación del Entorno Virtual**: Active el entorno virtual de su proyecto para asegurar que las dependencias se instalen correctamente en el entorno aislado.

3. **Instalación de Nuevas Librerías**: En caso de agregar nuevas dependencias, no es necesario ejecutar `pip freeze > requirements.txt` manualmente; Dwin se encargará de actualizar sus archivos de requisitos según sea necesario.

Siguiendo estas instrucciones, puede maximizar su eficiencia y enfocarse en el desarrollo de su proyecto con Dwin.
