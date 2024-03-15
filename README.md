# holbertonschool-AirBnB_clone
<html>
<body>
<h1>¡WELCOME TO THE AIRBNB CLONE PROJECT!</h1>
<img src="https://i.pinimg.com/originals/87/10/23/871023fca810e57347eab0ae811ccfdf.png" title="AirBnB clone project" /></a>
<hr>

<h2>DESCRIPTION</h2>
<p>It is a simple command interpreter to manage the objects used in the AirBnB clone project by:
<div>
  <ul>
    <li>Allowing for the creation of new objects.</li>
    <li>Allows retrieval of an object from a file, a database, etc.</li>
    <li>Allows operations to be performed on objects</li>
    <li>Allows object attributes to be updated.</li>
    <li>Allows objects to be destroyed.</li>
  </ul>
</div>

The project contains:
<div>
  <ul>
    <li>A parent class (called BaseModel) used for initialization, serialization, and deserialization of instances.</li>
    <li>Creates a simple flow of serialization/deserialization, as follows: Instance <-> Dictionary <-> JSON string <-> file</li>
    <li>Creation of all subclasses (User, State, City, Amenity, Place, Review)</li>
    <li>Creation of a the first abstracted storage engine of the project: File storage.</li>
    <li>Unittests to validate all classes as well as the storage engine.</li>
    </ul>
</div>
</p>

<h2>Command Interpreter 💻:</h2>
<pre>
    <p>The command interpreter allows you to interact with the application to create, update, delete, and display instances of the different models in the database.</p>
</pre>

<h2>How to StartT</h2>

- <p>To start the command interpreter, follow these steps:

<ol>
  <li>Clone the repository from [GitHub](git@github.com:marialegl/holbertonschool-AirBnB_clone.git).</li>
  <li>Open a terminal and navigate to the directory where you cloned the repository.</li>
  <li>Run the following command:</li>
</ol>

    ```bash
    ./console.py
    ```

<p>How to Use</p>
<pre>
<p>Once you've started the command interpreter, you can use the following commands:</p>
</pre>
<div>
  <ul>
    <li>`create <model_name>`: Create a new instance of the specified model.</li>
    <li>`show <model_name> <id>`: Show the details of a specific instance of the model.</li>
    <li>`update <model_name> <id> <attribute> <value>`: Update a specific attribute of an instance of the model.</li>
    <li>`destroy <model_name> <id>`: Delete a specific instance of the model.</li>
    <li>`all <model_name>`: Show all instances of the specified model.</li>
    <li>`quit` or `EOF`: Exit the command interpreter.</li>
    </ul>
</div>

<p>Examples</p>
<pre>
<p>
<div>
  <ul>
<li>To create a new user, you can run:</li>

    ```
    (hbnb) create User
    ```
<li>To show all users, you can run:</li>

    ```
    (hbnb) all User
    ```

<li>To exit the command interpreter, you can run:</li>

    ```
    (hbnb) quit
    ```
</p>
</pre>

<h2>Have fun exploring the functionalities of the AirBnB Clone command interpreter!</h2>

<br>

<p>David Vasquez</p>
<a href="https://www.linkedin.com/in/foultrip//">
  <img src="https://static-00.iconduck.com/assets.00/linkedin-icon-2048x2048-ya5g47j2.png" width="50">
</a>

<a href="https://github.com/FoulTrip">
 <img src="https://1000logos.net/wp-content/uploads/2021/05/GitHub-logo.png" width="100">
</a>

------------

<p>Maria Alejandra Gonzales</p>
<a href="https://www.linkedin.com/in/maria-alejandra-gonzalez-londo%C3%B1o-a5084a208/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">
  <img src="https://static-00.iconduck.com/assets.00/linkedin-icon-2048x2048-ya5g47j2.png" width="50">
</a>

<a href="https://github.com/marialegl">
 <img src="https://1000logos.net/wp-content/uploads/2021/05/GitHub-logo.png" width="100">
</center>

<footer><img src="https://img.freepik.com/vector-premium/fondo-textura-elegante-blanco_23-2148434267.jpg?size=626&ext=jpg&ga=GA1.1.1222169770.1701648000&semt=ais" width="1000", height ="200"></footer>