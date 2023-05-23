<?php

    include 'config.php';

    $user_fname = $_POST['fname'];
    $user_lname = $_POST['lname'];
    $user_email = $_POST['email'];
    $user_password = $_POST['password'];

    echo $user_email;
    echo $user_lname;

    // Validate the inputs
    if (empty($user_fname) || empty($user_lname) || empty($user_email)  || empty($user_password)) {
        die("Please fill in all fields.");
    }
    if (!filter_var($user_email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email address.");
    }

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $hashed_password = password_hash($user_password, PASSWORD_DEFAULT, ['cost' => 12]);
    // Insert the client data into the database
    $stmt = $conn->prepare("INSERT INTO $registered_table (user_fname, user_lname, user_email, user_password) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $user_fname, $user_lname, $user_email, $hashed_password);
    $stmt->execute();
    $_SESSION["loggedin"] = false;
    $conn->close();

    header("location: ../index.html");

    //echo "Registration successful!";
?>
