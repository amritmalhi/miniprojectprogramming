<?php
$user = $_POST["username"];
$pass = $_POST["password"];

$servername = "localhost";
$username = "deb15015n2_photo";
$password = "";
$dbname = "deb15015n2_photo";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
	die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT id FROM user WHERE username = '" . $user . "'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
	echo 'false';
} else {
	$sql = "INSERT INTO user (username, password) VALUES ('" . $user . "', '" . $pass . "')";

	if ($conn->query($sql) === TRUE) {
		echo 'true';
	} else {
		echo 'false';
	}
}




$conn->close();
		
?>