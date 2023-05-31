<?php
// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  // Get the submitted username and password
  $username = $_POST['username'];
  $password = $_POST['password'];

  // Validate the username and password
  // You can add your own validation logic here

  // Simulate successful login for demonstration purposes
  // In a real application, you would typically check against a database or external service
  if ($username === 'admin' && $password === 'password') {
    // Redirect to the home page or any other authenticated page
    header('Location: home.php');
    exit();
  } else {
    // Redirect back to the login page with an error message
    header('Location: login.html?error=1');
    exit();
  }
} else {
  // Redirect back to the login page if accessed directly
  header('Location: login.html');
  exit();
}
?>
