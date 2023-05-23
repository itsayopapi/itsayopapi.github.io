<?php

    session_start();
    include 'config.php';

    if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Retrieve the user input
    $user_email = $_POST['email'];
    $user_password = $_POST['password'];

    // Prepare and execute the query to retrieve the hashed password for the given email
    $stmt = $conn->prepare("SELECT user_password FROM $registered_table WHERE user_email = ?");
    $stmt->bind_param("s", $user_email);
    $stmt->execute();
    $stmt->bind_result($hashed_password);
    $stmt->fetch();

    // Verify the password
    if ($hashed_password && password_verify($user_password, $hashed_password)) {
        // Password is correct, set session variables and redirect to dashboard
        $_SESSION["loggedin"] = true;
        $_SESSION["email"] = $user_email;
        header("location: ../index.php");
    } else {
        // Password is incorrect, show error message
        $error = "Invalid email or password.";
    }

    // Close the statement and database connection
    $stmt->close();
    $conn->close();
    }
?>